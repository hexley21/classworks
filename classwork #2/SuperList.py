import random


class SuperList(list):    
    def min(self):
        return min(self)
    def max(self):
        return max(self)

super_list = SuperList()
super_list.extend([1, 2, 3, 4, 5, 6, 7])

wow_list = SuperList()
wow_list.extend([-7, -6, -5, -4, -3, -2, -1, 0])


cool_list = SuperList()
cool_list.extend([-23, 29, 46, -87, 65])

def test_class(super_list: SuperList):
    print(super_list.min())
    print(super_list.max(), "\n")


test_class(super_list)
test_class(wow_list)
test_class(cool_list)

