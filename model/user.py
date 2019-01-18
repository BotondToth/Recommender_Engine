# Felhasznalokat reprezentalo modell osztaly
# Eltarolja egy felhasznalo id, nem, kor, foglalkozas, iranyitoszam attributumait
class User:

  def __init__(self, id, gender, age, occupation, zip_code):
    self.id = id
    self.gender = gender
    self.age = age
    self.occupation = occupation
    self.zip_code = zip_code