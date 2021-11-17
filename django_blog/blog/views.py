from django.shortcuts import render

posts = [
    {
        'author': 'KamilB',
        'title': 'Blog Post 1',
        'content': 'First post text',
        'date_posted': 'November 17, 2021'
    },
    {
        'author': 'JackC',
        'title': 'Blog Post 2',
        'content': 'Second post text',
        'date_posted': 'November 17, 2021'
    },
    {
        'author': 'LeonB',
        'title': 'Blog Post 3',
        'content': 'Third post text',
        'date_posted': 'November 17, 2021'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
