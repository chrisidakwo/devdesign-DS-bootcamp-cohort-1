import statistics as st
import pandas as pd
import numpy as np

# amount = [5, 7, 10, 13, 15]
# print('')
# print(st.stdev(amount))

array_data = np.random.randint(60, 100, size=(5, 4))
df2 = pd.DataFrame(array_data, 
                  columns=['Math', 'Science', 'English', 'History'],
                  index=['Student1', 'Student2', 'Student3', 'Student4', 'Student5'])

print('')
print("\nDataFrame from array:")
print(array_data)
print('\n')
print(df2)
print('\n')
print(pd.DataFrame(array_data))

# B1:C2

# student1 = [80, 50, 60]
# student2 = [90, 68, 49]
# student3 = [90, 86, 71]

# student_scores = [
#     [80, 50, 60],
#     [90, 68, 49],
#     [90, 86, 71],
# ]

# plt.figure(figsize=(10, 6))
