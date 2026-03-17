from models.livre import Livre

class LivreAudio(Livre):
    def __init__(self, id, titre, auteur, duree):
        super().__init__(id, titre, auteur)
        self.duree = duree