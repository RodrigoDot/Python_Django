rodrigo
python123

>>> secao 3 - 24

## Ativar o ambiente


cd scripts/
activate.bat

## Iniciar um projeto Django

django-admin startproject <NOME>


## Iniciar o servidor

cd <PastaProjeto> python manage.py runserver


## Configurando o banco

As configuracoes gerais do django se encontram no arquivo settings.py na pasta raiz do projeto
Para configurar o bd basta localizar as configuracoes do banco.
Apos realizadas as devidas configuracoes basta criar as tabelas no banco

Na pasta raiz do projeto > python manage.py migrate

Apos realizar alguma mudanca no banco, basta rodar o comando a seguir para atualizar as models
Na pasta raiz do projeto > python manage.py makemigrations
E depois rodar o comando > python manage.py migrate para atualizar o banco


## Ver o codigo SQL gerado

Para ver o codigo SQL gerado basta utilizar o comando python manage.py sqlmigrate myapp 0001_initial


Agora eh necessario criar um ADMIN

python manage.py createsuperuser


## Criando aplicacoes

Na pasta raiz do projeto > python manage.py startapp <NOME>


## Criando registros no banco usando o Django SHELL

Usando o comando python manage.py shell na raiz do projeto eh possivel acessar o shell com todo o ambiente django carregado
Para criar registros basta importar as classes que serao utilizadas e atribuir valores aos campos

```python
from simple.courses.models import Courses
course = Courses()
course.name = 'Aprendendo Python'
course.description = 'Aprendendo Python na Udemy'
course.slug = 'Django'
from datetime import date
course.start_date = date.today()
course.save()
```

Outra forma de criar registros eh passando as propriedades com seus valores como argumento para o construtor da classe instanciada

```python
from simple.courses.models import Courses
from datetime import date
course = Courses(
  course.name = 'Aprendendo Python',
  course.description = 'Aprendendo Python na Udemy',
  course.slug = 'Django',
  course.start_date = date.today()
)
course.save()
```

Ou ainda utilizando a funcao create do objeto 'objects' da classe

```python
from simple.courses.models import Courses
Courses.objects.create(name='python')
```

Para atualizar registros basta atribuir novamente um valor ao atributo da classe intanciada
Para deletar um registro basta chamar a funcao .delete() no objeto instanciado


## Listando registros do banco

Ainda no SHELL do Django vamos listar os registros do banco em um array. Para isso utilizaremos uma funcao da classe models 'objects.all()'
```python
from simple.courses.models import Courses
courses = Courses.objects.all()
```

Agora para exibir esses registros utilizaremos as funcao print e for
```python
for course in courses:
  print(course.name)
```


## Filtrnado os resultados (QuerySet)

Para filtrar os resultados buscados no banco utilizamos a funcao filter(<parametro>) no objeto instanciado
```python
from simple.courses.models import Courses

courses = Courses.objects.filter(slug='django')
courses[0].name
courses = Courses.objects.filter(slug='django').filter(name='Aprendendo')
courses[0].name
courses = Courses.objects.filter(slug='django', name='Aprendendo')
courses[0].name
```

## Criando um Query Manager personalizado

*OBS.: Para esses Managers personalizados funcionarem eh necessario atualizar a tabela usando o comando makemigrations*

Para facilitar a consulta ao banco podemos criar query managers para diminuir a quantidade de codigo digitado a cada consulta realizada
Para isso criamos uma classe que extende um metodo da classe MODEL
```python
from django.db import models

class CoursesManager(models.Manager)

def search(self, query):
  return self.get_queryset().filter(
    name__icontains=query
    )

objects = CoursesManager()    
```

Com isso definimos uma metodo de busca personalizado e definimos o novo manager como o padrao para buscas da model


## AND, OR

Utilizando o operador AND
```python
from django.db import models

class CoursesManager(models.Manager)

def search(self, query):
  return self.get_queryset().filter(
    name__icontains=query, description__icontains=query
    )

objects = CoursesManager()
```
tambem pode ser assim

```python
from django.db import models

class CoursesManager(models.Manager)

def search(self, query):
  return self.get_queryset().filter(
    models.Q(name__icontains=query) & \
    models.Q(description__icontains=query)
    )

objects = CoursesManager()
```

Utilizando o operador OR
```python
from django.db import models

class CoursesManager(models.Manager)

def search(self, query):
  return self.get_queryset().filter(
    models.Q(name__icontains=query) | \
    models.Q(description__icontains=query)
    )

objects = CoursesManager()
```


## Adicionando os modulas das aplicacoes ao facilitar

Para visualizar as alicacoes no ACL do Django eh necessario cadastra-las.
Cada aplicacao tem um arquivo admin.py onde sao cadastrados os seus modulos de models

```python
from .models import Courses

admin.site.register(Courses)
```

Para cadastrar uma model basta importar a model e depois utilizar a classe admin.site.register(<NOME_DA_MODEL>) passando o nome da model como parametro


## Exibindo o nome dos registros na exibicao do ACL

Por padrao o ACL exibe informacoes estranhas em seu painel.
Para resolver isso criamos uma funcao na model para retornar o valor que queremos que seja exibido.
No fim da model

```python
def __str__(self):
  return self.name  
```


## Definindo labels para o front-end

Por padrao o Django utiliza o nome da model na exibicao no ACL, mas muitas vezes o nome da model nao fica legal na exibicao.
Podemos personalizar essas labels para deixar a coisa mais interessante utilizanto a classe META
No fim da model

```python
class Meta:
  verbose_name = 'Curso'
  verbose_name_plural = 'Cursos'
```

*OBS tanto a def que define os nomes exibidos no ACL quanto a classe Meta precisam estrar identados dentro da classe da model*


## Definindo os campos que sao exibidos no ACL

Podemos definir quais campo sao exibidos no ACL e a ordem em que eles devem aparecer.
Para criamos uma class que extende a admin.ModelAdmin e utilizamos seus metodos para fazer isso passando ela no registro do modulo
no arquivo admin.py da aplicacao


```python
class CoursesAdmin(admin.ModelAdmin):
  list_display = ['name', 'slug', 'start_date', 'created_at']
  search_fields = ['name', 'slug']


admin.site.register(Courses, CoursesAdmin)  
```


## Criando o Slug field automaticamente

Eh possivel criar o slug fields automaticamente usando uma propriedade da classe ModelAdmin

```python
prepopulated_fields = {
    'slug': ('name',)
}
```
