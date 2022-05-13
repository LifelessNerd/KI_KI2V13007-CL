class Country:
    """
    A Country has a name and a population size.
    People can be born and die, changing the population size.

    Attributes:
        name: str: the name of the country (required)
        population: int: how many people live there (required)
        BONUS Must be at least 0.

    """

    def __init__(self, name, pop):
        """
        @param name:
        @param pop:
        Initialises a Country with a name and population.
        BONUS: If the population size given is less then 0, raises
            ValueError("Population must be at least 0")

        """
        self.name = name
        if pop >= 0:
            self.population = pop
        else:
            raise ValueError("Population must be at least 0")

    def __repr__(self):
        """
        String representation of a country
        :return: str
        """
        return "{}, population {}".format(self.name, self.population)

    def births(self, births):
        """
        @param births:
        Adds the given number to the population.
        Prints "Population increased by x%", where x is
            how much the population grew by due to these births
            If the population was previously 0, it tells the user and no population is changed
        """

        try:
            oud = self.population
            self.population = self.population + births
            percentage = ((self.population - oud)/oud)*100
            print("Population increased by {}%".format(percentage))
        except:
            print("Could not change population: population of the country cannot be zero: division by zero occured.")
            self.population = oud
            print("The population of", self.name, "is kept at", self.population)




    def deaths(self, deaths):
        """
        @param deaths:
        Removes the given number from the population, unless that takes the
        population below 0, in which case it reduces it to 0
        Prints "Population decreased by x%", where x is
            how much the population decreased by due to these deaths.
            If the population was previously 0, it tells the user and no population is changed

        """
        try:
            oud = self.population
            self.population = self.population - deaths
            if self.population < 0:
                self.population = 0
            percentage = abs(((self.population - oud)/oud)*100)

            print("Population decreased by {}%".format(percentage))
        except:
            print("Could not change population: population of the country cannot be zero: division by zero occured.")
            self.population = oud
            print("The population of", self.name, "is kept at", self.population)


# nederland = Country(name="Nederland", pop=17000000)
# nederland.births(17000000)
# nederland.deaths(170000)


