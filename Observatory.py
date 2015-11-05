""" A class for observatories to use with the Virtual Radio Interferometer
Adapted from the vriObservatory.java class from the legacy code."""

class Observatory(object):
  def __init__(self, menu_name, full_name, 
    latitude, longitude, num_antennas, num_stations,
    ant_diameter, ant_el_limit, 
    antennas, stations, configs)
  self.menu_name = menu_name # Name of observatory in menu
  self.full_name = full_name # Actual name of the observatory
  self.latitude = latitude # Observatory latitude in radians
  self.longitude = longitude # Observatory longitude in radians
  self.num_antennas = num_antennas # Number of antennas
  self.num_stations = num_stations # Number of stations
  self.ant_diameter = ant_diameter # Diameter of antennas (meters)
  self.ant_el_limit = ant_el_limit # Antenna lower elevation limit (degrees)
  self.antennas = antennas # List of antennas (i.e instances of vriAntenna class)
  self.stations = stations # List of stations (instances of vriStation)
  self.configs = configs # List of antenna configurations (list of stations)



