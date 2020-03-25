from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'hello from Local Master Branch /n hello Git1'
def index2():
    return 'hello from Local Master Branch /n hello Git2'


if __name__=='__main__':
    app.run(debug=True)