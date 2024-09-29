import logging
logging.basicConfig(level=logging.DEBUG)

dzialanie = input("Podaj działanie, posługując się odpowiednią liczbą: \n Dodawanie - napisz: 1\n Odejmowanie - napisz: 2\n Mnożenie -napisz: 3\n Dzielenie - napisz: 4\n ")
num1 = input("Podaj składnik 1: " )
num2 = input("Podaj składnik 2: " )
if dzialanie == "1":
  num3 = input("Podaj składnik 3: " )
  num4 = input("Podaj składnik 4: " )
  logging.info(f"Dodaję {num1} i {num2} i {num3} i {num4}")
  print("Wynik to", int(num1)+int(num2)+int(num3)+int(num4))
elif dzialanie == "2":
  logging.info(f"Odejmuję {num1} i {num2}")
  print("Wynik to", int(num1)-int(num2))
elif dzialanie == "3":
  num3 = input("Podaj składnik 3: " )
  num4 = input("Podaj składnik 4: " )
  logging.info(f"Mnożę {num1} i {num2} i {num3} i {num4}")
  print("Wynik to", int(num1)*int(num2)*int(num3)*int(num4))
elif dzialanie == "4":
  logging.info(f"Dzielę {num1} i {num2}")
  print("Wynik to", int(num1)/int(num2))
else:
  print("Nie znam takiej operacji.")