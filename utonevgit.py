class Nev:
    def __init__(self,nev,elso,masodik,ujsz1,ujsz2,nem):
        self.nev = nev
        self.elso = elso
        self.masodik = masodik
        self.ujsz1 = ujsz1
        self.ujsz2 = ujsz2
        self.nem = nem
    def __str__(self):
        return f"Utónév: {self.nev}, neme: {self.nem}"

utonevek = []

with open("utonevek/UTONEV.TXT", "rt", encoding="ansi") as f:
    f.readline()
    for sor in f:
        sor = sor.strip().split(";")
        utonevek.append(Nev(sor[0],sor[1],sor[2],sor[3],sor[4],sor[5]))
        
for utonev in utonevek:
    print(utonev) 

adat = 0        
for utonev in utonevek:
    adat += 1
print(adat,"utónévről található adat a forrásban") 

elsok = 0
for sor in utonevek:
    if sor.nem == 'F':
        if sor.elso != "":
            elsok += int(sor.elso)
print(elsok,"férfiról volt adat")

elsokNo = 0
for sor in utonevek:
    if sor.nem == 'N':
        if sor.elso != "":
            elsokNo += int(sor.elso)
print(elsokNo,"nőröl volt adat")

print("Összesen",elsokNo + elsok,"emberről volt adat")
