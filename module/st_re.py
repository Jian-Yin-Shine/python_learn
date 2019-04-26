# 读书的时候，我记得java老师跟我们说过，最好是能够背诵一套正则
# 想想那个时候简直是不听话
# 现在复习一遍，防止面试的时候被问到

# 字符类(字符集合)
# []

# [xyz] : t[aeio]n 可以匹配tan, ten, tin, ton
# [^xyz]否定字符集
# [a-z], [^a-z]

import re
print(re.findall('fo[xro]', 'the quick brown fox jumps for food'))

# 特殊的字符类（集合）[] ：有固定写法
# . 一个占位符，除\n
# \d 等价于[0-9]
# \D 等价于[^0-9]
# \s 空白字符 ，等价于[\t\n\r\f\v]
# \S 非空白字符， 等价于[^\t\n\r\f\v]
# \w 单词字符，  等价于[a-zA-Z0-9_]
# \W 非单词字符， 等价于[^a-zA-Z0-9_]

# 边界
# ^ 行开头
# $ 行结尾
# \b 单词边界
# \B 非单词边界
# \A 字符串开头
# \Z 字符串结尾，除\n

# 重复限定
# *     ：前一个字符 0，或者无数次    zo*     可以匹配 z, zo, zoo, zooo
# ?     ：前一个字符 0，1次          colou?r 可以匹配 color, colour
# +     ：前一个字符 1，无数次        zo+     可以匹配 zo, zoo, zooo
# {n}   ：n 次                      \b[0-9]{3} 可以匹配 000~999
# {n,}  ：至少n次
# {n,m} ：n-m 次

# 选择 |
# 分组 ()



# 之前已经敲过了一些特殊字符，总结一下，
'''
正则表达式模式
模式字符串使用特殊的语法来表示一个正则表达式：

字母和数字表示他们自身。一个正则表达式模式中的字母和数字匹配同样的字符串。

多数字母和数字前加一个反斜杠时会拥有不同的含义。

标点符号只有被转义时才匹配自身，否则它们表示特殊的含义。

反斜杠本身需要使用反斜杠转义。

由于正则表达式通常都包含反斜杠，所以你最好使用原始字符串来表示它们。模式元素(如 r'\t'，等价于 \\t )匹配相应的特殊字符。

下表列出了正则表达式模式语法中的特殊元素。如果你使用模式的同时提供了可选的标志参数，某些模式元素的含义会改变。

模式	描述
^	匹配字符串的开头
$	匹配字符串的末尾。
.	匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。
[...]	用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
[^...]	不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。
re*	匹配0个或多个的表达式。
re+	匹配1个或多个的表达式。
re?	匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
re{ n}	匹配n个前面表达式。例如，"o{2}"不能匹配"Bob"中的"o"，但是能匹配"food"中的两个o。
re{ n,}	精确匹配n个前面表达式。例如，"o{2,}"不能匹配"Bob"中的"o"，但能匹配"foooood"中的所有o。"o{1,}"等价于"o+"。"o{0,}"则等价于"o*"。
re{ n, m}	匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式
a| b	匹配a或b
(re)	匹配括号内的表达式，也表示一个组
(?imx)	正则表达式包含三种可选标志：i, m, 或 x 。只影响括号中的区域。
(?-imx)	正则表达式关闭 i, m, 或 x 可选标志。只影响括号中的区域。
(?: re)	类似 (...), 但是不表示一个组
(?imx: re)	在括号中使用i, m, 或 x 可选标志
(?-imx: re)	在括号中不使用i, m, 或 x 可选标志
(?#...)	注释.
(?= re)	前向肯定界定符。如果所含正则表达式，以 ... 表示，在当前位置成功匹配时成功，否则失败。但一旦所含表达式已经尝试，匹配引擎根本没有提高；模式的剩余部分还要尝试界定符的右边。
(?! re)	前向否定界定符。与肯定界定符相反；当所含表达式不能在字符串当前位置匹配时成功。
(?> re)	匹配的独立模式，省去回溯。
\w	匹配数字字母下划线
\W	匹配非数字字母下划线
\s	匹配任意空白字符，等价于 [\t\n\r\f]。
\S	匹配任意非空字符
\d	匹配任意数字，等价于 [0-9]。
\D	匹配任意非数字
\A	匹配字符串开始
\Z	匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。
\z	匹配字符串结束
\G	匹配最后匹配完成的位置。
\b	匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
\B	匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。
\n, \t, 等。	匹配一个换行符。匹配一个制表符, 等
\1...\9	匹配第n个分组的内容。
\10	匹配第n个分组的内容，如果它经匹配。否则指的是八进制字符码的表达式。
正则表达式实例
字符匹配
实例	描述
python	匹配 "python".
字符类
实例	描述
[Pp]ython	匹配 "Python" 或 "python"
rub[ye]	匹配 "ruby" 或 "rube"
[aeiou]	匹配中括号内的任意一个字母
[0-9]	匹配任何数字。类似于 [0123456789]
[a-z]	匹配任何小写字母
[A-Z]	匹配任何大写字母
[a-zA-Z0-9]	匹配任何字母及数字
[^aeiou]	除了aeiou字母以外的所有字符
[^0-9]	匹配除了数字外的字符
特殊字符类
实例	描述
.	匹配除 "\n" 之外的任何单个字符。要匹配包括 '\n' 在内的任何字符，请使用象 '[.\n]' 的模式。
\d	匹配一个数字字符。等价于 [0-9]。
\D	匹配一个非数字字符。等价于 [^0-9]。
\s	匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。
\S	匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。
\w	匹配包括下划线的任何单词字符。等价于'[A-Za-z0-9_]'。
\W	匹配任何非单词字符。等价于 '[^A-Za-z0-9_]'。
'''

str = "<book><title>Python</title><author>Jian</author></book>"
# 重复限定符，尽可能多重复几次
print (re.findall('<.+>', str))

# 在重复限定符后面加上 ? 就是尽可能少重复
str = '<book><title>Python</title><author>Jian</author></book><>'
print (re.findall('<(.*?)>', str))

# re.finditer
# 和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
#
# re.finditer(pattern, string, flags=0)

# re.search 找到一个即可
str = '<book><title>Python</title><author>Jian</author></book><>'
print (re.search('<(.*?)>', str))

# re.match(pattern, string, flag =0)
# 只能从开头匹配
# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
a = re.match('w{3}', 'www.runoob.com')
print(a)