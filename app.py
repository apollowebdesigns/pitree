from flask import Flask, render_template, jsonify
from serialtest import get_dist
app = Flask(__name__)
from tree import light_tree, dim_tree
from multiprocessing import Process

def test(arg):
    print('in the thread')

def create_process():
    return Process(target=get_dist)

p = create_process()

@app.route('/start')
def start():
    light_tree()
    return 'Hello World'

@app.route('/stop')
def stop():
    dim_tree()
    return 'Hello World'

@app.route('/light')
def light():
    p.start()
    return 'Hello World'

@app.route('/dim')
def dim():
    p.join()
    return 'Hello World'

@app.route("/")
def mainapp():
   templateData = {}
   return render_template('index.html', **templateData)


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
