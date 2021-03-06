from abc import ABC


class CosmetologyBuild(ABC):

    def __init__(self, appoinment_for=None, produce_country=None, capacity_in_ml=None, price_in_uah=None,
                 amount_in_packet=None):
        self.appoinment_for = appoinment_for
        self.produce_country = produce_country
        self.capacity_in_ml = capacity_in_ml
        self.price_in_uah = price_in_uah
        self.amount_in_packet = amount_in_packet

    def __del__(self):
        return

    def __str__(self):
        return f"AppoinmentFor:{self.appoinment_for} ProduceCountry:{self.produce_country} " \
               f"CapacityInMl:{self.capacity_in_ml} PriceInUAH:{self.price_in_uah}" \
               f" AmountInPacket:{self.amount_in_packet}"
