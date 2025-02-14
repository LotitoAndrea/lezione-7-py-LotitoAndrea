lato1 = float(input("inserire primo lato "))
lato2 = float(input("inserire secondo lato "))
lato3 = float(input("inserire terzo lato "))
if lato1 < (lato2 + lato3) and lato2 < (lato1 + lato3) and lato3 < (lato1 + lato2):
    print("La figura è un triangolo.")
else:
    print("La figura non è un triangolo.")