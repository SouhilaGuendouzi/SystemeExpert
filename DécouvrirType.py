from typing import Type


class Regle:
    Listprémisses: list
    Listconclusions: list
    mode :None

    def __init__(self, mode ,Listprémisses, Listconslusions):
        self.Listprémisses = Listprémisses
        self.Listconslusions = Listconslusions
        self.mode=mode


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
            cET = trois[1].split(" ").count("ET")  # compter le nombre de ET
            cOU = trois[1].split(" ").count("OU")  # compter le nombre de OU
            quatre = trois[1].split("ET")
            cinq = trois[1].split("OU")
            six = deux[1].split("ALORS")[1]
            sept = six.split("ET")
            for j in sept:
                if (j not in listConclusion):
                    listConclusion.append(j)
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
                R = Regle("ET",LISTp, LISTc)
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
                R = Regle("OU",LISTp, LISTc)
                listRègles.append(R)
            else:
                stop = True
        if (stop == False):  # pas de conflit on passe à l'étape suivante ; extraction de la base de fait
            f2 = open(self.file2, "r")
            for j in f2:
                n = j.split("\n")[0]
                if n not in listBaseFait:
                         listBaseFait.append(n)
            BaseConnaisanceA = BaseConnaisance(listRègles, listBaseFait)
            return BaseConnaisanceA
        else:
            return None
class chainage:
    typeChainage =None
    baseConnaissance:BaseConnaisance

    def __init__(self,typeChainage,baseConnaissance):
        self.typeChainage=typeChainage
        self.baseConnaissance=baseConnaissance

    def chainage_avant(self, input):
            stop =False
            stop1=False
            BaseRèglesCopie=self.baseConnaissance.Règles
            if (input in self.baseConnaissance.BaseFait):
                stop=True
                print("trouvééé")
            else:
                while (len(BaseRèglesCopie)!=0 and stop==False):
                    cpt =0
                    for i in BaseRèglesCopie:
                        cpt=cpt+1
                    for i in BaseRèglesCopie:
                        stop1 = False
                        if i.mode=="ET":
                           for j in i.Listprémisses:
                              if (stop1==False):
                                 s = j.split(" ")
                                 s=s[1]
                                 if (self.baseConnaissance.BaseFait.count(s)==0):
                                     stop1=True
                                     print(s,"not in")
                           if (stop1==False) :
                               for j in i.Listconslusions:
                                   s = j.split(" ")
                                   s =s[1].split("\n")
                                   s=s[0]
                                   if (self.baseConnaissance.BaseFait.count(s)==0):
                                       self.baseConnaissance.BaseFait.append(s)
                                       if (s==input):
                                           stop = True
                                           print(input,"est prouvée")
                                           BaseRèglesCopie.remove(i)
                        elif i.mode=="OU":
                            for j in i.Listprémisses:
                                s = j.split(" ")
                                s = s[1]
                                if (stop1 == False):
                                    if (self.baseConnaissance.BaseFait.count(s)!=0):
                                        stop1 = True
                                if (stop1 == True):
                                    for j in i.Listconslusions:
                                        s = j.split(" ")
                                        s = s[1].split("\n")
                                        s = s[0]
                                        if (self.baseConnaissance.BaseFait.count(s)==0):
                                            self.baseConnaissance.BaseFait.append(s)
                                            if (s==input):
                                                stop = True
                                                print(input,"est prouvée")
                                                BaseRèglesCopie.remove(i)
                        else :print("mode inconnu")
                    if (cpt==len(BaseRèglesCopie)):
                        stop=True
                        print("on ne peux pas prouvez cette fait")
    def chainage_avant_baseFait(self):
        stop = False
        stop1 = False
        BaseRèglesCopie = self.baseConnaissance.Règles
        while (len(BaseRèglesCopie) != 0 and stop == False):
                cpt = 0
                for i in BaseRèglesCopie:
                    cpt = cpt + 1
                for i in BaseRèglesCopie:
                    stop1 = False
                    if i.mode == "ET":
                        for j in i.Listprémisses:
                            if (stop1 == False):
                                s = j.split(" ")
                                s = s[1]
                                if (self.baseConnaissance.BaseFait.count(s) == 0):
                                    stop1 = True
                        if (stop1 == False):
                            for j in i.Listconslusions:
                                s = j.split(" ")
                                s = s[1].split("\n")
                                s = s[0]
                                if (self.baseConnaissance.BaseFait.count(s) == 0):
                                    self.baseConnaissance.BaseFait.append(s)
                                    BaseRèglesCopie.remove(i)
                    elif i.mode == "OU":
                        for j in i.Listprémisses:
                            s = j.split(" ")
                            s = s[1]
                            if (stop1 == False):
                                if (self.baseConnaissance.BaseFait.count(s) != 0):
                                    stop1 = True
                            if (stop1 == True):
                                for j in i.Listconslusions:
                                    s = j.split(" ")
                                    s = s[1].split("\n")
                                    s = s[0]
                                    if (self.baseConnaissance.BaseFait.count(s) == 0):
                                        self.baseConnaissance.BaseFait.append(s)
                                        BaseRèglesCopie.remove(i)
                    else:
                        print("mode inconnu")
                if (cpt == len(BaseRèglesCopie)):
                    stop = True

c = DécouvrirType("fichier.txt", "baseFait.txt")
BaseConnaisanceB = c.Découvrir()
if BaseConnaisanceB!=None:
      #print(BaseConnaisanceB.Règles[0].Listconslusions) #j'étais entrain de faire le test
      ch=chainage(1,BaseConnaisanceB)
      ch.chainage_avant("amine")
      ch.chainage_avant_baseFait()
      BaseConnaisanceB.BaseFait.remove('') #j'ai supprimer l'espace
      print(BaseConnaisanceB.BaseFait)
else :
    print("on a pas traiter ce cas")
