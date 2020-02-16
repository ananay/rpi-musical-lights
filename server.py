from flask import Flask, render_template
import subprocess

app = Flask(__name__)
mode = 'off'

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/spectrum")
def spectrum():
    subprocess.Popen(['sudo','python', 'python/visualization.py', 'spectrum'], stdout=subprocess.PIPE)
    mode = 'spectrum'
    return ('spectrum')

@app.route("/energy")
def energy():
    subprocess.Popen(['sudo','python', 'python/visualization.py', 'energy'], stdout=subprocess.PIPE)
    mode = 'energy'
    return ('energy')

@app.route("/scroll")
def scroll():
    subprocess.Popen(['sudo','python', 'python/visualization.py', 'scroll'], stdout=subprocess.PIPE)
    mode = 'scroll'
    return ('scroll')


@app.route("/status"):
    return (mode)

@app.route("/kill")
def kill():
    global pp
    subprocess.Popen(['killall', 'python'])
    mode = 'off'
    return('off')

if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug=True)
