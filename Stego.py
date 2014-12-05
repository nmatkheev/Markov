# -*- coding: utf-8 -*-
"""
    Этот модуль содержит функции для построения акротекстов из предварительно построенных
    create in: 2014-08-06   
"""
# TODO работы много...
#TODO протестировать ...

__author__ = 'Fraudmon'

import datetime

from MarkoffLib import LoadChain

import sys

PLATFORM_PATH = u'platform_build\\dantsova.plf'

import random

def __step (platform, keys, keys_letter,  letter, textlist, c, error_words=None, depth=0):
    """
    Шаг алгоритма
    TODO
    :param platform:
    :param keys:
    :param keys_letter:
    :param letter:
    :param textlist:
    :param c:
    :return: True -- если удалось. False -- если ошибка стеганографии
    """
    def __count_words(textlist):
        count = 1
        while textlist[-count] != u".":
            count += 1
        return count

    depth_bad_error = list()
    while(True):

        if error_words==None:
            error_words = list()

        next_word = None
        last_word = textlist[-1]

        point_exist = False
        if last_word == u'.':
            words = keys_letter[letter]
            #i = random.randrange(len(words))
            i_max = -1
            max = 0
            for i in range(len(words)):
                next_word = words[i]
                pot = platform[next_word]
                if len(pot) > max:
                    i_max = i
                    max = len(pot)
            next_word = words[i_max]
            textlist.append(next_word)
            return True

        pot = platform[last_word]
        i_pot_good = list()

        #Найдём все слова.
        for i in range(len(pot)):
            #if i == 578:
            #    print 'dd'
            #print i
            word = pot[i][0]
            if len(word)<1 and word != u'.':
                mess= u'Мусор в i=@i@ в слове "@last_word@"->"@word@"'\
                    .replace(u'@last_word@', last_word)\
                    .replace(u'@i@', str(i))\
                    .replace(u'@word@', word)
                #TODO print mess
                continue
            if word[0] == letter:
                i_pot_good.append(i)
            if word == u'.':
                point_exist = True

        i_max = -1
        max = 0
        for i in i_pot_good:
            count = pot[i][1]
            if count > max:

                #Проверяем, что слово не из левого списка:
                word = pot[i][0]
                isuse = True
                for word_ch in error_words:
                    if word_ch == word:
                        isuse = False
                        break

                if isuse:
                    i_max = i
                    max = count

        if i_max==-1:
            if point_exist:
                next_word = u'.'
                textlist.append(next_word)
                return __step (platform, keys, keys_letter,  letter, textlist, c)
            #мы не нашли слова -- ошибка стеганографии.

            #TODO сделать глубину более глубокой, чем на 1
            if depth == 0:
                bad_word = textlist[-1]
                print u">>-" + bad_word
                textlist.pop(-1)
                depth_letter = bad_word[0]
                depth_bad_error.append(bad_word)
                is_good = __step (
                    platform, keys, keys_letter, depth_letter,  textlist, c,
                    error_words=depth_bad_error, depth=depth+1
                )
                if is_good:
                    print u">>+" + textlist[-1]
                    continue
                #else
                #уберём слово и добавим прошлое
                textlist.pop(-1)
                textlist.append(bad_word)
                #сознательно допускаем ошибку
            i_max = -1
            max = 0
            for i in range(len(pot)):
                count = pot[i][1]
                if count > max:
                    i_max = i
            next_word = pot[i_max][0]
            textlist.append(next_word)
            return False
        else:
            next_word = pot[i_max][0]
            textlist.append(next_word)

            if __count_words(textlist) > c:
                if point_exist:
                    next_word = u"."
                    textlist.append(next_word)

            return True

def MakeAcrotext(platform, message, c=10, ret_list=False):
    """
    Функция создания акротекста.
    ВАЖНО: в данный момент функция работает только с кирилическими русскими буквами
    Function for creation acrotext.
    ATTENTION: You can use only russian letters!
    :param platform:
    построенная цепь маркова (платформа). Используйте LoadPlatform для построения платформы
    build Markov chain
    :param message:
    искомое сообщение, из которого следует создать акротекст
    message for acrotext constructing
    :param c:
    параметр, показывающий со скольки слов можно ставить '.'
    this parameter mean minimal numbers of word in one sentence.
    :return:
    возвращает акротекст (текст, где первые буквы -- буквы из message)
    return acrotext
    """


    textlist = list()

    keys = list()
    keys_letter = dict()
    for key in platform:
        if len(key) < 2:
            #INFO gubrige in platform
            continue
        keys.append(key)
        letter = key[0]
        if keys_letter.has_key(letter):
            keys_letter[letter].append(key)
        else:
            new_letter_list = list()
            new_letter_list.append(key)
            keys_letter[letter] = new_letter_list

    textlist.append(u'.')
    correct_count = 0
    uncorrect_count = 0
    for letter in message:
        if letter not in u'йцукенгшщзхфвапролджэячсмитбю':
            continue
        try:
            correct = __step(platform, keys, keys_letter, letter, textlist, c)
        except:
            print u"ERROR in __step(platform, keys, keys_letter, letter, textlist, c)"\
                .replace(u'letter', letter)\
                .replace(u'c', str(c))
            print str(sys.exc_info())
            #TODO здесь разумно поставить бряку
            correct = __step(platform, keys, keys_letter, letter, textlist, c)
        if correct:
            correct_count += 1
        else:
            uncorrect_count += 0

        print u">>" + textlist[-1]

    print "[@c@ :: @un@]"\
        .replace('@c@', str(correct_count))\
        .replace('@uc@', str(uncorrect_count))
    if ret_list:
        return textlist
    rettext = u""
    for word in textlist:
        rettext += word
        if word != u'.':
            rettext += u' '
    return rettext

#Различные параметры c алгоритма для тестирования
DEFAULT_C_TEST_STEGO_LIST = [8, 10, 12, 20]

def TestMarkovChainAcro(message, platform_path, c_list):
    """
    Функция акростеганографии.
    :param message:
    сообщение, из которого необходимо создать акротекст
    message for acrosteganography
    :param platform_path:
    путь к платфроме
    platform path
    :param c_list:
    список различных параметров c для тестирования
    list of some c parameter for testing
    :return:
    возвращает список полученных акротекстов
    """
    random.seed(message)
    platform = LoadChain(platform_path)
    if not platform:
        error = u"Not exist file " + platform_path
        raise EnvironmentError(error)

    list_text = list()
    for c in c_list:
        text = MakeAcrotext(platform, message, c=c)

        print u"return text. c=@c@ message='@m@'::"\
            .replace(u'@c@', str(c))\
            .replace(u'@m@', message)
        print "::::"
        text2 = text.replace(u'.', u'.\n')
        print text2
        print "::::"
        list_text.append(text2)

    return list_text
##############
if __name__ == '__main__':
    #please write YOU message in the down line
    message = u'в недрах тундры выдры в гетрах тырят в ведра ядра кедра'

    begin = datetime.datetime.now()
    print u"TestMarkovChainAcro begin", str(begin), "message=", message
    TestMarkovChainAcro(message, platform_path=PLATFORM_PATH, c_list=[8, 10, 12, 20])
    end = datetime.datetime.now()
    print "All is done" + str(end)
    print "Spend time:" + str(end-begin)