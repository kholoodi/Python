def search(word, character):
    for i in range(0, len(word)):
        if word[i] == character:
            return i
    return -1

	
def main():
    print(search('Programming','o'))
    print(search('Java','a'))
    print(search('like','z'))
    print(search('python','n'))
     

   

if __name__ == '__main__': 
    main()