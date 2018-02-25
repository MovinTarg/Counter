from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key='movintarg'

@app.route('/')
def home():
    if 'counter' not in session:
        session['counter']=0
    session['counter']+=1
    return render_template('index.html', counter=session['counter'])

@app.route('/addTwo')
def add2():
    session['counter']+=1
    return redirect('/')

@app.route('/reset')
def rst():
    session['counter']=0
    return redirect('/')

app.run(debug=True)