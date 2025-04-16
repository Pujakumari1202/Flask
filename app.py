from  flask import Flask
app=Flask(__name__)


# Decorator to create a route
@app.route('/')
def welcom():
    return 'Welcome to my Flask Learning series'



# starting point of our program
if __name__=='__main__':
    app.run()