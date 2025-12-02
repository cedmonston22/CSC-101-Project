import unittest
import methods
import data

class TestCases(unittest.TestCase):

    def setUp(self):
        self.sample_energy_data = [
            {
                "Room Number": 101,
                "Shower Energy": 10,
                "Light Energy": 20,
                "Fan Energy": 30,
                "Air Purifier Energy": 40,
                "Device Energy": 50,
            },
            {
                "Room Number": 102,
                "Shower Energy": 20,
                "Light Energy": 30,
                "Fan Energy": 40,
                "Air Purifier Energy": 50,
                "Device Energy": 60,
            },
            {
                "Room Number": 103,
                "Shower Energy": 30,
                "Light Energy": 40,
                "Fan Energy": 50,
                "Air Purifier Energy": 60,
                "Device Energy": 70,
            },
        ]

    def test_calculate_average_all(self):
        result = methods.calculate_average_all(self.sample_energy_data)
        expected = {
            "Shower Energy": 20.0,
            "Light Energy": 30.0,
            "Fan Energy": 40.0,
            "Air Purifier Energy": 50.0,
            "Device Energy": 60.0,
        }
        self.assertEqual(result, expected)

    def test_find_above_average_shower(self):
        result = methods.find_above_average(self.sample_energy_data, "Shower Energy")
        expected = "Rooms with above average Shower Energy usage: [103]"
        self.assertEqual(result, expected)

    def test_energy_type_average_shower(self):
        result = methods.energy_type_average(self.sample_energy_data, "Shower Energy")
        expected = "Average Shower Energy usage: 20.0 Watts"
        self.assertEqual(result, expected)

    def test_total_energy_average(self):
        result = methods.total_energy_average(self.sample_energy_data)
        self.assertEqual(result, 200.0)

    def test_highest_total_energy(self):
        result = methods.highest_total_energy(self.sample_energy_data)
        expected = "Room 103 has the highest total energy with 250 Watts"
        self.assertEqual(result, expected)

    def test_lowest_total_energy(self):
        result = methods.lowest_total_energy(self.sample_energy_data)
        expected = "Room 101 has the lowest total energy with 150 Watts"
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()