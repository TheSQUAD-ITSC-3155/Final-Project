from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():  
    return render_template('index.html')

@app.route('/home', methods=['POST', 'GET'])
def goHome():
    return render_template('home.html')

@app.route('/createpost', methods=['POST', 'GET'])
def postcreate():
    return render_template('createpost.html')

@app.route('/account', methods=['POST', 'GET'])
def createA():
    return render_template('account.html')
'''
@app.get('/newAccount')
def newA():
    return render_template('newAccount.html')

@app.get('/home')
def goHome():
    return render_template('home.html')

@app.post('/createpost')
def postcreate():
    return render_template('createpost.html')

@app.get('/account')
def createA():
    return render_template('account.html')
'''
if __name__ == "__main__":
    app.run(debug = True)