from django.db import models
import uuid
# Create your models here.

class sloganBody(models.Model):
    image = models.ImageField(upload_to='img')
    title = models.CharField(max_length=100)
    slogan = models.TextField()
    button1N = models.CharField(max_length=100)
    button2N = models.CharField(max_length=100)
    button1L = models.CharField(max_length=100)
    button2L = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __repr__(self) -> str:
        return f"{self.title} {self.slogan} {self.image}"


class deletedSlogan(models.Model):
    image = models.ImageField(upload_to='img')
    title = models.CharField(max_length=100)
    slogan = models.TextField()
    button1N = models.CharField(max_length=100)
    button2N = models.CharField(max_length=100)
    button1L = models.CharField(max_length=100)
    button2L = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __repr__(self) -> str:
        return f"{self.title} {self.slogan} {self.image}"


class home(models.Model):
    contact = models.CharField(max_length=100)
    brandName = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    banner1T = models.CharField(max_length=100)
    banner1PD = models.CharField(max_length=100)
    banner2T = models.CharField(max_length=100)
    banner2PD = models.CharField(max_length=100)

    def __repr__(self) -> str:
        return f"{self.contact} {self.brandName}"


class aboutme(models.Model):
	bd_img = models.ImageField(upload_to='img')
	bd_title = models.CharField(max_length=100)
	button1N = models.CharField(max_length=100)
	button2N = models.CharField(max_length=100)
	button1L = models.CharField(max_length=100)
	button2L = models.CharField(max_length=100)
	AU_img = models.ImageField(upload_to='img')
	Au_text = models.TextField()
	aU_title = models.CharField(max_length=100)
	aU_details = models.TextField()
	banner1T = models.CharField(max_length=100)
	banner1PD = models.CharField(max_length=100)
	banner2T = models.CharField(max_length=100)
	banner2PD = models.CharField(max_length=100)


	def __repr__(self) -> str:
		return f"{self.bd_title} {self.aU_details}"


class services(models.Model):
	img = models.ImageField(upload_to='img')
	bd_title = models.CharField(max_length=100)
	button1N = models.CharField(max_length=100)
	button2N = models.CharField(max_length=100)
	button1L = models.CharField(max_length=100)
	button2L = models.CharField(max_length=100)
	sr_text = models.CharField(max_length=100)
	sr_title = models.CharField(max_length=100)
	sr_details = models.TextField()
	sr_btn = models.CharField(max_length=100)
	sr_btnL = models.CharField(max_length=100)
	banner1T = models.CharField(max_length=100)
	banner1PD = models.TextField()
	banner2T = models.CharField(max_length=100)
	banner2PD = models.TextField()
	banner3T = models.CharField(max_length=100)
	banner3PD = models.TextField()
	banner4T = models.CharField(max_length=100)
	banner4PD = models.TextField()
	banner5T = models.CharField(max_length=100)
	banner5PD = models.TextField()


	def __repr__(self) -> str:
		return f"{self.bd_title} {self.aU_details}"

class contactme(models.Model):
	bd_img = models.ImageField(upload_to='img')
	bd_title = models.CharField(max_length=100)
	button1N = models.CharField(max_length=100)
	button2N = models.CharField(max_length=100)
	button1L = models.CharField(max_length=100)
	button2L = models.CharField(max_length=100)
	topTx = models.CharField(max_length=100)
	topTi = models.CharField(max_length=100)
	conTi = models.CharField(max_length=100)
	locationT = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	emailT = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	numberT = models.CharField(max_length=100)
	number = models.CharField(max_length=100)


	def __repr__(self) -> str:
		return f"{self.bd_title} {self.bd_img}"


class features(models.Model):
	image = models.ImageField(upload_to='img')
	top_text = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	description = models.TextField()
	banner_1_title = models.CharField(max_length=100)
	banner_1_details = models.TextField()
	banner_2_title = models.CharField(max_length=100)
	banner_2_details = models.TextField()
	banner_3_title = models.CharField(max_length=100)
	banner_3_details = models.TextField()
	banner_4_title = models.CharField(max_length=100)
	banner_4_details = models.TextField()



	def __repr__(self) -> str:
		return f"{self.title} {self.description}"


class addproducts(models.Model):
	productId = models.UUIDField(primary_key=True ,editable=False)
	thumbnail = models.ImageField(upload_to='img' , null=True , blank=True)
	name = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	price = models.TextField()
	offerPrice = models.TextField()
	rating = models.TextField()
	offerParsentage = models.CharField(max_length=100)
	delivey_Time = models.CharField(max_length=100)
	certificate = models.TextField()
	description = models.TextField()
	efectiveness = models.TextField()
	star1 = models.IntegerField(default = 0)
	star2 = models.IntegerField(default = 0)
	star3 = models.IntegerField(default = 0)
	star4 = models.IntegerField(default = 0)
	star5 = models.IntegerField(default = 0)
	reviews = models.IntegerField(default = 0)
	time = models.DateTimeField(auto_now_add=True)

	def __repr__(self) -> str:
		return f"{self.name} {self.price}"


class productimages(models.Model):
	product_id = models.ForeignKey(addproducts , on_delete=models.CASCADE , editable=False)
	image = models.ImageField(upload_to='img')

class contact_page(models.Model):
	id = models.AutoField(primary_key=True)
	image = models.ImageField(upload_to='img')
	top_title = models.CharField(max_length=100)
	button_1_name = models.CharField(max_length=100)
	button_2_name = models.CharField(max_length=100)
	button_1_link = models.CharField(max_length=100)
	button_2_link = models.CharField(max_length=100)
	contact_box_text = models.CharField(max_length=100)
	contact_box_title = models.CharField(max_length=100)
	conTi = models.CharField(max_length=100)
	location_title = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	email_title = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	number_title = models.CharField(max_length=100)
	number = models.CharField(max_length=100)


	def __repr__(self) -> str:
		return f"{self.top_title}"


class testimonial(models.Model):
	background_image = models.ImageField(upload_to='img', null=True, blank=True)
	profile_picture = models.ImageField(upload_to='img')
	description = models.TextField()
	claint_name = models.CharField(max_length=100)

	def __repr__(self) -> str:
		return f"{self.claint_name} "


class posts(models.Model):
	postId = models.UUIDField(default=uuid.uuid4(), primary_key=True, editable=False)
	background = models.ImageField(upload_to='img', null=True, blank=True)
	button_1_name = models.CharField(max_length=100, null=True, blank=True)
	button_2_name = models.CharField(max_length=100, null=True, blank=True)
	button_1_link = models.CharField(max_length=100, null=True, blank=True)
	button_2_link = models.CharField(max_length=100, null=True, blank=True)
	post_image1 = models.ImageField(upload_to='img', null=True, blank=True)
	post_image2 = models.ImageField(upload_to='img', null=True, blank=True)
	title = models.CharField(max_length=500)
	details = models.TextField()
	date = models.DateTimeField(auto_now_add=True)

	def __repr__(self) -> str:
		return f"{self.title} "

class post_comments(models.Model):
	commentId = models.UUIDField(unique=True, primary_key=True , editable=False)
	postId = models.ForeignKey(posts, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	image = models.ImageField(upload_to='img', default='img/deafult.png')
	number = models.CharField(max_length=100)
	comment = models.TextField()
	date = models.DateTimeField(auto_now_add=True)

	def __repr__(self) -> str:
		return f"{self.name} "


class comments_reply(models.Model):
	replyId = models.AutoField(primary_key=True)
	parent = models.ForeignKey(post_comments, on_delete=models.CASCADE)
	postId = models.ForeignKey(posts, on_delete=models.CASCADE)
	childrens = models.IntegerField(null=True, blank=True)
	name = models.CharField(max_length=100)
	image = models.ImageField(upload_to='img', default='img/deafult.png')
	number = models.CharField(max_length=100)
	reply = models.TextField()
	date = models.DateTimeField(auto_now_add=True)

	def __repr__(self) -> str:
		return f"{self.name} "

class messageme(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	number = models.CharField(max_length=100)
	message = models.TextField()
	sent_date = models.DateTimeField(auto_now_add=True)

	def __repr__(self) -> str:
		return f"{self.name} {self.message}"










