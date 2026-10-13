from stand import Stand


class StandPreseExtra(Stand):
    def __init__(self, codice, mq, padiglione, prezzo_base, prese):
        super().__init__(codice, mq, padiglione, prezzo_base)
        self.prese = int(prese)

    def get_prezzo(self):
        # Sovrascrive il metodo genitore
        # Prezzo base + soprapprezzo del 7% per ogni presa
        return self.prezzo_base * (1+ 0.07 * self.prese)

    def __str__(self):
        # Verifichiamo lo stato di assegnazione (come nella classe base)
        stato = "Disponibile" if self.disponibile else f"Assegnato a {self.espositore.codice}"
        return (f"{self.codice} {self.mq} {self.padiglione} {self.get_prezzo()} {stato}")