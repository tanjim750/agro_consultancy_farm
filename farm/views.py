from django.shortcuts import render
from .models import (sloganBody , home ,deletedSlogan , aboutme , services ,
                     contact_page , features , addproducts,
                     productimages, testimonial, posts )
import uuid
# Create your views here.

def index(request):
    footer = home.objects.get(id = 1)
    carousel = sloganBody.objects.all()
    about = aboutme.objects.get(id = 1)
    service = services.objects.get(id = 1)
    feature = features.objects.get(id = 1)
    products = addproducts.objects.all()
    condt = contact_page.objects.get(id=1)
    testimonia_image = testimonial.objects.get(id=1)
    testimonia_data = testimonial.objects.all()
    context = {'footer':footer , 'main':carousel ,
               'about':about , 'service':service ,
               'feature':feature , 'products': products,
               'condt':condt , 'testimonia_data':testimonia_data,
               'testimonia_image':testimonia_image}
    return render(request, 'index.html', context)


def addproduct(request):
    if request.method == "POST":
        productId = str(uuid.uuid4())
        images = request.FILES.getlist("images")
        Thumbnail = request.FILES["thumbnail"]
        name = request.POST.get("name")
        author = request.POST.get("author")
        price = request.POST.get("price")
        offerPrice = request.POST.get("offerPrice")
        offerParsentage = request.POST.get("offerParsentage")
        rating = request.POST.get("rating")
        dvTime = request.POST.get("dvTime")
        certificate = request.POST.get("certificate")
        description = request.POST.get("description")
        efectiveness = request.POST.get("efectiveness")



        productData = addproducts(thumbnail = Thumbnail,
                                  productId = productId,
                                  name=name,
                                  author=author,
                                  price=price,
                                  offerPrice=offerPrice,
                                  offerParsentage=offerParsentage,
                                  rating=rating,
                                  delivey_Time=dvTime,
                                  certificate=certificate,
                                  description=description,
                                  efectiveness=efectiveness)

        productData.save()
        id = addproducts.objects.get(productId= productId)
        for img in images:
            image = productimages(product_id = id,
                                  image = img)
            image.save()



    return  render(request, 'adminproduct.html')


def about(request):
    footer = home.objects.get(id=1)
    aboutdt = aboutme.objects.get(id = 1)

    context = {'aboutdt':aboutdt , 'footer':footer}
    return render(request , 'about.html' , context)

def service(request):
    footer = home.objects.get(id=1)
    data = services.objects.get(id = 1)
    testimonia_image = testimonial.objects.get(id=1)
    testimonia_data = testimonial.objects.all()
    context = {'footer':footer ,"data" :data ,
               'testimonia_image':testimonia_image, 'testimonia_data':testimonia_data}
    return render(request, 'service.html', context)

def products(request):
    footer = home.objects.get(id=1)
    product = addproducts.objects.all()
    feature = features.objects.get(id = 1)
    context = {'footer': footer, "product": product , 'feature':feature}
    return render(request, 'product.html', context)

def viewproduct(request, id , value):
    details = addproducts.objects.get(productId = id)
    img = details.productimages_set.all()
    print(img)
    context = {'details':details , 'img':img}
    return render(request, 'produtsdtl.html',context)

def contact(request):
    footer = home.objects.get(id=1)
    condt = contact_page.objects.get(id= 1)
    context = {'footer':footer, 'condt':condt }
    return render(request, 'contact.html', context)


def blogposts(request):
    footer = home.objects.get(id=1)
    condt = contact_page.objects.get(id= 1)
    post = posts.objects.all()
    img = posts.objects.get(id=1)
    context = {'footer':footer, 'condt':condt, 'post':post, 'img':img}

    return render(request, 'blog.html', context)

def viewblogposts(request,id,value):
    footer = home.objects.get(id=1)
    condt = contact_page.objects.get(id= 1)
    post = posts.objects.get(postId= id)
    context = {'footer':footer, 'condt':condt, 'post':post }

    return render(request, 'detail.html', context)








