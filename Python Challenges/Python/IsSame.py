def is_same(name1, name2):
  if name1 == name2:
      return "متشابهتين"
  else:
      return "غير متشابهتين"



def main():

  print(is_same("Ayman","ayman"))
  print(is_same("Amro", "Amrow"))
  print(is_same("Norah", "Norah"))
  print(is_same("Mishal", "Anas"))
  print(is_same("Abdullah", "Abdullah"))

if __name__ == '__main__': main()