# Codewars style ranking system
# KATA LINK: https://www.codewars.com/kata/51fda2d95d6efda45e00004e

# Write a class called User that is used to calculate the amount that a user will progress through a ranking system similar to the one Codewars uses.

# Business Rules:
# A user starts at rank -8 and can progress all the way to 8.
# There is no 0 (zero) rank. The next rank after -1 is 1.
# Users will complete activities. These activities also have ranks.
# Each time the user completes a ranked activity the users rank progress is updated based off of 
#   the activity's rank
# The progress earned from the completed activity is relative to what the user's current rank is 
#   compared to the rank of the activity
# A user's rank progress starts off at zero, each time the progress reaches 100 the user's rank is 
#   upgraded to the next level
# Any remaining progress earned while in the previous rank will be applied towards the next rank's progress 
#   (we don't throw any progress away). The exception is if there is no other rank left to progress towards 
#   (Once you reach rank 8 there is no more progression).
# A user cannot progress beyond rank 8.
# The only acceptable range of rank values is -8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8. Any other value 
#   should raise an error.

# The progress is scored like so:

# Completing an activity that is ranked the same as that of the user's will be worth 3 points
# Completing an activity that is ranked one ranking lower than the user's will be worth 1 point
# Any activities completed that are ranking 2 levels or more lower than the user's ranking will be ignored
# Completing an activity ranked higher than the current user's rank will accelerate the rank progression. 
#   The greater the difference between rankings the more the progression will be increased. The formula is 
#   10 * d * d where d equals the difference in ranking between the activity and the user.


class User():
    
  def __init__(self):
    self.rank = -8
    self.progress = 0
    self.ranks = { i:i if i < 0 else i-1 for i in [ x for x in range(-8, 9) if x != 0 ] }
      
  def inc_progress(self, rank):
    if -9 < rank < 9 and rank != 0:
      if rank == self.rank:
        self.progress += 3
      
      elif self.ranks[rank] == self.ranks[self.rank]-1:
        self.progress += 1
      
      elif rank > self.rank:
        d = self.ranks[rank] - self.ranks[self.rank]
        self.progress += 10 *(d**2)
      
      while self.progress >= 100:
        self.progress -= 100
        self.rank = self.rank + 1 if self.rank != -1 else 1
      
      if self.rank >= 8:
        self.progress = 0
        self.rank = 8
    else:
      1/0
