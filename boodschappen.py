def toonmenu(gekozennaam):
  print("Welkom bij uw boodschappenlijstje. Hier kunt u producten toevoegen, verwijderen, u boodschappenlijst bekijken, u producten wijzigen, boodschappen doen en uw producten opslaan.")
  print("")
  print("Hallo, " + gekozennaam + "!")
  print("Kies 1 om uw boodschappen te bekijken.")
  print("Kies 2 om een product toe te voegen.")
  print("Kies 3 om een product te verwijderen.")
  print("Kies 4 om een product te wijzigen.")
  print("Kies 5 om boodschappen te doen.")
  print("Kies stop om te stoppen.")
  print("")

def keuzecheck(gekozenkeuze, bdslst):
  if gekozenkeuze == "1":
    keuze1(bdslst)
  elif gekozenkeuze == "2":
    keuze2(bdslst)
  elif gekozenkeuze == "3":
    keuze3(bdslst)
  elif gekozenkeuze == "4":
    keuze4(bdslst)
  elif gekozenkeuze == "5":
    keuze5(bdslst)
  else: 
    print("Dat is geen keuze!")
    print("")

def keuze1(boodschaplijst):
  if boodschaplijst == {}:
    print("Uw boodschappenlijst is leeg.")
    print("")
  else:
    for key, value in boodschaplijst.items():
      print(key, " €", value)
    print("")

def keuze2(boodschaplijst):
  prdtvg = input("Wat is het product dat u wilt toevoegen? ").lower()
  prdprs = float(input("En hoe duur is dat product? "))
  boodschaplijst[prdtvg] = prdprs
  print("")
  print("Uw product is toegevoegd!")
  print("")

def keuze3(boodschaplijst):
  if boodschaplijst == {}:
    print("U heeft geen boodschappen op uw lijstje staan!")
    print("")
  else:
    for key, value in boodschaplijst.items():
      print(key, " €", value)
    print("")
    prdver = input("Welk product wilt u verwijderen? ").lower()
    print("")
    if prdver in boodschaplijst:
      del boodschaplijst[prdver]
      print("Dat product is verwijderd!")
      print("")
    else:
      print("Dat product staat niet op uw lijst!")
      print("")

def keuze4(boodschaplijst):
  for key, value in boodschaplijst.items():
      print(key, " €", value)
      print("")
  if boodschaplijst == {}:
    print("Uw boodschappenlijst is leeg!")
    print("")
  else:
    prdwzg = input("Welk product wilt u wijzigen? ").lower()
    if prdwzg in boodschaplijst:
      watwzg = input("Wilt u de prijs of de naam wijzigen? ").lower()
      if watwzg == "prijs":
        del boodschaplijst[prdwzg]
        prswzg = float(input("Wat moet de nieuwe prijs worden? "))
        print("")
        boodschaplijst[prdwzg] = prswzg
        print("De prijs is gewijzigd!")
        print("")
      elif watwzg == "naam":
        namwzg = input("Wat moet de nieuwe naam worden? ").lower()
        print("")
        boodschaplijst[namwzg] = boodschaplijst[prdwzg]
        del boodschaplijst[prdwzg]
        print("")
        print("De naam is gewijzigd!")
        print("")
      else: 
        print("Dat is niet een van de keuzes!")
        print("")
    else: 
      print("Dat product staat niet in uw lijst!")
      print("")

def keuze5(boodschaplijst):
  kooplijst = {}
  if boodschaplijst == {}:
    print("U heeft nog geen boodschappen op uw lijst staan!")
    print("")
  else:
    for key, value in boodschaplijst.items():
      print(key, " €", value)
    print("")
    print("Typ een product uit de lijst dat u wilt kopen. Klik op enter na elk product. U hoeft alleen de naam in te vullen. Typ klaar als u alles heeft ingevuld.")
    kpltvg = input("").lower()
    while kpltvg != "klaar":
      if kpltvg in boodschaplijst:
        kooplijst[kpltvg] = boodschaplijst[kpltvg]
        kpltvg = input("").lower()
        def som(kopen):
          return sum(kopen.values())
      else:
        print("Dat product staat niet op uw boodschappenlijst.")
        kpltvg = input("").lower()
    print("Dat kost in totaal: " + "€" + str(som(kooplijst)))
    print("")

def main():
  boodschappenlijst = {}
  naam = input("Wat is uw naam? ")
  print("")
  toonmenu(naam)
  while (keuze := input("Wat kiest u? ").lower()) != "stop":
    print(keuze)
    keuzecheck(keuze, boodschappenlijst)
    toonmenu(naam)
  print("Oké, fijne dag!")

main()
