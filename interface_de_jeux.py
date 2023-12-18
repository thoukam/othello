from tkinter import*
from PIL import ImageTk,Image
from subprocess import call
import webbrowser

root=Tk()

def lancer_jeux():
    pass
    #interface_homme_homme.run()
#fonction d'aide qui utilise le lien vers le site contenant les regles du jeux 
def regle_du_jeux():
    webbrowser.open_new("https://www.eothello.com/")

#fonction pour lancer le jeux Homme-Homme
def Homme_Homme():
    call(["python","interface_homme_homme.py"])

#fonction pour lancer le jeux Homme-machine
def Homme_machine():
    call(["python","ouverture.py"])


largeur_fenetre=790
hauteur_fenetre=650
largeur_ecran=root.winfo_screenwidth()#largeur de mon ecran
hauteur_ecran=root.winfo_screenheight()#hauteur de mon ecran
#coordonnées x,y pour positionné la fenetre au centre de mon ecran
x_coordonne=(largeur_ecran/2)-(largeur_fenetre/2)
y_coordonne=(hauteur_ecran/2)-(hauteur_fenetre/2)

root.geometry("%dx%d+%d+%d" %(largeur_fenetre,hauteur_fenetre,x_coordonne,y_coordonne))
root.title("OTHELLO")
root.configure(background="#808080")
root.iconbitmap("photo\\societe.ico")
root.resizable(False,False)

#image de font de la fenetre d'acceuil
image_a=ImageTk.PhotoImage(Image.open("photo\\othello.jpg"))
image_b=ImageTk.PhotoImage(Image.open("photo\\Othello2_modifier.png"))
l1=Label(root,image=image_a, border=0,relief=SUNKEN,bg="#272727").place(x=0,y=140,width=790,height=700)
l1=Label(root,image=image_b, border=0,relief=SUNKEN,bg="#272727").place(x=0,y=0,width=790,height=200)

#btnjeux= Button(root, text="jouer", font=("Arial", 16), bg="#483D88", fg="white", command=lancer_jeux).pack()

#creation d'un menu
mainmenu=Menu(root)
#premier menu avec ces attributs ou actions
first_menu=Menu(mainmenu,tearoff=0)
first_menu.add_command(label="Homme vs Homme",command=Homme_Homme)
    #sous menu
sous_menu=Menu(first_menu,tearoff=0)
first_menu.add_cascade(label="Homme vs Machine",underline=0,menu=sous_menu)
sous_menu.add_command(label=" Facile", command=Homme_machine)
sous_menu.add_command(label=" Dificile")
first_menu.add_separator()
first_menu.add_command(label="Quitter",command=root.quit)#pour quitter la fenetre

#deuxieme menu avec ces attributs ou fonction qui definie le niveau de jeux homme vs machine
second_menu=Menu(mainmenu,tearoff=0)
second_menu.add_command(label="Facile")
second_menu.add_command(label="Difficile")

#troisiéme menu avec ces attributs ou actions
autres_options_menu =Menu(mainmenu, tearoff=0)
autres_options_menu.add_command(label="Annuler le dernier coup")
autres_options_menu.add_command(label="statistique de jeux")
autres_options_menu.add_command(label="Enregistrer la partie")
autres_options_menu.add_command(label="Charger une partie")

parametre_menu=Menu(mainmenu,tearoff=0)
parametre_menu.add_command(label="parametre du son")
parametre_menu.add_command(label="Changer le thème")
parametre_menu.add_command(label="style du tableau")
parametre_menu.add_command(label="score en direct")

#menu aide et regles de jeux
aide_menu=Menu(mainmenu,tearoff=0)
aide_menu.add_command(label="Aide",command=regle_du_jeux)

#affiche les menus
mainmenu.add_cascade(label="Jeux",menu=first_menu)
mainmenu.add_cascade(label="options", menu=autres_options_menu)
mainmenu.add_cascade(label="Parametres", menu=parametre_menu)
mainmenu.add_cascade(label="Aide/Règles du jeu", menu=aide_menu)

#boucle principale
root.config(menu=mainmenu)
root.mainloop()