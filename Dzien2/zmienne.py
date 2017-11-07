imie = "Joanna"
nazwisko = "Kowalska"
wiek = 34

print(imie + ' ' + nazwisko + 'ma' + str(wiek) + 'lata.')

#od wersji 3.6 formatowanie stringu

print(f"{imie}{nazwisko} ma {wiek} lata.")

#starszy format
print("{0}{1} ma {2} lata".format(imie, nazwisko, wiek))

# print(imie)
#
# print(imie[3:5])
# print(3 + 7)
# print(3 == 5)
#
# print(imie.lower())
# print(imie.count('a'))
