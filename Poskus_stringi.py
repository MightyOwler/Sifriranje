sporocilo ="živijo" ##https://developers.google.com/edu/python/strings
print("Prvi znak:",sporocilo[0]) ##napiše tisti znak po vrsti
print("Dolžina:" , len(sporocilo))
print(sporocilo + " živijo")

a = 5 ##ne moremo napisati print("vrednost a-ja je:" + a)
print("Vrednost a-ja je: " + str(a))

print(sporocilo.upper()) ##obstaja tudi sporocilo.lower()

print(sporocilo.strip()) ##odstrani vse presledke

print(sporocilo.isalpha())
print(sporocilo.isdigit())
print(sporocilo.isspace())

print(sporocilo.startswith("ž")) #tudi ends with

print(sporocilo.find("v"))

print(sporocilo.replace("i", "u")) ##zamenja številke

print(sporocilo.split("i")) #odstrani i-je in da tam presledke
print(sporocilo.join("1,2,3")) #čudno

print(sporocilo[3:])

text ="%d little pigs come out, or I'll %s, and I'll %s, and I'll blow your %s down." % (3, 'huff', 'puff', 'house') #lahko poenostavimo 
print(text)
                                                                                        
