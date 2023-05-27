from flask import Flask 

app = Flask(__name__)

# /welcome
# Returns “welcome”
@app.route('/welcome')
def welcome_page():
    """ return "welcome" """
    return """
        <html>
          <body>
            <h1>Welcome!</h1>
          </body>
        </html>
    """

@app.route('/welcome/back')
def welcome_back():
    return "welcome back"
# /welcome/home
# Returns “welcome home”

@app.route('/welcome/home')
def welcome_home():
    return "welcome home"


# /welcome/back
# Return “welcome back”

##to test python3 -m unittest test.py
##have to ^c to get out of developer mode first 
# ^C(venv) Marlis-MBP:greet Marli$ python3 -m unittest test.py
# ...
# ----------------------------------------------------------------------
# Ran 3 tests in 0.003s

# OK
