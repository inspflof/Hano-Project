from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()

class Tour():vwd fsf
    def __init__(self,nb_tour,composition=None):
        self.nb_tour=nb_tour
        self.composition=composition


    def get_tour(self):
        return self.nb_tour
    

    def get_compo(self):
        return self.composition
    
    def get_all(self):
        return self.nb_tour,self.composition



def creer_pile():
    """retourne une pile vide pile"""
    return []


def empiler(pile,elem):
    """empile elem sur pile et retourne pile"""
    pile.append(elem)
    return pile

def depiler(pile):
    """depile un element, le retourne et le supprime"""
    x=pile.pop()
    return x,pile

def est_vide(pile):
    """verifie si une pile est vide et retourne true ou false"""
    if len(pile)==0:
        return True
    return False



def creation_hanoï(nb_palettes):
    """creer une tour hanoï"""
    f=[]
    for i in range(1,nb_palettes+1):
        f.append(i)
    tour1=Tour(1,f)
    tour2=Tour(2)
    tour3=Tour(3)
    return [tour1,tour2,tour3]

def resolution_hanoï(tours,nb_palettes,compo_og=None):
    f=[]
    for i in range(1,nb_palettes+1):
        f.append(i)
    hanoï=tours
    t1,t2,t3=Tour.get_compo([hanoï[0]]),Tour.get_compo([hanoï[1]]),Tour.get_compo([hanoï[2]])
        
    # return tours,nb-



x=creation_hanoï(5)
print(Tour.get_all(x[0]))
print(Tour.get_all(x[1]))
print(Tour.get_all(x[2]))
print(x)








