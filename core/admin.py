from django.contrib import admin
from .models import Movie, MovieList

# Register your models here.
admin.site.register(Movie)
admin.site.register(MovieList)