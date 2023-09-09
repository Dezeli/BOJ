# DNA 해독
import sys

N = int(sys.stdin.readline().rstrip())

dna_dict = {
    ("A", "A"): "A",
    ("A", "G"): "C",
    ("A", "C"): "A",
    ("A", "T"): "G",
    ("G", "A"): "C",
    ("G", "G"): "G",
    ("G", "C"): "T",
    ("G", "T"): "A",
    ("C", "A"): "A",
    ("C", "G"): "T",
    ("C", "C"): "C",
    ("C", "T"): "G",
    ("T", "A"): "G",
    ("T", "G"): "A",
    ("T", "C"): "G",
    ("T", "T"): "T",
}

dna = sys.stdin.readline().rstrip()
dna = [i for i in dna]

dna.reverse()
one_dna = ""
for i in dna:
    if one_dna:
        one_dna = dna_dict[(one_dna, i)]
    else:
        one_dna = i

print(one_dna)
