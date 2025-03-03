urun1=int(input("1.ürün toplam miktarı:"))
urun2=int(input("2.ürün toplam miktarı:"))
toplam=urun1+urun2
if toplam<200:
    print("ödenecek",toplam)
else:
    odeme=toplam*0,75
    print=("odenecek miktar",odeme)