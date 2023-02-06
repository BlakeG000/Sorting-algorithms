from random import shuffle
from random import randrange
from time import perf_counter

def main():
  mylist = [20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
  lista = [1,3,5,7]
  listb = [2,4,6,8,9,10,11]
  #merge_sort(mylist)
  test_algorithm(merge_sort,"./merge_sort_test.csv")

  
def time_exec(num_iters,func,*args,**kwargs):
  sort_times = []
  result = None
  for _ in range(num_iters):
    start_time = perf_counter()
    result = func(*args,**kwargs)
    end_time = perf_counter()
    sort_times.append(end_time-start_time)
  return sum(sort_times)/num_iters,result

def swap(mylist,i,j): 
  temp = mylist[j]
  mylist[j] = mylist[i]
  mylist[i] = temp
  
def scramble(mylist, n):
  list_len = len(mylist)
  for _ in range(n):
    i = randrange(list_len)
    j = randrange(list_len)
    swap(mylist,i,j)

    
def test_algorithm(sort_func,out_file_name,n_trials=5, n_scramble=5,start=20,stop=5001,skip=20):
  with open(out_file_name,'w') as f:
    f.write('list_length,randomized,reversed,shuffled\n')
    for list_length in range(start,stop,skip):
      print(f"testing list of length {list_length}")
      randomized_list = list(range(list_length))
      shuffle(randomized_list)
      randomized_time, _ = time_exec(n_trials,sort_func,randomized_list)

      reversed_list = list(range(list_length))
      reversed_list.reverse()
      reversed_time, _ = time_exec(n_trials,sort_func,reversed_list)
      
      scrambled_list = list(range(list_length))
      scramble(scrambled_list,n_scramble)
      scrambled_time, _ = time_exec(n_trials,sort_func,scrambled_list)

      out_string = f"{list_length},{randomized_time},{reversed_time},{scrambled_time}\n"
      f.write(out_string)
  
def merge(lista,listb):
  sortedlist = []
  acounter = 0
  bcounter = 0
  while True:
    if lista[acounter] < listb[bcounter]:
      sortedlist.append(lista[acounter])
      acounter += 1
      if acounter == len(lista):
        while bcounter < len(listb):
          sortedlist.append(listb[bcounter])
          bcounter +=1
        return sortedlist
    else:
      sortedlist.append(listb[bcounter])
      bcounter += 1
      if bcounter == len(listb):
        while acounter < len(lista):
          sortedlist.append(lista[acounter])
          acounter +=1
        return sortedlist
def merge_sort(mylist):
  if len(mylist) > 1:
    var = len(mylist)//2
    left = merge_sort(mylist[var:])
    right = merge_sort(mylist[:var])
    return merge(left,right)
  else:
    return mylist
  
  

if __name__ == '__main__':
  main()