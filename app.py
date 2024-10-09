from flask import Flask, render_template, request

app = Flask(__name__)

### ERROR HANDLERS ###
@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html'), 404

### INDEX ROUTE ###
@app.route('/')
def index():
    return render_template('index.html')

### DEVICE ROUTES ###
@app.route('/devices', methods=['GET', 'POST'])
def devices():
    if request.method == 'GET':
        return "<p>GET, Devices!</p>"
    if request.method == 'POST':
        return "<p>POST, Devices!</p>"

### ALARM ROUTES ###
@app.route('/alarms', methods=['GET', 'POST'])
def alarms():
    if request.method == 'GET':
        return "<p>GET, Alarms!</p>"
    if request.method == 'POST':
        return "<p>POST, Alarms!</p>"

### VIDEO ROUTES ###
@app.route('/videos', methods=['GET', 'POST'])
def videos():
    if request.method == 'GET':
        return "<p>GET, Videos!</p>"
    if request.method == 'POST':
        return "<p>POST, Videos!</p>"

if __name__ == '__main__':
    app.run(debug=True)