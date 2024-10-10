## 一、大型知识点

### 1.None的作用：

在Python中，`None` 是一个特殊的常量，它通常用来表示“无”或“空”。`None` 是 `NoneType` 类型的唯一实例，并且它在Python中有着多种用途：

1. **表示空值**：`None` 可以用来表示一个变量当前没有被赋予具体的值。

2. **默认参数**：在函数定义中，可以将参数的默认值设置为 `None`，这样在调用函数时，如果没有提供该参数，它将自动采用默认值 `None`。

3. **条件语句**：在条件语句中，`None` 被视为 `False`，但它与 `0`、`False`、空字符串 `''` 或空列表 `[]` 等其他被视为假的值是不同的。***（在函数返回值中的作用有些时候可以用-1替代，None在返回值存在0的时候会混淆）***

4. **返回值**：函数可以返回 `None`，表示没有有效的返回值或者操作没有成功。

5. **与对象标识**：由于 `None` 是唯一的，它可以用作对象标识，例如在列表或字典中表示某个特定位置的占位符。

6. **避免副作用**：在某些情况下，使用 `None` 作为函数参数可以避免不必要的副作用。

7. **兼容性**：在一些旧的代码或库中，可能会使用 `None` 来表示某些特定的状态或条件。

8. **类型检查**：在进行类型检查时，可以使用 `is None` 来确定一个变量是否为 `None`。

以下是一些使用 `None` 的示例：

```python
def my_function(param=None):
    if param is None:
        print("没有提供参数")
    else:
        print("参数的值是：", param)

my_function()  # 输出: 没有提供参数
my_function(123)  # 输出: 参数的值是： 123

# 检查变量是否为空
value = None
if value is None:
    print("变量是空的")
else:
    print("变量有值")

# 使用 None 作为占位符
my_list = [None] * 5  # 创建一个包含5个 None 的列表
```

### 2.活用字典：

在字典中查找元素的平均时间复杂度为O（1），因此在一些含有搜索的题目中，我们不仅可以使用列表的查找/二分查找，还可以使用字典的查找。

### 3.字典的一些基本操作：

##### 删除键值对

使用 `del` 语句或 `pop()` 方法删除键值对。

```python
del my_dict['key1']  # 删除键为 'key1' 的键值对

# 使用 pop 方法，同时获取删除的值，None为未找到该键时的默认返回值
removed_value = my_dict.pop('key2', None)
```

##### 遍历字典

遍历字典时，可以遍历键、值或键值对。

```python
for key in my_dict:
    print(key)  # 遍历所有键

for value in my_dict.values():
    print(value)  # 遍历所有值

for key, value in my_dict.items():
    print(f'{key}: {value}')  # 遍历所有键值对
```

##### 检查键是否存在

使用 `in` 关键字检查键是否存在于字典中。

##### 获取所有键或值的列表

使用 `keys()`、`values()` 或 `items()` 方法。

```python
keys = my_dict.keys()  # 返回所有键的视图
values = my_dict.values()  # 返回所有值的视图
items = my_dict.items()  # 返回所有键值对的视图
```

##### 更新字典

使用 `update()` 方法更新字典。

```python
my_dict.update({'key4': 'value4', 'key5': 'value5'})
```

### ASCLL表

A：65

a：97

## 二、小型的技巧

1. 当一个字符串用在条件判断中时，是用来判断这个字符串是否为空的。

## 三、一些常见的函数或者变量名称

- BinarySearch：二分搜索，函数中常用target代表搜索的对象
- Euler_sieve：欧拉筛