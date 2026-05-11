import sqlite3

class VeritabaniYonetici:
    def __init__(self, db_adi="kutuphane.db"):
        self.conn = sqlite3.connect(db_adi)
        self.cursor = self.conn.cursor()
        self.tablo_olustur()

    def tablo_olustur(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS kitaplar 
                            (id INTEGER PRIMARY KEY, ad TEXT, yazar TEXT, isbn TEXT)''')
        self.conn.commit()

    def kitap_ekle(self, ad, yazar, isbn):
        self.cursor.execute("INSERT INTO kitaplar (ad, yazar, isbn) VALUES (?, ?, ?)", (ad, yazar, isbn))
        self.conn.commit()

    def kitaplari_getir(self):
        self.cursor.execute("SELECT * FROM kitaplar")
        return self.cursor.fetchall()