from Prac_08.unreliable_car import UnreliableCar

prius = UnreliableCar('prius', 100)
for count in range(5):
    prius.drive(5)
    print(prius)