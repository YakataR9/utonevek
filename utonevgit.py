class Nev:
    def __init__(self,nev,elso,masodik,ujsz1,ujsz2,nem):
        self.nev = nev
        self.elso = elso
        self.masodik = masodik
        self.ujsz1 = ujsz1
        self.ujsz2 = ujsz2
        self.nem = nem

with open("UTONEV.txt", "rt", encoding="ansi") as f:
    for sor in f:
        
        