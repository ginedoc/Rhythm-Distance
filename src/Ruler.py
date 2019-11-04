from music_objects import *

class Ruler:
	def __init__(self):
		None

	def execute(self, seg1=RhythmSegment(), seg2=RhythmSegment()):
		None

class LinearRuler(Ruler):
	def __init__(self):
		super().__init__()

	def execute(self, seg1=RhythmSegment(), seg2=RhythmSegment()):
		seg = seg1 - seg2
		onsets = seg.onsets()

		score = 0

		for n in seg.elements():
			for v in seg1.elements():
				try:
					ratio = n.onset / max(seg.length(), seg1.length())
				except:
					ratio = 0.0

				if n.onset > v.onset:
					score += (n.onset - v.onset) / n.onset * ratio
					
				elif n.onset < v.onset:
					score += (v.onset - n.onset) / (max(seg.length(), seg1.length()) - n.onset) * (1-ratio)

		if len(onsets) != 0:
			#score /= len(seg.elements())
			score /= len(np.unique(onsets))

		return abs(score)