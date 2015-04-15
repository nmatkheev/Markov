# -*- coding: utf-8 -*-
# TODO "для последующей обработки виде" -- дальше что?..
"""
Модуль для загрузки текстов из сети и представления их в удобном для последующей обработки виде

(пример работы см. в конце файла)
"""

from urllib2 import urlopen, HTTPError
import codecs

# TODO Автор, яви себя миру!
__author__ = '...'

wiki_random = 'https://ru.wikipedia.org/wiki/Служебная:Случайная_страница'


def downloadHtml(url=wiki_random, path='./unnamed.html'):
    """
    Функция загружает страницу из сети и сохраняет ее по заданному адресу.
    :param url: адрес файла в сети. По умолчанию - случайная страница ru.wikipedia.org
    :param path: : локальный адрес для сохранения файла
    :return: path в случае удачного завершения, иначе None
    """
    if '://' not in url:
        url = 'http://' + url

    remote_file = None
    try:
        remote_file = urlopen(url)
    except HTTPError as error:
        if remote_file:
            remote_file.close()
        print 'HTTP Error', error.code, ':', error.msg, '(page:', url, ')'
        return None

    local_file = open(path, 'w')
    for line in remote_file:
        local_file.write(line)
    local_file.close()
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
    p_start = html.find('<p>', position)
    p_end = html.find('</p>', position)

    while p_start != -1 and p_end != -1:
        if p_end < p_start + 3:
            return text
        raw_paragraph = html[p_start+3:p_end]

        position = p_end + 4
        p_start = html.find('<p>', position)
        p_end = html.find('</p>', position)

        if (u'•' in raw_paragraph) or (u'|' in raw_paragraph) or (u'Координаты' in raw_paragraph):
            continue

        buff = ''
        brace_counter = 1
        for c in raw_paragraph:
            if c in ('<', '{', '(', '['):
                brace_counter -= 1
            elif c in ('>', '}', ')', ']'):
                brace_counter += 1
            else:
                if brace_counter > 0:
                    buff += c

        buff = __delSpecChars(buff)
        buff = __replacePunctuation(buff)

        if len(buff) > 100:
            text += buff.lower() + ' '

    return text


def textByWord(text):
    # TODO param и return описать
    """
    Разбивает текст по 1 слову на строку. Знаки препинания приравниваются к словам.
    :param text:
    :return:
    """
    words = text.split()
    new_text = ''
    for word in words:
        new_text += word + '\n'
    return new_text


def __replacePunctuation(str_):
    str_ = str_.replace(u"«", u" ")
    str_ = str_.replace(u"»", u" ")
    str_ = str_.replace(u"'", u" ")
    str_ = str_.replace(u'"', u" ")
    str_ = str_.replace(u"(", u" ")
    str_ = str_.replace(u")", u" ")

    str_ = str_.replace(u".", u" . ")
    str_ = str_.replace(u",", u" , ")
    str_ = str_.replace(u"?", u" . ")
    str_ = str_.replace(u"!", u" . ")

    str_ = str_.replace(u":", u" , ")
    str_ = str_.replace(u";", u" , ")
    str_ = str_.replace(u"—", u" — ")  # исправить здесь, если тире не нужно в конечном тексте
    str_ = str_.replace(u"\n", u".")

    return str_


def __delSpecChars(str_):
    pos = str_.find('&#')
    while pos != -1:
        semicolon = str_.find(';', pos)
        str_ = str_[:pos] + str_[semicolon+1:]
        pos = str_.find('&#')
    return str_


if __name__ == '__main__':
    downloadHtml(path='./ololo.html')
    htmlPage = codecs.open('./ololo.html', 'r', 'utf-8').read()
    # out = codecs.open('out.txt', 'w', 'utf-8')
    pureText = html2text(htmlPage)
    # out.write(byWord(pureText))
    # out.close()
    print textByWord(pureText)