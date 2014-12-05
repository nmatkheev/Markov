# -*- coding: utf-8 -*-
"""
    Описание модуля
    
    TODO
    
    Fraudmon
    create in: 2014-08-06   
"""
# TODO работы много...
#TODO протестировать ...

__author__ = 'Pavel'

import codecs
import datetime
import json
import sys

def SafeChain(chain, path):
    """
    safe chain
    """
    fw= codecs.open (path, 'w', encoding='utf8')
    begin = datetime.datetime.now()
    print "SafeChain:"
    str_chain = json.dumps(chain,
              sort_keys=True,
              ensure_ascii=False
              )

    #INFO для удобства восприятия в Notepad++
    str_chain = str_chain.replace(']], ', ']],\n')
    str_chain = str_chain.replace('], ', '],\n\t')
    u_str_chain = str_chain.decode('utf8')
    fw.write(u_str_chain)

    end = datetime.datetime.now()
    spendtime = (end-begin)

    print ":done. " + str(spendtime)

    fw.close()

def LoadChain(path):
    """

    """
    chain = None
    fr = None
    try:
        fr = open(path, 'r')
        chain = json.load(fr)
    except:
        print "ERROR: " + str(sys.exc_info())
        return None
    finally:
        if fr != None:
            fr.close()
    return chain
