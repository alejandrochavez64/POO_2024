#6.- Mostrar todas las tablas del 1 al 10. Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10

for tabla in range(1,11):
 print(f"\nTabla Multiplicar del {tabla}")
 for i in range(1,11):
   print(f"{tabla} X {i} = {tabla*i}")
