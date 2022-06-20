def match_arrays(array1, array2):
	if array1 == array2:
		return True
	else:
	    return False
	
	
def main():
    print(match_arrays(["word1", "wo", "word2"], ["word1", "wo", "word2"]))
    print(match_arrays(["32", "hello", "there"],["hello", "there", "23"]))
    print(match_arrays(["hello", "wo"], ["hello", "there", "wo"]))
     

   

if __name__ == '__main__': 
    main()