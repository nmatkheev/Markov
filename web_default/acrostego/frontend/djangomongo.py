# -*- coding: utf-8 -*-
import django.dispatch

proc_done = django.dispatch.Signal(providing_args=["id", "acrotext"])

def toProcessing(session_id, text):
    """
    Вызывается со стороны Django, помещает текст на обработку в БД
    """
    pass

def processingComplete(session_id, acrotext):
    """
    Вызывается со стороны Mongo после окончания обработки файла. Подбрасывает сигнал об окончании обработки
    """
    proc_done.send('djangomongo', id = session_id, acrotext = acrotext)

def getAcrotext(session_id):
    """
    Вызывается со стороны Django после получения сигнала об окончании обработки.
    Возвращает акротекст по идентификатору сессии
    """
    pass