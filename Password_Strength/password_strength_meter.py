#!/usr/bin/env python

import re

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/10/20 下午9:34
'''

'''
密码强度检测，给定一个密码判断密码强度，强度共分三级。

密码要求：
    必须由10-15位指定字符组成:
        十进制数字
        大写字母
        小写字母
        特殊字符（如: !@#$%^&*-_）

强度规定：
    强（Strong）: 符合所有组合规则， 例如: Aatb32_67mnq,其中包含大写字母、小写字母、数字和特殊字符,是合格的强密码。
    一般（Average）： 符合三种组合规则
    弱（Weak）： 符合两种及以下组合规则
'''

password1 = r'AbCd@135246_'
password2 = r'AbCa'

def strength_check(password : str) -> str:

    # 检查密码长度
    def length_check(password = password, low = 10, upper = 15):
        if not low <= len(password) <= upper:
            return 'The password too short.'

    # 检查是否有非法字符
    special = {chr(x) for x in range(33, 39)} | {chr(x) for x in range(63, 65)}
    special.update('*+-_'); special.discard('"')
    print(special)
    # regex = re.compile('')

    # 检查字符组合

    return length_check(password)




print(strength_check(password1))
