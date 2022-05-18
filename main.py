from advertisment import HouseSell, ApartmentSell, ApartmentRent, HouseRent, StoreSell, StoreRent
from region import Region
from samples import create_samples
from user import User
ali=User(fname='ali',lname='alavi',tel='')
reg1 = Region(name='Tehran_Abasabd')
class Handler():
    advertisment_types={
       1: ApartmentSell, 2: ApartmentRent,
       3: HouseSell, 4: HouseRent,
       5: StoreSell, 6: StoreRent
    }
    SWITCHES={
      'r':'get_report',
      's':'show_all'
    }

    def get_report(self):
        for adv in self.advertisment_types.values():
              print(adv.file_name,adv.manager.count())
    def show_all(self):
        for adv in self.advertisment_types.values():
              for obj in adv.object_list:
                  print(obj.show_detail())
                  print('.' * 20)
    def run(self):
        for key in self.SWITCHES.keys():
            print(f'press {key} for {self.SWITCHES[key]}')
        user_input=input('Enter your Choice : ')
        switch = self.SWITCHES.get(user_input, None)
        if switch is None:
          print('*' * 20)
          print('Oops!! invalid input')
          self.run()
        choice=getattr(self,switch,None)
        choice()
        self.run()




if __name__ == '__main__':
  create_samples()
  handle = Handler().run()


