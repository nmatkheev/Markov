# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django import forms
from django.views.decorators.csrf import csrf_exempt
from djangomongo import proc_done, toProcessing, getAcrotext
import django.dispatch

@csrf_exempt
def acrstg(request):
    text = request.POST['text']
    session_id = '123' # должно получаться из request

    wait = True
    def done(sender, **kwargs): # обработчик сигнала
        global wait
        if kwargs['id'] == session_id:
            wait = False
    proc_done.connect(done)

    toProcessing(session_id, text)

    while (wait): # ждем сигнала
        pass

    acrotext = getAcrotext(session_id)# получаем акротекст

    return HttpResponse(acrotext);


@csrf_exempt
def index(request):
    template = loader.get_template('frontend/index.html')
    context = RequestContext(request, {
            })
    return HttpResponse(template.render(context))



#@csrf_exempt
# def index(request):
#     template = loader.get_template('frontend/index.html')
#     if request.method == 'POST':
#         form = TextForm(request.POST)
#         if form.is_valid():
#             context = RequestContext(request, {
#             'swearing':', bitches',
#             'answer':'got text',
#             'form':form,
#             'text':form.cleaned_data['text']
#             })
#         else:
#             form = TextForm();
#             context = RequestContext(request, {
#             'swearing':', dear friends',
#             'answer':'no text',
#             'form':form
#             })
#     else:
#         form = TextForm();
#         context = RequestContext(request, {
#             'swearing':', dear friends',
#             'answer':'no text',
#             'form':form
#             })
#
#     return HttpResponse(template.render(context))

#class TextForm(forms.Form):
#    text = forms.CharField(label='Input text', max_length=300, widget=forms.Textarea)
