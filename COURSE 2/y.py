

a = [ 20, 40, 70, 30, 10, 80, 50, 90, 60]
b = [ 35, 45, 55, 60, 50, 40]
c = []

def check():

    for i in a:
        for j in b:
            if i == j:
                break
            else:
                c.append(i)


         



check()
print(c)