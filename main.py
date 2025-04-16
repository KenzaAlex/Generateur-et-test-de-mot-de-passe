from password_generator import generate_password
from password_checker import check_password_strength
from db import save_password, get_blacklisted_passwords
from db import save_password
import sys

def demander_bool(question):
    reponse = input(question + " (o/n) : ").lower()
    return reponse == "o"

def menu():
    while True:
        print("\n===== MENU SECUREPASS =====")
        print("1. Générer un mot de passe")
        print("2. Vérifier un mot de passe")
        print("3. Afficher les mots de passe blacklistés")
        print("4. Quitter")

        choix = input("Choix : ")

        if choix == "1":
            try:
                longueur = int(input("Longueur du mot de passe : "))
                use_lowercase = demander_bool("Inclure des lettres minuscules ?")
                use_uppercase = demander_bool("Inclure des lettres majuscules ?")
                use_digits = demander_bool("Inclure des chiffres ?")
                use_symbols = demander_bool("Inclure des symboles ?")

                password = generate_password(
                    length=longueur,
                    use_lowercase=use_lowercase,
                    use_uppercase=use_uppercase,
                    use_digits=use_digits,
                    use_symbols=use_symbols
                )

                print(f"\n Mot de passe généré : {password}")

                save = demander_bool("Souhaitez-vous l'enregistrer dans la base de données ?")
                if save:
                    save_password(password, longueur, use_lowercase, use_uppercase, use_digits, use_symbols)

            except ValueError:
                print("Veuillez entrer une longueur valide.")

        elif choix == "2":
        
            password = input("Entrez le mot de passe à vérifier : ")
            score, recommandations = check_password_strength(password)

            print(f"\n Score de robustesse : {score}/100")
            if recommandations:
                print("Recommandations :")
                for r in recommandations:
                    print(f" - {r}")
            else:
                print("✅ Mot de passe robuste.")

        elif choix == "3":
            
            blacklist = get_blacklisted_passwords()
            if blacklist:
                print("\n Mots de passe blacklistés :")
                for pwd in blacklist:
                    print(f" - {pwd}")
            else:
                print("✅ Aucun mot de passe dans la blacklist.")
        elif choix == "4":
            print("👋 Merci d’avoir utilisé SecurePass. À bientôt !")
            sys.exit()
        else:
            print(" Choix invalide, réessayez.")

if __name__ == "__main__":
    menu()
