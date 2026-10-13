# Importiamo tutte le classi
from stand import Stand
from stand_prese_extra import StandPreseExtra
from stand_premium import StandPremium
from espositore import Espositore





class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        # Usiamo dei dizionari per cercare stand ed espositori tramite il loro codice
        self.stand = { }
        self.espositori = { }

    # Getter e Setter per il nome del centro fieristico
    @property
    def nome(self):
        return self.nome

    @nome.setter
    def nome(self, nuovo_nome):
        self.nome = nuovo_nome

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        # TODO

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # TODO

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
