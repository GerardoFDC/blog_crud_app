from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from activite.forms import BlogForm
from activite.models import Blog
# Create your views here.


def bienvenue(request):
    return HttpResponse('<h1> <center>Bienvenue à vous! <center> </h1>')

def index (request):
    return render (request, 'activite/index.html')

def about (request):
    return render (request, 'activite/about.html')    

def project (request):
    return render (request, 'activite/project.html')   

    
def staff (request):
    return render (request, 'activite/staff.html')   

def contact (request):
    return render (request, 'activite/contact.html')             




def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
           
            blog = form.save()
           
            return redirect('blog-detail', blog.id)

    else:
        form = BlogForm()

    return render(request,
            'activite/blog_create.html',
            {'form': form})




def blog_detail(request, blog_id):  
    blog = get_object_or_404(Blog, id=blog_id)  
    return render(request,
          'activite/blog_detail.html',
          {'blog': blog}) 



         
def blog_list(request):  
   blogs = Blog.objects.all()
   return render(request,
           'activite/blog_list.html',  
           {'blogs': blogs})  



def blog_update(request, id):
    blog = Blog.objects.get(id=id)

    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
          
            form.save()
           
            return redirect('blog-detail', blog.id)
    else:
        form = BlogForm(instance=blog)

    return render(request,
                'activite/blog_update.html',
                {'form': form})


def blog_delete(request, id):
    blog = Blog.objects.get(id=id) 

    if request.method == 'POST':
       
        blog.delete()
        
        return redirect('blog-list')

    return render(request,
                    'activite/blog_delete.html',
                    {'blog': blog})              