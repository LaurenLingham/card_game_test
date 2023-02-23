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


  def check_for_ace(self, card):
    if card.value = 1: # = should be ==
      return True
    else # should have : after else (else:) however the else statement isn't necessary as it will automatically be False if it isn't True
      return False
   

  dif highest_card(self, card1 card2): # dif should be def, needs a comma separating each parameter
  if card1.value > card2.value: # if statement should be indented as part of function
    return card # card should be card1
  else:
    return card2


def cards_total(self, cards): # Should be indented as a function of the class
  total # should be followed with = 0 to initialise the variable
  for card in cards:
    total += card.value
    return "You have a total of" + total # total should be cast to a string, return should start at same position as for loop otherwise it will only iterate through the first card
  
```
