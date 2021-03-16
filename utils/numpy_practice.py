import numpy as np

# 创建一个一维数组
from PIL import Image

a = np.array([[1, 2, 3], [2, 3, 2]])

print(a)

# 获取数组的维度
print(f'数组的维度:{a.shape}')

# 获取数组的轴
print(f'数组的轴:{a.ndim}')

# 获取数组中元素的总数
print(f'数组元素的总数:{a.size}')

# 获取数组中元素的类型,元素类型都是一致的
print(f'数组中元素的类型:{a.dtype}')

# 获取数组中每个元素的字节大小
print(f'数组中每个元素的字节大小: {a.itemsize}')

# 创建一个二维数组
# | 1 2 3 |
# | 4 5 6 |

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b[0, 0], b[0, 1], b[1, 0])

# 直接创建一个多维数组,使用0进行初始化
s = np.zeros((2, 2))
print(s)

# 创建一个多维数组，使用1进行初始化
d = np.ones((2, 2))
print(d)

# 创建一个多维数组，使用指定的值进行初始化
f = np.full((2, 2), 7)
print(f)

# 创建一个2*2的矩阵
k = np.eye(2)
print(k)

# 创建一个2维数组使用随机值进行填充
h = np.random.random((2, 2))
print(h)

# 生成一个包含15个随机数的数组
tg = np.arange(15)
print(f'15个随机数的数组:{tg}')

# 重新构造成一个新的数组
array = tg.reshape(3, 5)
print(f'重新构造的新的数组为:{array}')

# 创建一个从0-2包含9个元素的数组
new_array = np.linspace( 0, 2, 9 )
print(f'从0-2包含9个元素的数组为{new_array}')


# --------------------------------------------------
# 数组之间的运算
# 1. 减和加,是对应位置的元素级别的
array1 = np.arange(3)
print(array1)
array2 = np.array([20, 50, 89])
print(array2 - array1)

# 2. 乘和除，对应位置的元素之间进行乘和除
print(f'乘的结果为:{array2 * array1}')

# 3. 乘积
print(f'乘积的结果为:{array2 @ array1}')

# 4.+=或者*=会直接改变原数组，而不会创建新的数组
print(f'array2数组原始的值为{array2}')
array2 += array1
print(f'array2数组新的值为:{array2}')

# 当使用不同类型的数组进行操作时，结果数组的类型对应于更一般或更精确的数组（称为向上转换的行为）
a1 = np.ones(3, dtype=np.int32)
b1 = np.linspace(0, 3, 3)
print(f'b1数组的元素类型为:{b1.dtype.name}')
print(f'a1数组的元素类型为:{a1.dtype.name}')
c1 = a1 + b1
print(f'c1数组的元素类型为:{c1.dtype.name}')

# 计算数组中元素的总和,最小值、最大值，这些一元的操作都是作为ndarray类的方法实现的
v1 = np.ones(2)
print(v1)
print(f'v1数组元素的总和为:{v1.sum()}')
print(f'v1数组的维度为: {v1.shape}')
print(f'v1数组元素的最小值为:{v1.min()}')
print(f'v1数组元素的最大值为:{v1.max()}')

# 通过指定axis 参数，您可以沿数组的指定轴应用操作
b2 = np.arange(12).reshape(3, 4)
print(b)
print(f'b数组的维度为: {b.shape}')
print(f'b数组0轴的总和为:{b.sum(axis=0)}')


# -----------------通函数------------------
# NumPy提供熟悉的数学函数，例如sin，cos和exp。在NumPy中，这些被称为“通函数”，在NumPy中，这些函数在数组上按元素进行运算，产生一个数组作为输出。
n = np.arange(3)
print(f'指数:{np.exp(b)}')


# ----------------索引、切片和迭代----------
# 一维数组可以进行索引，切片和迭代操作
b3 = np.arange(3)
print(f'b3数组为:{b3}')
print(f'b3数组的第一个元素为: {b3[0]}')
print(f'b3数组的切片为:{b3[:]}')
for i in b3:
    print(f'b3中的元素为:{i}')


# 多维数组的每个轴都有一个索引，使用逗号分隔
def f(x, y):
    return 10 * x + y


c2 = np.fromfunction(f, (5, 4), dtype=int)
print(f'c2数组为:{c2}')
print(f'c2数组的第二列为:{c2[0:5, 1]}')

# 当提供的索引数量少于轴的数量的时候，会默认为完整的切片
print(f'c2数组的最后一行为:{c2[-1, 0:5]}')

# 对多维数组进行 迭代（Iterating） 是相对于第一个轴完成的
m = np.arange(162).reshape(2, 9, 9)
for i in m:
    print(i)
print(m.ndim)
print('------------------------------')
# 但是，如果想要对数组中的每个元素执行操作，可以使用flat属性，该属性是数组的所有元素的迭代器
for x in m.flat:
    print(x)

# 一个数组的形状是由每个轴的元素数量决定的
# 将数组进行展开
res = m.ravel()
print(f'm数组改变之后的形状为:{res}')

# 可以使用这个方式来展开一个嵌套的列表
var = [[2, 3, 4], [1, 2, 4]]
n_array = np.array(var)
print(n_array.ravel())

# 改变数组的形状,得到一个新的数组
new_m = m.reshape(9, 9, 2)
print(f'm数组改变形状之后得到的新的数组为:{new_m}')

# 改变数组的形状，数组翻转,得到一个新的数组
new_m2 = m.T
print(f'm数组翻转之后的形状为:{new_m2}')
