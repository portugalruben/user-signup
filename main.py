from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

# The previuos code just initializes flask and provides the app object to be run.
# With last 5 lines (after @app.route("/")) it is a fully fledged program.

@app.route('/login', methods=['POST','GET'])
def login():
    # Next 5 lines request the info from the a form inside the login.html file.
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password_verify = request.form['password-verify']
        email = request.form['email']
        
        # Once all the 4 variables are in, we proceed to validate the input.
        # The specifications require that the first 3 are not null strings,
        # certain lengths for usr and pwrd, equivalence of pwrds, and valid not null email.
        
        if (len(username) < 3) or (len(username) > 20):
            error_username = "That's not a valid username"
            return render_template('login.html', username=username, email=email, error_username=error_username)
        
        if (len(password) < 3) or (len(password) > 20):
            error_password = "That's not a valid password"
            return render_template('login.html', username=username, email=email, error_password=error_password)
        
        if password != password_verify:
            error_verify = "Passwords don't match"
            return render_template('login.html', username=username, email=email, error_verify=error_verify)
        
        if email:
            if not ((email.count("@") == 1) and (email.count(".") == 1)):
                error_email = "That's not a valid email"
                return render_template('login.html', username=username, email=email, error_email=error_email)
            if (len(email) < 3) and (len(email) > 20):
                error_email = "That's not a valid email"
                return render_template('login.html', username=username, email=email, error_email=error_email)
        else:
            #return redirect("/welcome")
            return render_template('welcome.html', username=username)
        
        #return redirect("/welcome")
        return render_template('welcome.html', username=username)
        
""" 
@app.route("/welcome", methods=['POST', 'GET'])
def welcome():
    if request.method == 'POST':
        username = request.form['username']
        return render_template('welcome.html', username=username)
"""
        

#This is the first function that I added. It was returning: "Hello, user-signup"
@app.route("/")
def index():

    return render_template('login.html')

if __name__ == '__main__':
    app.run()
