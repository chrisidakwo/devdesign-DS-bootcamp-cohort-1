# Using the provided COVID-19 sample data (case-studies/covid19-dataset.json), attempt the following tasks:
covidData = {
    "countries": {
        "Nigeria": {
            "population": 5_000_000,
            "total_cases": 250000,
            "active_cases": 16_500,
            "deaths": 3500,
            "recoveries": 230000,
            "testing": 1200000,
            "vaccination": {
                "first_dose": 3500000,
                "fully_vaccinated": 3200000,
                "boosters": 1800000
            },
            "monthly_cases": {
                "Jan": 45000,
                "Feb": 32000,
                "Mar": 25000,
                "Apr": 18000,
                "May": 15000,
                "Jun": 10000
            }
        },
        "Ghana": {
            "population": 8_000_000,
            "total_cases": 420000,
            "active_cases": 23_800,
            "deaths": 6200,
            "recoveries": 390000,
            "testing": 1900000,
            "vaccination": {
                "first_dose": 5100000,
                "fully_vaccinated": 4800000,
                "boosters": 2500000
            },
            "monthly_cases": {
                "Jan": 80000,
                "Feb": 65000,
                "Mar": 40000,
                "Apr": 25000,
                "May": 12000,
                "Jun": 8000
            }
        },
        "England": {
            "population": 3_000_000,
            "total_cases": 180000,
            "active_cases": 5_900,
            "deaths": 2100,
            "recoveries": 172000,
            "testing": 950000,
            "vaccination": {
                "first_dose": 2100000,
                "fully_vaccinated": 1950000,
                "boosters": 900000
            },
            "monthly_cases": {
                "Jan": 35000,
                "Feb": 30000,
                "Mar": 20000,
                "Apr": 12000,
                "May": 8000,
                "Jun": 5000
            }
        },
        "Kenya": {
            "population": 6_500_000,
            "total_cases": 350000,
            "active_cases": 15_200,
            "deaths": 4800,
            "recoveries": 330000,
            "testing": 1600000,
            "vaccination": {
                "first_dose": 3900000,
                "fully_vaccinated": 3500000,
                "boosters": 1600000
            },
            "monthly_cases": {
                "Jan": 70000,
                "Feb": 50000,
                "Mar": 35000,
                "Apr": 20000,
                "May": 10000,
                "Jun": 5000
            }
        }
    },
    "global": {
        "total_cases": 1200000,
        "active_cases": 61400,
        "total_deaths": 16600,
        "total_recoveries": 1122000,
        "total_vaccines_distributed": 25000000
    },
    "variants": {
        "Alpha": {"first_detected": "Sep 2020", "transmissibility": "Medium"},
        "Beta": {"first_detected": "Oct 2020", "transmissibility": "Medium"},
        "Delta": {"first_detected": "Dec 2020", "transmissibility": "High"},
        "Omicron": {"first_detected": "Nov 2021", "transmissibility": "Very High"}
    }
}

print('')

# 1. Find the country with the highest number of active cases

hightestCase = 0
countryName = None

for country, data in covidData['countries'].items():
    if data['active_cases'] > hightestCase:
        hightestCase = data['active_cases']
        countryName = country

print(f'The country with the highest active COVID19 cases is {countryName} with {hightestCase:,}')


# 2. Calculate the ratio of active cases to population for each country

print('')

ratio = {}

for country, data in covidData['countries'].items():
    activeCases = data['total_cases']
    population = data['population']

    countryRatio = (activeCases / population) * 100

    ratio[country] = round(countryRatio, 3)

print('************ RATIO OF ACTIVE CASES TO POPLUATION FOR EACH COUNTRY ************')
print(ratio)

print('')

# Task 3: Find the country with the highest recovery rate (recoveries/total_cases)

highestRate = 0
countryWithHighestRate = ""

# Loop through each country
for country, data in covid_data["countries"].items():
    # Calculate recovery rate
    recoveryRate = data["recoveries"] / data["total_cases"]
    
    # Check if this rate is higher than our current highest
    if recoveryRate > highestRate:
        highestRate = recoveryRate
        countryWithHighestRate = country

# Convert rate to percentage for display
percentage = highestRate * 100

print(f"Country with highest recovery rate: {countryWithHighestRate} with {percentage:.2f}%")
print('')

# Task 4: Calculate active cases as a percentage of population for each country
activeCasesPercentage = {}

# Loop through each country
for country, data in covid_data["countries"].items():
    # Calculate percentage
    percentage = (data["active_cases"] / data["population"]) * 100

    # Store the result in our dictionary, rounded to 2 decimal places
    activeCasesPercentage[country] = round(percentage, 2)

print('Active cases as a percentage of population for each country:', activeCasesPercentage)
print('')

# Task 5: Generate a new dictionary showing which countries have more than 20,000 active cases
highCaseCountries = {}
    
# Loop through each country
for country, data in covid_data["countries"].items():
    # Check if active cases exceed 20,000
    if data["active_cases"] > 20000:
        # Add this country and its active cases to our result dictionary
        highCaseCountries[country] = data["active_cases"]

print('Countries with more than 20,000 active cases:', highCaseCountries)
print('')

# Task 6: Calculate the total number of active cases across all countries

# Initialize a counter
totalActiveCases = 0

# Loop through each country and add its active cases to our total
for country, data in covid_data["countries"].items():
    totalActiveCases += data["active_cases"]

print(f'Total active cases across all countries: {total_active}')
print('')

# Task 7: Add a new key called "cases_per_million" to each country based on total_cases

# Make a copy of the original data to avoid modifying it directly
updatedData = covidData.copy()

# Loop through each country
for country, data in updatedData["countries"].items():
    # Calculate cases per million
    casesPerMillion = (data["total_cases"] / data["population"]) * 1000000
    # Add the new key to the country's data
    updatedData["countries"][country]["cases_per_million"] = round(casesPerMillion, 2)

print('Updated data with cases_per_million:', updatedData)
print('')

# Task 8: Using user input, update the active cases for a specific country and recalculate the global total

# Make a copy of the original data
updatedData = covid_data.copy()

# Get user input for country and new active case count
country = input("Enter country name (Nigeria, Ghana, England, or Kenya): ")
newActiveCases = int(input(f"Enter new active cases for {country}: "))

# Check if the country exists in our data
if country in updatedData["countries"]:
    # Get the old active cases value
    oldActiveCases = updatedData["countries"][country]["active_cases"]
    
    # Update the country's active cases
    updatedData["countries"][country]["active_cases"] = newActiveCases
    
    # Update the global active cases
    # First, subtract the old value and add the new value
    updatedData["global"]["active_cases"] = updatedData["global"]["active_cases"] - oldActiveCases + newActiveCases
    
    print(f"Updated {country}'s active cases from {oldActiveCases} to {newActiveCases}")
    print(f"New global active cases total: {updatedData['global']['active_cases']}")
else:
    print(f"Country '{country}' not found in the data.")

print('')

# Task 9: Calculate what percentage of global active cases each country represents

# Create an empty dictionary to store results
percentages = {}

# Calculate total active cases from all countries
totalActiveCases = 0
for country, data in covid_data["countries"].items():
    totalActiveCases += data["active_cases"]

# Calculate percentage for each country
for country, data in covid_data["countries"].items():
    percentage = (data["active_cases"] / totalActiveCases) * 100
    percentages[country] = round(percentage, 2)

print('Percentage of global active cases for each country:', percentages)
print('')
