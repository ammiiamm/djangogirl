from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect

def post_list(request):
    #posts = Post.objects.all()
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'post_list.html', {'posts':posts})

def post_new(request):
    form = PostForm(request.POST)
    if request.method == "POST":
        print('this is post request method')
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()  #save to database
            return redirect('post_detail', pk=post.pk)
            #return redirect('post_list')
    #else:
        #clear form
        #print('no post')
    return render(request, 'post_new.html',{'form':form})

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk) #if not found, return 404
    return render(request, 'post_detail.html', {'post': post})

def post_edit(request,pk):
    post = get_object_or_404(Post, pk=pk) #if not found, return 404
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()  #save to database
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        
    return render(request, 'post_new.html', {'form': form})