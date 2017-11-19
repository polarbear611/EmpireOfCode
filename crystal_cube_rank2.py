#!/usr/bin/python
# -*- coding: utf-8 -*-

def cg(g):
	for i in range(len(g)-1):
		if g[i][0]==g[i+1][0]:return False
	for l in g:
		for j in range(len(l)-1):
			if l[j+1]==l[j]:return False
	return True
def golf(c):
	for i in range(len(c)-1):
		if c[i][0][0]==c[i+1][0][0]:return False
	for g in c:
		if not cg(g):return False
	return True
# if __name__ == "__main__":
#     assert golf([[["X", "Z"],
#                   ["Z", "X"]],
#                  [["Z", "X"],
#                   ["X", "Z"]]]) == True, "1st example"
#   assert golf([[["X", "Z"],
#                   ["Z", "X"]],
#                  [["X", "Z"],
#                   ["Z", "X"]]]) == False, "2nd example"
#   print("All done? Earn rewards by using the 'Check' button!")

