import random, time

class CustomerProfile:
  def __init__(self):
    self.description = 'Typical customer usage'
  
  def linger(self):
    time.sleep(random.randrange(2, 10))

  def get_distracted(self):
    time.sleep(random.randrange(30, 60))
  
  def go_to_bathroom(self):
    time.sleep(random.randrange(60, 120))
  
  def go_to_lunch(self):
    time.sleep(random.randrange(120, 240))
