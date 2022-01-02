package kata

var DNAComplements = map[rune]string{
	'A': "T",
	'T': "A",
	'C': "G",
	'G': "C",
}

func DNAStrand(dna string) string {
	var newDNA string

	for _, word := range dna {
		newDNA += DNAComplements[word]
	}

	return newDNA
}
