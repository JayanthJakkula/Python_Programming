day1=['cs@gmail.com','ce@gmail.com','db@gmail.com','CE@gmail.com','DB@gmail.com']
day2=['CS@gmail.com','CE@gmail.com','ct@gmail.com','db@gmail.com']
day3=['Ce@gmail.com','CE@gmail.com','ct@gmail.com','db@gmail.com','Ct@gmail.com','DB@gmail.com']
s1=set()
s3=set()
s2=set()
for x in day1:
    
    s1.add(x.lower())
for x in day2:
    
    s2.add(x.lower())
    
for x in day3:
    s3.add(x.lower())

print("Unique attandees are:",s1|s2|s3)
print("who attend 3 days are:",s1&s2&s3)
print("who attend only one day:",s1^s2^s3)
print(len(s1&s2))
print(len(s3&s2))
print(len(s3&s1))





