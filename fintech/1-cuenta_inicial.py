saldo = 0

primer_movimiento = 200
if primer_movimiento > 0:
  print("Se ha realizado un depósito")
else:
  print("Se ha realizado un retiro")

saldo = saldo + primer_movimiento

# Another 4 transactions
segundo_movimiento = 100
if segundo_movimiento > 0:
  print("Se ha realizado un depósito")
else:
  print("Se ha realizado un retiro")
saldo = saldo + segundo_movimiento

tercer_movimiento = 300
if tercer_movimiento > 0:
  print("Se ha realizado un depósito")
else:
  print("Se ha realizado un retiro")
saldo = saldo + tercer_movimiento

cuarto_movimiento = -500
if cuarto_movimiento > 0:
  print("Se ha realizado un depósito")
else:
  print("Se ha realizado un retiro")
saldo = saldo + cuarto_movimiento

quinto_movimiento = -100
if quinto_movimiento > 0:
  print("Se ha realizado un depósito")
else:
  print("Se ha realizado un retiro")
saldo = saldo + quinto_movimiento


# Print the final balance
print("Tu saldo final es ",saldo)