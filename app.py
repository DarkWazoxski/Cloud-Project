from datetime import date, datetime
import os
import uuid
from werkzeug.utils import secure_filename
from flask import Flask, render_template,url_for,redirect,session,request,flash, jsonify
import secrets
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)                                                                                                                                                                                                      



app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

app.secret_key=secrets.token_hex(32)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin1234@localhost:5432/uni_site'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class new(db.Model):
	__tablename__ = 'news'
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	content = db.Column(db.Text, nullable=False)
	date=db.Column(db.Date, default=date.today)
	image=db.Column(db.String(100), nullable=False, default='default.jpg')
	def __init__(self,title,content,date,image):
		self.title=title
		self.content=content
		self.date=date
		self.image=image

class admins(db.Model):
	__tablename__="admins"
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(255), nullable=False)
	password = db.Column(db.String(255), nullable=False)

class department(db.Model):
	__tablename__="departments"
	department_id = db.Column(db.Integer, primary_key=True)
	department_name = db.Column(db.String(100), nullable=False)
	department_description = db.Column(db.Text, nullable=False)
	department_link= db.Column(db.String(1000), nullable=False)






@app.route("/")
def home():
	news= new.query.order_by(new.id.desc()).limit(3).all() 
	return render_template("home.html",news=news)



@app.route("/base")
def base():
	return render_template("base.html")
	
@app.route("/news")
def news():
	news= new.query.all() 
	return render_template("news.html",news=news)
	
@app.route("/departments")
def departments():
	departments= department.query.all()
	return render_template("departments-section.html", departments=departments	)


@app.route("/admin_auth", methods=["POST", "GET"])
def admin_auth():
	if request.method == "POST":
		username= request.form["username"]
		password= request.form["password"]
		
		admin = admins.query.filter_by(username=username,
												password=password).first()
		
		if admin:
			session["password"]=password
			session["username"]=username
			return redirect(url_for("admin_announces", username=username))
		return render_template("admin-authentification.html")
		
	else:
		if 'username' in session:
			username=session['username']
			return redirect(url_for('admin_announces', username=username))
		return render_template("admin-authentification.html")
		
@app.route("/admin_announces/<username>", methods=["POST", "GET"])
def admin_announces(username):
	if 'username' not in session:
		return redirect (url_for("admin_auth"))
	if username != session["username"]:
		return "<h1> page not found </h1>"
	if request.method == "POST":
		print("POST REQUEST RECEIVED!")

		title = request.form["title"]
		content = request.form["content"]
		date = datetime.strptime(
            request.form["date"], "%Y-%m-%d"
        ).date()
		file = request.files.get("image")

		if file and file.filename:
			image = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], image))
		else:
			image = "default.jpg"
		news = new(title=title, content=content, date=date, image=image)
		db.session.add(news)
		db.session.commit()



	news_all= new.query.all()

	
	return render_template("admin-annonces.html",username=username, news_all=news_all)

@app.route("/logout")
def logout():
	session.clear()
	flash("You have been logged out.", "info")
	return redirect(url_for("home"))




@app.after_request
def add_header(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response



@app.route("/delete_news/<news_id>", methods=["POST"])
def delete_news(news_id):
	post=new.query.get_or_404(news_id)
	
	db.session.delete(post)
	db.session.commit()
	return redirect(url_for('admin_announces', username=session["username"]))

@app.route("/edit_news/<news_id>", methods=["GET","POST"])
def edit_news(news_id):
	if 'username' not in session:
		return redirect (url_for("admin_auth"))
	post=new.query.get_or_404(news_id)

	if request.method=="POST":
		post.title = request.form["title"]
		post.content = request.form["content"]
		post.date = datetime.strptime(
            request.form["date"], "%Y-%m-%d"
        ).date()
		file = request.files.get("image")

		if file and file.filename:
			image = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], image))
			post.image=image

		db.session.commit()
	
		return redirect(url_for("admin_announces", username=session["username"]))
	

	return render_template("edit-announce.html", username=session["username"],news=post)
	

if __name__=="__main__":
	app.run(debug=True)