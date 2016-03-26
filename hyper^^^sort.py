import sys

class ListWrapper():
	def __init__(self, l):
		self.l = l

def bubblesort(L):
	v = L.l
	s = len(v)
	for i in range(1, s+1):
		for j in range(s-i):
			if (v[j+1] < v[j]):
				v[j], v[j+1] = v[j+1], v[j]

def permutations(l):
	size = len(l)
	ret = []
	if (size<=1):
		ret.append(l[:])
	else:
		for i in range(size):
			L1 = l[:]
			del L1[i]
			P0 = permutations(L1)
			for j in range(size-1):
				ret = ret + [[l[i]] + P0[j]]
	return ret

def multilevelsort(L, k):
	if (k == 0):
		bubblesort(L)
	else:
		P = permutations(L.l)
		P = ListWrapper(P)
		multilevelsort(P, k-1)
		L.l = P.l[0]

def hypersort(v):
	L = ListWrapper(v)
	n = len(v)
	multilevelsort(L, n**(n**(n**(n**(n)))))
	return L.l

if __name__=="__main__":
	try:
		lis = range(1, sys.argv[1]+1)
	except:
		lis = [2, 3, 1]
	print hypersort(lis) # note: calling this line is in general a pretty bad idea, be warned :)
