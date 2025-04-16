from db import is_password_blacklisted
import string

def check_password_strength(password):
    score = 0
    recommandations = []

    if len(password) >= 12:
        score += 30
    elif len(password) >= 8:
        score += 20
    else:
        score += 10
        recommandations.append("Augmenter la longueur à au moins 12 caractères.")

    if any(c.islower() for c in password):
        score += 15
    else:
        recommandations.append("Ajouter des lettres minuscules.")
    
    if any(c.isupper() for c in password):
        score += 15
    else:
        recommandations.append("Ajouter des lettres majuscules.")
    
    if any(c.isdigit() for c in password):
        score += 15
    else:
        recommandations.append("Ajouter des chiffres.")
    
    if any(c in string.punctuation for c in password):
        score += 15
    else:
        recommandations.append("Ajouter des symboles spéciaux.")

    
    if is_password_blacklisted(password):
        score = 5
        recommandations.append("Ce mot de passe est trop courant (blacklisté dans la base).")

    return min(score, 100), recommandations
