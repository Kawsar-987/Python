def Selection(Array):
      n=len(Array)
      for i in range(n):
          min_index=i
          for j in range(i+1,n):
              if Array[j]<Array[min_index]:
                  min_index=j
          Array[i],Array[min_index]=Array[min_index],Array[i]
      return Array

Array=[64,25,12,22,11]
Sorted_Array=Selection(Array)
print(Sorted_Array)
