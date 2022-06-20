 
def word_repeat(word, n):
    x = 0
    while x < n:
      x =x+1 
      word.__add__(word)
    return word
        


def main():

  print(word_repeat("CoderHub", 2))
  print(word_repeat("Good", 3))

if __name__ == '__main__': main()