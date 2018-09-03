from flask import Flask  , session, render_template , request ,redirect ,g ,url_for
import os


app = Flask(__name__)

app.secret_key = os.urandom(24)




@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        if request.form['pass'] == '123'  and request.form['user'] == 'mahmoud':
            session.pop('user',None) #delete session if found
            session['user'] = request.form['user'] #create new  session
            return redirect(url_for('protected')) #go to page
         
    return render_template('index.html')

@app.route('/protected')
def protected():
    if g.user: # cheack for session
        return render_template('protected.html',name=g.user)
    return redirect(url_for('index')) #if not found to got log page 

@app.route('/logout') #logout user
def logout():
    session.pop('user',None)
    return redirect(url_for('protected'))


@app.before_request
def before_request():
    g.user = None # g run for request singel thread
    if 'user' in session:
        g.user = session['user'] #this is glopal var g.user



#logout

if __name__ == "__main__":
    app.run(debug=True)