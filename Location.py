""" Location class for antennas/stations for the Virtual Radio Interferometer """

class Location(object):
	""" Location class to show coordinates of antennas/stations """
	def __init__(self, x, y, z):
		""" x,y,z coordinates are defined with respect to the center of the observatory, 
		need to convert to geocentric coordinates at some point. """ 
		self.x = x # x coordinate (EW distance from observatory center)
		self.y = y # y coordinate (NS distance from observatory center)
		self.z = z # z coordinate (altitude rel. to observatory center)