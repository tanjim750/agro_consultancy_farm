from django.shortcuts import render , redirect
from django.http import JsonResponse , HttpResponse
from .models import (sloganBody , home ,deletedSlogan , aboutme , services ,
                     contact_page , features , addproducts,
                     productimages, testimonial, posts,
                     messageme, post_comments, comments_reply,
                     chat,reply , profile)
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.models import User
from .forms import register_form
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import make_password
import uuid


from collections import OrderedDict
from operator import getitem


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
    info = ''
    if request.user.is_authenticated:
        info = profile.objects.get(user = request.user)

    context = {'footer':footer , 'main':carousel ,
               'about':about , 'service':service ,
               'feature':feature , 'products': products,
               'condt':condt , 'testimonia_data':testimonia_data,
               'testimonia_image':testimonia_image,'info': info}
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
    info = profile.objects.get(user = request.user)
    context = {'aboutdt':aboutdt , 'footer':footer, 'info':info}
    return render(request , 'about.html' , context)

def service(request):
    footer = home.objects.get(id=1)
    data = services.objects.get(id = 1)
    testimonia_image = testimonial.objects.get(id=1)
    testimonia_data = testimonial.objects.all()
    info = profile.objects.get(user = request.user)
    context = {'footer':footer ,"data" :data ,
               'testimonia_image':testimonia_image, 'testimonia_data':testimonia_data,
               'info':info}
    return render(request, 'service.html', context)

def products(request):
    footer = home.objects.get(id=1)
    product = addproducts.objects.all()
    feature = features.objects.get(id = 1)
    info = profile.objects.get(user = request.user)
    context = {'footer': footer, "product": product , 'feature':feature, 'info':info}
    return render(request, 'product.html', context)

def viewproduct(request, id , value):
    details = addproducts.objects.get(productId = id)
    img = details.productimages_set.all()
    info = profile.objects.get(user = request.user)
    context = {'details':details , 'img':img, 'info':info}
    return render(request, 'produtsdtl.html',context)


@login_required()
def shopping(request, id):
    details = addproducts.objects.get(productId=id)
    img = details.productimages_set.all()

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
    info = profile.objects.get(user = request.user)
    context = {'footer':footer, 'condt':condt, 'info':info }
    return render(request, 'contact.html', context)


def blogposts(request):
    footer = home.objects.get(id=1)
    condt = contact_page.objects.get(id= 1)
    post = posts.objects.all()
    # img = posts.objects.get(id=1)
    info = profile.objects.get(user = request.user)

    context = {'footer':footer, 'condt':condt, 'post':post, 'info':info }

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
    info = profile.objects.get(user = request.user)

    context = {'footer':footer, 'condt':condt, 'post':post , 'comments':comments,
               'number_of_comments':number_of_comments, 'info':info }

    return render(request, 'detail.html', context)

def displayComments(request, id):
    post = posts.objects.get(postId=id)
    comments = post.post_comments_set.all()

    return JsonResponse({'comments':list(comments.values())})



def comment_replay(request, ):


    return render(request, 'replay.html')


def getMessages(request):
    user = User.objects.get(username=request.user)
    messages = user.chat_set.all()
    try:
        number_msg= reply.objects.get(user = user)
        if messages.count() == number_msg.number_of_message:
            numberOfmsg = number_msg.number_of_message - 1
        else:
            number_msg.number_of_message = messages.count()
            number_msg.save()
            numberOfmsg = number_msg.number_of_message
    except:
        data = reply(user = user,
                     number_of_message = messages.count())
        data.save()
        numberOfmsg = number_msg.number_of_message
    count = messages.count()
    return JsonResponse({"messages":list(messages.values()) , "numberOfmsg":numberOfmsg, "count":count})


def AdmingetMessages(request, user):
    user_msg = User.objects.get(username=user)
    messages = user_msg.chat_set.all()
    # numbersOfMsg = messages.count
    return JsonResponse({"messages":list(messages.values())})

def saveMessage(request):
    if request.method == 'POST':
        message = request.POST['message']
        type = request.POST['type']
        user = User.objects.get(username=request.user)
        msg = chat(message = message,
                   user= user,
                   type = type)
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
                pass

            user = authenticate(request, username=username, password=password)

            if user.is_superuser:
                messages.error(request, 'Username or password is wrong')
            else:
                if user is not None:
                    login(request, user)
                    return redirect(request.GET['next'] if 'next' in request.GET else 'index')


                else:
                    messages.error(request,'Username or password is wrong')
        if request.POST['formtype'] == 'register':
            username = request.POST['username'].lower()
            email = request.POST['email']
            password1 = make_password(request.POST['password1'])



            username_border = ""
            email_border = ""
            password1_border = ""
            password2_border = ""
            username_error = ""
            email_error = ""
            password1_error = ""
            password2_error = ""

            try:
                User.objects.get(username=username)
                username_error = 'Username already info! Try another one'
                username_border = "red"
            except:
                try:
                    User.objects.get(email=email)
                    email_error = 'Email already info! Use another one'
                    email_border = "red"
                except:
                    valid_emails = open('farm/valid_emails.txt', 'r')
                    read_emails = valid_emails.read().splitlines()
                    for valid_email in read_emails:
                        if valid_email in email:
                            if len(request.POST['password1']) >= 6:
                                if (request.POST['password1'] != 123456 or request.POST['password1'] != 654321 or
                                    request.POST['password1'] != 987654321 or request.POST['password1'] != 1234567890 or
                                    request.POST['password1'] != 123456789):
                                    if request.POST['password1'] == request.POST['password2']:
                                        data = User(username = username,
                                                    email = email,
                                                    password = password1)

                                        data.save()

                                        user = authenticate(request, username=username, password=request.POST['password1'])

                                        login(request, user)
                                        return redirect(request.GET['next'] if 'next' in request.GET else '/setup-profile-information')

                                    else:
                                        password2_error  = 'The two password fields didn’t match.'
                                        password2_border = "red"
                                else:
                                    password1_error = 'This password is too common.'
                                    password1_border = "red"
                            else:
                                password1_error = 'Your password must contain at least 6 characters.'
                                password1_border = "red"
                        else:
                            email_border = "red"
                            email_error = 'You are using spam email ! please use valid email.'

            conext = {'ub':username_border, 'eb':email_border,
                    'p1b':password1_border, 'p2b':password2_border,
                    'ue':username_error, 'ee':email_error, 'p1e':password1_error,
                    'p2e':password2_error}
            return render(request, 'login_singup.html', conext)
    return render(request , 'login_singup.html')

@login_required()
def logout_user(request):
    logout(request)
    return redirect('index')



def showMyMessages(request):
    if request.user.is_superuser:
        users = {}
        message = chat.objects.all().order_by('-sent_date')
        print(message)
        for u in message:
            if users.get(str(u.user)) is None and u.type == 1:
                users[str(u.user)]={'profile':str(u.user), 'message':u.message, 'date':u.sent_date, 'unseen':chat.objects.filter(user =u.user, type = 1, seen= 0).count()}
        anyUser = None
        context = {'users':users, 'anyUser':anyUser}
        return render(request, 'my_messages.html', context)
        # return JsonResponse(users)
    else:
        return HttpResponse('Invalid Url')

def user_messages(request):
    if request.user.is_superuser:
        users = {}
        message = chat.objects.all().order_by('-sent_date')
        print(message)
        for u in message:
            if users.get(str(u.user)) is None and u.type == 1:
                users[str(u.user)] = {'profile': str(u.user), 'message': u.message, 'date': u.sent_date,
                                      'unseen': chat.objects.filter(user=u.user, type=1, seen=0).count()}

    return JsonResponse(users)

def showUserMessages(request, user):
    if request.user.is_superuser:
        unseen = chat.objects.filter(user =User.objects.get(username=user) , seen= 0)
        for s in unseen:
            s.seen = 1
            s.save()
        users = {}
        message = chat.objects.all().order_by('-sent_date')
        for u in message:
            if users.get(str(u.user)) is None and u.type == 1:
                users[str(u.user)]={'profile':str(u.user), 'message':u.message, 'date':u.sent_date, 'unseen':chat.objects.filter(user =u.user, type=1, seen= 0).count()}
        if request.method == 'POST':
            message = request.POST['message']
            type = request.POST['type']
            save_msg = User.objects.get(username=user)
            msg = chat(message = message,
                       user= save_msg,
                       type = type)
            msg.save()
        anyUser = user
        context = {'users':users, 'anyUser':anyUser}
    else:
        return HttpResponse('Invalid Url')
    return render(request, 'my_messages.html', context)
@login_required()
def profile_info(request):
    header = home.objects.get(id=1)
    #print('done')
    info = profile.objects.get(user=request.user)
    if request.method == 'POST':
        if request.POST['type'] == 'info':
            name = request.POST['name']
            number = request.POST['number']
            date_of_birth = request.POST['date_of_birth']
            gender = request.POST['gender']
            address = request.POST['address']
            nationality = request.POST['nationality']

            info.name = name
            info.number = number
            info.date_of_birth = date_of_birth
            info.gender = gender
            info.address = address
            info.nationality = nationality
            info.save()

            messages.success(request, 'Your Profile has been successfully saved')

        elif request.POST['type'] == 'image':
            image = request.FILES['image']
            info.image = image
            info.save()

    cotext = {'footer':header, 'info':info}
    return render(request, 'profile_info.html', cotext)




