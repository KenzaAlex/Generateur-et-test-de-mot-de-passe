import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="Secure Pass",
        user="securite",
        password="secure",
        host="localhost",
        port="5432"
    )


def save_password(password, length, use_lowercase, use_uppercase, use_digits, use_symbols):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO passwords (password, length, use_lowercase, use_uppercase, use_digits, use_symbols)
            VALUES (%s, %s, %s, %s, %s, %s);
        """, (password, length, use_lowercase, use_uppercase, use_digits, use_symbols))
        conn.commit()
        print("Mot de passe enregistré dans la base de données.")
    except Exception as e:
        print("Erreur lors de l'enregistrement :", e)
    finally:
        if conn:
            cursor.close()
            conn.close()

def is_password_blacklisted(password):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM listeNoire WHERE password = %s;", (password.lower(),))
        result = cursor.fetchone()
        return result is not None
    except Exception as e:
        print("Erreur de vérification de la liste noire :", e)
        return False
    finally:
        if conn:
            cursor.close()
            conn.close()

def get_blacklisted_passwords():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM listeNoire ORDER BY password;")
        results = cursor.fetchall()
        return [row[0] for row in results]
    except Exception as e:
        print(" Erreur lors de la récupération de la blacklist :", e)
        return []
    finally:
        if conn:
            cursor.close()
            conn.close()