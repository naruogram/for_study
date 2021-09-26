from flask import Flask, render_template
from flask import request
import selenium_use.test as test
import selenium_use.subject as subject


app = Flask(__name__)
 
@app.route('/',methods =['POST','GET'])
def new():
    html = render_template('new.html')
    return html



@app.route('/send',methods =['POST','GET'])
def use():
    html=render_template('send.html')
    test.selenium()
    return html


# @app.route('/subject',methods =['POST','GET'])
# def get():
#     html=render_template('subject.html')
#     subject.getclass()
#     return html


if __name__ == "__main__":
 app.run()
   