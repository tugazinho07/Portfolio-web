from django.shortcuts import render
import datetime
from .models import *
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import NewForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def layout_view(request):
    return render(request, 'portfolio/layout.html')

def home_view(request):
    agora = datetime.datetime.now()
    local = 'Lisboa'

    context = {
        'hora': agora.hour,
        'local': local
    }

    return render(request, 'portfolio/home.html', context)

def about_view(request):
    context = {'cadeiras': Cadeira.objects.all(), 'educations': Education.objects.all()}
    return render(request, 'portfolio/about.html', context)

def projects_view(request):
    context = {'projects': Project.objects.all(),'tfcs': TFC.objects.all()}
    return render(request, 'portfolio/projects.html', context)

def web_view(request):
    context = {'noticias': Noticia.objects.all(), 'tecs': Tecnologia.objects.all(), 'labs': Lab.objects.all()}
    return render(request, 'portfolio/web.html', context)

def blog_view(request):
    context = {'news': New.objects.all()}
    return render(request, 'portfolio/blog.html', context)

def new_tarefa_view(request):
    form = NewForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))
    context = {'form': form}
    return render(request, 'portfolio/blog_new.html', context)

def contacts_view(request):
    return render(request, 'portfolio/contacts.html')

@login_required
def edit_tarefa_view(request, portfolio_id):
    tarefa = New.objects.get(id=portfolio_id)
    form = NewForm(request.POST or None, instance=tarefa)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))
    context = {'form': form, 'portfolio_id': portfolio_id}
    return render(request, 'portfolio/blog_edit.html', context)

def delete_tarefa_view(request, portfolio_id):
    New.objects.get(id=portfolio_id).delete()
    return HttpResponseRedirect(reverse('portfolio:blog'))

def sobre_este_view(request):
    return render(request, 'portfolio/sobre_este.html')

def contactos_view(request):
    return render(request, 'portfolio/contactos.html' )

def perguntas_quizz(request):
    score = 0
    nome = request.POST['nome']
    apelido = request.POST['apelido']
    Django = request.POST['Django']
    home = request.POST['web']
    servidor = request.POST['917229966']
    autor = request.POST['xadrez']
    if Django == "Django" :
        score += 10
    if home == "web" :
        score += 10
    if servidor == "917229966" :
        score += 15
    if autor == "xadrez" :
        score += 15
    return score

def desenha_grafico_resultados():
    participantes = sorted(PontuacaoQuizz.objects.all(), key=lambda t: t.pontuacao, reverse=True)     
    nomes = []     
    pontuacoes = []     
    for pt in participantes:         
        nomes.append(pt.nome +" "+pt.apelido)         
        pontuacoes.append(pt.pontuacao)     
        plt.barh(nomes, pontuacoes)     
        plt.savefig("portfolio/static/portfolio/images/grafico.png", bbox_inches='tight') 

def quizz(request):
    if request.method == 'POST':
        n = request.POST['nome']
        a = request.POST['apelido']
        p = perguntas_quizz(request)
        r = PontuacaoQuizz(nome=n, apelido=a, pontuacao=p)
        r.save()
    context = {
    'pontuacao': p
    }
    context = {
        'pontuacao': p,
        'labs': Lab.objects.all(),
        'tecs': Tecnologia.objects.all(),
    }
    desenha_grafico_resultados()
    return render(request,'portfolio/web.html', context)

def login_view(request):
    if request.method == "POST":
        nome_login = request.POST.get('username')
        password_login = request.POST.get('password')
        utilizador = authenticate(request, username=nome_login, password=password_login)

        if utilizador is not None:
            login(request, utilizador)
            context = {'post': New.objects.all(),}
            return render(request, 'portfolio/blog.html', context)
        else:
            return render(
                request, 'portfolio/login.html',
                {'message': "Credenciais Invalidas"}
            )

    return render(request, 'portfolio/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'portfolio/home.html')
