def iterate(i, n):
    if i >= 10:
        return
    
    if n != 4500:
        print(n)
        
    iterate(i + 1, n - 500)

iterate(0, 5000)


