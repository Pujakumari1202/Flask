from  flask import Flask
app=Flask(__name__)


# Decorator to create a route
@app.route('/')
def welcom():
    return 'Welcome to my Flask Learning series!..'


@app.route('/students')
def students():
    return "Welcome to my Flask Learning series guys!"



# starting point of our program
if __name__=='__main__':
    app.run(debug=True,port=8080)