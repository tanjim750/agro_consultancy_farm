import requests,os,re,json,sys
from flask import Flask,redirect,url_for,render_template,request,Response,flash,session,abort , jsonify
from werkzeug.utils import secure_filename           # Used to store filename
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from authlib.integrations.flask_client import OAuth
from wtforms.validators import InputRequired, Length, ValidationError
import random
from datetime import timedelta, datetime
from flask_session import Session
import uuid , time , ipapi

# moduls for login system
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt





app=Flask(__name__)
bcrypt = Bcrypt(app)

# configure user database 
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///files.db"
db.init_app(app)

# store users sessions to database (start)
app.config['SESSION_TYPE'] = 'sqlalchemy'

app.config['SESSION_SQLALCHEMY'] = db

sess = Session(app)
app.config["SESSION_PERMANENT"] = True
app.permanent_session_lifetime = timedelta(days=365)
#app.config["SESSION_COOKIE_NAME"] = "_seq"

#admin login system###########################################################################

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    secretLink = db.Column(db.Text , default="ghtfvhctrytcrex")


class RegisterForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                'That username already exists. Please choose a different one.')


class LoginForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')




@app.route('/admin/login/<value>', methods=['GET', 'POST'])
def login(value):
	secretLink = User.query.filter_by(id= 1).first().secretLink
	if value == secretLink:

		form = LoginForm()
		if form.validate_on_submit():
			user = User.query.filter_by(username=form.username.data).first()
			if user:
				if bcrypt.check_password_hash(user.password, form.password.data):
					login_user(user)
					return redirect("/admin")
			else:
				import smtplib
				import ssl
				from email.message import EmailMessage

				# Define email sender and receiver
				email_sender = 'quinnirene701@gmail.com'
				email_password = 'rrcjnzutcgbpuxqv'
				email_receiver = 'mdtanjim750@gmail.com'

				# Set the subject and body of the email
				subject = 'This is your admin secret link'
				secretLink = str(uuid.uuid4())
				body = f"go to this link: http://127.0.0.1:5000/admin/login/{secretLink}"

				em = EmailMessage()
				em['From'] = email_sender
				em['To'] = email_receiver
				em['Subject'] = subject
				em.set_content(body)

				# Add SSL (layer of security)
				context = ssl.create_default_context()

				# Log in and send the email
				with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
					smtp.login(email_sender, email_password)
					smtp.sendmail(email_sender, email_receiver, em.as_string())
					mylink = User.query.filter_by(id=1).first()
					mylink.secretLink = secretLink
					db.session.commit()
		return render_template('login.html', form=form)
	else:
		return abort(401)




@app.route('/admin/logout')
@login_required
def logout():

		logout_user()
		return redirect("/admin/login/gyuftyygvgvg")




@ app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form=form)







#############################################################################################

# store users sessions to database (end)
class sloganBody(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	image = db.Column(db.Text)
	title = db.Column(db.Text)
	slogan = db.Column(db.Text)
	button1N = db.Column(db.Text)
	button2N = db.Column(db.Text)
	button1L = db.Column(db.Text)
	button2L = db.Column(db.Text)
	creation_date = db.Column(db.DateTime, default= datetime.utcnow)
    
	def __repr__(self) -> str:
		return f"{self.title} {self.slogan} {self.image}"


class deletedSlogan(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	image = db.Column(db.Text)
	title = db.Column(db.Text)
	slogan = db.Column(db.Text)
	button1N = db.Column(db.Text)
	button2N = db.Column(db.Text)
	button1L = db.Column(db.Text)
	button2L = db.Column(db.Text)
	creation_date = db.Column(db.DateTime, default=datetime.utcnow)

	def __repr__(self) -> str:
		return f"{self.title} {self.slogan} {self.image}"

class home(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	contact = db.Column(db.Text)
	brandName = db.Column(db.Text)
	twitter = db.Column(db.Text)
	facebook = db.Column(db.Text)
	linkedin = db.Column(db.Text)
	instagram = db.Column(db.Text)
	banner1T = db.Column(db.Text)
	banner1PD = db.Column(db.Text)
	banner2T = db.Column(db.Text)
	banner2PD = db.Column(db.Text)

	def __repr__(self) -> str:
		return f"{self.contact} {self.brandName}"


class aboutme(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	bd_img = db.Column(db.Text)
	bd_title = db.Column(db.Text)
	button1N = db.Column(db.Text)
	button2N = db.Column(db.Text)
	button1L = db.Column(db.Text)
	button2L = db.Column(db.Text)
	AU_img = db.Column(db.Text)
	Au_text = db.Column(db.Text)
	aU_title = db.Column(db.Text)
	aU_details = db.Column(db.Text)
	banner1T = db.Column(db.Text)
	banner1PD = db.Column(db.Text)
	banner2T = db.Column(db.Text)
	banner2PD = db.Column(db.Text)
	feild1 = db.Column(db.Text )
	feild2 = db.Column(db.Text)

	def __repr__(self) -> str:
		return f"{self.bd_title} {self.aU_details}"

class services(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	img = db.Column(db.Text)
	bd_title = db.Column(db.Text)
	button1N = db.Column(db.Text)
	button2N = db.Column(db.Text)
	button1L = db.Column(db.Text)
	button2L = db.Column(db.Text)
	sr_text = db.Column(db.Text)
	sr_title = db.Column(db.Text)
	sr_details = db.Column(db.Text)
	sr_btn = db.Column(db.Text)
	sr_btnL = db.Column(db.Text)
	banner1T = db.Column(db.Text)
	banner1PD = db.Column(db.Text)
	banner2T = db.Column(db.Text)
	banner2PD = db.Column(db.Text)
	banner3T = db.Column(db.Text)
	banner3PD = db.Column(db.Text)
	banner4T = db.Column(db.Text)
	banner4PD = db.Column(db.Text)
	banner5T = db.Column(db.Text)
	banner5PD = db.Column(db.Text)
	feild1 = db.Column(db.Text )
	feild2 = db.Column(db.Text)

	def __repr__(self) -> str:
		return f"{self.bd_title} {self.aU_details}"

class contactme(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	bd_img = db.Column(db.Text)
	bd_title = db.Column(db.Text)
	button1N = db.Column(db.Text)
	button2N = db.Column(db.Text)
	button1L = db.Column(db.Text)
	button2L = db.Column(db.Text)
	topTx = db.Column(db.Text)
	topTi = db.Column(db.Text)
	conTi = db.Column(db.Text)
	locationT = db.Column(db.Text)
	location = db.Column(db.Text)
	emailT = db.Column(db.Text)
	email = db.Column(db.Text)
	numberT = db.Column(db.Text)
	number = db.Column(db.Text)


	def __repr__(self) -> str:
		return f"{self.bd_title} {self.bd_img}"

class messageme(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text)
	email = db.Column(db.Text)
	subject = db.Column(db.Text)
	message = db.Column(db.Text)
	sent_date = db.Column(db.DateTime, default=datetime.utcnow)

	def __repr__(self) -> str:
		return f"{self.name} {self.message}"


class addproducts(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	productId = db.Column(db.Text)
	img1 = db.Column(db.Text)
	img2 = db.Column(db.Text)
	img3 = db.Column(db.Text)
	name = db.Column(db.Text)
	author = db.Column(db.Text)
	price = db.Column(db.Text)
	offerPrice = db.Column(db.Text)
	rating = db.Column(db.Text)
	offerParsentage = db.Column(db.Text)
	dvTime = db.Column(db.Text)
	certificate = db.Column(db.Text)
	description = db.Column(db.Text)
	efectiveness = db.Column(db.Text)
	star1 = db.Column(db.Integer , default = 0)
	star2 = db.Column(db.Integer , default = 0)
	star3 = db.Column(db.Integer , default = 0)
	star4 = db.Column(db.Integer , default = 0)
	star5 = db.Column(db.Integer , default = 0)
	reviews = db.Column(db.Integer , default = 0)
	time = db.Column(db.DateTime, default=datetime.utcnow)

	def __repr__(self) -> str:
		return f"{self.name} {self.price}"


class review(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	product_id = db.Column(db.Integer)
	rate = db.Column(db.Integer)
	comment = db.Column(db.Text)
	time = db.Column(db.DateTime, default=datetime.utcnow)

	def __repr__(self) -> str:
		return f"{self.rate} {self.comment}"


# # '''

# with app.app_context():
#
# 		review.__table__.drop(db.engine)
# # '''



with app.app_context():
    db.create_all()



app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.config['UPLOAD_PATH'] = 'static/uploads'             # Storage path
def upload_file(file):                                       # This method is used to upload files
        if request.method == 'POST':
                f = request.files['file']
                print(f.filename)
                f.save(secure_filename(f.filename))
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
                return redirect("/")           # Redirect to route '/' for displaying images on fromt end



@app.route("/admin",methods=['GET','POST'])
@login_required
def admin():
	same = messageme.query.all()
	num = 0
	for i in same:
		if i.id not in session:
			num += 1
	footer = home.query.filter_by(id=1).first()
	if request.method == 'POST':
		contact = request.form["contact"]
		brandName = request.form["brandName"]
		twitter = request.form["twitter"]
		facebook = request.form["facebook"]
		linkedin = request.form["linkedin"]
		instagram = request.form["instagram"]
		banner1T = request.form["banner1T"]
		banner2T = request.form["banner2T"]
		banner1PD = request.form["banner1PD"]
		banner2PD = request.form["banner2PD"]
		# save = home(contact = contact,
		# 			brandName = brandName,
		# 			twitter = twitter,
		# 			facebook = facebook,
		# 			linkedin = linkedin,
		# 			instagram = instagram,
		# 			banner1T = banner1T,
		# 			banner1PD = banner1PD,
		# 			banner2T = banner2T,
		# 			banner2PD = banner2PD)
		#
		# db.session.add(save)
		footer.contact = contact
		footer.brandName = brandName
		footer.twitter = twitter
		footer.facebook = facebook
		footer.linkdine = linkedin
		footer.instagram = instagram
		footer.banner1T = banner1T
		footer.banner2T= banner2T
		footer.banner1PD = banner1PD
		footer.banner2PD = banner2PD
		db.session.commit()

		flash("New description has been successfully uploaded")

		return redirect("/admin")

	return render_template("admin.html" , footer = footer, num = num)

@app.route("/admin/slogan",methods=['GET','POST'])
@login_required
def slogan():
	same = messageme.query.all()
	num = 0
	for i in same:
		if i.id not in session:
			num += 1

	main = sloganBody.query.all()


	if request.method == 'POST':
		image = request.files["image"]
		path = '/uploads/'
		filename = secure_filename(image.filename)
		try:
			image.save(os.path.join(app.config['UPLOAD_PATH'], filename))
		except:
			return "There is No image file!! Please Select an Image."
		title = request.form["title"]
		slogan = request.form["slogan"]
		b1n = request.form["b1n"]
		b2n = request.form["b2n"]
		b1l = request.form["b1l"]
		b2l = request.form["b2l"]

		save = sloganBody(image = path+filename,
						  title = title,
						  slogan = slogan,
						  button1N = b1n,
						  button2N = b2n,
						  button1L = b1l,
						  button2L = b2l)
		db.session.add(save)
		db.session.commit()

		flash("Slogan has been successfully uploaded")

		return redirect("/admin/slogan")



	return render_template("slogan.html" , main = main , num = num)

@app.route("/admin/slogan/edit/id=<value>", methods=['GET','POST'])
@login_required
def editSlogan(value):
	same = messageme.query.all()
	num = 0
	for i in same:
		if i.id not in session:
			num += 1
	sloganE = sloganBody.query.filter_by(id=value).first()
	value = value
	if request.method == 'POST':
		img = request.files["image"]
		path = '/uploads/'
		filename = secure_filename(img.filename)
		if len(filename) != 0:
			img.save(os.path.join(app.config['UPLOAD_PATH'], filename))
		title = request.form["title"]
		slogan = request.form["slogan"]
		b1n = request.form["b1n"]
		b2n = request.form["b2n"]
		b1l = request.form["b1l"]
		b2l = request.form["b2l"]

		if len(filename) != 0:
			sloganE.image = path+filename
		sloganE.title = title
		sloganE.slogan = slogan
		sloganE.button1N = b1n
		sloganE.button2N = b2n
		sloganE.button1L = b1l
		sloganE.button2L = b2l

		db.session.commit()
		flash("Slogan has been successfully edited")


	return render_template("editslogan.html", slogan = sloganE , value = value , num = num)

@app.route("/admin/slogan/delete/id=<value>")
@login_required
def deleteSlogan(value):
	same = messageme.query.all()
	num = 0
	for i in same:
		if i.id not in session:
			num += 1
	sloganE = sloganBody.query.filter_by(id=value).first()
	save = deletedSlogan(image=sloganE.image,
					  title=sloganE.title,
					  slogan=sloganE.slogan,
					  button1N=sloganE.button1N,
					  button2N=sloganE.button2N,
					  button1L=sloganE.button1L,
					  button2L=sloganE.button2L)
	db.session.add(save)
	db.session.delete(sloganE)
	db.session.commit()
	return redirect("/admin/slogan")


@app.route("/admin/previous/slogans")
def previous():
	same = messageme.query.all()
	num = 0
	for i in same:
		if i.id not in session:
			num += 1
	main = sloganBody.query.all()

	return render_template("previousslogan.html" , main = main, num= num)


@app.route("/admin/deleted/slogans")
@login_required
def deleted():
	same = messageme.query.all()
	num = 0
	for i in same:
		if i.id not in session:
			num += 1
	main = deletedSlogan.query.all()

	return render_template("deletedslogan.html" , main = main , num =num)

@app.route("/admin/restore/slogan/id=<value>")
@login_required
def restoreSlogan(value):
	sloganE = deletedSlogan.query.filter_by(id=value).first()
	save = sloganBody(image=sloganE.image,
					  title=sloganE.title,
					  slogan=sloganE.slogan,
					  button1N=sloganE.button1N,
					  button2N=sloganE.button2N,
					  button1L=sloganE.button1L,
					  button2L=sloganE.button2L)
	db.session.add(save)
	db.session.delete(sloganE)
	db.session.commit()
	return redirect("/admin/slogan")


@app.route("/")
def index():
	main = sloganBody.query.all()
	footer = home.query.filter_by(id=1).first()
	aboutdt = aboutme.query.filter_by(id=1).first()

	return render_template("index.html" , main = main , footer = footer, aboutdt = aboutdt)

@app.route("/about")
def about():
	main = sloganBody.query.all()
	footer = home.query.filter_by(id=1).first()
	aboutdt = aboutme.query.filter_by(id=1).first()

	return render_template("about.html" , main = main , footer = footer , aboutdt = aboutdt)

@app.route("/admin/about",methods=['GET','POST'])
@login_required
def aboutedit():
	same = messageme.query.all()
	num = 0
	for i in same:
		if i.id not in session:
			num += 1

	aboutdt = aboutme.query.filter_by(id = 1).first()

	if request.method == 'POST':
		bd_img = request.files["bd_img"]
		bd_title = request.form["bd_title"]
		button1N = request.form["button1N"]
		button2N = request.form["button2N"]
		button1L = request.form["button1L"]
		button2L = request.form["button2L"]
		AU_img = request.files["AU_img"]
		Au_text = request.form["Au_text"]
		aU_title = request.form["aU_title"]
		aU_details = request.form["aU_details"]
		banner1T = request.form["banner1T"]
		banner2T = request.form["banner2T"]
		banner1PD = request.form["banner1PD"]
		banner2PD = request.form["banner2PD"]
		path = '/uploads/'
		filename1 = secure_filename(bd_img.filename)
		filename2 = secure_filename(AU_img.filename)
		if len(filename1) != 0:

			bd_img.save(os.path.join(app.config['UPLOAD_PATH'], filename1))
		if len(filename2) != 0:

			AU_img.save(os.path.join(app.config['UPLOAD_PATH'], filename2))
		# save = aboutme(bd_img = path+filename1,
		# 			 bd_title = bd_title,
		# 			 button1N = button1N,
		# 			 button2N = button2N,
		# 			 button1L = button1L,
		# 			 button2L = button2L,
		# 			 AU_img = path+filename2,
		# 			 Au_text = Au_text,
		# 			 aU_title = aU_title,
		# 			 aU_details = aU_details,
		# 			banner1T = banner1T,
		# 			banner1PD = banner1PD,
		# 			banner2T = banner2T,
		# 			banner2PD = banner2PD)
		#
		# db.session.add(save)
		if len(filename1) != 0:
			aboutdt.bd_img = path+filename1
		if len(filename2) != 0:
			aboutdt.AU_img = path+filename2

		aboutdt.bd_title = bd_title
		aboutdt.button1N = button1N
		aboutdt.button2N = button2N
		aboutdt.button1L = button1L
		aboutdt.button2L = button2L

		aboutdt.aU_title = aU_title
		aboutdt.Au_text = Au_text
		aboutdt.aU_details = aU_details
		aboutdt.banner1T = banner1T
		aboutdt.banner2T= banner2T
		aboutdt.banner1PD = banner1PD
		aboutdt.banner2PD = banner2PD
		db.session.commit()

		flash("New description has been successfully updated")

		return redirect("/admin/about")

	return render_template("aboutedit.html", aboutdt = aboutdt , num = num)

@app.route("/services")
def service():
	main = sloganBody.query.all()
	footer = home.query.filter_by(id=1).first()
	aboutdt = aboutme.query.filter_by(id=1).first()
	data = services.query.filter_by(id=1).first()


	return render_template("service.html" , main = main , footer = footer , aboutdt = aboutdt , data = data)

@app.route("/admin/service" , methods=['GET','POST'])
@login_required
def adminservice():
	same = messageme.query.all()
	num = 0
	for i in same:
		if i.id not in session:
			num += 1
	main = sloganBody.query.all()
	footer = home.query.filter_by(id=1).first()

	data = services.query.filter_by(id=1).first()
	if request.method == 'POST':
		img = request.files["img"]
		bd_title = request.form["bd_title"]
		button1N = request.form["button1N"]
		button2N = request.form["button2N"]
		button1L = request.form["button1L"]
		button2L = request.form["button2L"]
		sr_text = request.form["sr_text"]
		sr_title = request.form["sr_title"]
		sr_details = request.form["sr_details"]
		sr_btn = request.form["sr_btn"]
		sr_btnL = request.form["sr_btnL"]
		banner1T = request.form["banner1T"]
		banner3T = request.form["banner3T"]
		banner4T = request.form["banner4T"]
		banner5T = request.form["banner5T"]
		banner1PD = request.form["banner1PD"]
		banner2T = request.form["banner2T"]
		banner2PD = request.form["banner2PD"]
		banner3PD = request.form["banner3PD"]
		banner4PD = request.form["banner4PD"]
		banner5PD = request.form["banner5PD"]

		path = '/uploads/'
		filename = secure_filename(img.filename)


		# save = services(img = path+filename,
		# 				bd_title = bd_title,
		# 				button1N = button1N,
		# 				button2N = button2N,
		# 				button1L = button1L,
		# 				button2L = button2L,
		# 				sr_text = sr_text,
		# 				sr_title = sr_title,
		# 				sr_details = sr_details,
		# 				sr_btn = sr_btn,
		# 				sr_btnL = sr_btnL,
		# 				banner1T = banner1T,
		# 				banner2T = banner2T,
		# 				banner3T = banner3T,
		# 				banner4T = banner4T,
		# 				banner5T = banner5T,
		# 				banner5PD = banner5PD,
		# 				banner4PD = banner4PD,
		# 				banner2PD = banner2PD,
		# 				banner3PD = banner3PD,
		# 				banner1PD = banner1PD)
		# db.session.add(save)
		if len(filename) != 0:
			img.save(os.path.join(app.config['UPLOAD_PATH'], filename))
			data.img = path + filename
		data.bd_title = bd_title
		data.button1N = button1N
		data.button2N = button2N
		data.button1L = button1L
		data.button2L = button2L
		data.sr_text = sr_text
		data.sr_title = sr_title
		data.sr_details = sr_details
		data.sr_btn = sr_btn
		data.sr_btnL = sr_btnL
		data.banner1T = banner1T
		data.banner2T = banner2T
		data.banner3T = banner3T
		data.banner4T = banner4T
		data.banner5T = banner5T
		data.banner5PD = banner5PD
		data.banner4PD = banner4PD
		data.banner2PD = banner2PD
		data.banner3PD = banner3PD
		data.banner1PD = banner1PD

		db.session.commit()

		flash("New description has been successfully updated")

		return redirect("/admin/service")

	return render_template("adminservice.html" , main = main , footer = footer , data = data , num = num)


@app.route("/contact" , methods=['GET','POST'])
def contact():
	main = sloganBody.query.all()
	footer = home.query.filter_by(id=1).first()
	condt = contactme.query.filter_by(id=1).first()
	description = services.query.filter_by(id=1).first()


	if request.method == 'POST':

		name = request.form["name"]
		subject = request.form["subject"]
		email = request.form["email"]
		message = request.form["message"]

		save = messageme(name = name,
						 email = email,
						 subject = subject,
						 message = message)
		db.session.add(save)
		db.session.commit()
		# return "Message has been successfully send"

	return render_template("contact.html" , main = main , footer = footer , condt = condt , description = description)

@app.route("/admin/messages")
@login_required
def messages():
	msg = messageme.query.all()
	m = []
	for i in msg:
		m.append(messageme.query.filter_by(id = i.id).first())

	m.reverse()

	same = messageme.query.all()
	num = 0
	for i in same:
		if i.id not in session:
			num += 1




	return render_template("messages.html" , msg = m , num = num)

@app.route("/admin/read/messages<int:id>")
@login_required
def readmessages(id):
	msg = messageme.query.filter_by(id =id).first()
	session[msg.id] = msg.id
	same = messageme.query.all()
	num = 0
	for i in same:
		if i.id not in session:
			num +=1


	return render_template("viewmesssage.html" , msg = msg , same = same , num = num)

@app.route("/admin/contact" , methods=['GET','POST'])
@login_required
def admincontact():
	same = messageme.query.all()
	num = 0
	for i in same:
		if i.id not in session:
			num += 1
	condt = contactme.query.filter_by(id=1).first()
	if request.method == 'POST':
		bd_img = request.files["bd_img"]
		bd_title = request.form["bd_title"]
		button1N = request.form["button1N"]
		button2N = request.form["button2N"]
		button1L = request.form["button1L"]
		button2L = request.form["button2L"]
		topTx = request.form["topTx"]
		topTi = request.form["topTi"]
		conTi = request.form["conTi"]
		locationT = request.form["locationT"]
		location = request.form["location"]
		emailT = request.form["emailT"]
		email = request.form["email"]
		numberT = request.form["numberT"]
		number = request.form["number"]

		path = '/uploads/'
		filename = secure_filename(bd_img.filename)
		# bd_img.save(os.path.join(app.config['UPLOAD_PATH'], filename))
		# save = contactme(bd_img = path+filename,
		# 		 		 bd_title = bd_title,
		# 		 		 button1N = button1N,
		# 		 		 button2N = button2N,
		# 		 		 button1L = button1L,
		# 		 		 button2L = button2L,
		# 		 		 topTx = topTx,
		# 				 topTi = topTi,
		# 				 conTi = conTi,
		# 				 locationT = locationT,
		# 				 location = location,
		# 				 emailT = emailT,
		# 				 email = email,
		# 				 numberT = numberT,
		# 				 number = number)
		#
		# db.session.add(save)
		if len(filename) != 0:
			bd_img.save(os.path.join(app.config['UPLOAD_PATH'], filename))
			condt.bd_img = path + filename

		condt.bd_title = bd_title
		condt.button1N = button1N
		condt.button2N = button2N
		condt.button1L = button1L
		condt.button2L = button2L
		condt.opTx = topTx
		condt.topTi = topTi
		condt.conTi = conTi
		condt.locationT = locationT
		condt.location = location
		condt.emailT = emailT
		condt.email = email
		condt.numberT = numberT
		condt.number = number

		db.session.commit()

		flash("New description has been successfully updated")

		return redirect("/admin/contact")

	return render_template("admincontact.html" , condt = condt , num = num)

@app.route("/product" , methods=['GET','POST'])
def product():
	main = sloganBody.query.all()
	footer = home.query.filter_by(id=1).first()
	aboutdt = aboutme.query.filter_by(id=1).first()
	description = services.query.filter_by(id=1).first()
	product = addproducts.query.all()

	return render_template("product.html", main=main, product = product, footer=footer, aboutdt=aboutdt, description=description)

@app.route("/product/details/<int:id>/<value>" , methods=['GET','POST'])
def p_details(id,value):
	details = addproducts.query.filter_by(id = id).first()
	# txt = "Integer egestas, orci id condimentum eleifend nibh nisi pulvinar eros vitae ornare massa neque ut orci Nam aliquet lectus sed odio eleifend, at iaculis dolor egestas. Nunc elementum pellentesque augue sodales porta. Etiam aliquet rutrum turpis, feugiat sodales ipsum #consectetur nec."
	# details.description = txt
	# db.session.commit()
	rating = review.query.filter_by(product_id = id).all()
	print(rating)

	import re
	description = []
	efectiveness = []
	for i in range(1,21):
		title = re.search(f'#{i}(.+?)#', details.description)
		text = re.search(f'/{i}(.+?)/', details.description)
		etitle = re.search(f'#{i}(.+?)#', details.efectiveness)
		etext = re.search(f'/{i}(.+?)/', details.efectiveness)
		if title:
			description.append(title.group(1))
		if text:
			description.append(text.group(1))
		if etitle:
			efectiveness.append(etitle.group(1))
		if etext:
			efectiveness.append(etext.group(1))

	d_ln = len(description)
	dcontent = True
	if d_ln == 0:
		dcontent = False

	e_ln = len(efectiveness)
	econtent = True
	if e_ln == 0:
		econtent = False

	if request.method == "POST":
		rate = request.form["rate"]
		comment = request.form["comment"]
		save = review(product_id = id,
					  rate = rate,
					  comment = comment)
		db.session.add(save)
		db.session.commit()





	return render_template("produtsdtl.html",datetime = datetime.utcnow(),rating= rating, details = details ,efectiveness = efectiveness, e_ln = e_ln, econtent = econtent, description= description , dlen = d_ln, dcontent = dcontent)

@app.route("/admin/product" , methods= ["POST", "GET"])
@login_required
def adminproduct():
	same = messageme.query.all()
	num = 0
	for i in same:
		if i.id not in session:
			num += 1

	if request.method == "POST":
		path = '/uploads/'
		productId = str(uuid.uuid1())
		img1 = request.files["img1"]
		img2 = request.files["img2"]
		img3 = request.files["img3"]
		name = request.form["name"]
		author = request.form["author"]
		price = request.form["price"]
		offerPrice = request.form["offerPrice"]
		offerParsentage = request.form["offerParsentage"]
		rating = request.form["rating"]
		dvTime = request.form["dvTime"]
		certificate = request.form["certificate"]
		description = request.form["description"]
		efectiveness = request.form["efectiveness"]

		filename1 = secure_filename(img1.filename)
		img1.save(os.path.join(app.config['UPLOAD_PATH'], filename1))
		filename2 = secure_filename(img2.filename)
		img2.save(os.path.join(app.config['UPLOAD_PATH'], filename2))
		filename3 = secure_filename(img3.filename)
		img3.save(os.path.join(app.config['UPLOAD_PATH'], filename3))


		save = addproducts(img1 = path+filename1,
						   img2 = path+filename2,
						   img3 = path+filename3,
						   productId = productId,
						   name = name,
						   author = author,
						   price = price,
						   offerPrice = offerPrice,
						   offerParsentage = offerParsentage,
						   rating = rating,
						   dvTime = dvTime,
						   certificate = certificate,
						   description = description,
						   efectiveness = efectiveness)

		db.session.add(save)
		db.session.commit()

		flash("Your Product has been Added")


	return render_template("adminproduct.html", num = num)

@app.route("/admin/myproducts")
@login_required
def myproducts():
	products = addproducts.query.all()
	same = messageme.query.all()
	num = 0
	for i in same:
		if i.id not in session:
			num += 1
	return render_template("adminmyproducts.html", products = products ,num = num)

@app.route("/admin/product/edit/id=<int:id>", methods=["POST","GET"])
@login_required
def editproduct(id):
	same = messageme.query.all()
	num = 0
	for i in same:
		if i.id not in session:
			num += 1
	details = addproducts.query.filter_by(id=id).first()
	if request.method == "POST":
		path = '/uploads/'
		productId = str(uuid.uuid1())
		img1 = request.files["img1"]
		img2 = request.files["img2"]
		img3 = request.files["img3"]
		name = request.form["name"]
		author = request.form["author"]
		price = request.form["price"]
		offerPrice = request.form["offerPrice"]
		offerParsentage = request.form["offerParsentage"]
		rating = request.form["rating"]
		dvTime = request.form["dvTime"]
		certificate = request.form["certificate"]
		description = request.form["description"]
		efectiveness = request.form["efectiveness"]

		filename1 = secure_filename(img1.filename)
		if len(filename1) != 0:
			img1.save(os.path.join(app.config['UPLOAD_PATH'], filename1))
			details.img1 = path + filename1

		filename2 = secure_filename(img2.filename)

		if len(filename2) != 0:
			img2.save(os.path.join(app.config['UPLOAD_PATH'], filename2))
			details.img2 = path + filename2

		filename3 = secure_filename(img3.filename)

		if len(filename3) != 0:
			img3.save(os.path.join(app.config['UPLOAD_PATH'], filename3))
			details.img3 = path + filename3

		details.productId = productId
		details.name = name
		details.author = author
		details.price = price
		details.offerPrice = offerPrice
		details.offerParsentage = offerParsentage
		details.rating = rating
		details.dvTime = dvTime
		details.certificate = certificate
		details.description = description
		details.efectiveness = efectiveness

		db.session.commit()
		flash("Your Product has been Updated")


	return render_template("editproduct.html", details = details , num= num)


@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
	response = requests.get('https://api64.ipify.org?format=json').json()
	ip = response["ip"]
	# import ipapi
	response = requests.get(f"http://ip-api.com/json/{ip}").json()
	ln = response['lat']
	lo = response['lon']
	print(response)
	return f'<p>IP Address is : {ip}</p> \n <p>Location: {ln} & {lo}</p> \n '









if __name__=="__main__":
    app.run(debug=True)