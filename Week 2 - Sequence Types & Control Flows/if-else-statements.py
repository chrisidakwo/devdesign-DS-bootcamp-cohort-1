action = ""
light = "yellow"

if light == "green" or light == "blinking":
    # If branch
    action = "Go"
elif light == "yellow":
    action = "Slow down"
else:
    # else branch
    action = "Stop"

print(action)

print("\n")

# Print weather anomalities from sensor data
temperature = 35
humidity = 15

if temperature > 30 or humidity < 20:
    print("Warning: Unusual weather conditions detected")
else:
    print("Weather conditions are normal")

print("I'm outside the if/else block!")

# Multi-branching (Student grade)
# Advanced and/or mixture
# Ternary operators
# Loops - for, while
