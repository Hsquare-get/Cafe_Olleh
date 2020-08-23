from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    ediya_eventpage = 'https://www.ediya.com/contents/event.html?tb_name=event&bbs_section=view&Ctg=&page=1&idx=122/'
    angelinus_eventpage = 'http://www.angelinus.com/Event/Event_View.asp?Mode=VIEW&EventType=Event&Idx=626&SearchEventGubun=0/'
    pascucci_eventpage = 'http://www.caffe-pascucci.co.kr/event/eventView.asp?teSeq=431/'

    context = {'ediya_eventpage': ediya_eventpage,
               'angelinus_eventpage': angelinus_eventpage,
               'pascucci_eventpage': pascucci_eventpage}
    return render(request,'home.html',context)
