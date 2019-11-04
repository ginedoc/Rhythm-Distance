from Ruler import LinearRuler
from music_objects import *
from music21 import converter
from PhraseGroundtruth import *
import glob
import os

def notes_in_measure(measure):
	N = []
	for n in measure.getElementsByClass('Note'):
		N.append(Note(n.pitch.midi, n.offset, n.offset+n.quarterLength))
	for c in measure.getElementsByClass('Chord'):
		for n in c:
			N.append(Note(n.pitch.midi, n.offset, n.offset+n.quarterLength))
	for n in measure.getElementsByClass('Rest'):
		N.append(Rest(n.offset, n.offset+n.quarterLength))

	return N

if __name__ == '__main__':
	"""
	score= converter.parse('../score/b_4_1.xml')		
	ruler = LinearRuler()

	m1 = 10
	m2 = 11
	b=RhythmSegment()		
	v=RhythmSegment()
	b.append(notes_in_measure(score.measure(m1).parts[0].flat))
	v.append(notes_in_measure(score.measure(m2).parts[0].flat))
	print(ruler.execute(b, v))

	b=RhythmSegment()		
	v=RhythmSegment()
	b.append(notes_in_measure(score.measure(m1).parts[1].flat))
	v.append(notes_in_measure(score.measure(m2).parts[1].flat))
	print(ruler.execute(b, v))

	"""
	for filepath in glob.glob("../score/*"):
		filename = filepath.split('/')[-1].split('.')[0]
		score = converter.parse(filepath)
		measure_num = score.flat[-1].measureNumber
		SR = []
		SL = []
		ruler = LinearRuler()

		print(filename)
		for m in range(measure_num):
			b=RhythmSegment()		
			v=RhythmSegment()
			b.append(notes_in_measure(score.measure(m+1).parts[0].flat))
			v.append(notes_in_measure(score.measure(m+2).parts[0].flat))

			s = ruler.execute(b, v)
			SR.append(s)

			b=RhythmSegment()		
			v=RhythmSegment()
			b.append(notes_in_measure(score.measure(m+1).parts[1].flat))
			v.append(notes_in_measure(score.measure(m+2).parts[1].flat))

			s = ruler.execute(b, v)
			SL.append(s)


		if not os.path.exists('../results/'):
			os.mkdir('../results')
		if not os.path.exists('../results/'+filename):
			os.mkdir('../results/'+filename)
		
		with open('../results/'+filename+'/R', 'w') as f:
			for s in SR:
				f.write(str(s)+',\n')
		with open('../results/'+filename+'/L', 'w') as f:
			for s in SL:
				f.write(str(s)+',\n')		
	