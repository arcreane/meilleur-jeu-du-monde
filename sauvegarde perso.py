from tkinter import *
import os

projet = Tk()
projet.geometry ("1280x720")
projet.minsize (1280, 720)
projet.maxsize (1280, 720)

projet.rowconfigure(0, weight=1)
projet.columnconfigure(0, weight=1)



def genre():
    genre = genre_perso.get()
    file = open("genre.txt", "a")
    file.write(f"{genre}#")
    file.close()

genre_perso = StringVar()

br = Radiobutton(projet, text="Homme", value=1, font=("Courrier.tff", 20), variable=genre_perso) #1 pour Homme
br2 = Radiobutton(projet, text="Femme", value=2, font=("Courrier.tff", 20), variable=genre_perso) #2 pour Femme
br.pack()
br2.pack()

with os.mkdir('mondossier'):
    folder.write(f"File {i}.")

def titre():
    title=titre.get()
    file = open("titre.txt", "a")
    file.write(f"{title}#")
    file.close()

titre=StringVar()

nom1 = Entry(projet, width=40, textvariable=titre)
nom1.focus_set()
nom1.pack()


button = Button(projet, text="Valider", font=("Courrier.tff", 15), command=titre)
button.pack()

def capte():
    file = open("titre.txt", "r")
    text1 = file.read()
    texte2 = text1.split("#")
    label= Label(projet, text=texte2[0])
    #remplace le 0 par 1 ou 2 pour avoir les mots apres les #
    label.pack()



button2 = Button(projet, text="Tascapté", font=("Courrier.tff", 15), command=capte)
button2.pack()


projet.mainloop()



