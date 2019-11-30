# -*- coding: latin1 -*-

import sqlite3

con = sqlite3.connect("imc_calc.db")
cur = con.cursor()

sql = "create table calc_imc (id integer primary key, " \
      "nome varchar(100), " \
      "peso float(10), " \
      "altura float(10), " \
      "resultado float(100))"

cur.execute(sql)

con.close()

print ("DB Criada com Sucesso!")
