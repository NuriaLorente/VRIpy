""" Class for calculating baselines in physical space between 
 antennas for the Virtual Radio Interferometer """

 class Baseline(object):
 	 	def __init__(self, antenna_a, antenna_b):
 	 		self.antenna_a = antenna_a # First antenna
 	 		self.antenna_b = antenna_b # Second antenna
		
		def distance(self, antenna_a, antenna_b):
			distance = sqrt( (antenna_a.x - antenna_b.x)**2
				+ (antenna_a.y - antenna_b.y)**2
				+ antenna_a.z - antenna_b.z)**2 )
			return distance

			