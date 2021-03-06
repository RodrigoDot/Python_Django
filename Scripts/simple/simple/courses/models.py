from django.db import models


class CourseManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) |
            models.Q(description__icontains=query) |
            models.Q(slug__icontains=query)
        )


class Courses(models.Model):
    name = models.CharField(
        'Nome',
        max_length=100
    )
    slug = models.SlugField(
        'Atalho'
    )
    description = models.TextField(
        'Descrição',
        blank=True
    )
    about = models.TextField(
        'Sobre',
        blank=True
    )
    image = models.ImageField(
        upload_to='courses/images',
        verbose_name='Imagen',
        null=True,
        blank=True
    )
    start_date = models.DateField(
        'Data início',
        null=True,
        blank=True
    )
    created_at = models.DateField(
        'Criado em ',
        auto_now_add=True
    )
    updated_at = models.DateField(
        'Atualizado em ',
        auto_now=True
    )
    objects = CourseManager()

    def __str__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('courses:details', (), {'id': self.id})

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['name']
