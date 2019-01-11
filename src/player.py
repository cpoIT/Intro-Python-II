# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
  def __init__(self, name, curr_room, inventory=[]):
    self.name = name
    self.curr_room = curr_room
    self.inventory = inventory

  def __repr__(self):
    return "\n{}, are you lost? {}.\nInside your pockets there {} {} a crumb from the blueberry muffin you had this morning\n".format(
      self.name, 
      self.curr_room, 
      'are' if len(self.inventory) > 1 else 'is', 
      'nothing but' if not self.inventory else f'{self.inventory} and')

  def get_name(self):
    return self.name

  def get_room(self):
    return self.curr_room

  def get_inv(self):
    return self.inventory

  def add_item(self, added):
    self.added = added
    self.inventory.extend(added)
    return self.inventory

  def drop_item(self, dropped):
    self.dropped = dropped
    self.inventory.remove(dropped)
    return self.inventory

  def set_room(self, new_room):
    self.new_room = new_room
    self.curr_room = new_room
    return self.curr_room

  def return_outside(self):
    self.curr_room = 'outside'
    return  self.curr_room

