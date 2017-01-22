import sys
Origin = ["science.txt","art.txt"]
fz = ["fz_science.txt","fz_art.txt"]
def sort(name,i):
	input1 = open(name[i])
	In = input1.read()
	grade = In.split("\n")
	while '' in grade:
		grade.remove('')
	input1.close()
	return [grade[i] for i in range(0,len(grade))]
i = 0
while i <= 1:
	ori_grade = sort(Origin,i)
	fz_g = sort(fz,i)
	fz_grade = sorted(fz_g)
	fz_grade.reverse()
	order = []
	for k in range(0,len(ori_grade)):
		if(ori_grade[k] < min(fz_grade)):
			order.append(str(len(fz_grade)+1))
			break
		else:
			for j in range(0,len(fz_grade)):
				if(ori_grade[k] >= fz_grade[j]):
					order.append(str(j+1))		
					break

	file = open("cmp_"+Origin[i],"w")
	for l in order:
		file.write(l+"\n")
	file.close()
	i += 1
