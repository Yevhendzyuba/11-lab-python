from classes.cosmetology_build import CosmetologyBuild


class Mask(CosmetologyBuild):

    def __init__(self, appoinment_for, produce_country, capacity_in_ml, price_in_uah, amount_in_packet,
                 period_time_of_use=None):
        super().__init__(appoinment_for, produce_country, capacity_in_ml, price_in_uah, amount_in_packet)
        self.period_time_of_use = period_time_of_use

    def __del__(self):
        return

    def __str__(self):
        return super().__str__() + f"PeriodTimeOfUse:{self.period_time_of_use} "
