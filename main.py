import random
# 1. Sukurkite funkciją, kuri išvestų jūsų vardą ir kodėl pasirinkote
# programavimą. Iškvieskite šią funkciją tris kartus.
# def vardas():
#     print("Gintaras, pasirinkau nes noriu")
# vardas()
# vardas()
# vardas()

# 2. Sukurkite funkciją, kuri išvestų 5 eilučių eilėraštį. Iškvieskite šią funkciją 5
# kartus.
# def eilerastis():
#     print("5 eiluciu eilerastis")
# eilerastis()
# eilerastis()
# eilerastis()
# eilerastis()
# eilerastis()

# 3. Sukurkite tris funkcijas, kur kiekviena išvestų skirtingus tekstus. Iškvieskite
# visas tris funkcijas po vieną kartą.
# def tekst():
#     print("labas")
# def tekst1():
#     print("krabas")
# def tekst2():
#     print("kebabas")
# tekst()
# tekst1()
# tekst2()



# # 4. Sukurkite dvi funkcijas, kur vienoje būtų viena teksto eilutėje, kitoje kita.
# # Sukurkite trečią funkciją, kuri iškviestų pirmas dvi funkcijas. Iškvieskite šią
# # trečiąją funkciją už visų funkcijų ribų.
# def f1():
#     print("teksto eilute")
# def f2():
#     print("kita teksto eilute")
# def f3():
#     f1()
#     f2()
# f3()

# 5. Sukurkite funkciją, kurios viduje sugeneruotumėte du atsitiktinius
# skaičius. Funkcijoje suskaičiuokite ir išveskite šių dviejų skaičių sumą,
# kartu išvedant ir patį atliekamą veiksmą (pvz 7 + 2 = 9). Iškvieskite šią
# funkciją keletą kartų.
# import random
# def f1():
#     a = random.randint(1, 10)
#     b = random.randint(1, 10)
#     suma = a + b
#     print(f"{a} + {b} = {a + b}")
#
# f1()

# 6. Sukurkite ir iškvieskite funkciją, kurioje kintamuosiuose būtų saugoma
# informacija apie policininką (vardas, pavardė, amžius, alga, etatas,
# specializacija). Išveskite šią informaciją suformatuotai (pavyzdžiui įterpkite
# į sakinį, ar išveskite sąrašu ar pan.).

# def f1():
#     v = "Gintaras"
#     p = "Bolsius"
#     a = 25
#     alga = 1500
#     etatas = "pilotas"
#     specializacija = "Operis"
#
#     info = (
#         f'Policininkas {v} {p}:\n'
#         f'Amzius: {a} metu\n'
#         f'Alga: {alga} EUR\n'
#         f'Etatas: {etatas}\n'
#         f'Specializacija: {specializacija}'
#     )
#     print(info)
# f1()



# 7. Sukurkite funkciją, kuri išvestų 10 atsitiktinių skaičių. Po visų išvestų
# skaičių turėtų padėti tuščią eilutę. Šią funkciją iškvieskite 5 kartus.
# import random
# def ats():
#     for a in range(10):
#         sk = random.randint(10, 500)
#         print(sk, end= '\n')
# for i in range(5):
#     ats()
#




# 8. Sukurkite funkciją, kuri išvestų atsitiktinį skaičių. Už funkcijos ribų
# sukurkite ciklą, kurį būtų vykdomas 10 kartų. Iškvieskite sukurtą funkciją
# cikle. Turėtumėte pamatyti 10 atsitiktinių skaičių.

# def f1():
#     sk = random.randint(1, 50)
#     print(sk)
# for i in range(10):
#     f1()

# 9. Sukurkite funkciją pasisveikinimui, šiai funkcijai per argumentus
# perduokite vardą, funkcijoje išveskite tekstą labas ir gautą vardą.
# Sukurkite kitą funkciją, kuri irgi per argumentus gautų vardą, tačiau
# pasakytų 'viso gero' ir patį vardą. Ne funkcijose susikurkite kintamąjį
# vardui saugoti ir įrašykite vardą. Iškvieskite abi funkcijas, perduodant
# kintamąjį joms.

# vardas = "Kostas"
# def pasisveikinti(vardas):
#     print("labas", vardas)
# pasisveikinti(vardas)
# def pasisv(vardas):
#     print("viso gero", vardas)
# pasisv(vardas)


# 10.Sukurkite funkciją, kuriai perduotumėte du skaičius. Ši funkcija turi rasti
# kuris skaičius yra didesnis ir išvesti gautą atsakymą, o jei skaičiai lygūs -
# tuomet išvesti, kad skaičiai lygūs. Iškvieskite šią funkciją keletą kartų,
# duodant skirtingus skaičius.
#
# def f1():
#     c = random.randint(1,10)
#     d = random.randint(1, 10)
#     if c > d:
#         print(f"{c} yra didesnis uz {d}")
#     elif c < d:
#         print(f"{c} yra mazesnis uz {d}")
#     else:
#         print("Skaiciai lygus")
# for i in range(5):
#     f1()


# 11.Sukurkite funkciją, kuri per argumentus gautų automobilių duomenis
# (markė, modelis, gamybos metai, darbinis tūris). Ši funkcija turėtų šiuos
# duomenis išvesti kaip nors gražiai formatuotai. Iškvieskite šią funkciją du
# kartus, perduodant skirtingus duomenis jai.

# def f1(marke, modelis, metai, darbinis):
#     print(f"{marke} {modelis}, {metai} gamybos metai, {darbinis} L")
#     print(end= '\n')
# f1("BMW", "7 series", 2023, 3.0)
# f1("Mercedes-Benz", "S-class", 2023, 3.0)



# 12.Sukurkite funkciją sumai skaičiuoti, ši funkcija per argumentus turėtų
# gauti du skaičius, bei išvesti patį veiksmą kartu su atsakymu (pvz 7 + 5 =
# 12). Sukurkite tokias pačias funkcijas skirtumui, sandaugai ir dalmeniui
# rasti. Sukurkite dar vieną funkciją, kuri sugeneruotų du atsitiktinius
# skaičius, bei iškviestų kitas 4 funkcijas, perduodant joms sugeneruotus
# skaičius. Šią bendrąją funkciją iškvieskite keletą kartų.
# def sksuma(a, b):
#     suma = a + b
#     skirtumas = a - b
#     sandauga = a * b
#     dalmuo = a / b if b != 0 else "neribota"
#     print(f"{a} + {b} = {suma}")
#     print(f"{a} - {b} = {skirtumas}")
#     print(f"{a} * {b} = {sandauga}")
#     print(f"{a} / {b} = {dalmuo}\n")
# sksuma(5, 9)
# sksuma(18, 23)
# def sk():
#     a = random.randint(1, 10)
#     b = random.randint(1, 10)
#     sksuma(a, b)
# for i in range(3):
#     sk()

# 13.Susikurkite funkciją, kuri per argumentus priimtų žodžių masyvą.
# Funkcijoje išveskite visus žodžius iš masyvo atskirose eilutėse, nurodant
# žodžio ilgį (simbolių kiekį). Už funkcijos ribų susikurkite žodžių masyvą ir
# užpildykite jį duomenimis. Iškvieskite sukurtą funkciją perduodant turimą
# masyvą.

# def m1(masyvas):
#     for zodis in masyvas:
#         print(f"{zodis} - ilgis: {len(zodis)} simboliu")
#     print(end= '\n')
#
# zodziai = ["Vaikas", "geras", "klonas", "skalbimo masina", "gerbuvis"]
# m1(zodziai)


# 14.Susikurkite funkciją, kuri per argumentus priimtų skaičių masyvą. Funkcija
# turėtų atspausdinti visus skaičius, šalia jų išvedant to skaičiaus kvadratą ir
# jį padalintą iš dviejų. Už funkcijos ribų susikurkite du skaičių masyvus ir
# užpildykite jį duomenimis. Iškvieskite funkciją du kartus, kiekvieną kartą
# perduodant skirtingą turimą masyvą.

# def m1(masyvai):
#     for skaicius in masyvai:
#         print(f"{skaicius} kvadratas = {skaicius}**2 = {skaicius ** 2} dalyba = {skaicius}/2 = {skaicius / 2}")
#     print(end= '\n')
#
# sk = [8, 7, 15, 26, 24, 17, 6, 2, 1]
# sk2 = [9, 55, 74, 47, 88, 98, 99, 69]
# m1(sk)
# m1(sk2)


# 15.Susikurkite funkciją, kuri per argumentus priimtų pažymių masyvą, bei
# studento vardą su pavarde. Funkcija turėtų išvesti studento vardą ir
# pavardę, jo pažymius. Taip pat, suskaičiuoti vidurkį, bei jį išvesti. Už
# funkcijos ribų susikurkite reikiamus kintamuosius ir masyvus, arba
# objektus studentų pažymiams saugoti ir užpildykite juos duomenimis.
# Iškvieskite šią funkciją perduodant visus reikalingus duomenis.

# def fnc(vardas, pavarde, pazymiai):
#     print(f"{vardas} {pavarde}\nPazymiai: {pazymiai}")
#     print(f"Vidurkis: {sum(pazymiai)/ len(pazymiai)}\n")
# fnc("Petras", "Grazulis", [2, 4, 6, 8])
# fnc("Jonas", "Petrulis", [5, 8, 9, 10])

# 16.Susikurkite funkciją, kuri per argumentus priimtų skaičių masyvą. Funkcija
# turėtų rasti didžiausią skaičių iš masyvo bei išvesti gautą atsakymus. Taip
# pat, susikurkite funkciją, kuri per argumentus priimtų masyvą ir į jį
# sugeneruotų pasirinktą kiekį atsitiktinių skaičių. Susikurkite tris tuščius
# masyvus. Iškvieskite atsitiktinių skaičių generavimo funkciją tris kartus,
# kiekvieną kartą perduodant funkcijai vis kitą masyvą. Kai duomenys bus
# užpildyti, masyvuose esančią informaciją išsiveskite norimu būdu (per
# console.log arba per dar atskirą funkciją). Tuomet kvieskite didžiausio
# skaičiaus paieškos funkciją tris kartus, kiekvieną kartą perduodant
# skirtingą masyvą į ją.

# def tol(skaicius):
#     print(f"{skaicius}\nDidziausias skaicius is masyvo: {max(skaicius)}")
# tol([2,6,14,25,9,4])
#
# def fol(masyvas, kiekis):
#     for i in range(random.randint(1,10)):
#             masyvas.append(random.randint(5, 10))
# masyvas1 =[]
# masyvas2 =[]
# masyvas3 =[]
# fol(masyvas1, random.randint(1, 60))
# fol(masyvas2, random.randint(1, 60))
# fol(masyvas3, random.randint(1, 60))
# print("Masyvas 1:", masyvas1)
# print("Masyvas 2:", masyvas2)
# print("Masyvas 3:", masyvas3)

# 17.Susikurkite funkciją, kuri grąžintų bet kokį jūsų norimą sakinį. Iškvieskite
# šią funkciją ir išspausdinkite gautus rezultatus.



# 18.Susikurkite funkciją, kuri grąžintų atsitiktinai sugeneruotą skaičių.
# Iškvieskite šią funkciją kelis kartus ir gautus atsakymus išveskite kokiu
# norite būdu.



# 19.Susikurkite funkciją, kuri per argumentus priimtų studento vardą ir
# vidurkį. Ši funkcija turėtų sugeneruoti iš to sakinį (pvz Studentas Tomas
# turi vidurkį 8.7) ir tai grąžinti kaip atsakymą. Iškvieskite šią funkciją bent
# porą kartų, perduodant vis skirtingus duomenis. Gautus atsakymus
# išveskite.



# 20.Susikurkite funkciją, kuri per argumentus gautų skaičių. Ji turėtų surasti
# duoto skaičiaus mažiausią daliklį (skaičių iš kurio dalinasi be liekanos). Už
# funkcijos ribų sukite ciklą nuo 10 iki 30 ir kiekvienoje ciklo iteracijoje
# iškvieskite šią funkciją, perduodant ciklo kintamąjį.




# 21.Susikurkite funkciją, kuri per argumentus gautų skaičių. Ji turėtų patikrinti
# ar šis skaičius yra pirminis (grąžina True jei pirminis, ir False jei ne
# pirminis). Už funkcijos ribų sukite ciklą nuo 2 iki 15, kiekvienoje ciklo
# iteracijoje išveskite tikrinamą skaičių ir šalia jo iškviestos funkcijos
# atsakymą (pvz 10 false, 11 true, ...).




# 22.Susikurkite bent 3 matematines funkcijas, priimančias reikiamus
# # argumentus (pvz suma iš dviejų skaičių, suma iš trijų skaičių, skirtumas,
# # sandauga, dalyba) ir grąžinančias atitinkamus atsakymus. Taip pat,
# # susikurkite funkciją, kurioje būtų sugeneruojamas reikiamas kiekis
# # atsitiktinių skaičių ir išvedami visų skaičiavimų atsakymai su veiksmais
# # (iškviečiant atitinkamas kitas funkcijas ir perduodant reikiamus
# # kintamuosius) (pagal 23 pavyzdį). Iškvieskite šią pagrindinę funkciją bent
# # kartą.




# 23.Susikurkite funkciją kuri priimtų skaičių masyvą per argumentus. Ši
# funkcija turėtų rasti duotųjų skaičių sumą ir grąžinti gautą atsakymą. Už
# funkcijos ribų susikurkite du skaičių masyvus ir užpildykite juos
# duomenimis. Iškvieskite turimą funkciją du kartus, jai abu kartus
# perduodant skirtingą masyvą. Gautus atsakymus išveskite. Taip pat,
# raskite kuri suma gavosi didesnė ir išveskite atsakymą.




# 24.Susikurkite funkciją kuri per argumentus priimtų žodžių masyvą. Ji turėtų
# rasti ir grąžinti ilgiausią žodį masyve. Už funkcijos ribų susikurkite žodžių
# masyvą. Iškvieskite funkciją perduodant jai žodžių masyvą. Gautą
# atsakymą išveskite, taip pat, nurodykite šio žodžio ilgį.




# 25.Susikurkite funkciją kuri per argumentus priimtų pažymių masyvą. Ji
# turėtų patikrinti ar visi pažymiai teigiami: jei visi teigiami turėtų grąžintų
# True kaip atsakymą, o jei yra bent vienas neigiamas - False. Susikurkite du
# pažymių masyvus. Iškvieskite šią funkciją du kartus, abu kartus
# perduodant skirtingus masyvus. Gautus atsakymus paverskite į tekstą
# (jeigu gavote True - išveskite tekstą 'visi studento pažymiai teigiami', jei
# False - 'studentas turi bent vieną neigiamą pažymį'). Šiam iškonvertavimui
# iš True/False į tekstą galite pamėginti pasikurti atskirą funkciją, jai
# perduoti kitos funkcijos atsakymą.




# 26.Pabandykite parašyti bent dvi pasirinktas funkcijas, kuriose būtų
# naudojami default parametrai. Iškvieskite šias funkcijas įvairiais būdais
# (perduodant visus argumentus, bei neperduodant tų kuriuos galima
# praleisti (turinčius default reikšmes)).


#UZDAVINIAI IS WORDO LENGVESNI.



# 1. Sukurkite Funkciją kuri priima du int tipo kintamuosius. Juos susumuoja ir atspausdina.
# def kint(a, b):
#     suma = a + b
#     print(f"{a}+{b} = {suma}")
# kint(7, 9)


# 2. Sukurkite Funkciją kuri vadinasi PISq. Funkcija gražina float tipo reikšmę. Reikšmė yra : 9.8596; Gautą reikšmę atspausdinkite.
# def PISq():
#     return 9.8596
# print(PISq())



# 3. Sukurkite Funkciją kuri priima du int tipo kintamuosius. Funkcija gražina skaičių sandaugą.; Gautą reikšmę atspausdinkite.
# def kint(a, b):
#     print(f"{a} * {b} = {a*b}")
# kint(4, 3)


# 4. Sukurkite Funkciją kuri priima masyvą, prasuka ciklą ir atspausdina kiekvieną narį vienoje eilutėje.
# def masyvas1(masyvas):
#     for skaicius in masyvas:
#         print(skaicius, end= ' ')
#     print()
# sk = [random.randint(1, 100)for _ in range (10)]
# masyvas1(sk)


# 5. Sukurkite Funkciją kuri priima du int tipo kintamuosius, min ir max reikšmėms nustatyti ir sugeneruoja random int skaičių ir jį gražintų.
# def kint(minSk, maxSk):
#     sk = random.randint(minSk, maxSk)
#     return sk
# result = kint(1, 10)
# print(f"Atsitiktinis skaicius: {result}")


# 6. Sukurkite Funkciją kuri sugeneruotų random int skaičių masyvą ir jį gražintų.
# Funkcija priima tris int tipo kintamuosius, min, max ir length reikšmėms nustatyti.




# 7. Sukurkite Funkciją kuri panaudotų 6toje užduotyje sugeneruotą masyvą (priimtų kaip kintamąjį), susumuotų ir gražintų reikšmę.




# 8. Sukurkite Funkciją kuri priimtų 6toje užduotyje sugeneruotą masyvą ir gražintų jos skaičių vidurkį (double).




# 9. Sukurkite Funkciją kuri priimtų du int skaičius ir atspausdintų stačiakampį užpildytą žvaigždutėmis.
# Pirmas int - išoriniam ciklui, antras vidiniam.




# 10. Sukurkite Funkciją kuri priimtų sakinį kaip kintamąjį ir atspausdintų kiek jame yra raidžių(simbolių) ir tarpų.
# Sakinys - “Šiandien labai graži diena”. (kodas turi veikti padavus bet kokį sakinį)


# 11. Sukurkite Funkciją kuri priimtų sakinį, jį užkoduotų ir grąžintų. Kodavimas - sakinį apsukame iš kitos pusės. Pvz “Naglis” turi gautis “silgaN”.




#UZDAVINIAI IS WORDO SUNKESNI.