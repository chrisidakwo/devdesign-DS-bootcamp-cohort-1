# You're developing a recommendation system for an online store.

# Tasks:

# 1. Create a function calculate_similarity that takes two product dictionaries and returns a similarity score based on their categories and price range.
# 2. Create a function recommend_products that takes a list of all products (inventory), a target product, and an optional parameter for the number of recommendations (default 3).
# 3. Use keyword arguments to allow filtering by price range, category, or rating

# {
#     id: '101',
#     name: 'Bikeshed',
#     category: 'Utility',
#     price: 200,
#     rating: 4.5,
# }

def calculateSimilarity(product, targetProduct):
    categoryScore = 0
    priceScore = 0

    if product['category'] == targetProduct['category']:
        categoryScore = 0.6

    priceDiff = abs(product['price'] - targetProduct['price'])
    maxPrice = max((product['price'], targetProduct['price']))

    if (maxPrice > 0):
        priceSimilarity = 1 - (priceDiff / maxPrice)
    else:
        priceSimilarity = 1

    priceScore = 0.4 * priceSimilarity

    return categoryScore + priceScore


# TODO: Add a note on lambda and this function
def getSimilarityScore(productSimilarityPair):
    return productSimilarityPair[1]

def recommendProducts(inventory, targetProduct, recommendations = 3, minPrice = None, maxPrice = None, category = None, minRating = None):
    # Filter products based on criteria
    filteredProducts = []

    for product in inventory:
        if product['id'] == targetProduct['id']:
            continue

        # Apply filters if specified
        if minPrice is not None and product["price"] < minPrice:
            continue
        if maxPrice is not None and product["price"] > maxPrice:
            continue
        if category is not None and product["category"] != category:
            continue
        if minRating is not None and product["rating"] < minRating:
            continue

        filteredProducts.append(product)
    
    similarProducts = []
    for product in filteredProducts:
        similarityScore = calculateSimilarity(product, targetProduct)
        similarProducts.append((product, similarityScore))

    # similarProducts.sort(key = lambda x:x[1], reverse = True)
    similarProducts.sort(key = getSimilarityScore, reverse = True)

    topRecommendations = []
    for product, _ in similarProducts[0:recommendations]:
        topRecommendations.append(product)

    topRecommendations = [product for (product, _) in similarProducts[0:recommendations]]

    return topRecommendations

inventory = [
    {"id": 101, "name": "Wireless Headphones", "category": "Electronics", "price": 89.99, "rating": 4.5},
    {"id": 102, "name": "Bluetooth Speaker", "category": "Electronics", "price": 59.99, "rating": 4.2},
    {"id": 103, "name": "Smartphone Case", "category": "Electronics", "price": 19.99, "rating": 4.0},
    {"id": 104, "name": "Premium Headphones", "category": "Electronics", "price": 199.99, "rating": 4.8},
    {"id": 105, "name": "USB-C Cable", "category": "Electronics", "price": 12.99, "rating": 3.9},
    {"id": 106, "name": "Running Shoes", "category": "Footwear", "price": 79.99, "rating": 4.7},
    {"id": 107, "name": "Fitness Tracker", "category": "Electronics", "price": 99.99, "rating": 4.3},
    {"id": 108, "name": "Wireless Earbuds", "category": "Electronics", "price": 79.99, "rating": 4.4},
]

similarProducts = recommendProducts(
    inventory,
    {"id": 105, "name": "USB-C Cable", "category": "Electronics", "price": 12.99, "rating": 3.9},
    maxPrice = 80,
    minRating = 4.0
)
print(similarProducts)





# Explaining Product Similarity Scores
# "When we're shopping online, we often see recommendations for products similar to what we're looking at.
# 
# Let me explain how our function determines which products are 'similar':
# The Similarity Score: A 0-to-1 Scale
# Meaning that the calculateSimilarity function gives each potential match a score between 0 and 1:

# 0 means completely different products
# 1 means extremely similar products

# Two Main Factors
# We look at two main things when comparing products:
# 1. Category Match (60% of the score)
# Products in the same category are more likely to be alternatives for each other (hence it carries 60% of the similarity score):

# If two products are in the same category (like both are "Electronics"), they get 0.6 points
# If they're in different categories, they get 0 points for this part

# 2. Price Similarity (40% of the score)
# Products with similar prices are likely to be competing alternatives:

# If two products have exactly the same price, they get the full 0.4 points
# If their prices are very different, they get fewer points
# We calculate this on a sliding scale based on how big the price difference is

# Example
# Let's compare our target "Wireless Headphones" ($89.99) with two other products:
# Product A: Bluetooth Speaker ($59.99)

# Category: Both are "Electronics" → 0.6 points
# Price: They differ by $30 on a $90 item

# Price difference: $30
# Max price: $89.99
# Price similarity: 1 - (30/89.99) = 0.67
# Points: 0.4 × 0.67 = 0.27


# Total similarity score: 0.6 + 0.27 = 0.87

# Product B: Running Shoes ($79.99)

# Category: Different categories → 0 points
# Price: They differ by $10 on a $90 item

# Price similarity: 1 - (10/89.99) = 0.89
# Points: 0.4 × 0.89 = 0.36


# Total similarity score: 0 + 0.36 = 0.36

# So the Bluetooth Speaker (0.87) would be considered more similar to our Wireless Headphones than the Running Shoes (0.36), even though the shoes are closer in price, because the category match is weighted more heavily."
