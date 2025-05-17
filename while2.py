import random
puan = 0
while True:
    s1 = random.randint(1,100)
    s2 = random.randint(1,100)
    cevap = input(f"{s1}+{s2} toplamı kaçtır?")

    if cevap == "":
        print(f"Hoşçakal, puanın: {puan}")
        break
    if int(cevap) == s1+s2 :
        puan +=10
        print("Doğru, Puanın", puan)

    else:
         puan -=10
         print("Yanlış, Puanın:", puan)