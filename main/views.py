from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406351806',
        'name': 'Nadin Ananda',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
