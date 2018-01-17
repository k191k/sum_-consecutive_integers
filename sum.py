import itertools

#入力値
input_num = input()

t = 1
counter = 0
result = 0

while (counter < int(input_num)):
    
    head_num = []
    tail_num = []
    
    #基の値は２つに分ける
    original_t = ((t - 1) / 2)
    head_num.append(original_t)
    tail_num.append(original_t + 1)
    
    #奇数のみ計算
    for num in range(1, int(t) + 1, 2):

        #奇数の約数を求める
        if t%num == 0:
            middle_pos = ((num - 1) / 2) + 1
            middle_num = t / num
            head_num.append(middle_num - (num - middle_pos))
            
            if head_num[-1] < 0:
                #最小がマイナス値の場合は相殺
                head_num[-1] = (-1 * head_num[-1]) + 1
            
            #最大値を追加    
            tail_num.append(middle_num + (num - middle_pos))

        
    #総当りで連続する和の連続の有無を検証
    for head, tail in itertools.product(head_num, tail_num):
        if head== (tail + 1):
            counter+=1
            break
            
    t+=1
    head_num.clear()
    tail_num.clear()
    
#inputされた値、n番目の連続する整数の和が連続する表現が可能な数
print(t - 1)