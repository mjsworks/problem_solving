in the 1_petprofile.py
we have implemented __str__ and __repr__. 
__str__ generated human readable string to print when __repr__ is for debugging purpose.
in both these functions, we return what we want to print. we dont explicitly use print() here. The user used print() in there. So, when we write print(myObj). internally what python does is print(myObj.__str__())