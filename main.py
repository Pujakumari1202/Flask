## Integrate HTML with Flask
## HTTP verb GET And POST
from flask import Flask,render_template,url_for,redirect,request


app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')



@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    return render_template('result.html',result=res)



@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed and the marks is " + str(score)


# ### Result checker HTML page
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        ## convert string to float
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total_score=(science+maths+c+data_science)/4
    res=""
    return redirect(url_for('success',score=total_score))

    
    

if __name__=='__main__':
    app.run(debug=True,port=8080)