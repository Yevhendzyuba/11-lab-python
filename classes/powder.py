from classes.cosmetology_build import CosmetologyBuild


class Powder(CosmetologyBuild):

    def __init__(self, appoinment_for, produce_country, capacity_in_ml, price_in_uah, amount_in_packet,
                 shade_of_shine=None):
        super().__init__(appoinment_for, produce_country, capacity_in_ml, price_in_uah, amount_in_packet)
        self.shade_of_shine = shade_of_shine

    def __del__(self):
        return

    def __str__(self):
        return super().__str__() + f"ShadeOfShine: {self.shade_of_shine}"
