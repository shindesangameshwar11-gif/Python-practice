#wap to create a dict containing the details of products. 
# use update to modifty the price and add a new key called "quantiy"

a={
    "product Name " :"Mango",
    "price" : 500,

}

a.update(
    {
        "price" : 600,
        "Quantity" : "5KG"
    }
)

print(a)