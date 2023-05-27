from flask import Flask
from flask import request

app = Flask(__name__) # create variable- app  and Flask(__name__) is duddler
@app.route("/")
def hello_world():
    return "<h1> hello Duniya </h1>"

@app.route("/raj")
def hello_world1():
    return "<h1> HELLO WORLD 2 </h1>"

@app.route("/raj2")
def hello_world2():
    return "<h1>HELLO world3</h2?"

@app.route("/h")
def hello():
    print("hjf")

@app.route("/test")
def test():
    # return f"<h1>sum is {65+223}</h1>"
    # or 
    a = 43+134
    return "sum is {}".format(a)

# take input  
# format- http://127.0.0.1:5000/test2/?x=rajneesh
# step1: import request class
# step2: create func
@app.route("/test2/")
def test2():
    data = request.args.get('x')
    return "This is data input from url: {}".format(data)


if __name__ == "__main__":
    app.run(debug = True )
