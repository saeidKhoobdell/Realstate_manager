from deal import Sell, Rent
from estate import House, Apartment, Store
from base import BaseClass


class ApartmentSell(BaseClass,Apartment,Sell):
    file_name = 'Apartment for Sale'

    def show_detail(self):
        self.show_description()
        self.show_price()

    def __str__(self):
        return f"apartment : {self.user.fullname}\t id : {self.id}"


class HouseSell(BaseClass, House, Sell):
    file_name = 'House for Sale'

    def show_detail(self):
        self.show_description()
        self.show_price()


class ApartmentRent(BaseClass, Apartment, Rent):
    file_name = 'Appartment for Rent'

    def show_detail(self):
        self.show_description()
        self.show_price()


class HouseRent(BaseClass, House, Rent):
    file_name = 'House for Rent'

    def show_detail(self):
        self.show_description()
        self.show_price()


class StoreSell(BaseClass, Store, Sell):
    file_name = 'Store for Sale'

    def show_detail(self):
        self.show_description()
        self.show_price()


class StoreRent(BaseClass, Store, Rent):
    file_name = 'Store for Rent'

    def show_detail(self):
        self.show_description()
        self.show_price()
