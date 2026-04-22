from address import Address
from mailing import Mailing

to_addr = Address("644000", "Омск", "Ленина", "10", "5")
from_addr = Address("101000", "Москва", "Тверская", "22", "101")

shipment = Mailing(to_addr, from_addr, 450, "TRK998877")

print(f"Отправление {shipment.track} из {shipment.from_address.index}, "
      f"{shipment.from_address.city}, {shipment.from_address.street}, "
      f"{shipment.from_address.house} - {shipment.from_address.apartment} "
      f"в {shipment.to_address.index}, {shipment.to_address.city}, "
      f"{shipment.to_address.street}, {shipment.to_address.house} - "
      f"{shipment.to_address.apartment}. Стоимость {shipment.cost} рублей.")
