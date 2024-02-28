import math
def findRoots(a, b, c):  
    
    delta = b * b - 4 * a * c  
    sqrt_val = math.sqrt(abs(delta))  
  
  
    if delta > 0:  
        print(" 兩個實根 ")  
        print((-b + sqrt_val) / (2 * a))  
        print((-b - sqrt_val) / (2 * a))  
  
    elif delta == 0:  
        print(" 重根")  
        print(-b / (2 * a))  
  
  
    else:  
        print("共軛複根")  
        print(- b / (2 * a), " + i", sqrt_val)  
        print(- b / (2 * a), " - i", sqrt_val)
a = int(input('輸入 a:'))  
b = int(input('輸入 b:'))  
c = int(input('輸入 c:'))
  # If a is 0, then incorrect equation  
if a == 0:  
    print("輸入正確的一元二次方程式")  
  
else:  
    findRoots(a, b, c)  
  
 
  
 