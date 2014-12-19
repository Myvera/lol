# coding: utf-8

from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import context
from firstlol.engine import Infinite, Error




# Create your views here.

def LOL(request):
    return HttpResponse("Hello World")

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def lol_search(request):
    return render_to_response('search_form.html')


# Here, Start Bootstrap Design


def example1(request):
    return render_to_response('starter.html')

def search(request):
    query = request.GET['q']
    name = query.encode('utf-8')
    name = name.replace(" ", "")

    if Error(name) == 0:
        a = Infinite(name)
        level = a.Summoner_Level()
        n = a.How_Many()
        tier = a.League_Tier()

        # 배열선언
        kill = [0 for i in range(n)]
        mc = [0 for i in range(n)]
        champ = [0 for i in range(n)]
        kda = [0 for i in range(n)]
        playtime = [0 for i in range(n)]
        victory = [0 for i in range(n)]
        item = [[0 for i in range(9)] for j in range(n)]
        spell = [[0 for i in range(2)] for j in range(n)]

        for i in range(n):
            mc[i] = a.Create_Date(i)
            champ[i] = a.Champ(i)
            kill[i] = a.Kill(i)
            kda[i] = a.KDA(i)
            playtime[i] = a.Play_Time(i)
            victory[i] = a.Victory(i)

        for i in range(n):
            for j in range(7):
                item[i][j] = a.Item(i, j)
            for j in range(7, 9):
                item[i][j] = a.Summoner_Spell(i, j)

        return render_to_response('result.html', locals())

    else:
        message = '존재하지 않는 소환사 이름이거나 오류가 발생했습니다.'
        return render_to_response('result_error.html', locals())


def about(request):
    by = "제작자 : 황인성"
    time = "제작기간 : 2014.10.02~ (개발중)"
    tool = "Python, Django Webframework 이용 개발, Apache2.2, mod_wsgi를 이용해 서비스 중"
    return render_to_response('about.html', locals())

def contact(request):
    email = "황인성, hishis1029@gmail.com"
    return render_to_response('contact.html', locals())