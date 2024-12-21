def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
	"""Return a list of bmi calculated from arguments"""
	if ((type(height) is not list) or (not all(type(x) == int or type(x) == float for x in height)) or
	 	(type(weight) is not list) or (not all(type(x) == int or type(x) == float for x in weight)) or
		not len(height) == len(weight)):
		print("Wrong agument type")
		return []
	ret = []
	for i in range(len(height)):
		ret.append(weight[i] / (height[i] ** 2))
	return ret 

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
	"""Return a list of boolean which is the result of x > limit for x in bmi (first argument)"""
	if ((type(limit) is not int) or (type(bmi) is not list) or (not all(type(x) == int or type(x) == float for x in bmi))):
		print("Wrong agument type")
		return []
	for i in range(len(bmi)):
		if bmi[i] > limit:
			bmi[i] = True
		else:
			bmi[i] = False
	return bmi