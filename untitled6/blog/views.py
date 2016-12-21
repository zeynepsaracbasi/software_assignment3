from django.core.exceptions import PermissionDenied
from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from tags.models import Tag
from .models import Blog


def show_blog(request):

    if request.method == "POST":
        blog = Blog.objects.create(name=request.POST.get("blog_name"),
                            description=request.POST.get("blog_description"),
                            owner=request.user)

        blog.tags.add(*request.POST.getlist("tag_names"))

    return render(request, "my_blogs.html", {"my_blogs": Blog.objects.filter(owner=request.user.id),
                                             "tags":Tag.objects.all()})



def get_blog(request, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
        print blog.owner
        if request.user.id != blog.owner.id:
            raise PermissionDenied
        return render(request, "detailed_blogs.html",{"blog": blog} )
    except Blog.DoesNotExist:
        raise Http404("We don't have any.")