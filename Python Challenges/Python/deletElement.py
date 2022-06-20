def delete_element_in_array(arr, index):
    for i in range(0,len(arr)):
        if index == i:
            del(arr[index])
    return arr


def main():

  print(delete_element_in_array([2 , 4 , 88],2))
  print(delete_element_in_array([-3 , 4 , 0],0))

if __name__ == '__main__': main()
