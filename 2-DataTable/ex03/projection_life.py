from matplotlib import pyplot as plt
from load_csv import load


def main():
	"""Program that loads the file population_total.csv, and displays the country information versus another country"""
	expectancy = load("life_expectancy_years.csv")
	data = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")

	product  = data.iloc[100]
	expectancy = expectancy.iloc[100]

	plt.scatter(product, expectancy)
	plt.title("1900")
	plt.ylabel("Life Expectancy")
	plt.xlabel("Gross domestic product")
	plt.xscale("log")
	plt.show()
	return


if __name__ == "__main__":
    main()