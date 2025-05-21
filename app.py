from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_citizen_data(barcode):
    conn = sqlite3.connect('citizens.db')
    cursor = conn.cursor()
    cursor.execute("SELECT nom, prenom, adresse, date_naissance, photo FROM citoyens WHERE code_barre=?", (barcode,))
    data = cursor.fetchone()
    conn.close()
    return data

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        barcode = request.form['barcode']
        citizen = get_citizen_data(barcode)
        if citizen:
            return render_template('result.html', citizen=citizen)
        else:
            return "Citoyen non trouvé."
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
