from matplotlib import pyplot as plt
from load_csv import load

def main():
	"""Program that loads the file life_expectancy_years.csv, and displays the country information"""
	data = load("life_expectancy_years.csv")

	ypoints = data["France"].values
	xpoints = data.index.values
	xpoints = [int(x) for x in xpoints]
	plt.plot(xpoints, ypoints)
  
	plt.title("France Life expectancy Projections")
	plt.ylabel("Life expectancy")
	plt.xlabel("Year")
	
	plt.show()
	return


if __name__ == "__main__":
    main()