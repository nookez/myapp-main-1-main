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
    # ข้อมูลตัวอย่างของหนังที่คุณสามารถดึงจากฐานข้อมูลจริง
    movies = {
        1: {'title': 'Movie 1', 'description': 'รายละเอียดของ Movie 1', 'poster': 'POSTER1.png'},
        2: {'title': 'Movie 2', 'description': 'รายละเอียดของ Movie 2', 'poster': 'POSTER2.png'},
        3: {'title': 'Moonfall', 'description': 'รายละเอียดของ Movie 3', 'poster': 'POSTER3.png'},
        4: {'title': 'Movie 4', 'description': 'รายละเอียดของ Movie 4', 'poster': 'POSTER4.png'},
        5: {'title': 'Movie 5', 'description': 'รายละเอียดของ Movie 5', 'poster': 'POSTER5.png'},
        6: {'title': 'Movie 6', 'description': 'รายละเอียดของ Movie 6', 'poster': 'POSTER6.png'},
    }
    
    movie = movies.get(id, {'title': 'Unknown Movie', 'description': 'No description available', 'poster': 'default.png'})
    
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
def home(request):
    top_picks = [
        {'id': 1, 'title': 'Movie 1', 'poster': 'POSTER1.png'},
        {'id': 2, 'title': 'Movie 2', 'poster': 'POSTER2.png'},
        {'id': 3, 'title': 'Movie 3', 'poster': 'POSTER3.png'},
    ]

    coming_soon = [
        {'id': 4, 'title': 'Coming Soon 1', 'poster': 'POSTER4.png'},
        {'id': 5, 'title': 'Coming Soon 2', 'poster': 'POSTER5.png'},
        {'id': 6, 'title': 'Coming Soon 3', 'poster': 'POSTER6.png'},
    ]

    popular_celebrities = [
        {'id': 7, 'name': 'Celebrity 1', 'poster': 'POSTER7.png'},
        {'id': 8, 'name': 'Celebrity 2', 'poster': 'POSTER8.png'},
        {'id': 9, 'name': 'Celebrity 3', 'poster': 'POSTER9.png'},
    ]

    news_items = [
        {'id': 10, 'title': 'News 1', 'poster': 'POSTER10.png'},
        {'id': 11, 'title': 'News 2', 'poster': 'POSTER11.png'},
        {'id': 12, 'title': 'News 3', 'poster': 'POSTER12.png'},
    ]

    context = {
        'top_picks': top_picks,
        'coming_soon': coming_soon,
        'popular_celebrities': popular_celebrities,
        'news_items': news_items,
    }
    return render(request, 'home.html', context)