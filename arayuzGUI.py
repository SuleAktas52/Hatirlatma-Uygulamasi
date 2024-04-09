# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 17:41:53 2024

@author: AktasSule
"""

from tkinter import *
from tkcalendar import DateEntry

master= Tk()

canvas= Canvas(master, height=450, width=750) #ana obje olusturuldu.

canvas.pack() #arayuze eklemeyi saglar. pack = place= grid

#frame yapisi birden fazla widgets in birlestirilmis halidir.
frame_ust= Frame(master, bg= '#add8e6') #frame olusturma
frame_ust.place(relx=0.1, rely=0.1, relwidth=0.75, relheight=0.1)
#relx, rely= baslangic noktalari

frame_alt_sol= Frame(master, bg='#add8e6')
frame_alt_sol.place(relx=0.1, rely=0.21, relwidth=0.23, relheight=0.5)

frame_alt_sag= Frame(master, bg='#add8e6')
frame_alt_sag.place(relx=0.34, rely=0.21, relwidth=0.51, relheight=0.5)

hatirlatma_tipi_etiket= Label(frame_ust, bg='#add8e6', 
                              text='Hatirlatma Tipi:', font='Verdana 10 bold')
hatirlatma_tipi_etiket.pack(padx=10, pady=10, side=LEFT) 
#side: hangi tarafta konumlandirilmasini istiyorsak.
#padx,y: objelerin ic tarafina ya da etrafina bosluk birakilmasi

hatirlatma_tipi_opsiyon= StringVar(frame_ust)
hatirlatma_tipi_opsiyon.set("\t")

hatirlatma_tipi_acilir_menu= OptionMenu(frame_ust,hatirlatma_tipi_opsiyon 
                                        , "Dogum Gunu", "Alisveris", "Odeme")
hatirlatma_tipi_acilir_menu.pack(padx=10, pady=10, side=LEFT)

hatirlatma_tarihi_etiket= Label(frame_ust, bg='#add8e6',
                                text='Hatirlatma Tarihi:', font='Verdana 10 bold')
hatirlatma_tarihi_etiket.pack(padx=10, pady=10, side=LEFT)

hatirlatma_tarih_secisi= DateEntry(frame_ust, width=12,  #Tarih olusturma
                                   background='orange', foreground= 'black', border='de_DE')

hatirlatma_tarih_secisi._top_cal.overrideredirect(False)
hatirlatma_tarih_secisi.pack(padx=10, pady=10, side=LEFT)

degisken=Label(frame_alt_sol, text="Hatirlatma Yontemi"
               ,bg='#add8e6', font='Verdana 10 bold')
degisken.pack(padx=10, pady=10, anchor=NW) 
#anchor:bir degeri nereye yaslayacagimizi soyle NW(North West)

var= IntVar()

R1= Radiobutton(frame_alt_sol, text="Sisteme Kaydet", 
                variable= var, value=1, bg='#add8e6', font='Verdana 10')
R1.pack(anchor=NW, padx=15, pady=5)

R2= Radiobutton(frame_alt_sol, text="E-posta Gonder",
                variable= var, value=2, bg='#add8e6', font='Verdana 10')
R2.pack(anchor=NW, padx=15, pady=5)

var1= IntVar()
C1=Checkbutton(frame_alt_sol, text="Bir hafta once", 
               variable=var1, onvalue=1, offvalue=0, bg='#add8e6', font='Verdana 10') 
#onvalue: secilmis hali offvalue:secilmemis hali
C1.pack(anchor=NW, padx=25, pady=2)

var2= IntVar()
C2=Checkbutton(frame_alt_sol, text="Bir ay once", 
               variable=var2, onvalue=1, offvalue=0, bg='#add8e6', font='Verdana 10')
C2.pack(anchor=NW, padx=25, pady=2)

var3= IntVar()
C3=Checkbutton(frame_alt_sol, text="Ayni gun", 
               variable=var3, onvalue=1, offvalue=0, bg='#add8e6', font='Verdana 10')
C3.pack(anchor=NW, padx=25, pady=2)

from tkinter import messagebox

def gonder():
    son_mesaj= ""
    try:
      if var.get():
          if var.get()==1:
              son_mesaj+= "Veriniz basariyla sisteme kaydedilmistir."
            
              tip= hatirlatma_tipi_opsiyon.get() if hatirlatma_tipi_opsiyon.get() == '' else "Genel "           
              tarih= hatirlatma_tarih_secisi.get()
              mesaj= metin_alani.get("1.0", "end")
            
              with open("hatirlatmalar.txt", "w") as dosya: #dosya acma w:yazma r:okuma
                  dosya.write(
                    '{} kategorisinde, {} tarihine ve "{}" notuyla hatirlatma'. format(
                        tip,
                        tarih,
                        mesaj
                        ))
                  dosya.close()
            
          elif var.get() == 2:
              son_mesaj+= "E-posta yoluyla hatirlatma size ulasilacaktir."
            
          messagebox.showinfo("Basarili Islem", son_mesaj)
      else:
          son_mesaj+= "Gerekli alanlarin dolduruldugundan emin olun!!"
          messagebox.showwarning("Yetersiz Bilgi", son_mesaj)
        
    except:
        son_mesaj += "Islem basarasiz oldu!"
        messagebox.showerror("Basarisiz Islem!", son_mesaj)
    finally:
        master.destroy()
    return

degisken2=Label(frame_alt_sag, text="Hatirlatma Mesaji",bg='#add8e6', font='Verdana 10 bold')
degisken2.pack(padx=10, pady=10, anchor=NW)

metin_alani= Text(frame_alt_sag, height=9, width=45)
metin_alani.tag_configure('style', foreground='#bfbfbf', font=('Verdana', 7, 'bold'))
metin_alani.pack()

karsilama_metni= "Mesajini buraya gir..."
metin_alani.insert(END, karsilama_metni, 'style')

gonder_butonu=Button(frame_alt_sag, text="Gonder", command=gonder) #command=master.destroy
gonder_butonu.pack(anchor=S)




master.mainloop() #arayuzu calistirma 
#mainloop(): surekli cagirilmasini saglar boylelikle kullanici devamli arayuzu gorur.




