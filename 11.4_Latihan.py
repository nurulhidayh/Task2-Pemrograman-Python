def persegipanjang(panjang, lebar):
    luas = panjang * lebar
    print("Luasnya : ",luas)
    return luas

def persegi(sisi):
    luas = sisi * sisi
    print("Luasnya : ",luas)
    return luas

print("Persegi Panjang")
a = int(input("Masukkan panjang : "))
b = int(input("Masukkan lebar   : "))
persegipanjang(a,b)

print("Persegi")
s = int(input("Masukkan sisi : "))
persegi(s)