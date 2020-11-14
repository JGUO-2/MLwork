# -*- coding: utf-8 -*-
"""
  通过定义类
 实现阿拉伯数字转为罗马数字
"""

class Translation():                #定义类

    def int_to_roman(self, num):    #定义阿拉伯数字转为罗马数字函数
        """
        type num: int
        rtype: str
        将数字分解为千位，百位，十位和个位，然后查表将字符串相加

        """
        arabic = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]                    #用表记录关键的阿拉伯数字，
        roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']    #用表记录关键的罗马数字
        ret = ''
        i = 0
        # 将输入循环除以1000，900，500 ...，余数为remainder，将对应的罗马字符串加remainder次
        while num:
            remainder = num // arabic[i]
            ret += roman[i] * remainder
            num = num - remainder * arabic[i]
            i += 1
        return ret

if __name__ == '__main__':

    while 1:
        print("**********阿拉伯数字转为罗马数字***********")
        integer = input("enter:")           #输入需要转换的阿拉伯数字
        if not integer.isdigit():
            print("请输入一个阿拉伯数字！")
            continue
        n = int(integer)
        translation = Translation()         #将类进行实例化
        print('Output:',translation.int_to_roman(n))

