from abc import ABC,abstractmethod


class EstateAbstract(ABC):

    def __init__(self, user, area, room, built_year, region, address, *args, **kwargs):
        self.user = user
        self.area = area
        self.room = room
        self.built_year = built_year
        self.region = region
        self.address = address
        super().__init__(*args, **kwargs)

    def show_description(self):
        pass


class Apartment(EstateAbstract):

      def __init__(self, has_elevator,has_parking, floor, *args, **kwargs):
          self.has_elevator = has_elevator
          self.has_parking = has_parking
          self.floor = floor
          super().__init__(*args, **kwargs)

      def show_description(self):
          print(f"Apartment {self.id} \t area : {self.area}")


class House(EstateAbstract):
    def __init__(self, has_yard, floors_count, floor, *args, **kwargs):
      self.has_yard = has_yard
      self.floors_count = floors_count
      self.floor = floor
      super().__init__(*args, **kwargs)

    def show_description(self):
      print(f"Apartment {self.id} \t user : {self.user}")

  # def show_description(self):
  #   print(f"House: {self.id}")


class Store(EstateAbstract):
  def show_description(self):
    print(f"Store: {self.id}")