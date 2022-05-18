from user import User
from region import Region
from advertisment import ApartmentRent,ApartmentSell,HouseRent,HouseSell,StoreSell,StoreRent
from random import choice
FIRST_NAME = ['saeid', 'saeid_1', 'saeid_2']
LAST_NAME = ['khoobdell', 'khoobdell_1', 'khoobdell_2']
MOBILES = ['09358985481', '09358985481_1', '09358985481_2', '09358985481_3', '09358985481_4']


def create_samples():
    for mobile in MOBILES:
        User(choice(FIRST_NAME), choice(LAST_NAME), mobile)

    reg1 = Region(name='Tehran_Abasabd')
    reg2 = Region(name='Tehran_Nezamabad')

    # Create advertisment

    apartment_sale = ApartmentSell(has_elevator=True, has_parking=True, floor=3, user=User.object_list[0]
        , area=120, room=2, region=reg1, address='', built_year=9, price_per_meter=10, discountable=True)

    apartment_rent = ApartmentRent(has_elevator=True, has_parking=True, floor=3, user=User.object_list[1]
        , area=400, room=2, region=reg1, address='', built_year=9 ,initial_price=200,monthly_price=10)

    house_sale = HouseSell(has_yard=True, floors_count=3, floor=3, user=User.object_list[2]
        , area=200, room=2, region=reg1, address='', built_year=9, price_per_meter=10, discountable=True)

    house_rent = HouseRent(has_yard=True, floors_count=3, floor=3, user=User.object_list[3]
        , area=500, room=2, region=reg1, address='', built_year=9, initial_price=200, monthly_price=10)

    store_sale = StoreSell(user=User.object_list[4],region=reg1, area=200, room=10,
        built_year =1990, address='', price_per_meter=10)
    store_rent = StoreRent(user=User.object_list[4], region=reg1, area=200,
            room=10, built_year=1990, address='',initial_price=200,monthly_price=10)
    print("#" * 20, "\t samples created \t", "#" * 20)
