import weather

class MetroForecast():


    def __init__(self, metropolis):
        self.metropolis = metropolis
        self.weather_handle = weather.Weather()

    @staticmethod
    def find_min_index(in_list):
        res = 0
        minim = 1000
        for i in range(len(in_list)):
            if int(in_list[i]) < minim:
                minim = int(in_list[i])
                res = i
            i += 1
        return res

    @staticmethod
    def find_max_index(in_list):
        res = 0
        maxim = 0
        for i in range(len(in_list)):
            if int(in_list[i]) > maxim:
                maxim = int(in_list[i])
                res = i
            i += 1
        return res

    def test(self):
        weather_handle = weather.Weather()
        location = self.weather_handle.lookup_by_location(self.metropolis)
        condition = location.condition()
        print(condition['text'])

         # Get weather forecasts for the upcoming 10 days.
        forecastslist = location.forecast()[:5]
        for forecasts in forecastslist:
            print(forecasts['text'])
            print(forecasts['date'])
            print(forecasts['high'])
            print(forecasts['low'])


    def compute_stats(self):
        weather_handle = weather.Weather()
        self.dates = []
        self.high_temperatures = []
        self.low_temperatures = []
        self.rainy_days_index = []
        self.current_condition = ""
        location = self.weather_handle.lookup_by_location(self.metropolis)
        condition = location.condition()
        self.current_condition = condition['text']

        # Get weather forecasts for the upcoming 10 days.
        day_count = 0
        forecastslist = location.forecast()[:5]

        for forecasts in forecastslist:
            self.dates.append(forecasts['date'])
            self.high_temperatures.append(forecasts['high'])
            self.low_temperatures.append(forecasts['low'])
            forecast_text = str(forecasts['text'])
            if forecast_text.find('Rain') != -1:
                self.rainy_days_index.append(day_count)
            day_count += 1

    def print_stats(self):
        print("Highest temperature will be observed on: ", self.dates[self.find_max_index(self.high_temperatures)])
        print("Lowest temperature will be observed on: ", self.dates[self.find_min_index(self.low_temperatures)])
        if len(self.rainy_days_index) > 0:
            print("It will rain on the following dates ... (In the next 5 days)")
            for i in self.rainy_days_index:
                print(self.dates[i])
        else :
            print("It seems like there wont be any rain in the next five days")




def main():
    metro = "Halifax"
    metro_report = MetroForecast(metro)
    metro_report.compute_stats()
    metro_report.print_stats()

if __name__ == '__main__':
    main()