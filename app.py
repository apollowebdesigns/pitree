from flask import Flask, render_template, jsonify
from serialtest import get_dist
app = Flask(__name__)
from tree import light_tree, dim_tree
import _thread

def test():
    print('in the thread')

_thread.start_new_thread(test)

@app.route('/start')
def start():
    get_dist()
    return 'Hello World'

@app.route('/stop')
def stop():
    return 'Hello World'

@app.route('/light')
def light():
    light_tree()
    return 'Hello World'

@app.route('/dim')
def dim():
    dim_tree()
    return 'Hello World'

@app.route("/")
def mainapp():
   templateData = {}
   return render_template('index.html', **templateData)


if __name__ == '__main__':
    app.run()
