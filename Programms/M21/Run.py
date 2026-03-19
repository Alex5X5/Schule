from Programms.M21.Fahrzeuge import Auto
from Programms.M21.Fahrzeuge import Fahrzeug
from Programms.M21.Fahrzeuge import LKW

lkw = LKW("Iveco Strali HI-WAY", 120, 500, 12880, 6, 18000)
print("")
for key in lkw.__dict__.keys():
    print(f"{key}:{lkw.__dict__[key]}")
print("")

auto = Auto("Peugot 308", 203, 125, 1598, 0, 4.25)
print("")
for key in auto.__dict__.keys():
    print(f"{key}:{auto.__dict__[key]}")
print("")

l:list[Fahrzeug] = [lkw, auto]

for f in l:
    f.fahren()