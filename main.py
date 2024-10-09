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







# 10.Sukurkite funkciją, kuriai perduotumėte du skaičius. Ši funkcija turi rasti
# kuris skaičius yra didesnis ir išvesti gautą atsakymą, o jei skaičiai lygūs -
# tuomet išvesti, kad skaičiai lygūs. Iškvieskite šią funkciją keletą kartų,
# duodant skirtingus skaičius.


# 11.Sukurkite funkciją, kuri per argumentus gautų automobilių duomenis
# (markė, modelis, gamybos metai, darbinis tūris). Ši funkcija turėtų šiuos
# duomenis išvesti kaip nors gražiai formatuotai. Iškvieskite šią funkciją du
# kartus, perduodant skirtingus duomenis jai.






# 12.Sukurkite funkciją sumai skaičiuoti, ši funkcija per argumentus turėtų
# gauti du skaičius, bei išvesti patį veiksmą kartu su atsakymu (pvz 7 + 5 =
# 12). Sukurkite tokias pačias funkcijas skirtumui, sandaugai ir dalmeniui
# rasti. Sukurkite dar vieną funkciją, kuri sugeneruotų du atsitiktinius
# skaičius, bei iškviestų kitas 4 funkcijas, perduodant joms sugeneruotus
# skaičius. Šią bendrąją funkciją iškvieskite keletą kartų.



# 13.Susikurkite funkciją, kuri per argumentus priimtų žodžių masyvą.
# Funkcijoje išveskite visus žodžius iš masyvo atskirose eilutėse, nurodant
# žodžio ilgį (simbolių kiekį). Už funkcijos ribų susikurkite žodžių masyvą ir
# užpildykite jį duomenimis. Iškvieskite sukurtą funkciją perduodant turimą
# masyvą.
# 14.Susikurkite funkciją, kuri per argumentus priimtų skaičių masyvą. Funkcija
# turėtų atspausdinti visus skaičius, šalia jų išvedant to skaičiaus kvadratą ir
# jį padalintą iš dviejų. Už funkcijos ribų susikurkite du skaičių masyvus ir
# užpildykite jį duomenimis. Iškvieskite funkciją du kartus, kiekvieną kartą
# perduodant skirtingą turimą masyvą.


# 15.Susikurkite funkciją, kuri per argumentus priimtų pažymių masyvą, bei
# studento vardą su pavarde. Funkcija turėtų išvesti studento vardą ir
# pavardę, jo pažymius. Taip pat, suskaičiuoti vidurkį, bei jį išvesti. Už
# funkcijos ribų susikurkite reikiamus kintamuosius ir masyvus, arba
# objektus studentų pažymiams saugoti ir užpildykite juos duomenimis.
# Iškvieskite šią funkciją perduodant visus reikalingus duomenis.





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




