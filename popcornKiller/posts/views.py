from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

# Create your views here.
from .models import Posts
from .forms import PostsForm


def create_view(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}

    # add the dictionary during initialization
    form = PostsForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form']= form
    return render(request, "create_view.html", context)


def list_view(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}

    # add the dictionary during initialization
    context["dataset"] = Posts.objects.all()

    return render(request, "list_view.html", context)


def detail_view(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}

    # add the dictionary during initialization
    context["data"] = Posts.objects.get(id = id)

    return render(request, "detail_view.html", context)


def update_view(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}

    # fetch the object related to passed id
    obj = get_object_or_404(Posts, id = id)

    # pass the object as instance in form
    form = PostsForm(request.POST or None, instance = obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)

    # add form dictionary to context
    context["form"] = form

    return render(request, "update_view.html", context)


def delete_view(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}

    # fetch the object related to passed id
    obj = get_object_or_404(Posts, id = id)

    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to 
        # home page
        return HttpResponseRedirect("/")

    return render(request, "delete_view.html", context)

