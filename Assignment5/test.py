def mean(values):
     length = len(values)
     total_sum = 0
     for i in range(length) :
              total_sum += values[i]
     total_sum = sum(values)
     average = total_sum/length
     return average
x = [1,2,3,4]
n = mean(x)
print (n)