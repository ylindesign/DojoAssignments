# Find & Replace
str = "It's thanksgiving day. It's my birthday,too!"
print str.find("day")
print str.replace('day', "month", 1)

# Min & Max
x = [2,54,-2,7,12,98]
print max(x)
print min(x)

# First & Last
y = ["hello",2,54,-2,7,12,98,"world"]
print y[0]
print y[-1]
y_string = []
y_string.append(y[0])
y_string.append(y[-1])
print y_string

# New List
z = [19,2,54,-2,7,12,98,32,10,-3,6]
z.sort()
a = z[:len(z)/2]
b = z[len(z)/2:]
b.insert(0, a)
print b