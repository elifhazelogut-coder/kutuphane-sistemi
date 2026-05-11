# kutuphane-sistemi
# Kastamonu Üniversitesi Kütüphane Yönetim Sistemi

# Proje Hakkında

Bu proje, Python programlama dili kullanılarak geliştirilmiş masaüstü tabanlı bir kütüphane otomasyon sistemidir.  
Projenin amacı, kullanıcıların kitap kayıt işlemlerini kolaylaştırmak, verileri düzenli bir şekilde saklamak ve temel bir kütüphane yönetim altyapısı oluşturmaktır.

Sistem sayesinde kullanıcı:
- Yeni kitap ekleyebilir
- Kitap bilgilerini görüntüleyebilir
- Verileri kalıcı olarak SQLite veritabanında saklayabilir

Bu proje eğitim amaçlı geliştirilmiş olup:
- Nesne yönelimli programlama (OOP)
- Veritabanı yönetimi
- Grafiksel kullanıcı arayüzü geliştirme
- Modüler yazılım mimarisi
konularını uygulamalı olarak göstermektedir.



# Projenin Amacı

Kütüphanelerde kitap kayıt işlemlerinin dijital ortamda yönetilmesini sağlamak amaçlanmıştır.

Bu proje ile:
- Manuel kayıt işlemleri azaltılmıştır
- Kitap bilgileri güvenli şekilde saklanmıştır
- Kullanıcı dostu bir masaüstü arayüzü oluşturulmuştur
- Python ile GUI uygulama geliştirme pratiği yapılmıştır

---

# Kullanılan Teknolojiler

| Teknoloji = Açıklama |
| Python 3 = Ana programlama dili |
| Tkinter = Grafiksel kullanıcı arayüzü |
| SQLite3 = Veritabanı sistemi |
| OOP = Nesne yönelimli programlama |
| Git & GitHub = Versiyon kontrol sistemi |

# Yazılım Mimarisi

Proje modüler bir yapıda geliştirilmiştir.  
Her dosyanın belirli bir görevi bulunmaktadır.

# Kullanılan Mimari Yaklaşım

Projede temel seviyede katmanlı mimari yaklaşımı uygulanmıştır:

- Arayüz Katmanı (`ui.py`)
- Veritabanı Katmanı (`database.py`)
- Veri Modeli Katmanı (`models.py`)
- Başlatma Katmanı (`main.py`)

Bu yapı sayesinde:
- Kod okunabilirliği artmıştır
- Modüller birbirinden bağımsız geliştirilmiştir
- Bakım ve güncelleme işlemleri kolaylaştırılmıştır


# Proje Dosya Yapısı

```bash
project/
│
├── main.py
├── ui.py
├── database.py
├── models.py
├── kutuphane.db
└── README.md
