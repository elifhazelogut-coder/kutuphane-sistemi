import tkinter as tk
from tkinter import messagebox
from database import VeritabaniYonetici

class KutuphaneUygulamasi:
    def __init__(self, root):
        self.root = root
        self.root.title("Kastamonu Üni. Kütüphane Sistemi")
        self.db = VeritabaniYonetici()
        
        # --- Arayüz Elemanları ---
        # Kitap Adı
        tk.Label(root, text="Kitap Adı:").grid(row=0, column=0, padx=5, pady=5)
        self.ent_ad = tk.Entry(root)
        self.ent_ad.grid(row=0, column=1, padx=5, pady=5)

        # Yazar Adı (Yeni Eklendi)
        tk.Label(root, text="Yazar:").grid(row=1, column=0, padx=5, pady=5)
        self.ent_yazar = tk.Entry(root)
        self.ent_yazar.grid(row=1, column=1, padx=5, pady=5)

        # ISBN (Yeni Eklendi)
        tk.Label(root, text="ISBN:").grid(row=2, column=0, padx=5, pady=5)
        self.ent_isbn = tk.Entry(root)
        self.ent_isbn.grid(row=2, column=1, padx=5, pady=5)

        # Kaydet Butonu
        tk.Button(root, text="Kitabı Kaydet", command=self.kaydet, bg="green", fg="white").grid(row=3, column=0, columnspan=2, pady=10)
        
        # Liste Ekranı
        self.liste = tk.Listbox(root, width=60)
        self.liste.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        self.listele()

    def kaydet(self):
        # Kullanıcının kutucuklara yazdığı verileri alıyoruz
        ad = self.ent_ad.get()
        yazar = self.ent_yazar.get()
        isbn = self.ent_isbn.get()

        if ad and yazar and isbn:
            # Artık "Bilinmiyor" yerine değişkenleri gönderiyoruz
            self.db.kitap_ekle(ad, yazar, isbn)
            messagebox.showinfo("Başarılı", f"'{ad}' başarıyla eklendi!")
            
            # Kutucukları temizle
            self.ent_ad.delete(0, tk.END)
            self.ent_yazar.delete(0, tk.END)
            self.ent_isbn.delete(0, tk.END)
            
            self.listele()
        else:
            messagebox.showwarning("Uyarı", "Lütfen tüm alanları doldurun!")

    def listele(self):
        self.liste.delete(0, tk.END)
        for kitap in self.db.kitaplari_getir():
            # Listede Kitap Adı, Yazar ve ISBN'i göster
            self.liste.insert(tk.END, f"ID: {kitap[0]} | Kitap: {kitap[1]} | Yazar: {kitap[2]} | ISBN: {kitap[3]}")