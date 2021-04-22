### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

# indentation is wrong, no colon after the else statement, the if statement should have an equality operator(==).
  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
   
# incorrect indentation. the keyword for defining the function was spelt incorrectly (def was spelt as dif, no comma to seperate card1 and card2, return statement on line 29 is incomplete card1 was written as card)
  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
  

# line 36 is incomplete, total should be equals to a value, incorrect indentation.
def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```
