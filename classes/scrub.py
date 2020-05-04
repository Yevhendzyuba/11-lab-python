from classes.cosmetology_build import CosmetologyBuild
from classes.natural_components import NaturalComponents


class Scrub(CosmetologyBuild):

    def __init__(self, appoinment_for, produce_country, capacity_in_ml, price_in_uah, amount_in_packet,
                 natural_components=None):
        super().__init__(appoinment_for, produce_country, capacity_in_ml, price_in_uah, amount_in_packet)
        self.natural_components = natural_components

    def __del__(self):
        return

    def __str__(self):
        return super().__str__() + f"NaturalComponents:{self.natural_components}"
