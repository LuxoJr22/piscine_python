import pandas as pd

def load(path: str) -> pd.core.frame.DataFrame:
	"""Load a csv file"""
	try:
		df = pd.read_csv(path)
		return df
	except FileNotFoundError:
		print("The file doesn't exist")
	except PermissionError:
		print("Permission needed to open this file")
	except ValueError:
		print("Can't open this file")