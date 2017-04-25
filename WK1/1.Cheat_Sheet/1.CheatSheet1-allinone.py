#coding: utf-8
#劇情：小三徵求系統
#載入特定功能的模組

import os
print (os.name)
print (os.getcwd())

#區塊結構的表示方法
#函式（function)的寫法
def main():
    print ('Hello 大家好啊！')         #系統內建的函數, 輸出資料

    s1 = "This is Alger's greeting"  #字串變數
    print (s1) 
    print ('This is also Alger\'s greeting') #跳脫字元的使用方法

    para1 = "Ben"
    para1 = raw_input("請輸入性別=")   #系統內建的函數, 輸入資料
    print(type(para1))
    para2 = int(input("請輸入年齡＝"))
    foo(para1, para2)              #呼叫函式 （函數,副程式,sub ...)

    print ('='* 60)                #字串的乘法
    print('當前的工作路徑是：' + os.getcwd()) #字串的加法

    counter = 0                    #整數變數
    counter += 1                   #變數的加法運算
    counter += 2
    print ("counter = ", counter)  #函式的參數, 可變數量的參數

    #變數就是容器的名字
    fruit = ['蘋果', '橘子', '香蕉']  #資料的容器
    for i in fruit:                 #迴圈結構
        print('我喜歡吃的水果是'+i)

    print ("從0數到9")              #迴圈的邊界表示法
    for i in range(10):
        print ("我有 %d 個億！" %i)  #字串格式化的表示方法

# def foo(para1, para2):  自定義函數, 有兩個參數
def foo(gender, age):
    result = [gender, age]                     #注意資料型別的運用
    print ( "性別為 %c 年齡為 %d" %(result[0], result[1]))     #字串格式化的表示方法
    if gender != 'f':                          #比較判斷運算（大於, 等於, 小於） 
        print ("別鬧了,我只找女生")              #邏輯判斷運算（且, 或）
    elif (age >= 26) and (gender == 'f') :     #這裡很容易忘記冒號
        print ("大姐您找別人吧！")
    else:
        print ("嗯...OK")
    return result

'''
主題：小三徵求系統
版本：第一版
作者：Alger
'''  

if __name__ == '__main__':
    main()