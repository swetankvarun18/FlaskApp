from flask import Flask,redirect, url_for, request, render_template, make_response, session,escape 

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!  " 
"""
@app.route('/blog/<guest>')
def show_blog(guest):
    return 'Blog Number %s' % guest

@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'Revision Number %f' % revNo

@app.route('/user/<int:score>/')
def hello_user(score):
    if name == 'admin':
        return redirect(url_for('hello'))
    else:
        return redirect(url_for('show_blog',guest = name))
#@app.route('/location/<path:/home/swetank/>')
#def locate(/home/swetank):
#    return 'location is '

if __name__ == "__main__":
    app.add_url_rule('/hello','hello',hello)
    app.run(host ='0.0.0.0',port = 5000,debug=True)

@app.route("/success/<name>")
def success(name):
    return 'welcome %s ' % name
@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name = user))


@app.route('/hello/<int:score>')
def hello_name(score):
#    return '<html><body><h1>Hello world!</h1></body></html>'
     return render_template('hello.html',marks = score)


@app.route('/result')
def result():
    dict = {'phy':50, 'che':60, 'maths':70}
    return render_template('result.html',result = dict)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/')
def student():
    return render_template('student.html')

@app.route('/result', methods = ['POST','GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html",result = result)

#flask cookies
@app.route('/')
def index():
    return render_template('cookie.html')
@app.route('/setcookie', methods = ['POST','GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']

    resp = make_response(render_template('readcookie.html'))
    resp.set_cookie('userID', user)
    return resp
@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return '<h1>welcome '+name+'</h1>'

# flask session

app.secret_key = 'I need to win the world!'

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return 'Logged in as ' + username + '<br>' + \
        "<b><a href = '/logout'>click here to log out</a></b>"
    return "You are not logged in <br><a href = '/login'></b>" + \
        "click here to log in</b></a>"
@app.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for("index"))
    return '''
    <form action = "" method = "POST">
      <p><input type = text name = username /></p>
      <p><input type = submit value = Login /></p>
    </form>
    '''
@app.route('/logout')
def logout():
    #remove the username form the session if it is there
    session.pop('username',None)
    return redirect(url_for('index'))

#flashing messages

@app.route('/')
def index():
    return render_template('index.html')

"""


if __name__ == '__main__':
    app.run('0.0.0.0',debug = True)
