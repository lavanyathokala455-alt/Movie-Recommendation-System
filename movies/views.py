from django.shortcuts import render
from django.db.models import Q
from .models import Movie

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

def movie_list(request):
    query = request.GET.get('q', '').strip().replace(" movies", "")
    filter_type = request.GET.get('type')

    movies = Movie.objects.all()

    if query:
     movies = movies.filter(
        Q(title__icontains=query) |
        Q(language__icontains=query) |
        Q(genre__icontains=query)
    )

    if filter_type == "recommended":
        movies = Movie.objects.filter(rating__gte=8)

    elif filter_type == "top":
        movies = Movie.objects.all().order_by('-rating')

    elif filter_type == "thriller":
        movies = Movie.objects.filter(genre__icontains="thriller")

    elif filter_type == "comedy":
        movies = Movie.objects.filter(genre__icontains="comedy")

    elif filter_type == "all":
        movies = Movie.objects.all()

   
    return render(request, 'movies/movie_list.html', {'movies': movies})
def movie_detail(request, id):
    movie = Movie.objects.get(id=id)
    return render(request, 'movies/movie_detail.html', {'movie': movie})

def signup_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('/login/')

    return render(request, 'movies/signup.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('/')

    return render(request, 'movies/login.html')

def logout_view(request):
    logout(request)
    return redirect('/login/')