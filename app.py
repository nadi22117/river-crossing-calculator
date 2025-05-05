from flask import Flask, request, jsonify, render_template
from Heding import compute_crossing

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate')
def calculate():
    vb = float(request.args.get('vb'))
    vr = float(request.args.get('vr'))
    theta = float(request.args.get('theta'))
    D = float(request.args.get('D'))

    result = compute_crossing(vb, vr, theta, D)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=10000)
