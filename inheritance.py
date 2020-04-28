def check_the_parents(parent, child):
	if inheritance[child] == parent:
		print("Yes")
		return True
	else:
		try:
			check_the_parents(inheritance[child], parent)
		except KeyError:
			print("No")
			return False
inheritance = {}
for i in range(int(input())):
	input_class = input().split(":")
	if len(input_class) == 1:
		inheritance[input_class[0]] = "object"
	elif len(input_class[1]) == 1:
		inheritance[input_class[0]] = input_class[1]
	else:
		inheritance[input_class[0]] = input_class[1].split()
print(inheritance)
for i in range(int(input())):
	input_inheritance = input().split()
	check_the_parents(*input_inheritance)

# 4
# A
# B : A
# C : A
# D : B C

# A B
# B D
# C D
# D A
