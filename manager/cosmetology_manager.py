from classes import mask
from classes import scrub
from classes import powder
from classes import natural_components


class CosmetologyBuildManager:
    def __init__(self, cosmetology_builds_list=None):
        if cosmetology_builds_list is None:
            self.cosmetology_builds_list = []
        else:
            self.cosmetology_builds_list = cosmetology_builds_list

    def find_by_produce_country(self, produce_country):
        """
        find by produce country
        >>> cosmetology_manager.find_by_produce_country("Ukraine")
        AppoinmentFor:1 ProduceCountry:Ukraine CapacityInMl:123 PriceInUAH:340 AmountInPacket:423

        >>> cosmetology_manager.find_by_produce_country("France")
        AppoinmentFor:3 ProduceCountry:France CapacityInMl:345 PriceInUAH:456 AmountInPacket:123

        >>> cosmetology_manager.find_by_produce_country("Spain")
        AppoinmentFor:2 ProduceCountry:Spain CapacityInMl:56 PriceInUAH:546 AmountInPacket:243

        """
        found_items_by_produce_country = list(
            filter(lambda cosmetology_build: cosmetology_build.produce_country == produce_country,
                   self.cosmetology_builds_list))
        return print("".join(str(c) for c in found_items_by_produce_country))

    def find_by_price_in_uah(self, price_in_uah):
        """
        find by price in uah
        >>> cosmetology_manager.find_by_price_in_uah(456)
        AppoinmentFor:3 ProduceCountry:France CapacityInMl:345 PriceInUAH:456 AmountInPacket:123

        >>> cosmetology_manager.find_by_price_in_uah(340)
        AppoinmentFor:1 ProduceCountry:Ukraine CapacityInMl:123 PriceInUAH:340 AmountInPacket:423

        >>> cosmetology_manager.find_by_price_in_uah(546)
        AppoinmentFor:2 ProduceCountry:Spain CapacityInMl:56 PriceInUAH:546 AmountInPacket:243

        """
        found_items_by_price_in_uah = list(
            filter(lambda cosmetology_build: cosmetology_build.price_in_uah == price_in_uah,
                   self.cosmetology_builds_list))
        return print("".join(str(d) for d in found_items_by_price_in_uah))


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE, verbose=True,
                    extraglobs={'cosmetology_manager': CosmetologyBuildManager(
                        cosmetology_builds_list=[mask(1, "Ukraine", 123, 340, 423),
                                                 scrub(3, "France", 345, 456, 123),
                                                 powder(2, "Spain", 56, 546, 243)])})
