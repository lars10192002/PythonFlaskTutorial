#encoding:utf-8 
from flask import Flask,url_for,redirect
app = Flask(__name__)

# @app.route('/')
# def index():
#   urll=(url_for('news',id='99999'))
#   return '反轉的內容是%s' % urll

# @app.route('/news/<id>') #反轉
# def news(id):
#       return u'請求的參數是 :' %id

# @app.route('/')
# def index():
#     print("首先訪問了index()這個視圖！")
#     urll = url_for('user_login')
#     return redirect(urll)

# @app.route('/user_login')
# def user_login():
#   return "This is Login page ,Please login"


@app.route('/user/<name>')
def get_user(name):
  return "get name from : "+ name

@app.route('/news/<int:id>')
def get_news(id):
  return "get news from : "+ str(id)

#HW
@app.route('/')
def index():
  urll=(url_for('my_list',id='99999'))
  return '反轉的內容是%s' % urll


@app.route('/list/<id>')
def my_list(id):
      return 'list'%id

if __name__ == '__main__':
  app.run(port=2080,debug=True)