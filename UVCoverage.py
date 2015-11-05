""" Class for calculating UV coverage of an interferometer for the Virtual Radio interferometer """

class UVCoverage(object):
	def __init__(self, observatory):
		self.observatory = observatory

	def baselines(observatory):
		for i in observatory.num_antennas:
			for j in range(i,observatory.num_antennas):
				
