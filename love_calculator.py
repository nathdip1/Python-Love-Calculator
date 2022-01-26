from functools import reduce


print("***Hey love birds..:) Wlecome to the love calculator***")
boy_nm = input("Enter Boy's name: ").lower()
girl_nm = input("Enter Girl's name: ").lower()

a = len(boy_nm)
b = len(girl_nm)
sum_len = a+b
c = 0

if boy_nm == girl_nm:
    print("Your love percentage is 100%")
else:
    for i in boy_nm:
        for j in girl_nm:
            for k in range(0,255):
                if i == j:
                    c = c+k
                else:
                    continue
    if c == 0:
        print("No common letter found in the given name")
    elif c > 0:
        result = (c * sum_len) // 100
        if result == 100:
            print("Your love percentage is 100%")
        elif result > 100:
            reduce = 51
            for digits in range(0,1000000):
                result = result - reduce
                if result < 100:
                    print(f"Your love percentage is {result}%")
                    break
                else:
                    digits +=1

                
                
                    


       