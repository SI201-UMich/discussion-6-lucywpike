import unittest
import os
import csv

class HorseRaces:
    def __init__(self, filename):
        self.race_dict = self.load_results(self.process_csv(filename))

    def process_csv(self, f):
        '''
        Parameters: 
            f, name or path or CSV file: string

        Returns:
            list of lists
        '''
        table = []

        # Do not modify this code
        # This opens the CSV and saves it as a list of lists
        base_path = os.path.abspath(os.path.dirname(__file__))
        full_path = os.path.join(base_path, f)
        # Open the file to be read by Python
        with open(full_path) as file:
            # Get each of the rows in this file
            rows = file.readlines()
            for row in rows:
                # Because this is a CSV, we SPLIT the row by commas
                # We go through each line and build a list of cells
                table_row = []
                for cell in row.strip().split(','):
                    table_row.append(cell)
                # Append the list of cells to the table
                table.append(table_row)
        # print(table)
        return table

###############################################################################
##### TASK 1
###############################################################################
    def load_results(self, table):
        '''
        Given the processed CSV (as a list of lists), populate a nested dictionary with the horse information.

        NOTE: You will need to use float() to convert the race time from str to float.

        Parameters: 
            table, a list of lists
                inner lists are individual rows in the CSV
                inner elements are the cells of each row
                EXAMPLE: [["Horse", "Tenno Sho Fall", "Tenno Sho Spring", "Teio Sho"],
                          ["Special Week", "16.5", "16.3", "17.0"]]

        Returns:
            nested dict structure from csv
            outer keys are (str) horses, outer values are dicts
            inner keys are (str) races, inner values are (int) race times
            EXAMPLE: {'Special Week': {'Tenno Sho Fall': 16.5, 'Tenno Sho Spring': 16.3, 'Teio Sho': 17.0}}
        '''
        result_dict = {} # creates empty dictionary to be filled in with horse names and their race times 

        headers = table[0] # sets the first row of the table as the headers 

        for row in table[1:]: # iterates through the rest of the rows in the table, which contain the horse names
            horse_name = row[0] # sets the first element of each row as the horse name, which will be the key in the outer dict 
            result_dict[horse_name] = {} # creates an empty dictionary for each horse name, which will be filled in with the race names and times 

            for i in range(1, len(row)): # iterates through the rest of the elements in each row, which contain the race times
                race_name = headers[i] # sets the header of each column as the race name, which will be the key in the inner dict
                race_time = float(row[i]) # converts the race time from a string to a float, which will be the value in the inner dict
                result_dict[horse_name][race_name] = race_time # adds the race name and time to the inner dict for each horse

        return result_dict # returns the nested dictionary with the horse names as keys and their race times as values

###############################################################################
##### TASK 2
###############################################################################

    def horse_fastest_race(self, horse):
        '''
        Given the name of a horse, return its fastest race and time.
        If the horse does not exist, return (None, 999.9)

        Parameters:
            horse, name of a race: str

        Returns:
            tuple of fastest race name and the time
            EXAMPLE: ('Teio Sho', 14.8)
        '''
        fastest_race = None
        fastest_time = 999.9

        if horse not in self.race_dict:
            return (fastest_race, fastest_time)
        
        horse_information = self.race_dict[horse] 

        for race, time in horse_information.items():
            if time < fastest_time:
                fastest_race = race
                fastest_time = time 
        return (fastest_race, fastest_time) 

###############################################################################
##### TASK 3
###############################################################################
        
    def horse_personal_best(self):
        '''
        Calculate the fastest race and time for each horse.

        Returns:
            A dictionary of tuples of each horse, with their fastest race and time.
            EXAMPLE: {"Oguri Cap": ("Tenno Sho Fall", 16.6), "Mejiro McQueen": ("Tenno Sho Fall", 16.1)}
        '''
        pass

###############################################################################
##### TASK 4
###############################################################################

    def get_average_time(self):
        '''
        Calculate the average race time for each horse.

        Returns:
            A dictionary with each horse and their average time.
            EXAMPLE: {'Gold Ship': 16.5, 'Daiwa Scarlet': 17.2}
        '''
        pass

###############################################################################
##### DO NOT MODIFY THE UNIT TESTS BELOW!
###############################################################################
class dis7_test(unittest.TestCase):
    '''
    Unit tests to check that our functions were implemented correctly.
    '''
    def setUp(self):
        self.horse_races = HorseRaces('race_results.csv')

    def test_load_results(self):
        # Check that outer values are dictionaries
        self.assertIsInstance(self.horse_races.race_dict['Special Week'], dict)
        # Check one horse's time
        self.assertAlmostEqual(self.horse_races.race_dict['Special Week']['Tenno Sho Spring'], 16.3)

    def test_horse_fastest_race(self):
        nonexistent_horse = self.horse_races.horse_fastest_race('Bob')
        self.assertEqual(nonexistent_horse[0], None)
        fastest_horse = self.horse_races.horse_fastest_race('Symboli Rudolf')
        self.assertEqual(fastest_horse[0], 'Teio Sho')
        self.assertAlmostEqual(fastest_horse[1], 14.8)

    def test_horse_personal_best(self):
        self.assertEqual(self.horse_races.horse_personal_best()['Oguri Cap'][0], 'Tenno Sho Fall')
        self.assertAlmostEqual(self.horse_races.horse_personal_best()['Oguri Cap'][1], 16.6)

    def test_get_average_time(self):
        self.assertAlmostEqual(self.horse_races.get_average_time()['Gold Ship'], 16.5)

def main():
    unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
