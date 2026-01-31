file = open('','')

try:
    file.wrtie()
finally:
    file.close()
    
with open('test.txt','w') as file:
    file.write("")