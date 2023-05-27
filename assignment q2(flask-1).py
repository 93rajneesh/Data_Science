# Q2. Create a simple Flask application to display ‘Hello World!!’. Attach the screenshot of the output in
# Jupyter Notebook.

from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "<h1>hello world</h1>"

if __name__ == "__main__":
    app.run(debug=True)
