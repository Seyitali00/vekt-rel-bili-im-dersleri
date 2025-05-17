import random

corba = ["Yoğurt","Mercimek","Brokoli","Ezo Gelin"]
anayemek=["Mantı","Makarna","Köfte","Kızarmış Tavuk","Ispanak"]
icecek= ["Kola","ÖzerHisar Ayran","Soda","Icetea"]

print("Menü tavsiye programı")

print(f"Bugün size {random.choice(corba)} corbası")
print(f"Ana yemek olarak {random.choice(anayemek)}")
print(f"İçecek olarak ise {random.choice(icecek)} öneriyorum")