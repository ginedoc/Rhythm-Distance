import csv
import json
import numpy as np
from fractions import Fraction

class PhraseGroundtruth:
	def __init__(self, src):
		with open(src, 'r', encoding='utf-8', errors='ignore') as f:
			csv_file = [n for n in csv.reader(f)]

			self.time_signature = csv_file[0][1].split(' : ')[1]
			self.beats_per_bar, self.note_value \
					 = list(map(int, self.time_signature.split('/')))
			self.phrases = [n for n in csv_file[1:]]

	# nth phrase
	def phrase(self, n=1):
		phrase = list(map(Fraction, self.phrases[n-1][:-2])) + \
									[self.phrases[n-1][-2]]
		on_note = phrase[0] + Fraction(phrase[1]/self.beats_per_bar)
		off_note = phrase[2] + Fraction(phrase[3]/self.beats_per_bar)
		duration = off_note - on_note + Fraction(phrase[4]/self.beats_per_bar)
		return on_note, off_note, duration

	def phrase_in_ratio(self):
		phrases = []
		for n in range(len(self.phrases)):
			phrases += [self.phrase(n)[1]] + [self.phrase(n)[0]]
		return np.unique(phrases)

	def phrase_in_measure(self):
		phrases = []
		for n in range(len(self.phrases)):
			on, off, _ = self.phrase(n)
			phrases.append(int(on))
			phrases.append(int(off))
		return np.unique(phrases)

class Syncopation:
	def __init__(self, path='../data/Syncopation', score='b_20_1', model='WNBD', track='R'):
		self.src = ('%s/%s_syncopation/%s_%s_%s.json')%(path, score, score, model, track)
		with open(self.src) as f:
			self.values = json.load(f)
		#
		self.syncopation = [0 for _ in range(self.values['number_of_bars'])]
		for n in (self.values)['bars_with_valid_output']:
			self.syncopation[n] = (self.values)['syncopation_by_bar'][n]
	
	def syncopation_by_bar(self):
		return self.syncopation
	def syncopation_by_measure(self, measure=1):
		return self.syncopation[measure-1]
	def syncopation_by_measures(self, on_measure=1, off_measure=2):
		if on_measure <= 0:
			on_measure = 1
		if off_measure < 0:
			off_measure = len(self.ssyncopation)-off_measure
		return self.syncopation[on_measure-1:off_measure]
	def mean_per_bar(self):
		return self.values['mean_syncopation_per_bar']
	def feature(self, method=0):
		if method==0:
			return [((self.syncopation)[i]-(self.syncopation)[i-1]) for i in range(1, len(self.syncopation))]

