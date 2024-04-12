class Nev:
    def __init__(self,nev,elso,masodik,ujsz1,ujsz2,nem):
        self.nev = nev
        self.elso = elso
        self.masodik = masodik
        self.ujsz1 = ujsz1
        self.ujsz2 = ujsz2
        self.nem = nem

utonevek = []

with open("utonevek/UTONEV.TXT", "rt", encoding="ansi") as f:
    f.readline()
    for sor in f:
        sor = sor.strip().split(";")
        utonevek.append(Nev(sor[0],sor[1],sor[2],sor[3],sor[4],sor[5]))
        
