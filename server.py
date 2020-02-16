from flask import Flask, render_template
import subprocess

app = Flask(__name__)
mode = 'off'

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/spectrum")
def spectrum():
    subprocess.Popen(['killall', 'python'])
    subprocess.Popen(['sudo','python', 'python/visualization.py', 'spectrum'], stdout=subprocess.PIPE)
    mode = 'spectrum'
    return ('spectrum')

@app.route("/energy")
def energy():
    subprocess.Popen(['killall', 'python'])
    subprocess.Popen(['sudo','python', 'python/visualization.py', 'energy'], stdout=subprocess.PIPE)
    mode = 'energy'
    return ('energy')

@app.route("/scroll")
def scroll():
    subprocess.Popen(['killall', 'python'])
    subprocess.Popen(['sudo','python', 'python/visualization.py', 'scroll'], stdout=subprocess.PIPE)
    mode = 'scroll'
    return ('scroll')

@app.route("/lightson")
def lights_on():
    subprocess.Popen(['killall', 'python'])
    subprocess.Popen(['sudo','python', 'python/visualization.py', 'scroll'], stdout=subprocess.PIPE)
    mode = 'lights_on'
    return ('lights_on')

@app.route("/status")
def status():
    return (mode)

@app.route("/kill")
def kill():
    global pp
    subprocess.Popen(['killall', 'python'])
    mode = 'off'
    return('off')

if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug=True)
