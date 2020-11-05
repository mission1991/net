from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('movies:movie_category', args=[self.slug])


class Movie(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)
    synopsis = models.TextField(blank=True)
    poster = models.ImageField(upload_to="posters", blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=1, null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter')
    director = models.CharField(max_length=140, null=True, blank=True)
    released_date = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']
        index_together = [['id', 'slug']]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movies:movie_detail', args=[self.id, self.slug])


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_user')
    comment = models.TextField()
    rating = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='review_voter')

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('movies:movie_detail', self.comment)

