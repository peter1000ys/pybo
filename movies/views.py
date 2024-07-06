from django.shortcuts import render, redirect
from .models import Movie, Review
from .forms import MovieForm, ReviewForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html', context)

def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():

            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form': form
    }
    return render(request, 'movies/create.html', context)


    
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    reviews = movie.review_set.all()
    review_form = ReviewForm()
    context = {
        'movie': movie,
        'review_form': review_form,
        'reviews': reviews,

    }
    return render(request, 'movies/detail.html', context)


def delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    movie.delete()
    return redirect('movies:index')

def update(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'POST':

        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail',movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        'movie': movie,
        'form': form
    }
    return render(request, 'movies/update.html', context)

@login_required
def reviews_create(request, pk):
    movie = Movie.objects.get(pk=pk)
    reviews = movie.review_set.all()
    review_form = ReviewForm(request.POST)
    if review_form.is_valid():
        review = review_form.save(commit=False)
        review.movie = movie
        review.user = request.user
        review.save()
        return redirect('movies:detail', movie.pk)
    context = {
        'review_form': review_form,
        'movie': movie,
        'reviews': reviews,
    }
    return render(request, 'movies/detail.html', context)


@login_required
def reviews_delete(request, movie_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.user == review.user:
        review.delete()
    return redirect('movies:detail', movie_pk)