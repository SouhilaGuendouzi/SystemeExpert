from typing import Type


class Regle:
    Listprémisses: list
    Listconclusions: list

    def __init__(self, Listprémisses, Listconslusions):
        self.Listprémisses = Listprémisses
        self.Listconslusions = Listconslusions


class BaseConnaisance:
    Règles: list[Regle]
    BaseFait: Type[list]

    def __init__(self, Règles, BaseFait):
        self.Règles = Règles
        self.BaseFait = BaseFait


class DécouvrirType:
    def __init__(self, file1, file2):
        self.file1 = file1;
        self.file2 = file2;

    def Découvrir(self):
        listPrémisse = []    # cette liste a pour but d'insérer les prémisses
        listConclusion = []  # cette liste a pour but d'insérer les conclusions
        listBaseFait = []    # cette liste a pour but d'insérer les fait lus par le fichier 2
        listRègles = []      # cette liste a pour but d'insérer les règles
        f = open(self.file1, "r")
        stop = False
        for x in f:
            listConclusion.clear()
            listPrémisse.clear()
            un = x.split(":")
            deux = un[1].split(",")
            trois = deux[0].split("SI")
            cET = trois[1].split(" ").count("et")  # compter le nombre de ET
            cOU = trois[1].split(" ").count("ou")  # compter le nombre de OU
            quatre = trois[1].split("et")
            cinq = trois[1].split("ou")
            six = deux[1].split("ALORS")[1]
            sept = six.split("et")
            for j in sept:  # hna khdamt b j[1] bah matadkhoulich "\n" maahoum
                if (j[1] not in listConclusion):
                    listConclusion.append(j[1])

            if (len(quatre) == cET + 1 and cOU == 0):
                for i in quatre:
                    if (i not in listPrémisse):
                        listPrémisse.append(i)
                LISTp = []
                LISTc = []
                for t in listPrémisse:
                    LISTp.append(t)
                for k in listConclusion:
                    LISTc.append(k)
                R = Regle(LISTp, LISTc)
                listRègles.append(R)
            elif (len(cinq) == cOU + 1 and cET == 0):
                for i in cinq:
                    if (i not in listPrémisse):
                        listPrémisse.append(i)
                LISTp=[]
                LISTc=[]
                for t in listPrémisse:
                    LISTp.append(t)
                for k in listConclusion:
                    LISTc.append(k)
                R = Regle(LISTp, LISTc)
                listRègles.append(R)
            else:
                stop = True
        if (stop == False):  # pas de conflit on passe à l'étape suivante ; extraction de la base de fait
            f2 = open(self.file2, "r")
            for j in f2:
                n = j.split("\n")[0]
                for z in n:
                    if z not in listBaseFait:
                        listBaseFait.append(z)
            BaseConnaisanceA = BaseConnaisance(listRègles, listBaseFait)

            return BaseConnaisanceA

        else:
            return None
c = DécouvrirType("fichier.txt", "baseFait.txt")
BaseConnaisanceB = c.Découvrir()
if BaseConnaisanceB!=None:
      print(BaseConnaisanceB.Règles[0].Listconslusions) #j'étais entrain de faire le test
else :
    print("on a pas traiter ce cas")
