## Jinja2 template engine

'''
{%...%} conditions,for loops
{{    }} expressions to print output
{#....#} this is for comments
'''
from flask import Flask, redirect,url_for,render_template,request
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
# dictionary key value pair
#    exp={'score':score,'res':res}
#    return render_template('result.html',result=exp)
   return render_template('result.html',result=res,score=score)



@app.route('/fail/<int:score>')
def fail(score):
   return "The person has failed and the marks is " + str(score)



@app.route('/submit',methods=['POST','GET'])
def submit():
   total_score=0
   if request.method=='POST':
      science=float(request.form['science'])
      maths=float(request.form==['maths'])
      c=float(request.form['c'])
      data_science=float(request.form['datascience'])
      total_score=(science+maths+c+data_science)/4
   res=""
   return redirect(url_for('success',score=total_score))
                  



if __name__=='__main__':
 app.run(debug=True,port=8080)




