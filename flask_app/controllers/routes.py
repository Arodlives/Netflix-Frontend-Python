
from flask_app import app
from flask import render_template, redirect, session, request, flash, url_for,Flask






@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup/registration' ,methods=['POST'])
def reroutetostep1():
    #page  that  shows  stepone  register  html
    return render_template('/signupregistration.html')

@app.route('/signup/regform')
def reroutestep2of3():
    #pre filled email from landing page then password 
    return render_template('signupregform.html')



@app.route('/signup/')
def reroutetoplan():
    #just  displays you're on  step two after  clicking next leads  to  planform 
    return render_template('/signup.html')

@app.route('/signup/platform')
def routetopayment():
    #displays all payment  plans  and  description along with pricing
    return redirect('/paymentPicker')

@app.route('/paymentPicker')
def routetonetflixmainpage():
    #cc,paypal,giftcode
    return redirect('/maincontent')


@app.route('/signup/creditoption')
def insertcc():
    pass

@app.route('/signup/paypaloption')
def instertpaypal():
    pass

@app.route('/signup/giftoption')
def insertgiftcard():
    pass



