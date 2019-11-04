from Ruler import LinearRuler
from music_objects import *

n1 = Note(0, 1, 3)
n2 = Note(0, 2, 2.5)
n3 = Note(0, 1, 4)

N1 = [n1, n2, n3]

n1 = Note(0, 1, 3)
n2 = Note(0, 3, 4)
n3 = Note(0, 2, 4)

N2 = [n1, n2, n3]

seg1 = RhythmSegment(N1)
seg2 = RhythmSegment(N2)

ruler = LinearRuler()
ruler.execute(seg1, seg2)
