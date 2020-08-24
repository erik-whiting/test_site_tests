import random, time

class EmployeeProfile:
  # For testing purposes, I am making the wait times much shorter than
  # they probably would be in a real life situation.
  def __init__(self):
    self.description = 'Typical employee usage'
  
  def linger(self):
    time.sleep(random.randrange(1, 5))
  
  def double_check(self):
    time.sleep(random.randrange(2, 8))
    