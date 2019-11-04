# Rhythm-Distance

* Calculate distance between two Rhythm Segment.
* User Ruler Class to measure the distance.


* for example (in main)

<pre><code>	m1 = 10
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
</code><pre>