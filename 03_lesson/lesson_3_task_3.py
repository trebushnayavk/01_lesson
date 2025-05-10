from address import Address
from mailing import Mailing

address = Address("236038", "Калининград", "Юрия Гагарина", "3", "45")
from_address1 = Address("234856", "Москва", "Дзержинского", "23", "56")
from_address2 = Address("213456", "Зеленоград", "Погодина", "46", "789")
from_address3 = Address("345678", "Волгоград", "Непройдёнова", "123", "345")

cost1 = 1000
cost2 = 900
cost3 = 9000

track1 = "234Tr56"
track2 = "678yu5645y"
track3 = "ghj456vv43"

mailing = Mailing(address,  [from_address1, cost1, track1], [from_address2, cost2, track2], [from_address3, cost2, track3])

print(mailing)