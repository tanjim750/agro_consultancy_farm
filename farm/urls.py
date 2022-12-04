from django.urls import path
from . import  views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name= 'index'),
    path('admin-add-products' , views.addproduct, name='p'),
    path('about' , views.about),
    path('services' , views.service),
    path('product' , views.products),
    path('contact' , views.contact),
    path('blog-posts' , views.blogposts),
    path('product/details/<id>/<value>' , views.viewproduct),
    path('shopping/product=<id>' , views.shopping),
    path('blog-post/<id>/<value>' , views.viewblogposts),
    path('comments/<id>' , views.displayComments),
    path('comment-replay' , views.comment_replay),
    path('get-message/' , views.getMessages),
    path('save-message/' , views.saveMessage),
    path('accounts/login/' , views.login_signup),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)