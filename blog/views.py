from django import forms
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View
from .forms import PostCreateForm
from .models import post

# Create your views here.
class BlogListView(View):
    def get(self, request, *args, **kwargs):
        context={
            
        }
        return render(request,'blog_list.html',context)


class BlogCreateView(View):
    def get(self,request, *args, **kwargs):
        form=PostCreateForm()
        context={
            'form':form
        }
        return render(request,'blog_create.html', context)

    def post(self,request, *args, **kwargs):
        if request.method=="POST":
            form=PostCreateForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data.get('title')
                content = form.cleaned_data.get('content')

                p, created=post.objects.get_or_create(title=title,content=content)
                p.save()
                return redirect('blog:home')





        context={

        }
        return render(request,'blog_create.html', context)
