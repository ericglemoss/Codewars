# Your task is to sort a given string. Each word in the string will contain a single number.
#This number is the position the word should have in the result.

# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

# If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.


def order(sentence):
  temp = sentence.split(" ")
  out = [None] * len(temp)
  if not sentence:
      return ""
  else:
      for word in temp:
          for char in word:
              if 49 <= ord(char) <= 57:
                  out[int(char)-1] = word
  return " ".join(out)
