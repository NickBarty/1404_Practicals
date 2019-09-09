import random


def main():
    years = 10
    starting_population = 1000
    population = starting_population
    current_year = 1
    print("Welcome to gopher population simulator \nStarting population:", starting_population)
    while years > 0:
        population_growth = random.randint(9, 20)
        population_reduction = random.randint(4, 25)
        born = population * population_growth // 100
        die = population * population_reduction // 100
        population -= die
        population += born
        born_percent = (born * 100) / population
        die_percent = (die * 100) / population
        print("Year:", current_year, "\n*****")
        print("{} gophers were born ({:.2f}%). {} died ({:.2f}%). \npopulation: {}\n".format(born, born_percent, die,
                                                                                             die_percent, population))
        current_year += 1
        years -= 1


main()
