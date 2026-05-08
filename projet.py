import tkinter as tk
from tkinter import ttk
import math


def calculer_resultat():
    try:
        Z = int(entry_Z.get())
        A = int(entry_A.get())
        choix = combo.get()
        N= A - Z
        
        if choix == "Nombre de neutrons":
            resultat = N
            if Z <= A:
                label_resultat["text"] = f"Nombre de neutrons : {resultat}"
            else:
                label_resultat["text"] = "Erreur: A doit être supérieur ou égal à Z.(shéma atomique incorrect)"

        elif choix == "masse des neutrons":
            resultat = N * 1.6749286e-27
            label_resultat["text"] = f"masse des neutrons : {resultat} kg"
        elif choix == "masse des électrons":
            resultat = Z * 9.10938356e-31
            label_resultat["text"] = f"masse des électrons : {resultat} kg"
        elif choix == "masse des protones":
            resultat = Z * 1.6726219e-27
            label_resultat["text"] = f"masse des protones : {resultat} kg"
        elif choix == "masse du noyau":
            resultat = N * 1.6749286e-27 + Z * 1.6726219e-27
            label_resultat["text"] = f"masse du noyau : {resultat} kg"
        elif choix == "Charge du noyau":
            resultat = f"+{Z}e"
            label_resultat["text"] = f"Charge du noyau : {resultat}"
        elif choix == "Charge des électrons":
            resultat = f"-{Z}e"
            label_resultat["text"] = f"Charge des électrons : {resultat}"
        elif choix == "Charge de l'atome":
            label_resultat["text"] = "Charge de l'atome : neutre (0)"
        elif choix == "la masse d'atome":
            resultat= N * 1.6749286e-27 + Z * 1.6726219e-27 + Z*9.11*10**-31
            label_resultat["text"]="la masse d'atome est:", resultat

        init_electrons(Z)

        slide_to_frame(frame_resultat)
    except:
        label_resultat["text"] = "Erreur dans les données."
        slide_to_frame(frame_resultat)
def slide_to_frame(frame):
    # Simple transition fade (simulate with raise)
    frame.tkraise()
# Animation atomique 
electrons = []
angles = []
rayons = []
vitesse = []
orbites_max = 3  # nombre d'orbites K,L,M
def init_electrons(Z):
    global electrons, angles, rayons, vitesse
    electrons.clear()
    angles.clear()
    rayons.clear()
    vitesse.clear()
    # Répartir les électrons par orbite (simplifié : K=2, L=8, M=18, N=30)
    orbites = [2, 8, 18, 30]
    total = 0
    for i, max_e in enumerate(orbites):
        nb = min(max_e, Z-total)
        for j in range(nb):
            electrons.append(j)
            angles.append(j*(2*math.pi/nb))
            rayons.append(50 + i*40)  # orbite rayon
            vitesse.append(0.05 + 0.01*i)  # vitesse différente par orbite
        total += nb
        if total >= Z:
            break

def dessiner_modele_atomique():
    
    canvas.delete("all")
    # fond dynamique
    
    taille_noyau = 20 
    canvas.create_oval(250-taille_noyau, 250-taille_noyau,
                       250+taille_noyau, 250+taille_noyau,
                       fill="red", outline="green", width=3)
    # orbites et électrons
    couleurs_orbites = ["blue"]
    for i, angle in enumerate(angles):
        r = rayons[i]
        # orbite par canvas
        canvas.create_oval(250-r, 250-r, 250+r, 250+r,
                           outline=(couleurs_orbites), dash=(3,3), width=1)
        # position electron a partir x et y
        x = 250 + r * math.cos(angle)
        y = 250 + r * math.sin(angle)
        couleur_e = ("white")
        canvas.create_oval(x-7, y-7, x+7, y+7, fill=couleur_e)
        # avancer angle
        angles[i] += vitesse[i]
    canvas.after(35, dessiner_modele_atomique)
# --Interface Tkinter - n9aad interface
window = tk.Tk()
window.title("Assistant Atomique 🧪❇")
window.geometry("400x800")
window.configure(bg="black")
frame_menu = tk.Frame(window, bg="black")
frame_saisie = tk.Frame(window,bg="black")
frame_resultat = tk.Frame(window,bg="black") 
for frame in (frame_menu, frame_saisie, frame_resultat):
    frame.grid(row=0, column=0, sticky='nsew')
# ----- Menu --- lpage d'accueil
tk.Label(frame_menu, text="Bienvenue dans l'Assistant Atomique 🧪❇", font=("Consolas", 14), bg="#0b0f14", fg="#00f5d4").pack(pady=30)
tk.Button(frame_menu, text="Commencer", command=lambda: slide_to_frame(frame_saisie), fg="#b33300").pack(pady=10)
tk.Button(frame_menu, text="Quitter", command=window.destroy, fg="#b33300").pack(pady=10)
# ---- Saisie --# lpage li fihaa les entry w les boutons ofen keydkhl l user data
tk.Label(frame_saisie, text="Entrez les données de l'atome", font=("Consolas", 13),fg="yellow",bg="#0b0f14").pack(pady=10)
tk.Label(frame_saisie, text="Nombre atomique (Z)",font=("Consolas", 12),fg="yellow",bg="#0b0f14").pack()
entry_Z = tk.Entry(frame_saisie)
entry_Z.pack()
tk.Label(frame_saisie, text="Nombre de masse (A)",font=("Consolas", 12),fg="yellow",bg="#0b0f14").pack()
entry_A = tk.Entry(frame_saisie)
entry_A.pack()
tk.Label(frame_saisie, text="Choisissez le calcul à faire",font=("Consolas", 12),fg="red",bg="#0b0f14").pack(pady=5)
combo = ttk.Combobox(frame_saisie, values=[
    "Nombre de neutrons",
    "Charge du noyau",
    "Charge des électrons",
    "Charge de l'atome",
    "masse des neutrons",
    "masse des protones",
    "masse des électrons",
    "masse du noyau",
    "la masse d'atome"
])
combo.current(0)
combo.pack()
tk.Button(frame_saisie, text="Calculer", command=calculer_resultat).pack(pady=10)
tk.Button(frame_saisie, text="Retour au menu", command=lambda: slide_to_frame(frame_menu)).pack()
# -------- Résultat --------# lpage li fihaa lresultat w lcanvas
label_resultat = tk.Label(frame_resultat, text="",fg=("red") ,bg=("black"),font=("Consolas", 12))
label_resultat.pack(pady=10)
canvas = tk.Canvas(frame_resultat, width=500, height=500, bg="black")
canvas.pack(pady=10)
tk.Button(frame_resultat, text="Nouveau calcul", command=lambda: slide_to_frame(frame_saisie)).pack()
tk.Button(frame_resultat, text="Menu principal", command=lambda: slide_to_frame(frame_menu)).pack(pady=5)
slide_to_frame(frame_menu)
dessiner_modele_atomique()
window.mainloop()