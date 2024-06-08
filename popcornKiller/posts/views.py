from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from .models import Post
from .forms import PostForm

from users.models import User

@csrf_exempt
def create_view(request):
    if request.method == 'POST':
        title = request.POST['title']
        email = request.POST['email']
        writer = get_object_or_404(User, email=email)
        movie = request.POST['movie']
        content = request.POST['content']
        post = Post(title=title, writer=writer, movie=movie, content=content)
        post.save()
        return HttpResponseRedirect('/posts')
    else:
        return render(request, "create_view.html")


def list_view(request):
    if request.method == 'GET':
        # dictionary for initial data with 
        # field names as keys
        context = {
            "Post": Post.objects.all()
        }

        # add the dictionary during initialization

        return render(request, "list_view.html", context)


def detail_view(request, id):
    if request.method == 'GET':
        # dictionary for initial data with 
        # field names as keys
        context = {
            "Post": Post.objects.get(id=id)
        }

        # add the dictionary during initialization

        return render(request, "detail_view.html", context)


@csrf_exempt
def update_view(request, id):
    if request.method == 'PUT':
        # dictionary for initial data with 
        # field names as keys
        context = {}

        # fetch the object related to passed id
        obj = get_object_or_404(Post, id=id)

        # pass the object as instance in form
        form = PostForm(request.POST or None, instance=obj)

        # save the data from the form and
        # redirect to detail_view
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/" + id)

        # add form dictionary to context
        context["Post"] = form

        return render(request, "update_view.html", context)


@csrf_exempt
def delete_view(request, id):
    # dictionary for initial data with 
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Post, id=id)

    if request.method == "DELETE":
        # delete object
        obj.delete()
        # after deleting redirect to 
        # home page
        return HttpResponseRedirect("/")

    return render(request, "delete_view.html", context)
