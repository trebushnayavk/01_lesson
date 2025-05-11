from address import Address
from mailing import Mailing

to_address = Address( "785678","Санкт-Петербург", "Пограничника", "90", "65")
from_address = Address("894565", "Москва", "Самойлова", "76", "123")

mailing = Mailing(
    to_address = to_address,
    from_address = from_address,
    cost = 1340,
    track = "ghj345dl2"
)

print(mailing)