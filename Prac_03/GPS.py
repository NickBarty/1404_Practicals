import random


def main():
    YEARS = 10
    STARTING_POPULATION = 1000
    population = STARTING_POPULATION
    current_year = 1
    print("Welcome to gopher population simulator \nStarting population:", STARTING_POPULATION)
    while YEARS > 0:
        population_growth = random.randint(9, 20)
        population_reduction = random.randint(4, 25)
        born = population * population_growth // 100
        die = population * population_reduction // 100
        population -= die
        population += born
        born_percent = (born * 100) / population
        die_percent = (die * 100) / population
        print("Year:", current_year, "\n*****")
        print("{} gophers were born ({:.2f}%). {} died ({:.2f}%). \npopulation: {}".format(born, born_percent, die,
                                                                                           die_percent, population))
        current_year += 1
        YEARS -= 1


main()
