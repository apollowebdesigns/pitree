from flask import Flask, render_template, jsonify
from serialtest import SerialClass
app = Flask(__name__)
from tree import light_tree, dim_tree
from multiprocessing import Process

serials = SerialClass()

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
    serials.go = False
    serials.get_dist()
    return 'Hello World'

@app.route('/dim')
def dim():
    serials.go = False
    return 'Hello World'

@app.route("/")
def mainapp():
   templateData = {}
   return render_template('index.html', **templateData)


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
