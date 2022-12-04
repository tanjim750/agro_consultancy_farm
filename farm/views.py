from django.shortcuts import render , redirect
from django.http import JsonResponse , HttpResponse
from .models import (sloganBody , home ,deletedSlogan , aboutme , services ,
                     contact_page , features , addproducts,
                     productimages, testimonial, posts,
                     messageme, post_comments, comments_reply,
                     chat,)
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.models import User
from .forms import register_form
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import uuid


# from decimal import Decimal

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


@login_required()
def shopping(request, id):
    details = addproducts.objects.get(productId=id)
    img = details.productimages_set.all()
    print(img)
    context = {'details': details, 'img': img}
    return render(request, 'order_product.html', context)


def contact(request):
    footer = home.objects.get(id=1)
    condt = contact_page.objects.get(id= 1)
    if request.method == 'POST':
        name = request.POST["name"]
        number = request.POST["number"]
        email = request.POST["email"]
        message = request.POST["message"]

        msg = messageme(name=name,
                         email=email,
                         number=number,
                         message=message)
        msg.save()
    context = {'footer':footer, 'condt':condt }
    return render(request, 'contact.html', context)


def blogposts(request):
    footer = home.objects.get(id=1)
    condt = contact_page.objects.get(id= 1)
    post = posts.objects.all()
    # img = posts.objects.get(id=1)

    context = {'footer':footer, 'condt':condt, 'post':post, }

    return render(request, 'blog.html', context)

def viewblogposts(request,id,value):
    footer = home.objects.get(id=1)
    condt = contact_page.objects.get(id= 1)
    post = posts.objects.get(postId= id)
    comments = post.post_comments_set.all()
    number_of_comments = comments.count() + post.comments_reply_set.all().count()
    if request.method == 'POST':
        if request.POST.get('type') == 'rtc':
            if 'name' in request.session and 'number' in request.session:
                name = request.session['name']
                number = request.session['number']
                reply = request.POST['reply']
                get_parent = request.POST['parent']
            else:
                reply = request.POST['reply']
                get_parent = request.POST['parent']
                name = request.POST['name']
                number = request.POST['number']
                request.session['name'] = name
                request.session['number'] = number
            parent = post_comments.objects.get(commentId = get_parent)
            comments_reply.objects.create(parent = parent,
                                              reply = reply,
                                              postId = post,
                                              name = name,
                                              number = number,
                                              )
        elif request.POST.get('type') == 'rtr':
            if 'name' in request.session and 'number' in request.session:
                name = request.session['name']
                number = request.session['number']
                reply = request.POST['replyto']
                get_parent = request.POST['parent']
                get_childrens = request.POST['childrens']
            else:
                reply = request.POST['replyto']
                get_parent = request.POST['parent']
                get_childrens = request.POST['childrens']
                name = request.POST['name']
                number = request.POST['number']
                request.session['name'] = name
                request.session['number'] = number
            parent = post_comments.objects.get(commentId = get_parent)
            # childrens = comments_reply.objects.get(replyId = get_childrens)
            comments_reply.objects.create(parent = parent,
                                              reply = reply,
                                              childrens = get_childrens,
                                              postId = post,
                                              name = name,
                                              number = number,
                                              )
        elif request.POST.get('type') == 'cmnt':
            if 'name' in request.session and 'number' in request.session:
                name = request.session['name']
                number = request.session['number']
                comment = request.POST['comment']
            else:
                name = request.POST['name']
                number = request.POST['number']
                request.session['name'] = name
                request.session['number'] = number
                comment = request.POST['comment']

            post_comments.objects.create(postId = post,
                                     commentId= uuid.uuid4(),
                                    name = name,
                                    number = number,
                                    comment = comment)

    context = {'footer':footer, 'condt':condt, 'post':post , 'comments':comments, 'number_of_comments':number_of_comments }

    return render(request, 'detail.html', context)

def displayComments(request, id):
    post = posts.objects.get(postId=id)
    comments = post.post_comments_set.all()

    return JsonResponse({'comments':list(comments.values())})



def comment_replay(request, ):


    return render(request, 'replay.html')


def getMessages(request):
    messages = chat.objects.all()
    return JsonResponse({"messages":list(messages.values())})

def saveMessage(request):
    if request.method == 'POST':
        message = request.POST['message']

        msg = chat(message = message)
        msg.save()

    return HttpResponse('Message sent successfully')


def login_signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    register = register_form
    if request.method == 'POST':
        if request.POST['formtype'] == 'login':
            username = request.POST['username']
            password = request.POST['password']
            try:
                user = User.objects.get(username=username)
            except:
                print('User Dose not exist')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(request.GET['next'] if 'next' in request.GET else 'index')


            else:
                print('Username or password is wrong')
        if request.POST['formtype'] == 'register':

            form = register_form(request.POST)
            try:
                User.objects.get(username=request.POST['username'])
                messages.error(request, 'Username already exist! Try another one')
            except:
                try:
                    User.objects.get(email=request.POST['email'])
                    messages.error(request, 'Email already exist! Use another one')
                except:
                    if len(request.POST['password1']) >= 6:
                        if (request.POST['password1'] != '123456' or request.POST['password1'] != '654321' or
                            request.POST['password1'] != '0987654321' or request.POST['password1'] != '1234567890' or
                            request.POST['password1'] != '123456789'):
                            if request.POST['password1'] == request.POST['password2']:


                                user = form.save(commit=False)
                                user.username = user.username.lower()
                                user.save()

                                messages.success(request, 'User account was created!')

                                login(request, user)

                                return redirect(request.GET['next'] if 'next' in request.GET else 'index')

                            else:
                                messages.error(
                                    request, 'The two password fields didn’t match.')
                        else:
                            messages.error(
                                request, 'This password is too common.')
                    else:
                        messages.error(
                            request, 'Your password must contain at least 6 characters.')


    conext = {'form':register}
    return render(request , 'login_singup.html',conext)


