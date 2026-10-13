


class Stand:
    def __init__(self, codice, mq, padiglione, prezzo_base):
        self.codice = codice
        self.mq = int(mq)
        self.padiglione = int(padiglione)
        self.prezzo_base = float(prezzo_base)
        self.espositore = None # Al momento della creazione lo stand è vuoto

    def get_prezzo(self):
        # Restituisce il prezzo finale. Per lo Standard è uguale al prezzo base
        return self.prezzo_base

    @property
    def disponibile(self):
        # Verifica se lo stand è libero
        return self.espositore is None

    def __lt__(self, other):
        # Definisce il criterio di 'minore di' per l'ordinamento
        return self.get_prezzo() < other.get_prezzo()

    def __str__(self):
        stato = "Disponibile" if self.disponibile else f"Assegnato a {self.espositore.codice}"
        return (f"{self.codice} {self.mq } {self.padiglione} {self.get_prezzo()} {stato}")