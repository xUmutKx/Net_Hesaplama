import tkinter as tk
from tkinter import messagebox, scrolledtext

def net_hesapla(dogru_sayisi, yanlis_sayisi):
    net = dogru_sayisi - (yanlis_sayisi / 4)
    return net

def hesaplama(soru_sayisi, yanlis_sayisi, bos_sayisi):
    dogru_sayisi = soru_sayisi - (yanlis_sayisi + bos_sayisi)
    yanlis_sayisi = yanlis_sayisi
    if bos_sayisi == '':
        bos_sayisi = 0
    else:
        bos_sayisi = int(bos_sayisi)
    net_sayisi = net_hesapla(dogru_sayisi, yanlis_sayisi)
    return dogru_sayisi, yanlis_sayisi, bos_sayisi, net_sayisi

def soru_sayisi_sec(soru_formati):
    global turkce_soru_sayisi, sosyal_soru_sayisi, matematik_soru_sayisi, fen_soru_sayisi
    soru_formati_frame.pack_forget()  
    hesapla_button.config(state=tk.NORMAL)  

    turkce_soru_sayisi, sosyal_soru_sayisi, matematik_soru_sayisi, fen_soru_sayisi = soru_formati.split("/")
    turkce_soru_sayisi = int(turkce_soru_sayisi)
    sosyal_soru_sayisi = int(sosyal_soru_sayisi)
    matematik_soru_sayisi = int(matematik_soru_sayisi)
    fen_soru_sayisi = int(fen_soru_sayisi)

    global etiketler
    etiketler = []

    turkce_soru_label = tk.Label(window, text=f"Türkçe Soru Sayısı: {turkce_soru_sayisi}", font=("Arial", 14, "bold"), bg="gray10", fg="white")
    turkce_soru_label.pack()
    etiketler.append(turkce_soru_label)

    turkce_yanlis_label = tk.Label(window, text="Türkçe Yanlış Sayısı:", font=("Arial", 12), bg="gray10", fg="white")
    turkce_yanlis_label.pack()
    etiketler.append(turkce_yanlis_label)
    global turkce_yanlis_entry
    turkce_yanlis_entry = tk.Entry(window, bg="gray40", fg="white")
    turkce_yanlis_entry.pack()

    turkce_bos_label = tk.Label(window, text="Türkçe Boş Sayısı:", font=("Arial", 12), bg="gray10", fg="white")
    turkce_bos_label.pack()
    global turkce_bos_entry
    turkce_bos_entry = tk.Entry(window, bg="gray40", fg="white")
    turkce_bos_entry.pack()
    etiketler.append(turkce_bos_label)
    etiketler.append(turkce_bos_entry)

    sosyal_soru_label = tk.Label(window, text=f"Sosyal Soru Sayısı: {sosyal_soru_sayisi}", font=("Arial", 14, "bold"), bg="gray10", fg="white")
    sosyal_soru_label.pack()
    etiketler.append(sosyal_soru_label)

    sosyal_yanlis_label = tk.Label(window, text="Sosyal Yanlış Sayısı:", font=("Arial", 12), bg="gray10", fg="white")
    sosyal_yanlis_label.pack()
    global sosyal_yanlis_entry
    sosyal_yanlis_entry = tk.Entry(window, bg="gray40", fg="white")
    sosyal_yanlis_entry.pack()
    etiketler.append(sosyal_yanlis_label)
    etiketler.append(sosyal_yanlis_entry)

    sosyal_bos_label = tk.Label(window, text="Sosyal Boş Sayısı:", font=("Arial", 12), bg="gray10", fg="white")
    sosyal_bos_label.pack()
    global sosyal_bos_entry
    sosyal_bos_entry = tk.Entry(window, bg="gray40", fg="white")
    sosyal_bos_entry.pack()
    etiketler.append(sosyal_bos_label)
    etiketler.append(sosyal_bos_entry)

    matematik_soru_label = tk.Label(window, text=f"Matematik Soru Sayısı: {matematik_soru_sayisi}", font=("Arial", 14, "bold"), bg="gray10", fg="white")
    matematik_soru_label.pack()
    etiketler.append(matematik_soru_label)

    matematik_yanlis_label = tk.Label(window, text="Matematik Yanlış Sayısı:", font=("Arial", 12), bg="gray10", fg="white")
    matematik_yanlis_label.pack()
    global matematik_yanlis_entry
    matematik_yanlis_entry = tk.Entry(window, bg="gray40", fg="white")
    matematik_yanlis_entry.pack()
    etiketler.append(matematik_yanlis_label)
    etiketler.append(matematik_yanlis_entry)

    matematik_bos_label = tk.Label(window, text="Matematik Boş Sayısı:", font=("Arial", 12), bg="gray10", fg="white")
    matematik_bos_label.pack()
    global matematik_bos_entry
    matematik_bos_entry = tk.Entry(window, bg="gray40", fg="white")
    matematik_bos_entry.pack()
    etiketler.append(matematik_bos_label)
    etiketler.append(matematik_bos_entry)

    fen_soru_label = tk.Label(window, text=f"Fen Soru Sayısı: {fen_soru_sayisi}", font=("Arial", 14, "bold"), bg="gray10", fg="white")
    fen_soru_label.pack()
    etiketler.append(fen_soru_label)

    fen_yanlis_label = tk.Label(window, text="Fen Yanlış Sayısı:", font=("Arial", 12), bg="gray10", fg="white")
    fen_yanlis_label.pack()
    global fen_yanlis_entry
    fen_yanlis_entry = tk.Entry(window, bg="gray40", fg="white")
    fen_yanlis_entry.pack()
    etiketler.append(fen_yanlis_label)
    etiketler.append(fen_yanlis_entry)

    fen_bos_label = tk.Label(window, text="Fen Boş Sayısı:", font=("Arial", 12), bg="gray10", fg="white")
    fen_bos_label.pack()
    global fen_bos_entry
    fen_bos_entry = tk.Entry(window, bg="gray40", fg="white")
    fen_bos_entry.pack()
    etiketler.append(fen_bos_label)
    etiketler.append(fen_bos_entry)

def hesaplama_yap():
    turkce_yanlis_sayisi = turkce_yanlis_entry.get()
    turkce_bos_sayisi = turkce_bos_entry.get()
    sosyal_yanlis_sayisi = sosyal_yanlis_entry.get()
    sosyal_bos_sayisi = sosyal_bos_entry.get()
    matematik_yanlis_sayisi = matematik_yanlis_entry.get()
    matematik_bos_sayisi = matematik_bos_entry.get()
    fen_yanlis_sayisi = fen_yanlis_entry.get()
    fen_bos_sayisi = fen_bos_entry.get()

    if not turkce_yanlis_sayisi.isdigit() or not sosyal_yanlis_sayisi.isdigit() or not matematik_yanlis_sayisi.isdigit() or not fen_yanlis_sayisi.isdigit():
        messagebox.showerror("Hata", "Yanlış veya boş sayıları sadece rakamlarla giriniz.")
        return
    
    turkce_yanlis_sayisi = int(turkce_yanlis_sayisi)
    turkce_bos_sayisi = int(turkce_bos_sayisi) if turkce_bos_sayisi else 0
    sosyal_yanlis_sayisi = int(sosyal_yanlis_sayisi)
    sosyal_bos_sayisi = int(sosyal_bos_sayisi) if sosyal_bos_sayisi else 0
    matematik_yanlis_sayisi = int(matematik_yanlis_sayisi)
    matematik_bos_sayisi = int(matematik_bos_sayisi) if matematik_bos_sayisi else 0
    fen_yanlis_sayisi = int(fen_yanlis_sayisi)
    fen_bos_sayisi = int(fen_bos_sayisi) if fen_bos_sayisi else 0

    turkce_dogru_sayisi, turkce_yanlis_sayisi, turkce_bos_sayisi, turkce_net_sayisi = hesaplama(turkce_soru_sayisi, turkce_yanlis_sayisi, turkce_bos_sayisi)
    sosyal_dogru_sayisi, sosyal_yanlis_sayisi, sosyal_bos_sayisi, sosyal_net_sayisi = hesaplama(sosyal_soru_sayisi, sosyal_yanlis_sayisi, sosyal_bos_sayisi)
    matematik_dogru_sayisi, matematik_yanlis_sayisi, matematik_bos_sayisi, matematik_net_sayisi = hesaplama(matematik_soru_sayisi, matematik_yanlis_sayisi, matematik_bos_sayisi)
    fen_dogru_sayisi, fen_yanlis_sayisi, fen_bos_sayisi, fen_net_sayisi = hesaplama(fen_soru_sayisi, fen_yanlis_sayisi, fen_bos_sayisi)

    toplam_dogru_sayisi = turkce_dogru_sayisi + sosyal_dogru_sayisi + matematik_dogru_sayisi + fen_dogru_sayisi
    toplam_yanlis_sayisi = turkce_yanlis_sayisi + sosyal_yanlis_sayisi + matematik_yanlis_sayisi + fen_yanlis_sayisi
    toplam_bos_sayisi = turkce_bos_sayisi + sosyal_bos_sayisi + matematik_bos_sayisi + fen_bos_sayisi
    toplam_net_sayisi = turkce_net_sayisi + sosyal_net_sayisi + matematik_net_sayisi + fen_net_sayisi

    turkce_puani = turkce_net_sayisi * 3.3
    sosyal_puani = sosyal_net_sayisi * 3.4
    matematik_puani = matematik_net_sayisi * 3.3
    fen_puani = fen_net_sayisi * 3.4

    toplam_puan = turkce_puani + sosyal_puani + matematik_puani + fen_puani + 100
    if toplam_puan > 500:
        toplam_puan = 500

    sonuclar_text.configure(state='normal')
    sonuclar_text.delete(1.0, tk.END)
    sonuclar_text.insert(tk.END, f"Türkçe\n\nDoğru Sayısı: {turkce_dogru_sayisi}\nYanlış Sayısı: {turkce_yanlis_sayisi}\nBoş Sayısı: {turkce_bos_sayisi}\nNet Sayısı: {turkce_net_sayisi}\n\n")
    sonuclar_text.insert(tk.END, f"Sosyal\n\nDoğru Sayısı: {sosyal_dogru_sayisi}\nYanlış Sayısı: {sosyal_yanlis_sayisi}\nBoş Sayısı: {sosyal_bos_sayisi}\nNet Sayısı: {sosyal_net_sayisi}\n\n")
    sonuclar_text.insert(tk.END, f"Matematik\n\nDoğru Sayısı: {matematik_dogru_sayisi}\nYanlış Sayısı: {matematik_yanlis_sayisi}\nBoş Sayısı: {matematik_bos_sayisi}\nNet Sayısı: {matematik_net_sayisi}\n\n")
    sonuclar_text.insert(tk.END, f"Fen\n\nDoğru Sayısı: {fen_dogru_sayisi}\nYanlış Sayısı: {fen_yanlis_sayisi}\nBoş Sayısı: {fen_bos_sayisi}\nNet Sayısı: {fen_net_sayisi}\n\n")
    sonuclar_text.insert(tk.END, f"Toplam\n\nDoğru Sayısı: {toplam_dogru_sayisi}\nYanlış Sayısı: {toplam_yanlis_sayisi}\nBoş Sayısı: {toplam_bos_sayisi}\nNet Sayısı: {toplam_net_sayisi}\nToplam Puan: {toplam_puan:.2f}\n\n")
    sonuclar_text.configure(state='disabled')

def yeniden_hesapla():
    soru_formati_frame.pack(side=tk.TOP)  
    hesapla_button.config(state=tk.DISABLED)  
    sonuclar_text.delete(1.0, tk.END)  

    for etiket in etiketler:
        etiket.destroy()

    etiketler.clear()

window = tk.Tk()
window.title("Net Hesaplama")
window.geometry("1920x1080")
window.configure(bg="gray10")

soru_formati_frame = tk.Frame(window, bg="gray10")
soru_formati_frame.pack()

soru_formati_label = tk.Label(soru_formati_frame, text="Soru Formatını Seçin:", font=("Arial", 18), bg="gray10", fg="white")
soru_formati_label.pack()

button_30_30_30_30 = tk.Button(soru_formati_frame, text="30/30/30/30", command=lambda: soru_sayisi_sec("30/30/30/30"), bg="gray30", fg="white")
button_30_30_30_30.pack(side=tk.LEFT, padx=5)

button_40_20_40_20 = tk.Button(soru_formati_frame, text="40/20/40/20", command=lambda: soru_sayisi_sec("40/20/40/20"), bg="gray30", fg="white")
button_40_20_40_20.pack(side=tk.LEFT, padx=5)

button_25_25_25_25 = tk.Button(soru_formati_frame, text="25/25/25/25", command=lambda: soru_sayisi_sec("25/25/25/25"), bg="gray30", fg="white")
button_25_25_25_25.pack(side=tk.LEFT, padx=5)

sonuclar_text = scrolledtext.ScrolledText(window, height=10, width=50, bg="gray40", fg="white")
sonuclar_text.pack(side=tk.BOTTOM)
sonuclar_text.configure(state='disabled')

yeniden_hesapla_button = tk.Button(window, text="Baştan Başla",font=("Arial", 12, "bold"),  command=yeniden_hesapla, bg="gray30", fg="white")
yeniden_hesapla_button.pack(side=tk.BOTTOM)

hesapla_button = tk.Button(window, text="Hesapla", font=("Arial", 12, "bold"), command=hesaplama_yap, bg="gray30", fg="white")
hesapla_button.pack(side=tk.BOTTOM)

sonuclar_label = tk.Label(window, text="Sonuçlar:", font=("Arial", 16, "bold"), bg="gray10", fg="white")
sonuclar_label.pack(side=tk.BOTTOM)

window.mainloop()
