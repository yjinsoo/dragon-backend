import time

class Pod:
  def __init__(self, name, cpu_usage):
    self.name = name
    self.cpu_usage = cpu_usage
    
  def is_overload(self):
    if self.cpu_usage >= 80 :
      return True
    else:
      return False
  
object01 = Pod("DB-Pod",90)
object01.is_overload()


print("==========END==========")
while True:
  time.sleep(60)
