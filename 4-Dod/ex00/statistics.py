def mean(values):
	"""Return mean of a list"""
	if (not values):
		print("ERROR")
		return
	ret = 0
	for x in values:
		ret += x
	return ret / len(values)

def median(values):
	"""Return median of a list"""
	if (not values):
		print("ERROR")
		return
	s = sorted(values)
	l = len(values)
	if (l % 2 == 1):
		ret = s[l//2]
	else:
		ret = (s[l//2 - 1] + s[l//2]) /2
	return ret


def quartile(values):
	"""Return quartiles of a list"""
	if (not values or len(values) < 4):
		print("ERROR")
		return
	s = sorted(values)
	l = len(values)
	m = median(values)
	f = [x for x in values if x <= m]
	t = [x for x in values if x >= m]

	return([float(median(f)), float(median(t))])
	
def var(values):
	"""Return variance of a list"""
	if (not values):
		print("ERROR")
		return
	
	m = mean(values)
	l = len(values)
	ret = 0
	for i in values:
		ret += (i - m)**2
	return (ret / l)

def std(values):
	"""Return standard deviation of a list"""
	if (not values):
		print("ERROR")
		return

	return var(values)**.5


def ft_statistics(*args: any, **kwargs: any) -> None:
	"""Applicate statistics formulas input as kwargs to args"""
	formula = list(kwargs.values())
	if not all(type(x) == float or type(x) == int for x in args) or not all(type(x) == str for x in formula):
		print("Type Error")
		return
	formulas = {"mean":mean, "median":median, "quartile":quartile, "std":std, "var":var}

	for i in formula:
		if i in formulas.keys():
			ret = formulas[i](args)
			if (ret):
				print(i, ":", ret)
	return