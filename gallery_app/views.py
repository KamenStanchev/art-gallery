from django.shortcuts import render

from gallery_app.models import Picture, Category, AboutUs


def home(request):
    return render(request, 'gallery_app/home.html')


def gallery(request):
    pictures = Picture.objects.all()
    alert = None
    if not pictures:
        alert = 'There are not any pictures'
    context = {'pictures': pictures,
               'alert': alert}
    return render(request, 'gallery_app/gallery.html', context)


def picture_details(request, pk):
    picture = Picture.objects.get(id=pk)
    categories = ', '.join(list(p.name for p in picture.category.all()))
    print(categories)
    context = {'picture': picture,
               'categories': categories,
               }
    return render(request, 'gallery_app/picture_details.html', context)


def categories_page(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'gallery_app/categories_page.html', context)


def view_by_category(request, pk):
    category = Category.objects.get(id=pk)
    pictures = Picture.objects.filter(category=category)
    alert = None
    if not pictures:
        alert = f'There are not any pictures in {category.name.title()}'
    context = {'pictures': pictures,
               'alert': alert}
    return render(request, 'gallery_app/gallery.html', context)


def about_us(request):
    try:
        about_us_description = AboutUs.objects.filter(is_used=True)[0].description
    except:
        about_us_description = None

    return render(request, 'gallery_app/about_us.html', context={
        'description': about_us_description,
    })
