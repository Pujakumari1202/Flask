## Building Url Dynamically
### Variables rules and URL building

from flask import Flask,redirect,url_for

# object of Flask class
app=Flask(__name__)


# Decolator 
@app.route('/')
def welcome():
    return "Welcome to my Flask Learning series2!.."


@app.route('/success/<int:score>')
def success(score):
    return "<html><body><h1>The person has passed and the marks is " + str(score) + "</h1></body></html>"
    


@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed and the marks is " + str(score)


### Result checker
# @app.route('/results/<int:score>')
# def results(score):
#     result=""
#     if score<50:
#         result='fail'
#     else:
#         result='success'
#     return result



## Dynamic URL Building
@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks<50:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result,score=marks))


if __name__=='__main__':
    app.run(debug=True,port=8080)


