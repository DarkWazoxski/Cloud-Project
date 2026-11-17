from flask import Flask, redirect, request, url_for, render_template, session
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)

age= 106

@app.route('/')
@app.route('/base')
def base():
    return render_template('base.html')
@app.route('/home')
def home():
    return render_template('home.html',content = age, lol=("mlor","mlor2","9wd" ))

@app.route('/departments')
def departments():
    return render_template('departments-section.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/admin_authentication', methods=['POST', 'GET'])
def admin_authentication():
    if request.method == "POST":
        username= request.form['username']
        session['username'] = username 
        return redirect(url_for('admin_announces', username=username))
    else:
         if 'username' in session:
            username = session['username']
            return redirect(url_for('admin_announces', username=username))
         return render_template('admin-authentification.html')

@app.route('/admin-announces/<username>')
def admin_announces(username):
    if 'username' not in session:
        return redirect(url_for('admin_authentication'))
    if username != session['username']:
        return redirect(url_for('admin_authentication'))
    username = session['username']
    return render_template('admin-annonces.html', username=username)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('admin_authentication'))

@app.after_request
def add_no_cache(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

if __name__=="__main__":
    app.run()