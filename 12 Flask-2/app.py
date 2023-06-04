from flask import Flask,request,render_template ,jsonify

app = Flask(__name__)

@app.route("/",methods = ['GET','POST'])
def home_page():
    return render_template('index.html')
@app.route("/math", methods = ['POST']) #data pass through post method
def math_operation():
    if(request.method == "POST"):
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if(ops =='add'):
            r = num1+num2
            result1 = f'the sum of  {num1} and {num2} is {r}'
        if(ops == 'subtract'):
            r = num1 - num2
            result1 = f'answer is {r}'
        if(ops =='multiply'):
            r = num1 * num2
            result1 = f'multipy of {num1} and {num2} is {r}'
        if(ops == 'divide'):
            r = num1/num2
            result1 = f'ans is {r}'
    return render_template('results.html',result = result1) #insert the value of result1 on result.html

@app.route("/data_passed_by_used_of_postman", methods = ['POST']) #data pass through post method
def math_operation1():
    if(request.method == "POST"):
        ops = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        if(ops =='add'):
            r = num1+num2
            result1 = f'the sum of  {num1} and {num2} is {r}'
        if(ops == 'subtract'):
            r = num1 - num2
            result1 = f'answer is {r}'
        if(ops =='multiply'):
            r = num1 * num2
            result1 = f'multipy of {num1} and {num2} is {r}'
        if(ops == 'divide'):
            r = num1/num2
            result1 = f'ans is {r}'
    return jsonify(result1) #jsonify used for json 
       



if __name__ == "__main__":
    app.run(debug=True)