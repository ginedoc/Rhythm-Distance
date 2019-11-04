import numpy as np

class Notation:
	def __init__(self, midi_num, onset, offset):
		self.reset(midi_num, onset, offset)

	def reset(self, midi_num, onset, offset):
		self.midi_num = midi_num
		self.onset = onset 
		self.offset = offset

class Note(Notation):
	def __init__(self, midi_num, onset, offset):
		super().__init__(midi_num, onset, offset)

class Rest(Notation):
	def __init__(self, onset, offset):
		super().__init__(0, onset, offset)

class RhythmSegment:

	def __init__(self):
		self._elements = []

	def __sub__(self, sub):

		segment = RhythmSegment()
		onsets = self.onsets()+sub.onsets()
		self_rest = [n.onset for n in self.elements() if isinstance(n, Rest)] 
		sub_rest = [n.onset for n in sub.elements() if isinstance(n, Rest)] 

		for onset in np.unique(onsets):

			d1 = self.elements('onset', onset)
			d2 = sub.elements('onset', onset)
			diff_num = abs(len(d1) - len(d2))
			
			if (onset in self_rest) + (onset in sub_rest) == 1:
				segment.append([Rest(onset, -1)])
				continue

			if diff_num > 0:
				segment.append([Note(-1, onset, -1) for _ in range(diff_num)])

		return segment


	def onsets(self):
		results = [n.onset for n in self._elements]
		return results

	def append(self, elements=[]):
		try:
			(self._elements) += elements
		except:
			(self._elements) += [elements]

	def remove(self, n):
		del self._elements[n]

	def elements(self, by='order', *args):
		(self._elements).sort(key=lambda n: n.onset)

		if by=='order':
			return (self._elements)
		elif by=='onset':
			return [n for n in self._elements if n.onset==args[0]]
		elif by=='offset':
			return [n for n in self._elements if n.offset==args[0]]

	def length(self):
		last = sorted(self._elements, key=lambda n: n.onset+n.offset)[-1]
		first = self.elements()[0]


		if last != None and first != None:
			return last.onset + last.offset - first.onset
		else:
			return 0


