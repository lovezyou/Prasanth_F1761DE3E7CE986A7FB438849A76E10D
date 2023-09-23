
# this function for perform linear search to find target product
def linearSearchProduct(productList, targetProduct):#product list and target products are given as parameters 
	indices = []                                    #this list is to store the index values of the target product are found in this function 

	for index, product in enumerate(productList):   #here the list of products are enumerated
		if product == targetProduct:                #the target is found using if statement
			indices.append(index)                   #lastly the found index are added to the list "indices[]"

	return indices                                  #finally the list of index are returned 



# Example usage:
products = ["jean", "shorts", "T-shirt", "T-shirt", "jean", "jean", "shirt", "pant" ,"jean"]
target =  "jean"
target1 = "kitkat"
result = linearSearchProduct(products, target)
print(result)
