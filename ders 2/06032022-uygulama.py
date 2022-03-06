#
#kullanıcıdan isim, soyisim, telefon numarası alarak bir listeye atayınız..
bilgiler=[]#boş liste tanımlar

isim=input("Adınız:")
soyisim=input("Soyadınız:")
tel=input("Telefon Numaranız")
print(bilgiler)
bilgiler.append(isim)
bilgiler.append(soyisim)
bilgiler.append(tel)
print(bilgiler)
print("---------------")
print("Adı:",bilgiler[0])
print("Soyadı:",bilgiler[1])
print("Telefon Numarası:",bilgiler[2])
print("-----------------")
