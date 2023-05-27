# <!-- Q4. Create a “/welcome” route to display the welcome message “Welcome to ABC Corporation” and a “/”
# route to show the following details:
# Company Name: ABC Corporation
# Location: India
# Contact Detail: 999-999-9999 -->

from flask import Flask

app = Flask(__name__)

@app.route("/")
def Company_name():
    return '''Company Name: ABC Corporation
    Location: India 
    Contact Detail: 999-999-9999'''
@app.route("/welcome")
def welcome():
    return "Welcome to ABC Corporation"

if __name__ =="__main__":
    app.run(debug=True,port=8000)