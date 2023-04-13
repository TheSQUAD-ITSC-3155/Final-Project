from flask import Flask, render_template
app = Flask(__name__)

app = Flask(__name__)

@app.route('/')
def index():  
    return render_template('login.html')

@app.get('/newAccount')
def list_all_movies():
    return render_template('newAccount.html')

@app.get('/home')
def list_all_movies():
    return render_template('home.html')

@app.get('/createpost')
def list_all_movies():
    return render_template('createpost.html')

@app.get('/account')
def list_all_movies():
    return render_template('account.html')

if __name__ == "__main__":
    app.run(debug = True)