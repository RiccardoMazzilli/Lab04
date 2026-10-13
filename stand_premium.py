from stand import Stand



class StandPremium(Stand):
    def __init__(self, codice, mq, padiglione, prezzo_base, posizione):
        super().__init__(codice, mq, padiglione, prezzo_base)
        self.posizione = posizione

    def get_prezzo(self):
        # Sovrascrive il metodo genitore
        # prezzo base + sovrapprezzo del 30%
        return self.prezzo_base * 1.30

    def __str__(self):
        stato = "Disponibile" if self.disponibile else f"Assegnato a {self.espositore.codice}"
        return (f"{self.codice} {self.mq} {self.padiglione} {self.get_prezzo()} {stato}")