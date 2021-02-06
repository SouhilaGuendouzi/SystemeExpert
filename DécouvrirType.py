class BaseConnaisance:
    def __init__(self, Règles, BaseFait):
        self.Règles=Règles
        self.BaseFait=BaseFait
class Regle:
    def __init__(self, Listprémisses, Listconslusions):
        self.Listprémisses=Listprémisses
        self.Listconslusions=Listconslusions
class DécouvrirType:
    def __init__(self,file1,file2):
        self.file1=file1;
        self.file2 = file2;

    def Découvrir(self):
        listPrémisse=[]  #cette liste a pour but d'insérer les prémisses
        listConclusion=[] #cette liste a pour but d'insérer les conclusions
        listBaseFait=[] #cette liste a pour but d'insérer les fait lus par le fichier 2
        f = open(self.file1, "r")
        stop=False
        for x in f:
            un = x.split(":")
            deux =un[1].split(",")
            trois = deux[0].split("SI")
            cET=trois[1].split(" ").count("et") #compter le nombre de ET
            cOU=trois[1].split(" ").count("ou") #compter le nombre de OU
            quatre =trois[1].split("et")
            cinq=trois[1].split("ou")
            six =deux[1].split("ALORS")[1].split(" ");
            for j in six[1]:
                if (j not in listConclusion and j!="\n"):
                    listConclusion.append(j)
            if (len(quatre)==cET+1 and cOU==0):
               for i in quatre:
                  if (i not in listPrémisse):
                    listPrémisse.append(i)
            elif (len(cinq)==cOU+1 and cET==0):
                for i in cinq:
                    if (i not in listPrémisse):
                       listPrémisse.append(i)
            else :
                stop=True
        if (len(listPrémisse)!=0 and stop==False):
              print(listPrémisse)
              print(listConclusion)
              f2= open(self.file2, "r")
              for j in f2:
                  n=j.split("\n")[0]
                  for z in n :
                      if z not in listBaseFait :
                       listBaseFait.append(z)
              R =Regle(listPrémisse,listConclusion)
              BaseConnaisanceA=BaseConnaisance(R,listBaseFait)
              return("RAHA mliha n9adou nabdou l khadma taana ")

        else:
            return ("hna wi ykono les règles fihoum ET w OU maa Ba3de")

c = DécouvrirType("fichier.txt","baseFait.txt")
print(c.Découvrir())