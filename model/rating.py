# Egy ertekelest reprezentalo modell osztaly
# Eltarolja egy ertekeles felhasznalo- es film-id, ertekeles, idopont attributumait
class Rating:

  def __init__(self, userId, movieId, rating, timestamp):
    self.userId = userId
    self.movieId = movieId
    #Az ertekeles 1-5 kozotti ertekeket vehet fel (1: legrosszabb, 5: legjobb)
    self.rating = rating
    self.timestamp = timestamp