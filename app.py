from flask import Flask, render_template, request, redirect, url_for
from password_generator import generate_password
from password_checker import check_password_strength
from db import save_password, get_blacklisted_passwords

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    length = int(request.form.get('length', 12))
    use_lower = 'lowercase' in request.form
    use_upper = 'uppercase' in request.form
    use_digits = 'digits' in request.form
    use_symbols = 'symbols' in request.form

    password = generate_password(length, use_lower, use_upper, use_digits, use_symbols)
    print(f"Mot de passe généré : {password}") 
    save_password(password, length, use_lower, use_upper, use_digits, use_symbols)

    return render_template('resultat.html', password=password)
     
    

@app.route('/check', methods=['POST'])
def check():
    password = request.form.get('password')
    score, feedback = check_password_strength(password)
    return render_template('resultat.html', password=password, score=score, feedback=feedback)

@app.route('/blacklist')
def blacklist():
    blacklisted = get_blacklisted_passwords()
    return render_template('blacklist.html', blacklisted=blacklisted)

if __name__ == '__main__':
    app.run(debug=True)
