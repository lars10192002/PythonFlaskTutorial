from flask import Flask
from flask import render_template
import random
app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index_extend.html')

@app.route('/item')
def item():

    return render_template('item.html')
# def shop():

#     books = [{'name':'java','price':300},{'name':'ruby','price':400},{'name':'python','price':200}]
#     return render_template( 'shop.html', **locals())


# def index():
#     title = 'python key && value'
#     author = 'Luca'
#     rand = random.randint(0,2)
#     return render_template( 'index.html', **locals())

@app.route('/user/<name>')
def get_name(name):
    return render_template('user.html', name = name)

def do_index_class(index):
    if index % 3 == 0:  return 'line'
    else: return ''
def do_border_class(index):
    return 'border'
    # if index % 1 == 0:  return 'border'
    # else: return ''
app.add_template_filter(do_index_class,'index_class')
app.add_template_filter(do_border_class,'border_class')

if __name__ == "__main__":
    app.run(debug=True,port=2080)