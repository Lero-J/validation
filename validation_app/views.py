from django.shortcuts import render
from .forms import PostForm, UserForm


def index(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            form = PostForm()
        else:
            print(form.errors)
    ctx = {
        'form': form
    }
    return render(
        request=request,
        template_name='validation_app/main_page.html',
        context=ctx
    )


def create_user(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            form = PostForm()
        else:
            print(form.errors)
    ctx = {
        'form_user': form
    }
    return render(
        request=request,
        template_name='validation_app/users.html',
        context=ctx
    )