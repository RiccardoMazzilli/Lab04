


class Espositore:
    def __init__(self, codice, nome, cognome):
        self.codice = codice
        self.nome = nome
        self.cognome = cognome

    def verifica_identita(self, altro_espositore):
        # Verifica se due espositori sono la stessa persona tramite il codice
        return self.codice == altro_espositore