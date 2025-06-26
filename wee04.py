# Array to test with
my_array = ["testing", "secondlongest", "longest", "long"]
my_array2 = ["lalalalala", "lululul", "lalalalalalala", "long", "lsdlasldlasldlsa"]
my_array3 = ["lalalalala", "lululul", "lalalalalalala", "sdkoaskdoaksdok", "lsdlasldlasldlsa"]
my_array4 = None


def longest_word(words: list[str]) -> str:
    # Check if words is None
    if words == None or len(words) == 0:
        return None

    # Assume first word is the longest to start
    longestWord = ""
    longestWord = words[0]

    # Examine every remaining word
    for i in range (1, len(words)):
        # If we find a longer word, remember it
        if len(words[i]) > len(longestWord):
            longestWord = words[i]
    
    return longestWord

print ( longest_word(my_array) )
print( longest_word(my_array4) )


def shortest_word(words: list[str]) -> str:
    # Check if words is None
    if words == None or len(words) == 0:
        return None

    # Start out by treating the first word as the shortest
    shortestWord = ""
    shortestWord = words[0]

    # Go through the rest of the words
    for i in range (1, len(words)):
        # If we find a shorter one, update our record
        if len(words[i]) < len(shortestWord):
            shortestWord = words[i]
    
    return shortestWord

print ( shortest_word(my_array) )
print( shortest_word(my_array4) )

def odd_words(words: list[str]) -> list[str]:
    # Check if words is None
    if words == None or len(words) == 0:
        return None

    oddWords = [] # place to collect odd-length words

    for i in range(0, len(words)):
        # length is odd if remainder of ÷2 is 1
        if len(words[i]) % 2 != 0:
            oddWords.append(words[i])
    
    return oddWords

print ( odd_words(my_array) )
print ( odd_words(my_array4) ) 


def average_words(words):
    # Check if words is None
    if words == None or len(words) == 0:
        return None

    # Compute the average length
    total_length = 0
    for w in words:
        total_length += len(w)
    average = total_length / len(words)

    # Collect words whose length is within ±1 of that average
    result = []
    for w in words:
        if abs(len(w) - average) <= 1:
            result.append(w)

    return result

print ( average_words(my_array) )
print ( average_words(my_array4) )

def intersect(foo, bar):
    # Check if either foo or bar is None
    if foo == None or bar == None:
        return False

    # Compare every element in foo against every element in bar
    for i in range(len(foo)):
        for j in range(len(bar)):
            # found match
            if foo[i] == bar[j]:
                return True
            
    return False

print ( intersect(my_array, my_array2) )

# Reflection
# This task for me was a bit of a challange, as I had to go back to review my notes, however once I reviewed my notes, and tried it a couple of times, I managed to succesfully create the code, which resulted in me completing the entire task, through trial and error I was able to complete this task, though I had to admittedly conslt a few youtube videos, on the theories behind it as I was lost more than a few times while writing the code. Overall, this task for me was quite a challenge but one in which I was able to succeed in, I would give myself a 90/100

#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# Basic testing. This block validates the logic of the code. Additional 
# requirements such as single return statements are not tested here but 
# must be met anyway.
if __name__ == "__main__":
  testA = ["a", "list", "of", "nearly", "random", "words", "and", "strings"]
  testB = []
  testC = ["a", "be", "cat", "door", 
           "eagle", "galaxy", "forests", "harvests", 
           "important", "journalist"]
  testD = ["Frodo", "Gandalf", "Gollum", "Legolas", "Aragorn", "Rivendell"]
  testE = ["Saruman", "Boromir", "Faramir", "Sauron", "Gollum", "Minas Tirith"]
  testF = None

  # -------- Testing
  print("\nTesting shortest_word")
  if shortest_word(testF) is not None:
    print("shortest_word FAILS null test")
  else:
    print("shortest_word passes null test")

  if shortest_word(testB) is not None:
    print("shortest_word FAILS empty test")
  else:
    print("shortest_word passes empty test")

  if shortest_word(testA) is not testA[0]:
    print("shortest_word FAILS length test")
  else:
    print("shortest_word passes length test")

  # -------- Testing
  print("\nTesting longest_word")
  if longest_word(testF) is not None:
    print("longest_word FAILS null test")
  else:
    print("longest_word passes null test")

  if longest_word(testB) is not None:
    print("longest_word FAILS empty test")
  else:
    print("longest_word passes empty test")

  if longest_word(testA) is not testA[len(testA)-1]:
    print("longest_word FAILS length test")
  else:
    print("longest_word passes length test")
  
  # -------- Testing
  print("\nTesting odd_words")
  if odd_words(testF) is not None:
    print("odd_words FAILS null test")
  else:
    print("odd_words passes null test")
  
  if odd_words(testB) is not None:
    print("odd_words FAILS empty test")
  else:
    print("odd_words passes empty test")

  odd_test = [testC[i] for i in range(0, len(testC), 2)]
  if odd_words(testC) != odd_test:
    print("odd_words FAIlS logic test")
  else:
    print("odd words passes logic test")

  # -------- Testing
  print("\nTesting average_words")
  if average_words(testF) is not None:
    print("average_words FAILS null test")
  else:
    print("average_words passes null test")
  
  if average_words(testB) is not None:
    print("average_words FAILS empty test")
  else:
    print("average_words passes empty test")

  odd_test = [testC[i] for i in range(0, len(testC), 2)]
  if average_words(testC) != ['eagle', 'galaxy']:
    print("average_words FAILS logic test")
  else:
    print("average_words words passes logic test")

  # -------- Testing
  print("\nTesting intesect")
  if intersect(testF, testA):
    print("intersect FAILS first null test")
  else:
    print("intersect passes first null test")

  if intersect(testA, testF):
    print("intersect FAILS second null test")
  else:
    print("intersect passes second null test")
  
  if intersect(testB, testA):
    print("intersect FAILS first empty test")
  else:
    print("intersect passes first empty test")

  if intersect(testA, testB):
    print("intersect FAILS second empty test")
  else:
    print("intersect passes second empty test")

  if not intersect(testD, testE):
    print("intersect FAILS logic test for true")
  else:
    print("intersect words passes logic test for true")
  
  if intersect(testA, testE):
    print("intersect FAILS logic test for false")
  else:
    print("intersect words passes logic test for false")
