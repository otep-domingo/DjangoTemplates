from re import template
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
# blog
from .forms import BlogForm
from .models import Blog


# Create your views here.

def default(request):
    # return HttpResponse("Weldome to Python and Django!")
    template = loader.get_template('default.html')
    return HttpResponse(template.render())

# Add Blog


def create_blog(request):
    # if request.method == "POST":
    #     form = BlogForm(request.POST)
    #     if form.is_valid():
    #         try:
    #             form.save()
    #             return redirect('search/')
    #         except:
    #             pass
    # else:
    #     form = BlogForm()
    blogid=request.POST['BlogId']
    title=request.POST['Title']
    author=request.POST['Author_Name']
    startdate=request.POST['Start_Date']
    enddate=request.POST['End_Date']
    blog = Blog(BlogID=blogid, Title=title, Author_Name=author, Start_Date=startdate,End_Date=enddate)
    blog.save()
    return render(request, 'create.html')

    # Search Blog


def retrieve_blog(request):
    blogs = Blog.objects.all()
    return render(request, 'search.html', {'blogs': blogs})


# Update Blog

def update_blog(request, pk):
    blogs = Blog.objects.get(id=pk)
    form = BlogForm(instance=blogs)

    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blogs)
        if form.is_valid():
            form.save()
            return redirect('/search')

    context = {
        'blogs': blogs,
        'form': form,
    }
    return render(request, 'update.html', context)

    # Delete Blog


def delete_blog(request, pk):
    blogs = Blog.objects.get(id=pk)

    if request.method == 'POST':
        blogs.delete()
        return redirect('/search')

    context = {
        'blogs': blogs,
    }
    return render(request, 'remove.html', context)
