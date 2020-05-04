from classes import scrub
from classes import mask
from classes import powder
from classes import natural_components
from classes import cosmetology_build
from manager import cosmetology_manager


class CosmetologyManagerUtils:
    cosmetology_builds_list = [mask(1, "Ukraine", 123, 340, 423), scrub(3, "France", 345, 456, 123),
                               powder(2, "Spain", 56, 546, 243)]

    @staticmethod
    def sort_by_amount_in_packet(reverse=None):
        """
        >>> cosmetology_manager_utils.sort_by_amount_in_packet(reverse = True)
        AppoinmentFor:1 ProduceCountry:Ukraine CapacityInMl:123 PriceInUAH:340 AmountInPacket:423 PeriodTimeOfUse:23 ShadeOfShine:White NaturalComponents:NaturalComponents.COFFE

        >>> cosmetology_manager_utils.sort_by_amount_in_packet(reverse = False)
        AppoinmentFor:3 ProduceCountry:France CapacityInMl:345 PriceInUAH:456 AmountInPacket:123 PeriodTimeOfUse:34 ShadeOfShine:Black NaturalComponents:NaturalComponents.SUGAR

        """
        sorted_by_amount_in_packet = sorted(CosmetologyManagerUtils.cosmetology_builds_list,
                                            key=lambda cosmetology_build: cosmetology_build.amount_in_packet,
                                            reverse=reverse)
        return print("".join(str(a) for a in sorted_by_amount_in_packet))

    @staticmethod
    def sort_by_capacity_in_ml(reverse=None):
        """
        Sort by capacity in ml
        >>> cosmetology_manager_utils.sort_by_capacity_in_ml(reverse = True)
        AppoinmentFor:1 ProduceCountry:Ukraine CapacityInMl:123 PriceInUAH:340 AmountInPacket:423 PeriodTimeOfUse:23 ShadeOfShine:White NaturalComponents:NaturalComponents.COFFE

        >>> cosmetology_manager_utils.sort_by_capacity_in_ml(reverse = False)
        AppoinmentFor:3 ProduceCountry:France CapacityInMl:345 PriceInUAH:456 AmountInPacket:123 PeriodTimeOfUse:34 ShadeOfShine:Black NaturalComponents:NaturalComponents.SUGAR

        """

        sorted_by_capacity_in_ml = sorted(CosmetologyManagerUtils.cosmetology_builds_list,
                                          key=lambda cosmetology_build: cosmetology_build.capacity_in_ml,
                                          reverse=reverse)
        return print("".join(str(b) for b in sorted_by_capacity_in_ml))


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True, extraglobs={"cosmetology_manager_utils": CosmetologyManagerUtils()})
