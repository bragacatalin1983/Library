from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Like
from django.core.mail import send_mail


def home(request):
    if request.method == 'GET':
        return render(request, 'home/home.html')
    else:
        user_name = request.POST['username']
        user_mail = request.POST['useremail']
        msg = request.POST['subject']
        message = "username: {} \n usermail : {} \n message : {}".format(
            user_name, user_mail, msg)
        send_mail('de la biblio', message, user_mail,
                  ['sectiaimpr.casatineretului@gmail.com'])
        return render(request, 'home/home.html', {'mesaj': 'Mail trimis cu succes!'})


def blog(request):
    blogs = Blog.objects.order_by('-date')
    user = request.user
    context = {
        'blogs': blogs,
        'user': user,
    }
    return render(request, 'blog/blog.html', context)


def posts(request, pk_id):
    posts = get_object_or_404(Blog, pk=pk_id)
    return render(request, 'posts/posts.html', {'posts': posts})


def desprenoi(request):
    return render(request, 'blog/desprenoi.html')


def blog_likes(request):
    user = request.user
    try:

        if request.method == 'POST':
            post_id = request.POST.get('blog_id')
            post_obj = Blog.objects.get(id=post_id)

            if user in post_obj.liked.all():
                post_obj.liked.remove(user)
            else:
                post_obj.liked.add(user)

            like, created = Like.objects.get_or_create(
                user=user, blog_id=post_id)

            if not created:
                if like.value == 'Like':
                    like.value = 'Unlike'
                else:
                    like.value = 'Like'
            like.save()

        return redirect('blog')
    except TypeError:
        return render(request, 'blog/blog.html', {'error_logged': 'Nu esti logat! Daca vrei sa dai like la posturile noastre te rugam sa dai refresh si sa te loghezi!'})
