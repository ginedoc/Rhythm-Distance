# Rhythm-Distance

* Calculate distance between two Rhythm Segment.
* User Ruler Class to measure the distance.


* for example (in main)

<pre><code>	
    // empty music segment
	b=RhythmSegment()		
	v=RhythmSegment()

    // add notes to rhythm segment
	b.append(notes_in_measure(score.measure(m1).parts[0].flat))
	v.append(notes_in_measure(score.measure(m2).parts[0].flat))

    // calculate the distance by ruler
	distance = ruler.execute(b, v)
	
</code><pre>