from adress import Address
from mailing import Mailing

to_address0 = Address( "345678","Москва", "Чернышевского", "13", "2")
to_address1 = Address( "567345","Астрахань", "Черняховского", "4", "45")
to_address2 = Address( "123456","Волгоград", "Пролетарская", "4", "123")
to_address3 = Address( "678905","Калининград", "Мира", "3", "1")

from_address0 = Address("234567", "Калининград", "Юрия Гагарина", "3", "45")
from_address1 = Address("234856", "Москва", "Дзержинского", "23", "56")
from_address2 = Address("213456", "Зеленоград", "Погодина", "46", "789")
from_address3 = Address("345678", "Волгоград", "Непройдёнова", "123", "345")

cost0 = 1250
cost1 = 1000
cost2 = 900
cost3 = 9000

track0 = "456rty45gh"
track1 = "234Tr56"
track2 = "678yu5645y"
track3 = "ghj456vv43"

mailing = Mailing([to_address0, to_address1, to_address2, to_address3], [from_address0, from_address1, from_address2, from_address3], [cost0, cost1, cost2, cost3], [track0, track1, track2, track3])

print(mailing)