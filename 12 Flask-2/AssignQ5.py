from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>hello world</h1>"

if __name__ == "__main__":
    app.run(debug=True)

@app.route("postman_api", method = ['POST'])
def country_name():
    
