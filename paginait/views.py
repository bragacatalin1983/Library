from django.shortcuts import render, get_object_or_404, redirect
from .models import Cursit, Liked
from django.contrib.auth.models import User


def paginait(request):
    its = Cursit.objects.order_by('-date')
    user = request.user
    context = {
        'its': its,
        'user': user,
    }

    return render(request, 'paginait.html', context)


def postari(request, pkit_id):
    postare = get_object_or_404(Cursit, pk=pkit_id)

    return render(request, 'postari.html', {'postare': postare})


def like_post(request):
    user = request.user
    try:

        if request.method == 'POST':
            post_id = request.POST.get('it_id')
            post_obj = Cursit.objects.get(id=post_id)

            if user in post_obj.isliked.all():
                post_obj.isliked.remove(user)
            else:
                post_obj.isliked.add(user)

            liked, created = Liked.objects.get_or_create(
                user=user, blog_id=post_id)

            if not created:
                if liked.value == 'Like':
                    liked.value = 'Unlike'
                else:
                    liked.value = 'Like'
            liked.save()

        return redirect('paginait')
    except TypeError:
        return render(request, 'paginait.html', {'error_logged': 'Nu esti logat! Daca vrei sa dai like la posturile noastre te rugam sa dai refresh si sa te loghezi!'})
