from  flask import Flask
app=Flask(__name__)


@app.route('/')
def welcom():
    return 'Welcome to my Flask Learning series'


if __name__=='__main__':
    app.run()