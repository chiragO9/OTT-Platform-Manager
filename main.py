class comedy_show:

  def __init__(self,name,channel,price,setup_box):
    self.name = name
    self.channel = channel
    self.price = price
    self.setup_box = setup_box

  
  def show(self):
    return f"""
      name is {self.name}
      channel is {self.channel}
      price is {self.price}
      setup box is {self.setup_box}
    """


  def apply_discount(self,discount_percent):
    discount_amount = (self.price * discount_percent) / 100
    new_price = self.price - discount_amount
    return f"Original price: {self.price} RS | After {discount_percent}% discount: {new_price} RS"

  def is_premium_channel(self):
    premium_channel  = ['HBO','netflix','Amazon prime']
    if self.channel in premium_channel:
      return f"{self.channel} is premium channel"
    else:
      return f"{self.channel} is regular channel"

x = comedy_show('friends','HBO',30,'tata sky')
y = comedy_show('how I met your mothher','romedy',20,'tata sky')

print(x.show())
print(x.apply_discount(20))
print(x.is_premium_channel())

print(y.show())
print(x.apply_discount(20))
print(x.is_premium_channel())