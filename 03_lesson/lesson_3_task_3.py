from adress import Address
from mailing import Mailing

adress = Address("236038", "Калининград", "Юрия Гагарина", "3", "45")
from_address1 = Address("234856", "Москва", "Дзержинского", "23", "56")
from_address2 = Address("213456", "Зеленоград", "Погодина", "46", "789")
from_address3 = Address("345678", "Волгоград", "Непройдёнова", "123", "345")

cost1 = 1000
cost2 = 900
cost3 = 9000

track1 = "234Tr56"
track2 = "678yu5645y"
track3 = "ghj456vv43"

mailing = Mailing(adress,  [from_address1, from_address2, from_address3], [cost1, cost2, cost3], [track1, track2, track3])

print(mailing)