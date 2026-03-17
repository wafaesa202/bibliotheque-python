# Liste qui contient tous les livres
bibliotheque = []

# Ajouter un livre
def ajouter_livre():
    titre = input("Titre : ")
    auteur = input("Auteur : ")

    livre = {
        "id": len(bibliotheque) + 1,
        "titre": titre,
        "auteur": auteur
    }

    bibliotheque.append(livre)
    print("Livre ajouté avec succès !")


# Afficher tous les livres
def afficher_livres():
    if not bibliotheque:
        print("Aucun livre dans la bibliothèque.")
        return

    print("\nListe des livres :")
    for livre in bibliotheque:
        print(f"{livre['id']} - {livre['titre']} - {livre['auteur']}")


# Rechercher un livre
def rechercher_livre():
    titre = input("Titre à rechercher : ")

    for livre in bibliotheque:
        if livre["titre"].lower() == titre.lower():
            print("Livre trouvé :")
            print(f"{livre['id']} - {livre['titre']} - {livre['auteur']}")
            return

    print("Livre non trouvé.")


# Supprimer un livre
def supprimer_livre():
    titre = input("Titre à supprimer : ")

    for livre in bibliotheque:
        if livre["titre"].lower() == titre.lower():
            bibliotheque.remove(livre)
            print("Livre supprimé avec succès !")
            return

    print("Livre non trouvé.")


# Menu principal
def menu():
    while True:
        print("\n===== MENU BIBLIOTHEQUE =====")
        print("1. Ajouter un livre")
        print("2. Afficher tous les livres")
        print("3. Rechercher un livre")
        print("4. Supprimer un livre")
        print("5. Quitter")

        choix = input("Votre choix : ")

        if choix == "1":
            ajouter_livre()
        elif choix == "2":
            afficher_livres()
        elif choix == "3":
            rechercher_livre()
        elif choix == "4":
            supprimer_livre()
        elif choix == "5":
            print("Au revoir !")
            break
        else:
            print("Choix invalide, veuillez réessayer.")


# Lancer le programme
menu()