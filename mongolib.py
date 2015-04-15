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
import random

# TODO Здесь должны быть настройки. Логин, пароль, ip, порт
# from settings import ... ... ... ...

# TODO Написать свои имена тут
__author__ = 'PavelMSTU|...|...'


def SetTask(text, akro_text=None, full_text=None):
    # TODO написать имя коллекции вместо ...
    """
    Данная функция добавляет задание в Mongo
    в коллекцию ... ... .
    :param text: текст, который следует добавить
    :param akro_text: текст, который уже был предварительно сформирован
    :param full_text: полный текст, который имеет оконцовку в виде текста text
    :return:
    возвращает _id задания по которому можно будет найти
    задание
    """

    if not isinstance(text, unicode):
        error = 'type(text) must be unicode, not {0}'.format(type(text))
        raise AttributeError(error)

    error = 'NotImplementedError'
    raise NotImplementedError(error)
    _id = 123123
    return _id


def GetTask(_id):
    # TODO написать имя коллекции вместо ...
    """
    Данная функция проводит следующие дейстивия:
    1) в коллекции ... ищет запись ответа с указанным _id
    2) если запись еще не обработана, то возвращает None, None
    3) если запись уже обработана, то возвращает err, mess;
    где err -- возникщая ошибка, mess - искомое сообщение
    :param _id: _id в коллекции ...
    :return:
    кортеж двух величин: err, mess:
    err -- возникшая ошибка. Возвращает None, если ошибка не возникла
    mess -- возвращаемый текст типа unicode
    """

    error = 'NotImplementedError'
    raise NotImplementedError(error)
    err = None
    mess = u'В недрах тундры выдры в гетрах'
    return err, mess


# Словарь, используемый в функциях SetTaskTest и GetTaskTest.
# после удаления функций SetTaskTest и GetTaskTest так же должен быть удален
__test_task_dict = dict()


def SetTaskTest(text, akro_text=None, full_text=None, sec_spend_time=10):
    """
    Тестовая функция для написания WEB-шкурки.

    После корректной работы SetTask и GetTask
    и их тестирования данная функция должна быть удалена.
    :param text: сообщение, для которого следует выполнить акротекст
    :param akro_text: текст, который уже был предварительно сформирован.
    В тестовой версии не используются
    :param full_text: полный текст, который имеет оконцовку в виде текста text
    В тестовой версии не используются
    :param sec_spend_time: время ожидания в секундах.
    :return:
    Возвращяет _id, который представляет собой якобы _id коллекции.
    """
    global __test_task_dict

    if not isinstance(text, unicode):
        error = 'type(text) must be unicode, not {0}'.format(type(text))
        raise AttributeError(error)

    _id = random.randint(0, 1000000)

    time_end_work = datetime.datetime.now() + datetime.timedelta(seconds=sec_spend_time)
    task = text
    __test_task_dict[_id] = (time_end_work, task)
    return _id


def GetTaskTest(_id):
    """
    Функция для получения ответа по указанному _id

    После корректной работы SetTask и GetTask
    и их тестирования данная функция должна быть удалена.

    Выполняет следующие действия:
    1) в словаре __test_task_dict ищет запись с ключем _id
    2) если запись еще не обработана, то возвращает None, None
    3) если запись может быть обработана, то обрабатывает её и возвращает err, mess;
    где err -- возникщая ошибка, mess - искомое сообщение
    :param _id: _id в коллекции ...
    :return:
    кортеж двух величин: err, mess:
    err -- возникшая ошибка. Возвращает None, если ошибка не возникла
    mess -- возвращаемый текст типа unicode
    """
    def __TestMakeAnsText(text):
        dict_char = {
            u'а': u'ахатина',
            u'б': u'бырр',
            u'в': u'вентерь',
            u'г': u'габбро',
            u'д': u'дупель',
            u'е': u'евхаристия',
            u'ё': u'ёхор',
            u'ж': u'жалейка',
            u'з': u'забрало',
            u'и': u'изюбр',
            u'й': u'йох',
            u'к': u'кьёккенмединги',
            u'л': u'ллойдия',
            u'м': u'метранпаж',
            u'н': u'нефоскоп',
            u'о': u'ойнохоя',
            u'п': u'палимпсет',
            u'р': u'рокада',
            u'с': u'синекдоха',
            u'т': u'терпентин',
            u'у': u'убихинон',
            u'ф': u'флоэма',
            u'х': u'хрущ',
            u'ц': u'церападус',
            u'ч': u'чадородие',
            u'ш': u'шпрехштальмейстер',
            u'щ': u'щетинозуб',
            u'ы': u'Ыджидпарма',
            u'э': u'эхинопс',
            u'ю': u'ююба',
            u'я': u'ястык',
            u'.': u'.',
            u'$': u'люди ищут работу, которая им не нравиться, чтобы заработать деньги на вещи, которые им не нужны',
        }
        ret = u""
        for c in text:
            if c in dict_char:
                ret += dict_char[c] + u" "
        return ret


    global __test_task_dict

    if _id not in __test_task_dict:
        error = '_id={0} not have in __test_task_dict!'.format(_id)
        return error, None

    time_, text = __test_task_dict[_id]
    if datetime.datetime.now() < time_:
        # Запись пока еще не готова.
        return None, None

    # Следует удалить ключ, т.к. задание обработано.
    __test_task_dict.pop(_id)

    akro_text = __TestMakeAnsText(text)

    return None, akro_text

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


def __test_SetGet():
    """
    Функция для тестирования
    :return:
    """

    text = u'быть знаменитым некрасиво, не это подымает ввысь.'
    print u"input:{0}".format(text)

    _id = SetTaskTest(text)
    akro_text = None
    while akro_text is None:
        err, akro_text = GetTaskTest(_id)
        if err:
            print "Error:", err
        elif akro_text is None:
            print "Текст еще не готов ({0})".format(datetime.datetime.now())
        sleep(1)
    print u"output:{0}".format(akro_text)

if __name__ == "__main__":

    # print "TEST mongolib " + str(datetime.datetime.now())
    # sleep(3)
    # __test()

    __test_SetGet()