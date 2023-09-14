#have to use import

import utility
import shopping.shopping_cart #we created a package and a package is just a folder containing modules. So to import a module from a package, we have to import the package and the module(import as above)


#print(utility)
#what happened if I run it, it created a _pycache_ folder, this _pycache_ is created every time we run a file with 'import' using module, _pycache_ is a compliled version of utility.py.
#so next I will run this utility from main, it will run from this _pycache_ since nothing has been modified in the utility.py.

#so I can use it in main as much I want it
#print(utility.multiply(2,3))

#print(shopping.shopping_cart)
#output give access to the package



#lets see if we can use the buy function
print(shopping.shopping_cart.buy('apple'))
#output ['apple]
