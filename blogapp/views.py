from django.shortcuts import get_object_or_404
from django.views import generic
from .models import Blog,BlogComments
from .forms import CommentForm
class BlogList(generic.ListView):
    queryset = Blog.objects.filter(is_active='1').order_by('-created_date')
    context_object_name = 'blog_list'  # Default: object_list
    paginate_by = 10
    template_name = 'index.html'

class BlogDetail(generic.DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]

        form = CommentForm()
        blog = get_object_or_404(Blog, pk=pk)
        comments = BlogComments.objects.filter(blog_fk=blog)

        context['blog'] = blog
        context['comments'] = comments
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)

        blog =  Blog.objects.filter(id=self.kwargs['pk'])[0]
        comments = BlogComments.objects.filter(blog_fk=blog)

        context['blog'] = blog
        context['comments'] = comments
        context['form'] = form

        if form.is_valid():
            
            blog_comment = form.cleaned_data['blog_comment']
            
            comment = BlogComments.objects.create(
                blog_comment=blog_comment, blog_fk=blog
            )

            form = CommentForm()
            context['form'] = form
            return self.render_to_response(context=context)
        
            
            
        return self.render_to_response(context=context)



# Create your views here.
