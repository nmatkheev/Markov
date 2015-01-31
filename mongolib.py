# -*- coding: utf-8 -*-
"""
    Это модуль основный функций по работе с базой данных MongoDB
    
    Module of mongolib
    
    Created in 2015.01.31  11:03 
    Autor: 'pavel'
"""
import sys
import datetime
from time import sleep


# TODO Здесь должны быть настройки. Логин, пароль, ip, порт
# from settings import ... ... ... ...

# TODO Написать свои имена тут
__author__ = 'Pavel|...'

# TODO этой функции в данном модуле не место -- перенести в модуль ...
def PearList2PearListCount (pearlist):
    """
    Данная функция переводит
    [("мама", "мыла"), ("мыла", "раму"), ("раму", "."), (".", "мама"), ("мама", "мыла")],
    в
    [("мама", "мыла", 2), ("мыла", "раму", 1), ("раму", ".", 1), (".", "мама", 1)]
    :param pearlist:
    :return:
    """
    error = "Функция пока не реализована"
    raise NotImplementedError(error)
# TODO этой функции в данном модуле не место -- перенести в модуль ...
def PearListCount2PearList (pearlistcount):
    """
    Данная функция переводит

    [("мама", "мыла", 2), ("мыла", "раму", 1), ("раму", ".", 1), (".", "мама", 1)]
    в
    [("мама", "мыла"), ("мыла", "раму"), ("раму", "."), (".", "мама"), ("мама", "мыла")],

    :param pearlistcount:
    :return:
    """
    error = "Функция пока не реализована"
    raise NotImplementedError(error)

# TODO этой функции в данном модуле не место -- перенести в модуль ...
def Text2PearList(text, is_count=False):
    # TODO дописать ссылки вместо ...
    """
    Данная функция получает на вход текст, а возвращает список пар:
        (слово, следующее слово)
    Например из текста "мама мыла раму . мама мыла" получется ответ:
    [("мама", "мыла"), ("мыла", "раму"), ("раму", "."), (".", "мама"), ("мама", "мыла")],
    если is_count=False. Если is_count=True:
    [("мама", "мыла", 2), ("мыла", "раму", 1), ("раму", ".", 1), (".", "мама", 1)]
    :param text: входной текст.
    ВАЖНО: входной текст уже должен быть предварительно обработан (только пробелы, кроме "." нет знаков припенания, ...)
    см. подробнее ... ...

    :return: ...
    """
    error = "Функция пока не реализована"
    raise NotImplementedError(error)

def InsertWords(pear_or_pearlist):
    """
    Данная функция добавляет пару pear_or_pearlist

    :param pear_or_pearlist:
        Пара или список пар. Одна пара -- это кортеж
        вида: (слово, следующее слово) или (слово, следующее слово, количество)
    :return:
    Возвращает None, если не было ошибки.
    """
    if isinstance(pear_or_pearlist, list):
        pearlist = pear_or_pearlist
    elif isinstance(pear_or_pearlist, tuple):
        pearlist = [pear_or_pearlist]
    else:
        error = "Тип pear_or_pearlist не list и не tuple!"
        raise EnvironmentError(error)
    # Далее работаем с pearlist, а не pear_or_pearlist
    if len(pearlist[0]) == 2:
        pearlist = PearList2PearListCount(pearlist)


    error = "Функция пока не реализована"
    raise NotImplementedError(error)

    # TODO Написать функцию

def GetNextWordList(word, letter=None, letter_position=1):
    # TODO дописать ссылки вместо ...
    """
    Данная функция возвращает список кортежей.
    [(следующее слово, количество), (следующее слово, количество), ...]
    :param word:
        слово, для которого ищутся все следующие слова.
    :param letter_position: См. letter. Если letter is None, то данное поле игнорируется
    :param letter: Если не None, то возвращает только такие пары,
        в которых letter_position буква для следующего слова совпадает с letter_position буквой в first_letter

    :return: ...
    """
    if letter is None:
        letter_position = None

    error = "Функция пока не реализована"
    raise NotImplementedError(error)

def GetCount(pear):
    """
    Для пары (слово, следующее слово) данная функция возвращает количество раз,
        когда данная пара встречалась
    :param pear:
    :return:
    """
    error = "Функция пока не реализована"
    raise NotImplementedError(error)

def Enrichment(count=None):
    """
    Функция обогащения коллекции pearlist из коллекции pearenrichment.
    Функция берет пару из pearenrichment, удаляет ее и добавляет в коллекцию pearlist
    :param count:
        максимальное количество пар, которые следует обогатить.
        Если None, то функция будет работать до тех пор, пока есть данные в pearenrichment
    :return:
        Возвращает количество обработанных пар
    """
    error = "Функция пока не реализована"
    raise NotImplementedError(error)

def __test():
    """
    Функция для тестирования данного модуля

    (Разумно ставить режим DEBUG'а и с бряками отлаживать)
    :return:
    """

    pear = ('мама', 'мыла')
    ret1 = InsertWords(pear)

    ret2 = InsertWords([pear, pear])

    text = "мама мыла раму мылом . мама любит масло рама ."
    pearlist = Text2PearList(text)

    word = 'мама'
    nextlist = GetNextWordList(word)

    ret3 = GetCount(word, nextlist[0][0])
    if ret3 != nextlist[0][1]:
        error = "Функция GetCount работает неверно!"
        print error


if __name__ == "__main__":

    print "TEST mongolib " + str(datetime.datetime.now())
    sleep(3)
    __test()