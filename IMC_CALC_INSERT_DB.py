# -*- coding: latin1 -*-

import sqlite3

con = sqlite3.connect("imc.db")
cur = con.cursor()

peso = float(input("Digite seu peso:"))
altura = float(input("Digite sua altura:"))
imc = peso / (altura * altura)

sql = "insert into calc_imc values (null, ?, ?, ?)"

recset = [(peso,altura,imc)]

cur.execute(sql, recset)
con.commit()

con.close()

if imc < 17:
  print ("Muito abaixo do peso ")
elif 17 <= imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 25:
    print ("Peso Normal")
elif 25 <= imc < 30:
    print ("Acima do Peso")
elif 30 <= imc < 35:
    print ("Obesidade I")
elif 35 <= imc < 40:
    print ("Obesidade II (severa)")
else:
    print ("Obesidade III (mórbida)")
