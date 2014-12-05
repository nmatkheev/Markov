# -*- coding: utf-8 -*-
"""
    ===============================
    Данный модуль содержит функции:
    1) для извлечения html страниц, используя http протокол
    2) для конвертации файлов html --> txt
    3) для "чистки" файлов txt, чтобы они были пригодны для постройки платформы
    ===============================
    This module have functions:
    1) for pulling dome html text files, using http protocol;
    2) for converts html --> txt
    3) for convert txt (only text) --> txt, that can be useful for building platform
    
    ~We am SOOBE(=Sorry Of Our Bad English)
"""
#TODO
__author__ = 'Pavel|Nikolay'

import datetime
import os
from time import sleep

#TODO НИКОЛАЮ: дописать return на английском
def ScourTxtText (path_txt_in, path_txt_out):
    """
    Данная функция "частит" txt файл, чтобы он был пригоден для постройки платформы
    This functions scour *.txt file for using it in platform building.
    :param path_txt_in:
    путь к входному файлу
    :param path_txt_out:
    путь к выходному файлу
    :return:
    возвращает количество слов, которое содержится в итоговом файле.
    (Точки тоже считаются словами)
    """

    #TODO НИКОЛАЮ: написать код
    error = "ScourTxtText unsupported!"
    raise NotImplementedError(error)

    return None

#TODO НИКОЛАЮ: английское описание
def GetHtmlPages(url, path_out):
    """
    Извлекает html страницу или несколько данных по url
    :param url:
    URL запроса
    :param path_out:
    -- если папка, то помещает в нее ВСЕ СОДЕРЖИМОЕ
    -- если путь к *.html, то сохраняет только html страницу
    :return:
    список путей ко всем извлеченным данным
    """

    #TODO НИКОЛАЮ: написать код

    #список всех извлеченных данных
    pulling_files_list = list()

    error = "GetHtmlPages unsupported!"
    raise NotImplementedError(error)

    return pulling_files_list

#TODO НИКОЛАЮ: английское описание
def Html2Txt (path_in_html, path_out_txt):
    """
    Convert HTML to TXT file
    :param path_in_html:
    :param path_out_txt:
    :return:
    возвращает None, если нет ошибки
    """

    #TODO НИКОЛАЮ: написать код

    error = "Html2Txt unsupported!"
    raise NotImplementedError(error)

    return None

#TODO НИКОЛАЮ: английское описание
def WikiUrlGenerator (lang='ru'):
    """
    Возвращает URL случайной страницы в википедии.
    Использует кнопку "случайная страница"
    :param lang:
    язык википедии для использования
    :return:
    возращает кортеж:
    (url, article_name), где article -- название статьи
    """
    url, article_name = None, None

    #TODO НИКОЛАЮ: написать код

    error = "WikiUrlGenerator unsupported!"
    raise NotImplementedError(error)

    return url, article_name

#TODO НИКОЛАЮ: английское описание
def TestHtmlPulling(platform_folder_in_path, need_count_words):
    """
    Тестовая функция
    :param platform_folder_in_path:
    путь к папке, в которой должны быть файлы построения платформы
    :param need_count_words:
    минимальное колличество необходимых слов.
    :return:
    """
    path_temp = 'temp'
    try:
        os.mkdir(path_temp)
    except:
        pass

    count_words = 0

    if isinstance(platform_folder_in_path, str):
        platform_folder_in_path = unicode(platform_folder_in_path, encoding='utf-8')

    if platform_folder_in_path[-1] != u'\\':
        platform_folder_in_path += u"\\"

    while count_words < need_count_words:
        url, article_name = WikiUrlGenerator()

        print "Извлекли статью ", article_name, " (url=", url, ")"
        print datetime.datetime.now()

        article_html = article_name + ".html"
        unscour_txt = article_name + ".unscour.txt"
        scour_txt = article_name + ".scour.txt"

        retlist = GetHtmlPages(url, path_out=article_html)

        if retlist is None or len(retlist) == 0:
            print "WARNING: GetHtmlPages uncorrect work!"
            sleep(10)
            continue

        if Html2Txt(path_in_html=article_html, path_out_txt=unscour_txt):
            print "WARNING: Html2Txt uncorrect work!"
            sleep(10)
            continue

        count_words += ScourTxtText(path_txt_in=unscour_txt, path_txt_out=platform_folder_in_path+scour_txt)
        #немножко поспим, чтобы не грузить трафик
        sleep(1)


########################
if __name__ == "__main__":
    print "HtmlPuller.py test  " + datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')

    TestHtmlPulling(platform_folder_in_path=u'palform_in', need_count_words=10000)
    #TestHtmlPulling(platform_folder_in_path=u'palform_in', need_count_words=10000000)
