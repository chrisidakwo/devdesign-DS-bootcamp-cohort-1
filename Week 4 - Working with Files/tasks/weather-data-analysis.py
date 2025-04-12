# You've been hired by a local meteorological office to analyze temperature data from the past month.

# Tasks:

# 1. Create a function called temperatureStats that accepts a list of daily temperatures and returns the minimum, maximum, and average temperatures.
# 2. Add a default parameter that lets the user choose between Celsius and Fahrenheit outputs.
# 3. Create a function called temperatureSummary that uses your first function and returns a formatted string summary of the results.

def temperatureStats(dailyTemps, tempUnit = 'c'):
    minTemp = min(dailyTemps)
    maxTemp = max(dailyTemps)
    averageTemp = sum(dailyTemps) / len(dailyTemps)

    if (tempUnit == 'f'):
        # TODO: Confirm the calculation here. 1 celsius = 33.8F
        minTemp = (minTemp * 9/5) + 32
        maxTemp = (maxTemp * 9/5) + 32
        averageTemp = (averageTemp * 9/5) + 32

    return minTemp, maxTemp, averageTemp


def temperatureSummary(temps):
    tempUnit = input('\nEnter your preferred temperature unit (c for Celsius, f for Farenheit): ').lower()

    minTemp, maxTemp, averageTemp = temperatureStats(temps, tempUnit)

    symbol = '°C' if tempUnit == 'c' else '°F'

    summary = '\n******** TEMP SUMMARY********\n'
    summary += f'- Minimum Temperature: {minTemp:.1f}{symbol}\n'
    summary += f'- Maximum Temperature: {maxTemp:.1f}{symbol}\n'
    summary += f'- Average Temperature: {averageTemp:.1f}{symbol}\n'

    return summary

# TODO: Explain at modules
if __name__ == '__main__':
    # temps = [32, 34, 35, 42, 79, 52, 57, 68, 81]
    temps = [18, 29, 34, 17, 23, 35, 12, 19, 22, 27, 28, 21]

    summary = temperatureSummary(temps)

    print(summary)
