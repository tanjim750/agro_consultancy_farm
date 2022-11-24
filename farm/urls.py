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
    path('blog-post/<id>/<value>' , views.viewblogposts),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)