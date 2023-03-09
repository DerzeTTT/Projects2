Reading = [Line for Line in open('../liczby.txt', 'r').read().split("\n") if Line != '']

def Get_Prime_Factors(T_Num):
    
	i = 2
	Found = []

	while i**2 <= T_Num:

		if T_Num%i:

			i += 1

		else:

			T_Num //= i
			Found.append(i)

	if T_Num > 1:

		Found.append(T_Num)

	return Found

def Get_Unique(T_List):

	Found = {};

	for v in T_List:

		if not Found.get(v):

			Found[v] = True;

	return list(Found);

Holding = {};

for v in Reading:

	Factors = Get_Prime_Factors(int(v))
	Holding[v] = {'Total':Factors, 'Unique':Get_Unique(Factors)}

def Get_Largest(Ind):

	Largest = ['', 0]

	for i in Holding:

		v = Holding.get(i)
		Val = len(v.get(Ind))

		if Val > Largest[1]:

			Largest[0], Largest[1] = int(i), Val

	return Largest;

for i in range(2):
	
	Picked = Get_Largest((i == 1 and 'Total') or 'Unique')
	print(Picked[0], Picked[1])