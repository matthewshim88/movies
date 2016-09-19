from django.shortcuts import render
from models import Movie, Actor

# Create your views here.

def index(request):
	allmovies = Movie.objects.all()
	context = {'allmovies':allmovies}
	return render(request, "newimdb/index.html", context)

def addMovie(request):
    if request.method == 'POST':
        Movies.objects.create(movie_title = request.POST['movie'])
    return redirect('/')

def addActor(request, id):
    if request.method=='POST':
    	Movies.objects.create(movie_title = request.POST['movie'])
    return redirect('/')
