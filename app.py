from flask import Flask
from serialtest import get_dist
app = Flask(__name__)

@app.route('/start')
def start():
   get_dist()
   return 'Hello World'

@app.route('/stop')
def stop():
   return 'Hello World'


if __name__ == '__main__':
   app.run()
