import functools

def collapse(L):
	if(len(L)==1):
		if(type(L[0])==str):
			return L[0]
		else:
			return collapse(L[0])

	t=functools.reduce((lambda a,b : (a + " " + b) if type(a)==str and type(b) == str else ((a+ " "+ collapse(b)) if type(a)==str and type(b)!=str else ((collapse(a) + " " + b) if type(a)!=str and type(b)==str else (collapse(a) + " "+ collapse(b))) )),L)
	return t

# L = [[[ [[[[[["this","is"]]]]]], [[ ["an", "interesting", "python"], ["programming", "exercise."] ] ] ]]]
 
# print(collapse(L))