class Kitap:
    def __init__(self, id, ad, yazar, isbn):
        self.id = id
        self.ad = ad
        self.yazar = yazar
        self.isbn = isbn

class Uye:
    def __init__(self, id, ad, soyad):
        self.id = id
        self.ad = ad
        self.soyad = soyad