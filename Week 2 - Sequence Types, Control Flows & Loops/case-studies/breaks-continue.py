# break - exits the loop entirely

print('')
# range(1, 11) would generate this: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(1, 11):
    if i % 2 == 0:
        print(f"Found the first even number: {i}")
        break
    else:
        print(i)

print('End of loop')

print('')

# continue - skips over the current iteration
for i in range(1, 11):
    if i % 2 == 0:  # Check for an even number
        continue
        print(f"Found the first even number: {i}")
    else:
        print(i)

print('')