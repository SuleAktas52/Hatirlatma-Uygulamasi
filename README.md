# Hatırlatma Uygulaması  Bu uygulama, kullanıcıların hatırlatma mesajları oluşturmasına ve yönetmesine olanak tanır. 
## Kullanılan Kütüphaneler  - 
`tkinter`: Grafik arayüz oluşturmak için kullanılan standart bir Python kütüphanesidir. - 
`tkcalendar`: Takvim widget'ı oluşturmak için kullanılan bir kütüphanedir. 

## Uygulama Özellikleri  
- Hatırlatma tipi seçimi (örneğin: Doğum Günü, Alışveriş, Ödeme)
- Hatırlatma tarihi seçimi 
- Hatırlatma mesajı girişi 
- Hatırlatma yöntemi seçimi (Sisteme Kaydet, E-posta Gönder)
- İleri tarihli hatırlatma seçenekleri (Bir hafta önce, Bir ay önce, Aynı gün)

## Kod Açıklamaları  
-  `Canvas` ve `Frame` widget'ları kullanılarak arayüz yapısı oluşturulmuştur.
-  `OptionMenu` ile hatırlatma tipi seçimi,
-  `DateEntry` ile tarih seçimi sağlanmıştır.
-  `Radiobutton` ve `Checkbutton` ile hatırlatma yöntemi ve ileri tarihli hatırlatma seçenekleri sunulmuştur.
-  `Text` widget'ı ile hatırlatma mesajı girişi sağlanmıştır.
-  `messagebox` kullanılarak kullanıcıya bilgi, uyarı ve hata mesajları gösterilmiştir.

# Notlar  
Tüm alanları doldurduktan sonra "Gönder" butonuna tıklamadan önce doğru ve eksiksiz bilgilerin girildiğinden emin olun. 
