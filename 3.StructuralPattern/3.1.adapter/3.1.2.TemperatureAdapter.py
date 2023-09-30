from abc import ABC, abstractmethod


class TemperatureAdapter(ABC):
    @abstractmethod
    def convertToFahrenheit(self):
        pass


class CelsiusTemperature(TemperatureAdapter):
    def __init__(self, t):
        self.t = t
    def convertToFahrenheit(self):
        return FahrenheitTemperature((self.t * 9/5) + 32)


class FahrenheitTemperature:
    def __init__(self, t):
        self.t = t

    def __str__(self):
        return f'{self.t}'


class TemperatureReportingSystem:
    def reportTemperature(self, ta):
        print(ta.convertToFahrenheit())
