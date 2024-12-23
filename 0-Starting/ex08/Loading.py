def ft_tqdm(lst: range):
	prct = int(0 * 100/len(lst))
	string = "█" * prct + " " * (100 - prct)
	print(f"\r{prct}%|{string}| {0}/{len(lst)}", end="")
	for i in lst:
		yield
		prct = int((i + 1) * 100/len(lst))
		string = "█" * prct + " " * (100 - prct)
		print(f"\r{prct}%|{string}| {i + 1}/{len(lst)}", end="")
