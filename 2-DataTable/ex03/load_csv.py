import pandas as pd

def load(path: str) -> pd.core.frame.DataFrame:
	"""Load a csv file"""
	try:
		df = pd.read_csv(path)
		df = df.transpose()
		df.columns = df.iloc[0]
		return df[1:]
	except FileNotFoundError:
		print("The file doesn't exist")
	except PermissionError:
		print("Permission needed to open this file")
	except ValueError:
		print("Can't open this file")