from django.db import models

# Create your models here.

from django.core.urlresolvers import reverse

class Post(models.Model):
    title = models.CharField('TITLE', max_length=50, null= True)
    slug = models.SlugField('SLUG', max_length=50, unique=True, null=True, allow_unicode=True, help_text="one word for title alias.")
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text="simple text")
    content = models.TextField('CONTENT', null=True)
    create_date = models.DateField('Create_date', auto_now=True,)
    modify_date = models.DateField('Modify_date', auto_now=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'my_post'
        ordering = ('-modify_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,))

    def get_previous_post(self):
        return self.get_previous_by_modify_date()

    def get_next_post(self):
        return self.get_next_by_modify_date()
