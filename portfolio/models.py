from django.db import models
from email.policy import default

class New(models.Model):
    titulo = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='media/', null=True, blank=True)
    autor = models.CharField(max_length=40)
    data = models.DateTimeField(auto_now_add=True)
    descricao = models.CharField(max_length=500)
    link = models.CharField(max_length=1000)

    def __str__(self):
          return self.titulo[:50]

class Person(models.Model):
    nome = models.CharField(max_length=60)
    linklusofona = models.CharField(max_length=1000, default='1')
    linklinkedin = models.CharField(max_length=1000, default='1')

    def __str__(self):
          return self.nome[:50]

class Tecnologia(models.Model):
    nome = models.CharField(max_length=30)
    acronimo = models.CharField(max_length=10, blank=True)
    ano = models.IntegerField()
    criador = models.CharField(max_length=40)
    logotipo = models.ImageField(upload_to='media/', null=True, blank=True)
    link = models.CharField(max_length=500)
    descricao = models.TextField(max_length=1000)

    def __str__(self):
          return self.nome[:50]


class Professor(models.Model):
    nome = models.CharField(max_length = 40)
    link_pag = models.CharField(max_length = 500)
    link_linkedin = models.CharField(max_length = 500)

    def __str__(self):
        return self.nome[:50]

class Education(models.Model):
    formacao = models.CharField(max_length=70)
    curso = models.CharField(max_length=60)
    topicos = models.CharField(max_length=500, default='1')
    local = models.CharField(max_length=50)
    periodo = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='media/', null=True, blank=True)
    logotipo = models.ImageField(upload_to='media/', null=True, blank=True)

    def __str__(self):
          return self.formacao[:50]


class Project(models.Model):
    titulo = models.CharField(max_length = 30)
    descricao = models.CharField(max_length = 500)
    imagem = models.ImageField(upload_to='media/', null=True, blank=True)
    anoRealizado = models.IntegerField()
    participantes = models.CharField(max_length = 100)
    chair = models.CharField(max_length = 40)
    linkGitHub = models.CharField(max_length = 500)
    lingua = models.CharField(max_length = 25)

    def __str__(self):
        return self.titulo[:40]


class Cadeira(models.Model):
    nome = models.CharField(max_length= 40)
    ano = models.IntegerField()
    semestre = models.CharField(max_length= 2)
    descricao = models.TextField(max_length=1000)
    ects = models.IntegerField()
    ano_letivo = models.IntegerField()
    topicos_abordados = models.TextField()
    raking = models.IntegerField()
    docente_teorica = models.ForeignKey(Professor, on_delete=models.CASCADE)
    docentes_praticas = models.ManyToManyField(Professor, related_name='cadeiras')
    link_cadeira = models.CharField(max_length=1000, default='1')
    linguagens = models.ManyToManyField(Tecnologia, blank=True)
    projetos = models.ManyToManyField(Project, blank=True)

    def __str__(self):
        return self.nome[:50]

class Achivement(models.Model):
    titulo = models.CharField(max_length=70, default='1')
    descricao = models.CharField(max_length=100, default='1')
    projetos = models.ManyToManyField(Project, blank=True)
    cadeira = models.CharField(max_length=40, default='1')

    def __str__(self):
          return self.titulo[:50]

class Noticia(models.Model):
    titulo = models.CharField(max_length=80)
    texto = models.TextField(max_length=1000)
    imagem = models.ImageField(upload_to='media/', null=True, blank=True)
    link = models.CharField(max_length=1000)
    
    def __str__(self):
          return self.titulo[:50]

class Lab(models.Model):
    titulo = models.CharField(max_length=70)
    descricao = models.TextField(max_length=1000)
    link = models.CharField(max_length=1000)

    def __str__(self):
          return self.titulo[:50]

class TFC(models.Model):
    titulo = models.CharField(max_length=50)
    sumario = models.TextField(max_length=1000)
    linkGitHub = models.CharField(max_length=1000)
    linkYoutube = models.CharField(max_length=1000)
    linkRelatorio = models.CharField(max_length=1000)
    ano = models.IntegerField()
    autor = models.CharField(max_length=70)
    orientador = models.ManyToManyField(Person)
    imagem = models.ImageField(upload_to='media/', null=True, blank=True)

    def __str__(self):
          return self.titulo[:50]

class PontuacaoQuizz(models.Model):     
    nome = models.CharField(max_length=20)    
    apelido = models.CharField(max_length=20)     
    pontuacao = models.IntegerField()

    def __str__(self):
        return self.nome[:50]
