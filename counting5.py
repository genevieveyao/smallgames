#define function
def count5(t):
    sum=0
    while t/5>=1:
        sum+=int(t/5)
        t=t/5
    return sum
#预设值
t = 2000
#input room number
rm = int(input('please input your room number'))
#test validity
if rm<0 or rm>10000 :
    print('inorder to save me, please only input number in [0,10000]')
else:
    #start trials
    while count5(t) != rm:
        if count5(t)<rm and count5(t+5)> rm:
            print('I am sorry, that you live in a pity room')
            t=''
            break
        t+=5*(rm-count5(t))
    print(t)



