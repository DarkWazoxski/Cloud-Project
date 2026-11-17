from flask import Flask, redirect, url_for, render_template


app = Flask(__name__)
age= 106

@app.route('/home')
def home():
    return render_template('home.html',content = age, lol=("mlor","mlor2","9wd" ))
@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/departments-section')
def departments():
    return render_template('departments-section.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/admin-annonces')
def admin_annonces():
    return render_template('admin-annonces.html')

if __name__=="__main__":
    app.run()