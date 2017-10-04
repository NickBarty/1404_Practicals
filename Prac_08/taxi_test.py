from Prac_08.taxi import Taxi

prius = Taxi('prius', 100)
prius.drive(40)
print(prius, prius.get_fare())
prius.start_fare()
prius.drive(100)
print(prius, prius.get_fare())
