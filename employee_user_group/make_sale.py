import random
from LuluTest import *

from vars import Vars
from employee_profile import EmployeeProfile

employee = EmployeeProfile()

vars = Vars()
page = vars.new_page()
actions = vars.new_actions(False) # Make headless later

actions.go(page)
actions.click(
  PageElement(('id', 'new-sale'))
)

line_items = random.randrange(1, 10)

for li in range(1, line_items+1):
  employee.linger()
  # Select an album
  dropdown = PageElement(('id', f'album-select-{li}'))
  random_album = random.randrange(1, 60)
  album_name = actions.get_attribute(
    PageElement(('id', f'{random_album}')),
    'innerText'
  )
  actions.select_drop_down(dropdown, album_name)

  # Set Quantity
  quantity_input = PageElement(('id', f'quantity-input-{li}'))
  random_quantity = random.randrange(1, 5)
  actions.clear_text(quantity_input)
  actions.input_text(quantity_input, random_quantity)

  # Add or submit
  if li != line_items:
    actions.click(
      PageElement(('xpath', f'//*[@id="add-{li}"]/button'))
    )
  else:
    print("Employee is double checking")
    employee.double_check()
    actions.click(
      PageElement(('xpath', '//*[@id="submit-box"]/button'))
    )
    print("Done double checking")

employee.linger()
actions.close()