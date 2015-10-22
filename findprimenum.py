### find prime number
###j.z. 10/20/2015

def list_prime(n):

    list = range(2,n)
    
    i=0
    while i < len(list)-1:
        
        j = i + 1
        while j <= len(list)-1:
                if list[j] % list[i] == 0:
                    list.pop(j) 
                else: j = j + 1
                    
        i = i + 1
 
    return list

n = 100 ###the range of prime number, user define
print "There are " + str(len(list_prime(n))) + " prime numbers from 2 to " + str(n) + " : " + str(list_prime(n))  
