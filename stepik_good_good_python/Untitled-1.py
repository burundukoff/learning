def square_or_square_root(arr):
    
    for i,j in enumerate(arr):
        if j**0.5 == int(j**0.5):
            arr[i]=int(j**0.5)
        else:
            arr[i]=j**2
    #print(arr)            
    return arr                

square_or_square_root([4,3,9,7,2,1])