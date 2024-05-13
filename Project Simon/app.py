import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Fenêtre principale
root = tk.Tk()
root.title("Système d'information médicale")


frame_profil = ttk.Frame(root, padding="3 3 12 12")
frame_profil.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

current_drug_list = []

smoking = tk.BooleanVar()
coffee = tk.BooleanVar()
alcohol = tk.BooleanVar()


ttk.Label(frame_profil, text="Profil personnel").grid(column=0, row=0, columnspan=4)

def add_smoke():
    smoke = smoking.get()
    if smoke:
        
        current_drug_list.append('Nicotine')
        listbox_drugs.insert(tk.END, 'Nicotine')
        print("Ajout du médicament: Nicotine")
        print(current_drug_list)
    else:
       index = current_drug_list.index('Nicotine')
       current_drug_list.remove('Nicotine') 
       listbox_drugs.delete( index)
       print("Retrait du médicament: Nicotine")
       print(smoke,index, current_drug_list)
       

def add_coffee():
    coff = coffee.get()
    if coff:      
        current_drug_list.append('Caféine')
        listbox_drugs.insert(tk.END, 'Caféine')
        print("Ajout du médicament: Caféine")
        print(current_drug_list)
    else:
       index = current_drug_list.index('Caféine')   
       current_drug_list.remove('Caféine') 
       listbox_drugs.delete( index)
       print("Retrait du médicament: Caféine")
       print(coff,index, current_drug_list)

def add_alcohol():
    vodka = alcohol.get()
    if vodka:
        current_drug_list.append('Alcool')
        listbox_drugs.insert(tk.END, 'Alcool')
        print("Ajout du médicament: Alcool")
        print(current_drug_list)
    else:
        index = current_drug_list.index('Alcool')   
        current_drug_list.remove('Alcool') 
        listbox_drugs.delete( index)
        print("Retrait du médicament: Alcool")
        print(vodka,index, current_drug_list)
    

ttk.Checkbutton(frame_profil, text="Fumeur", variable=smoking, command=add_smoke).grid(column=0, row=1)
ttk.Checkbutton(frame_profil, text="Consommation de caféine", variable=coffee, command=add_coffee).grid(column=1, row=1)
ttk.Checkbutton(frame_profil, text="Consommation d'alcool", variable=alcohol, command=add_alcohol).grid(column=2, row=1)


drug_name = tk.StringVar()
ttk.Entry(frame_profil, textvariable=drug_name).grid(column=0, row=2)

def lookup_drug(index):
    if index != None:
        print(index)
        drug = current_drug_list[index]
    else:
        drug = drug_name.get()
    if drug:
        top = tk.Toplevel(root)
        top.title(f"Résultats pour : {drug}")
        ttk.Label(top, text=f"Résultats pour le médicament : {drug.upper()}").pack(pady=20, padx=20)
        image_path = 'Nicotine.jpg'  # Assurez-vous que le chemin est correct
        img = Image.open(image_path)
        img = img.resize((200, 200), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        ttk.Label(top, image=photo).pack(pady=20)
        top.image = photo

        if drug in current_drug_list:
            #ttk.Button(top, text="Supprimer ce médicament", command=lambda: delete_drug()).pack(pady=10)
            delete_button = tk.Button(root, text="Supprimer médicament", command=lambda : delete_drug())
            delete_button.grid(row=2, column=1)
        # TODO -> add more information (DB)


ttk.Button(frame_profil, text="Chercher médicament", command=lookup_drug).grid(column=2, row=2)

def add_drug():
    drug = drug_name.get()
    if drug and drug not in current_drug_list:
        current_drug_list.append(drug)
        listbox_drugs.insert(tk.END, drug)
        drug_name.set("") 
    print("Ajout du médicament:", drug_name.get())

def delete_drug():
    try:
        index = listbox_drugs.curselection()[0]
        drug = listbox_drugs.get(index)
        current_drug_list.remove(drug)
        listbox_drugs.delete(index)
        print("Retrait du médicament:", drug)
    except IndexError:
        print("Aucun médicament sélectionné pour suppression.")

ttk.Button(frame_profil, text="Ajouter médicament", command=add_drug).grid(column=1, row=2)
ttk.Button(frame_profil, text="Définir une alarme").grid(column=3, row=2)

ttk.Label(frame_profil, text="Liste des médicaments:").grid(column=0, row=4, columnspan=3)
listbox_drugs = tk.Listbox(frame_profil, height=6)
listbox_drugs.grid(column=0, row=5, columnspan=3, sticky=(tk.W, tk.E))
listbox_drugs.bind('<Double-1>',  lambda x : lookup_drug(listbox_drugs.curselection()[0]))

scrollbar = ttk.Scrollbar(frame_profil, orient=tk.VERTICAL, command=listbox_drugs.yview)
scrollbar.grid(column=3, row=5, sticky=(tk.N, tk.S))
listbox_drugs.config(yscrollcommand=scrollbar.set)



for child in frame_profil.winfo_children():
    child.grid_configure(padx=5, pady=5)


root.mainloop()
