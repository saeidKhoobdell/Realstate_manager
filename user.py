from base import BaseClass


class User(BaseClass):

  def __init__(self,fname,lname,tel,*args,**kwargs):
    self.first_name = fname
    self.last_name = lname
    self.telephone = tel
    super().__init__(*args,**kwargs)

  def __str__(self):
    return f' {self.first_name} {self.last_name}'

  @property
  def fullname(self):
    return f' {self.first_name} {self.last_name}'