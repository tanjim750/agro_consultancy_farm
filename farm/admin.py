from django.contrib import admin
from .models import (sloganBody , home ,deletedSlogan , aboutme , services ,
                     contactme , features , addproducts,
                     productimages, contact_page, testimonial,
                     posts, messageme, post_comments,
                     comments_reply)

# Register your models here.

@admin.register(sloganBody)
class sloganbodyAdmin(admin.ModelAdmin):
    list_display = [
         'title','image', 'slogan', 'creation_date'
    ]


@admin.register(home)
class homeAdmin(admin.ModelAdmin):
    list_display = [
        'contact', 'brandName'
    ]

@admin.register(deletedSlogan)
class deletedsloganAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'image', 'slogan', 'creation_date'
    ]


@admin.register(aboutme)
class adminabout(admin.ModelAdmin):
    list_display = [
        "aU_title"
    ]

@admin.register(services)
class adminservice(admin.ModelAdmin):
    list_display = [
        'bd_title','img'
    ]

@admin.register(contact_page)
class contactadmin(admin.ModelAdmin):
    list_display = [
        'top_title', 'image'
    ]

@admin.register(features)
class contactadmin(admin.ModelAdmin):
    list_display = [
        'title', 'image'
    ]

@admin.register(addproducts)
class productsadmin(admin.ModelAdmin):
    list_display = [
        'productId', 'name', 'price', 'thumbnail', 'time'
    ]
@admin.register(productimages)
class productsimagesadmin(admin.ModelAdmin):
    list_display = [
        'product_id','image'
    ]

@admin.register(testimonial)
class admintestimonial(admin.ModelAdmin):
    list_display = [
        'claint_name','profile_picture' , 'background_image'
    ]

@admin.register(posts)
class adminpost(admin.ModelAdmin):
    list_display = [
        'title','post_image1' , 'post_image2', 'background', 'date'
    ]

@admin.register(messageme)
class admin_messages(admin.ModelAdmin):
    list_display = [
        'id','name', 'number', 'message' , 'sent_date'
    ]

@admin.register(post_comments)
class admin_post_comment(admin.ModelAdmin):
    list_display = [
        'name', 'number', 'comment' , 'date'
    ]

@admin.register(comments_reply)
class admin_comments_reply(admin.ModelAdmin):
    list_display = [
        'replyId','name', 'number', 'reply' , 'date'
    ]




