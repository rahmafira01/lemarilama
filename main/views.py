from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'aplikasi' : 'Lemari Lama',
        'name': 'Rahma Dwi Maghfira',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)