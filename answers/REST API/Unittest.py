import unittest
import requests

class TestWeatherAPI(unittest.TestCase):
#Test weather_data endpoint with valid parameters
    def test_weather_data_valid_params(self):
        params = {'station_id': 'USC00110187', 'record_date': '1985-01-01', 'page': 1, 'per_page': 10}
        response = requests.get('http://localhost:5000/api/weather', params=params)
        self.assertEqual(response.status_code, 200)

   # Test weather_stats endpoint with valid parameters
    def test_weather_stats_valid_params(self):
        params = {'station_id': 'USC00110187', 'record_year': '1985'}
        response = requests.get('http://localhost:5000/api/weather/stats', params=params)
        self.assertEqual(response.status_code, 200)
        
 #Since there arent any invalid parameters hence there's is no point of assseting empty params for validating the invalid parameters. Just using these two test cases.      
  
if __name__ == "__main__":
    unittest.main()
