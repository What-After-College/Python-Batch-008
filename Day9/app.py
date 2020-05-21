from flask import Flask
app=Flask(__name__)
@app.route('/')
def home():
    return "hellojhhuhsfufhjbvj"
@app.route('/hello/welcom')
def welcome():
    return "hello welcome"
@app.route('/<name>')
def dyn(name):
    return "hii {}".format(name)

if __name__=='__main__':
    app.run(debug=True)
