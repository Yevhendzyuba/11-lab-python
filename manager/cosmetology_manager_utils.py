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
    def sort_by_amount_in_packet(reverse = None):
        """
        >>> sport_build_manager_object_utils.sort_by_amount_in_packet(reverse = True)
        
        :param reverse:
        :return:
        """