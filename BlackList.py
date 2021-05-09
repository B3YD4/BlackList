import os
print("""
______ _       ___  _____  _   __      _     _____ _____ _____ 
| ___ \ |     / _ \/  __ \| | / /     | |   |_   _/  ___|_   _|
| |_/ / |    / /_\ \ /  \/| |/ /______| |     | | \ `--.  | |  
| ___ \ |    |  _  | |    |    \______| |     | |  `--. \ | |  
| |_/ / |____| | | | \__/\| |\  \     | |_____| |_/\__/ / | |  
\____/\_____/\_| |_/\____/\_| \_/     \_____/\___/\____/  \_/             
Yapımcı : B3YD4
Yapım Tarihi : 18.01.2020
İntikal-Hack-Team © 2018 – 2021 - Tüm Hakları Saklıdır.
""")


print("Başlayalım mı(e/h)")

soru = input("Dinliyorum? : ")

if soru == "e":
    isim = input("Kurbanın İsmi Nedir? : ")
    soyad = input("Kurbanın Soyadı Nedir? : ")
    dt = input("Kurbanın Doğum Tarihi Nedir?(GGAAYY yada direk YY Şeklinde Yazınız) : ")
    on = input("Kurbanın Okul Numarası? : ")
    partner = input("Kurbanın Partnerinin İsmi? : ")
    psa = input("Kurbanın Partnerinin Soyadı? : ")
    ct = input("Kurbanın Partneri İle Çıkma Tarihi? : ")
    pdt = input("Kurbanın Partnerinin Doğum Tarihi? : ")
    nick = input("Kurbanın Nick Name'i Nedir? : ")
    pet = input("Kurbanın Petinin İsmi Nedir? : ")
    ek = input("Eklemek İstediğin Anahtar Sözcük Varmı? : ")
    plaka = input("Kurbanın Yaşadığı Şehirde ki Plakası? : ")


    sayi = "123"
    sayi2 = "321"
    dosya = open(isim+".txt","w+")
    dosya.write(isim + dt+"\n")
    dosya.write(isim+soyad+dt+"\n")
    dosya.write(isim+dt+dt+"\n")
    dosya.write(isim+pet+"\n")
    dosya.write(isim+soyad+nick+"\n")
    dosya.write(isim+nick+soyad+"\n")
    dosya.write(isim+sayi+"\n")
    dosya.write(isim+sayi2+"\n")
    dosya.write(isim+on+dt+"\n")
    dosya.write(isim+dt+on+"\n")
    dosya.write(isim+soyad+sayi+"\n")
    dosya.write(isim+soyad+sayi2+"\n")
    dosya.write(isim+partner+dt+"\n")
    dosya.write(isim+partner+ct+"\n")
    dosya.write(isim+partner+pdt+"\n")
    dosya.write(partner+isim+dt+"\n")
    dosya.write(partner+isim+pdt+"\n")
    dosya.write(partner+isim+ct+"\n")
    dosya.write(isim+partner+pdt+"\n")
    dosya.write(partner+isim+pdt+"\n")
    dosya.write(isim+ct+"\n")
    dosya.write(isim+partner+dt+"\n")
    dosya.write(partner+isim+dt+"\n")
    dosya.write(isim+partner+psa+"\n")
    dosya.write(partner+isim+psa+"\n")
    dosya.write(isim+partner+soyad+"\n")
    dosya.write(partner+isim+soyad+"\n")
    dosya.write(isim+pet+"\n")
    dosya.write(nick+isim+"\n")
    dosya.write(nick+dt+"\n")
    dosya.write(nick+sayi+"\n")
    dosya.write(nick+sayi2+"\n")
    dosya.write(nick+dt+"\n")
    dosya.write(isim+ek+"\n")
    dosya.write(isim+sayi+ek+"\n")
    dosya.write(isim+sayi2+ek+"\n")
    dosya.write(nick+ek+"\n")
    dosya.write(ek+dt+"\n")
    dosya.write(isim+soyad+plaka+"\n")
    dosya.write(isim+plaka+plaka+"\n")
    dosya.write(isim+soyad+plaka+plaka+"\n")
    dosya.write(nick+plaka+plaka+"\n")
    dosya.write(nick+plaka+"\n")
    dosya.write(isim+soyad+ek+"\n")
    dosya.write(ek+isim+ek+"\n")
    dosya.write(isim+ek+"\n")
    dosya.write(plaka+isim+plaka+"\n")
    dosya.write(plaka+isim+ek+"\n")
    dosya.write(nick+plaka+"\n")
    dosya.write(nick+ek+"\n")
    dosya.write(nick+ek+isim+"\n")
    dosya.write(nick+isim+dt+"\n")
    dosya.write(pet+isim+dt+"\n")
    dosya.write(pet+nick+dt+"\n")
    dosya.write(pet+nick+sayi+"\n")
    dosya.write(pet+nick+sayi2+"\n")
    dosya.write(dt+isim+"\n")

    


    dosya.close()



if soru == "h":
    print("Hoşçakal!")
