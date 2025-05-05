from flask import Flask, request, jsonify
from flask import Flask, request, jsonify, render_template

from Heding import compute_crossing  # מייבא את הפונקציה שכתבת קודם

app = Flask(__name__)  # יוצר את השרת
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate')
def calculate():
    # קולט את המשתנים מהכתובת (URL)
    vb = float(request.args.get('vb'))
    vr = float(request.args.get('vr'))
    theta = float(request.args.get('theta'))
    D = float(request.args.get('D'))

    # מפעיל את פונקציית החישוב
    result = compute_crossing(vb, vr, theta, D)

    # מחזיר את התוצאה בפורמט JSON
    return jsonify(result)

# גורם לקובץ לרוץ רק אם מפעילים אותו ישירות (ולא בייבוא)
if __name__ == '__main__':
    app.run(debug=True)

