from flask import Flask, render_template
import subprocess

app = Flask(__name__)
mode = None

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/spectrum")
def spectrum():
    subprocess.Popen(['sudo','python', 'python/visualization.py', 'spectrum'], stdout=subprocess.PIPE)
    mode = 'spectrum'
    return ('spectrum')

@app.route("/kill")
def kill():
    global pp
    subprocess.Popen(['killall', 'python'])
    mode = None
    return('off')

if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug=True)
