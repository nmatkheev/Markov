# -*- coding: utf-8 -*-
"""
Модуль для загрузки текстов из сети и представления их в удобном для последующей обработки виде

(пример работы см. в конце файла)
"""

from urllib2 import urlopen, HTTPError
import codecs

wikirandom = 'https://ru.wikipedia.org/wiki/Служебная:Случайная_страница'

def downloadHtml(url = wikirandom, path='./unnamed.html'):
    """
    Функция загружает страницу из сети и сохраняет ее по заданному адресу.
    :param url: адрес файла в сети. По умолчанию - случайная страница ru.wikipedia.org
    :param path: : локальный адрес для сохранения файла
    :return: path в случае удачного завершения, иначе None
    """
    if '://' not in url:
        url = 'http://' + url

    try:
        remotefile = urlopen(url)
    except HTTPError as error:
        if remotefile:
            remotefile.close()
        print 'HTTP Error', error.code, ':', error.msg, '(page:', url, ')'
        return None

    localfile = open(path, 'w')
    for line in remotefile:
        localfile.write(line)
    localfile.close()
    return path

def html2text(html):
    """
    Парсит текст из HTML-страницы. Обрабатывается только содержимое <p>...</p>. Удаляются спец. символы вида &#xxx,
    знаки препринания удаляются (':', ';', '"', '"') или меняются на точки и запятые ('!','?'), текст переводится в
    нижний регистр.
    :param html: исходный текст страницы
    :return: текст, полученный в ходе обработки
    """
    position = 0
    text = ''
    pStart = html.find('<p>',position)
    pEnd = html.find('</p>', position)

    while pStart != -1 and pEnd != -1:
        if pEnd < pStart + 3:
            return text
        rawParagraph = html[pStart+3:pEnd]

        position = pEnd + 4
        pStart = html.find('<p>',position)
        pEnd = html.find('</p>', position)

        if (u'•' in rawParagraph) or (u'|' in rawParagraph) or (u'Координаты' in rawParagraph):
            continue

        buff = ''
        braceCounter = 1
        for c in rawParagraph:
            if c in ('<','{','(','['):
                braceCounter-=1
            elif c in ('>','}',')',']'):
                braceCounter+=1
            else:
                if braceCounter > 0:
                    buff += c

        buff = _delSpecChars(buff)
        buff = _replacePunctuation(buff)

        if len(buff) > 100:
            text += buff.lower() + ' '

    return text


def textByWord(text):
    """
    Разбивает текст по 1 слову на строку. Знаки препинания приравниваются к словам.
    """
    words = text.split()
    newText = ''
    for word in words:
        newText+= word + '\n'
    return newText

def _replacePunctuation(str):
    str = str.replace (u"«", u" ")
    str = str.replace (u"»", u" ")
    str = str.replace (u"'", u" ")
    str = str.replace (u'"', u" ")
    str = str.replace (u"(", u" ")
    str = str.replace (u")", u" ")

    str = str.replace (u".", u" . ")
    str = str.replace (u",", u" , ")
    str = str.replace (u"?", u" . ")
    str = str.replace (u"!", u" . ")

    str = str.replace (u":", u" , ")
    str = str.replace (u";", u" , ")
    str = str.replace (u"—", u" — ") #исправить здесь, если тире не нужно в конечном тексте
    str = str.replace (u"\n", u".")

    return str

def _delSpecChars(str):
    pos = str.find('&#')
    while pos != -1:
        semicolon = str.find(';',pos)
        str = str[:pos] + str[semicolon+1:]
        pos = str.find('&#')
    return str



if __name__ == '__main__':
    downloadHtml(path = './ololo.html')
    htmlPage = codecs.open('./ololo.html', 'r', 'utf-8').read()
    #out = codecs.open('out.txt', 'w', 'utf-8')
    pureText = html2text(htmlPage)
    #out.write(byWord(pureText))
    #out.close()
    print textByWord(pureText)