laby = [
"xx   xxxxxxxxxx",
"xxx  xxxxxxxxxx",
"xxxx  xxxxxxxxx",
"xxxxx  xxxxxxxx",
"xxxxxx  xxxxxxx",
"xxxxx  xxxxxxxx",
"xxxxx  xxxxxxxx",
"xxxxx  xxxxxxxx",
"xxxxxx  xxxxxxx",
"xxxx xxxxxxxxxx",
"xxxxx  xxxxxxxx",
"xxxxx  xxxxxxxx",
"xxxxx  xxxxxxxx",
"xxxxx  xxxxxxxx",
]

for item in laby:
    print(item)
       
class Character:
  def __init__(self, **details):
    for attr_name, attr_value in details.items():
        setattr(self, attr_name, attr_value)
details = {"position":8, "shape":1, "color":1}
Mcgyver = Character(**details)
print(Mcgyver.position)

class Gardien:
    def __init__(self, **details2):
        for attr_name, attr_value in details2.items():
            setattr(self, attr_name, attr_value)
details2= {"position":18, "shape":7, "color":4}
gardien = Gardien(**details2)
print(gardien.shape)
            
class Objet:
    def __init__(self, **details3):
        for attr_name, attr_value in details3.items():
            setattr(self, attr_name, attr_value)
details3= {"position":9, "shape":7, "color":6}
objet = Objet(**details3)
print(objet.color)