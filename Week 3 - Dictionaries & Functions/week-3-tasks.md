# 1. Pet Shop Inventory

You run a pet shop and the dictionary below represents your inventory:

```python
petShop = {
    "animals": {
        "dogs": {"Labrador": 3, "Beagle": 2, "Poodle": 1, "Mastiff": 5},
        "cats": {"Persian": 2, "Siamese": 1, "Maine Coon": 2},
        "fish": {"Goldfish": 12, "Angelfish": 5, "Betta": 3}
    },
    "supplies": {
        "food": {"Dog Food": 20, "Cat Food": 9, "Fish Food": 25},
        "toys": {"Dog Toys": 30, "Cat Toys": 20},
        "habitats": {"Aquariums": 5, "Cat Trees": 8, "Dog Beds": 7}
    },
}
```

## Task 1

Your task is to dynamically update the quantity of a supply item after a sale.

Request as much information from the user in order to know what product is to be sold.

Print out your inventory after each sale.

## Task 2

Create a shopping list of supplies that are low in stock (fewer than 10)

## Task 3

Find which animal type has the most variety. Variety in this case means the animal with the most headcount and number of breeds.

---

# 2. Working with COVID-19 Data

Using the provided COVID-19 sample data, attempt the following tasks:

-  Find the country with the highest number of active cases
- Calculate the ratio of active cases to population for each country
- Find the country with the highest recovery rate (recoveries/total_cases)
- Calculate active cases as a percentage of population for each country
- Generate a new dictionary showing which countries have more than 20,000 active cases
- Calculate the total number of active cases across all countries
- Add a new key called "cases_per_million" to each country based on total_cases
- Using user input, update the active cases for a specific country and recalculate the global total
- Calculate what percentage of global active cases each country represents. Represent the result as a dictionary.