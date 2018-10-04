from flask import Flask, request, redirect, render_template
import os


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/signup")
def index():
    return render_template('index.html')




def valid_length(input):
    for i in input:
        if i == " ":
            return False
    return (len(input) >= 3 and len(input)<=20)

def match(password, verify):
    return password == verify

def valid_email(email):
    if email == "":
        return True
    if not valid_length(email):
        return False
    periods = 0
    at_symbols = 0
    for i in email:
        if i == ".":
            periods += 1
        elif i == "@":
            at_symbols += 1
    return periods == 1 and at_symbols == 1
    




@app.route("/signup", methods=['POST'])

def process():
    username = request.form['username']
    password = request.form['password']
    verify= request.form['verify']
    email = request.form['email']
    
    username_error = ""
    Password_len= ""
    match_error = ""
    email_error = ""
    
    if valid_length(username)and valid_length(password)and \
        match(password,verify) and valid_email(email):
            return render_template('welcome.html', username= username)
            

    if not valid_length(username):
        username_error = "The Username is Invalid"
        print(username_error)
    if not valid_length(password):
        Password_len = "Password need be between 3-20 char"
        print(Password_len)
    if not match(password,verify):
        match_error = "Passwords do not match"
        print(match_error)
    if not valid_email(email):
        email_error= "Invalid Email"
        print(email_error)

    return render_template('index.html', username_error=username_error, Password_len=Password_len, match_error=match_error, email_error=email_error) 
    

app.run()





