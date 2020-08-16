import random
from LuluTest import *

from vars import Vars
from customer_profile import CustomerProfile

customer = CustomerProfile()

vars = Vars()
page = vars.new_page()
actions = vars.new_actions(False) # Make headless later

actions.go(page)
customer.linger()
actions.click(
  PageElement(('id', 'bands'), 'bands')
)
customer.linger()

band_id = random.randrange(30)
actions.click(
  PageElement(('id', f'band-{band_id}'), 'random band')
)
customer.get_distracted()

actions.click(
  PageElement(('link text', 'Bands'), 'back')
)
customer.linger()
actions.close()
