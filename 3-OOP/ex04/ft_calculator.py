class calculator:

	@staticmethod
	def dotproduct(V1: list[float], V2: list[float]) -> None:
		ret = 0
		for i in range(len(V1)):
			ret += V1[i] * V2[i]
		print("Dot product is :", ret)
		return
		return

	@staticmethod
	def add_vec(V1: list[float], V2: list[float]) -> None:
		ret = []
		for i in range(len(V1)):
			ret.append(float(V1[i] + V2[i]))
		print("Add Vector is :", ret)
		return

	@staticmethod
	def sous_vec(V1: list[float], V2: list[float]) -> None:
		ret = []
		for i in range(len(V1)):
			ret.append(float(V1[i] - V2[i]))
		print("Sous Vector is :", ret)
		return