from matplotlib import pyplot as plt
from load_csv import load

def value_to_float(x):
    """Convert value to int"""
    if type(x) == float or type(x) == int:
        return x
    if 'K' in x:
        if len(x) > 1:
            return float(x.replace('k', '')) * 1000
        return 1000.0
    if 'M' in x:
        if len(x) > 1:
            return float(x.replace('M', '')) * 1000000

def main():
	"""Program that loads the file population_total.csv, and displays the country information versus another country"""
	data = load("population_total.csv").iloc[:251]

	xpoints = data.index.values
	xpoints = [int(x) for x in xpoints]

	ypoints = data["France"].values
	ypoints = [value_to_float(x) / 1000000 for x in ypoints]
	plt.plot(xpoints, ypoints)
      
	ypoints2 = data["Belgium"].values
	ypoints2 = [value_to_float(x) / 1000000 for x in ypoints2]
	plt.plot(xpoints, ypoints2)

	plt.title("Population Projections")
	plt.ylabel("Population in Millions")
	plt.xlabel("Year")
	
	plt.legend(["France", "Belgium"], loc='lower right')
	plt.show()
	return


if __name__ == "__main__":
    main()