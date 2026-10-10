#Write a Python program to create a product dictionary and update its price using update().

product = {
            "product name" : "pintola oats",
            "price" : 500,
            "weight" : "1kg",
          }

product.update({"price" : 600})
print(product)