import random, time

class EmployeeProfile:
  def __init__(self):
    self.description = 'Typical employee usage'
  
  def linger(self):
    time.sleep(random.randrange(2, 10))
  
  def double_check(self):
    time.sleep(random.randrange(10, 30))
    