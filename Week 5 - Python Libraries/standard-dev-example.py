import statistics as st

# Calculating standard deviation WITHOUT libraries
numbers = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]

mean = sum(numbers) / len(numbers)
squared_diff_sum = sum((x - mean) ** 2 for x in numbers)
std_dev = (squared_diff_sum / len(numbers)) ** 0.5

print(f"\nStandard deviation (manually): {std_dev}")

print(f"\nStandard deviation (using the statistics library): {st.stdev(numbers)}")