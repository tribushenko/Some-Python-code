varies_dict, funcs_dict = {}, {}


def create(namespace, variable):
	if namespace in funcs_dict:
		funcs_dict[namespace] += variable
	else:
		funcs_dict[namespace] = variable
	return funcs_dict


def add(namespace, variable):
	if namespace not in varies_dict:
		varies_dict[namespace] = [variable]
	else:
		varies_dict[namespace] += [variable]


def get(variable, namespace):
	try:
		if variable in varies_dict[namespace]:
			return namespace
		else:
			return get(variable, namespace=funcs_dict[namespace])
	except KeyError:
		try:
			return get(variable, namespace=funcs_dict[namespace])
		except KeyError:
			return None


n = int(input("Enter the number: "))
for i in range(n):
	cmd, namespace, variable = input().split()
	if cmd == "add":
		add(namespace, variable)
	elif cmd == "create":
		create(namespace, variable)
	else:
		print(get(variable, namespace))
