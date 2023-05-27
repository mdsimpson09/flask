from flask import Flask, request
from operations import add, sub, mult, div
app = Flask(__name__)

# Put your app in here.
# Build a simple calculator with Flask, which uses URL query parameters to get the numbers to calculate with.

# Make a Flask app that responds to 4 different routes. Each route does a math operation with two numbers, a and b, which will be passed in as URL GET-style query parameters.

# /add
# Adds a and b and returns result as the body.
# /sub
# Same, subtracting b from a.
# /mult
# Same, multiplying a and b.
# /div
# Same, dividing a by b.
# For example, a URL like http://localhost:5000/add?a=10&b=20 should return a string response of exactly 30.

# Write the routes for this but don’t hardcode the math operation in your route function directly. Instead, we’ve provided helper functions for this in the file operations.py:

@app.route("/add")
def do_add():
    """Add a and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)

    return str(result)

@app.route("/sub")
def do_sub():
    """Subtract and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)

    return str(result)

@app.route("/mult")
def do_mult():
    """Multiply a and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)

    return str(result)

@app.route("/div")
def do_div():
    """Divide a and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)

    return str(result)

operators = {
        'add': add,
        'sub': sub,
        'mult': mult,
        'div': div,
        }

@app.route("/math/<oper>")
def do_math(oper):
    """math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)

# ^C(venv) Marlis-MBP:greet Marli$ python3 -m unittest test.py
# ...
# ----------------------------------------------------------------------
# Ran 3 tests in 0.003s

# OK
# (venv) Marlis-MBP:greet Marli$ cd -
# /Users/Marli_1/bootcamp/flask-greet-calc
# (venv) Marlis-MBP:flask-greet-calc Marli$ cd calc
# (venv) Marlis-MBP:calc Marli$ python3 -m unittest test.py
# .....
# ----------------------------------------------------------------------
# Ran 5 tests in 0.004s

# OK
# (venv) Marlis-MBP:calc Marli$ 
