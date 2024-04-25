

class FlatMate:
    """
    Creates a flat mate and pays a share of the bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, days_in_house2):
        weight = self.days_in_house / (self.days_in_house + days_in_house2)
        return bill.amount * weight
