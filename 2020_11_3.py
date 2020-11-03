from graphillion import GraphSet
import graphillion.tutorial as tl

from nltk import ngrams
import itertools
import collections

branch = []

stop = []


def recursive(data: str, combs: tuple):
	nexts = []

	for comb in combs:
		if comb[0][0] == data:
			nexts.append(comb[0][1])
			branch.append(comb[0])
	if not nexts:
		stop.append(data)
		return data
	else:
		return data + " " + str([recursive(comp, combs) for comp in nexts])


def get_contents():
	items = []
	strings = open("../Nginx/Nginx_DataSet")

	for string in strings:
		if "RUN" in string:
			items.append(string.replace("RUN","").replace("&&","").replace("\\","").split())
			
		else:
			if string.islower():
				items.append(string.replace("&&","").replace("\\","").split())

	strings.close()
	return items

def get_combinations(items: list):
	sentence_combinations = []
	for item in items:
		sentence_combinations.append(list(ngrams(item, 2)))

	target_combinations = []
	for sentence in sentence_combinations:
	    target_combinations.extend(sentence)

	ct = collections.Counter(target_combinations).most_common()[:200]
	return ct

def main():
	items = get_contents()
	counters = get_combinations(items)

	ans = recursive("ln", counters)
	# print(ans)
	GraphSet.set_universe(branch)

	for one in stop:
		paths = GraphSet.paths("ln", one)
		for item in paths:
			print(item)

	

if __name__ == "__main__":
	main()

