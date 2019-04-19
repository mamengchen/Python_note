python3：
Number:数字
整数：int（没有其他的类型）
小数(浮点数)：float
我们可以使用type来查看数据类型（C++使用typeid.name）
在使用除法的时候如果要保证类型是整型则需要加//:例如（2//2）；
/：得到的是浮点型的
//：是整除（只保留整数部分）
这个进制的转化：
0b：表示二进制（0b10 = 2；0b11 = 3）
0o：表示八进制（0o10 = 8；0o11 = 9）
0x：表示十六进制（0x10 = 16； 0x1F = 31）
（以上等于后面的均是十进制的表示）
bin(10);bin(0o7);bin(0xE)把数据转化为2进制的
int：转化为十进制
hex：转化为十六进制
oct：转化为八进制
bool类型：表示真、假     complex：复数（36j）
非零表示真，零表示假；字符串有元素表示真，没有元素是假
列表中有元素表示真，没有元素是假；非空一般都被认为Ture
str字符串：单引号、双引号、三引号
比如我想显示文本中的单引号
("let's go")('let"s go')或者使用转义字符('let\'s go')
多行字符串的输入使用三引号
'''
hhhhhhhhhhhhhhhhh
hhhhhhhhhhhhhhhhh
hhhhhhhhhhhhhhhhh
'''
三引号也一样可以使用双引号表示"""  """;
注意：在IDLE上\n不会换行，得使用函数print：\n才会被替换成换行
当加入\时候单引号也可以多行输入：例如
'sss\
sss\
sss'
转义字符：（特殊的字符） 
\n 换行   \r 回车；但是两种不是一会事
\' 单引号
\t 横向制表符
如果想使用print('c:\north\wordwest')输出c:\north\wordwest；
第一种方式就是print('c:\\north\\wordwest')
第二种方式就是print(r'c:\north\wordwest'):不是一个普通字符串，而是一个原始字符串;
字符串的运算："hello" + "world" = "halloworld"
"hallow" * 3 = "hallowhallowhallow"
"hallo world"[0] = 'h':负数则从后面开始数
如果你需要获取一段例如"hallo world"[0:5] = "hallo";
如果是负数则便是排除如"hallo world"[0:-1] = "hallo worl";

python的基本数据类型：
列表：[1,2,3,4,5]["hello","world",1,9,True,False]
一个列表的内部元素可以插入任意的元素类型，列表中也可以嵌套列表（相当于二维数组）
如果使用单一的[number]访问列表则表示一个字符串，如果使用[first:list]则表示一个列表
两个列表链接起来就是使用+
列表×number=列表重复的number次数加起来

元祖：(1,2,3,4,5)
也可以是不同类型的放在一起(1,2,3,True,False,"asd")
访问性质和列表一样，[number]取出的元素为元素本身属性，[first:list]为元祖性质
+于*一样
因为：元祖的符号和数学()相同，在表示一个元素的元祖时候，我们需要在元素后面加，例如('1',);
如果想表示没有元素的元祖则直接()就可以了
元祖和列表的区别：
1、元祖是不可变的，列表是可变的；

int、str、list(列表)、tuple(元组)、bool、float（典型的标识）

序列：
1、每个元素都会被分配一个序号
2、切片[first:list];[first:list:jump]jump:打印一次跳过jump-1个
3、可以+于*；如果我想判断一个元素是否在序列中使用in，not in（表示不在）
4、如果我们想知道一个序列长度则用 len(序列)； max(序列)求最大值； min(序列)求最小值； ord('w') = 119：用于转化为ASCLL码

集合set：（最大特点：无序）没有下标索引，不支持切片操作，重复元素只显示一边（去重），不支持+于*
支持：in、not in、len
特有的：求两个集合的差集{1,2,3,4,5}-{2,4} = {1,3,5}
		求两个集合的交集{1,2,3,4,5,6}&{3,4} = {3,4}
		合并两个集合{1,2,3,4,5,6} | {3,4,7} = {1,2,3,4,5,6,7}
集合的定义：{}     定义一个空的集合为：set();

字典dict：（key,value）
定义：{}    例子：{key1:value1, key2:value2}
是无序的,没有下标标识，用key标识value，字典中不能有两个key，原本的key中value会被新的key中value所替代
value：类型str int float list set dict
key：不是任意的类型，必须是不可变的类型例如int ，str