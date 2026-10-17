# Importiamo tutte le classi
from stand import Stand
from stand_prese_extra import StandPreseExtra
from stand_premium import StandPremium
from espositore import Espositore





class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self._nome = nome
        # Usiamo dei dizionari per cercare stand ed espositori tramite il loro codice
        self.stand = { }
        self.espositori = { }

    # Getter e Setter per il nome del centro fieristico
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nuovo_nome):
        self._nome = nuovo_nome

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                for line in f:
                    campi = line.strip().split(",")
                    if not campi or campi[0] == "":
                        continue
                    codice = campi[0]

                    # Per gli Stand (iniziano con ST)
                    if codice.startswith("ST"):
                        mq = campi[1]
                        padiglione = campi[2]
                        prezzo = campi[3]

                        if len(campi) == 4:
                            # Abbiamo uno Stand semplice
                            self.stand[codice] = Stand(codice, mq, padiglione, prezzo)
                        elif len(campi) == 5:
                            info_extra = campi[4]
                            if info_extra.isdigit():
                                # 5 Campi e l'ultimo è un numero, Stand con prese extra
                                self.stand[codice] = StandPreseExtra(codice, mq, padiglione, prezzo, info_extra)
                            else:
                                # 5 Campi e l'ultimo non è un numero, Stand Premium
                                self.stand[codice] = StandPremium(codice, mq, padiglione, prezzo, info_extra)

                    elif codice.startswith("ES"):
                        # Per gli Espositori
                        nome = campi[1]
                        cognome = campi[2]
                        self.espositori[codice] = Espositore(codice, nome, cognome)

        except FileNotFoundError:
            raise FileNotFoundError("Errore: il file non è stato trovato")


    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # Verifica che lo stand esista
        if codice_stand not in self.stand:
            raise ValueError(f"Stand {codice_stand} inesistente")

        # Verifica che l'espositore esista
        if codice_espositore not in self.espositori:
            raise ValueError(f"Espositore {codice_espositore} inesistente")

        stand_target = self.stand[codice_stand]
        espositore_target = self.espositori[codice_espositore]

        # Verifica che lo stand sia disponibile
        if not stand_target.disponibile:
            raise ValueError(f"Stand {codice_stand} non è disponibile")

        # Verifica che l'espositore non abbia già uno stand assegnato
        for s in self.stand.values():
            if s.espositore is not None and s.espositore.codice == espositore_target.codice:
                raise ValueError(f"L'espositore {codice_espositore} ha già lo stand assegnato")

        stand_target.espositore = espositore_target

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        if not self.espositori:
            print("Nessun espositore registrato")
            return

        for esp in self.espositori.values():
            stand_assegnato = None
            # Cerchiamo se c'è uno stand associato a questo espositore (confrontando gli espositori)
            for s in self.stand.values():
                if s.espositore is not None and s.espositore.codice == esp.codice:
                    stand_assegnato = s.codice
                    break

            if stand_assegnato:
                print(f"{esp} Stand assegnato: {stand_assegnato}")
            else:
                print(f"{esp} nessuno Stand assegnato")

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        return sorted(self.stand.values())
