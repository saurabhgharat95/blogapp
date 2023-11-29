from django.views import generic
from .models import Blog

class BlogList(generic.ListView):
    queryset = Blog.objects.filter(is_active='1').order_by('-created_date')
    context_object_name = 'blog_list'  # Default: object_list
    paginate_by = 10
    template_name = 'index.html'

class BlogDetail(generic.DetailView):
    model = Blog
    template_name = 'blog_detail.html'




# Create your views here.
