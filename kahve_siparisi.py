import tkinter as tk
from PIL import Image, ImageTk
import random
from tkinter import messagebox

root = tk.Tk()
root.geometry("1000x600")
root.title("Kahve Siparisi")

kahve_ucretleri = {
    "Espresso":30,
    "Latte":35,
    "Cappuccino": 32,
    "Americano": 28,
    "Mocha": 38
}

siparis_listesi = []

name_var = tk.StringVar()
tk.Label(root, text="Adiniz", bg="#fefcfb", font=("Arial",12)).pack(pady=5)
tk.Entry(root, textvariable=name_var, font=("Arial",12)).pack(pady=5)

kahve_var = tk.StringVar(value="Espresso")
tk.Label(root, text="Kahve secimi", bg="#fefcfb", font=("Arial",12)).pack(pady=5)
tk.OptionMenu(root, kahve_var,*kahve_ucretleri.keys()).pack(pady=5)

adet_var = tk.StringVar(value="1")
tk.Label(root, text="Adet", bg="#fefcfb", font=("Arial",12)).pack(pady=5)
tk.Entry(root, textvariable=adet_var, font=("Arial",12)).pack(pady=5)

total_label = tk.Label(root, text="Toplam = 0", bg="#fefcfb", font=("Arial",12))
total_label.pack(pady=5)

def toplam(*args):
    try:
        adet = int(adet_var.get())
        fiyat = kahve_ucretleri[kahve_var.get()]
        toplam = adet * fiyat
        total_label.config(text=f"Toplam = {toplam}", fg="green")
    except:
        total_label.config(text="Gecersiz giris", fg="red")

adet_var.trace_add("write", toplam)

kahve_var.trace_add("write", toplam)

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=5)


def siparis_ekle():
    try:
        name = name_var.get().strip()
        if not name:
            messagebox.showwarning("hata", "Lütfen adinizi giriniz")
            return
        kahve = kahve_var.get()
        adet = int(adet_var.get())
        toplam_fiyat = adet * kahve_ucretleri[kahve]
        order = {"isim": name, "kahve": kahve, "adet": adet, "toplam": toplam_fiyat}
        siparis_listesi.append(order)
        listbox.insert(tk.END, f"{adet} x {kahve} = {toplam_fiyat} €")
        toplam()
    except:
        messagebox.showerror("hata", "Gecerli bir adet giriniz")


listeye_ekle = tk.Button(root, text="Listeye ekle", command=siparis_ekle, font=("Arial",11)).pack(pady=5)



tk.mainloop()