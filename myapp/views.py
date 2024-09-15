from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm
from django.templatetags.static import static

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()  # Save data to MySQL
            return redirect('success_page')  # Redirect after successful save
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def toppick(request, id):
    movies = {
        1: {
            'title': 'Green Book',
            'description': 'รายละเอียดของ Movie 1',
            'poster': 'POSTER1.png',
            'actor_image': 'greenbookactor.jpg'
        },
        2: {
            'title': 'Black Panther',
            'description': 'รายละเอียดของ Movie 2',
            'poster': 'POSTER2.png',
            'actor_image': 'greenbookactor.jpg'
        },
        3: {
            'title': 'Moonfall',
            'description': 'รายละเอียดของ Movie 3',
            'poster': 'POSTER3.png',
            'actor_image': 'greenbookactor.jpg'
        },
        4: {
            'title': 'Titanic',
            'description': 'รายละเอียดของ Movie 4',
            'poster': 'POSTER4.png',
            'actor_image': 'greenbookactor.jpg'
        },
        5: {
            'title': 'Friday the 13th',
            'description': 'รายละเอียดของ Movie 5',
            'poster': 'POSTER5.png',
            'actor_image': 'greenbookactor.jpg'
        },
        6: {
            'title': 'Sadtra9',
            'description': 'รายละเอียดของ Movie 6',
            'poster': 'POSTER6.png',
            'actor_image': 'greenbookactor.jpg'
        },
    }

    movie = movies.get(id, {
        'title': 'Unknown Movie',
        'description': 'No description available',
        'poster': 'default.png',
        'actor_image': 'defaultactor.jpg'
    })

    return render(request, 'toppick.html', {'movie': movie})


def coming_soon_detail(request, id):
    # ดึงข้อมูลหนังที่กำลังจะมาในอนาคต
    movie = {'id': id, 'title': f'Coming Soon {id}', 'description': 'ตัวอย่างหนัง'}
    return render(request, 'coming_soon_detail.html', {'movie': movie})

def celebrity_detail(request, id):
    # ดึงข้อมูลดารา
    celebrity = {'id': id, 'name': f'Celebrity {id}', 'bio': 'ข้อมูลของดารา'}
    return render(request, 'celebrity_detail.html', {'celebrity': celebrity})

def news_detail(request, id):
    # ดึงข้อมูลข่าว
    news = {'id': id, 'title': f'News {id}', 'content': 'เนื้อหาข่าว'}
    return render(request, 'news_detail.html', {'news': news})
