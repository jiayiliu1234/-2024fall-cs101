#### 1. Python 变量的指针本质
广义地，可以把 python 中一切可赋值的东西都称为变量，而所有的变量都是指针（或者说引用），包括列表的元素，字典的值。其指针本质体现在赋值、函数形参、函数返回值、存放元素到容器中等处。**脑子里时时刻刻要有类似 pythontutor 里那种从 identifier 指向对象的箭头！**

- python 中赋值是让左侧变量指向右侧变量指向的对象（如果右侧是变量）或让左侧变量指向右侧对象（如果右侧是对象）

- 函数形参相当于用实参赋值得到，即形参指向实参变量指向的对象（如果实参是变量）或指向实参这个对象（如果实参是对象）

- 函数调用得到的返回值（如果有）相当于`return x`语句中`x`赋值给它，即返回值指向`x`指向的对象（如果`x`是变量）或返回值指向`x`这个对象（如果`x`是对象）：

  ```python
  a = [1, 2]
  def f():
      return a
  f()[0] = 0
  print(a)
  # output: [0, 2]
  ```

- 存放元素到容器中也一样，容器可赋值的地方都是广义的变量，也就都是指针：

  ```python
  a = []
  x = [0, 1]
  a.append(x) # a[-1]指向x指向的对象，不会copy一份x
  x[1] = 2
  print(a[0][1])
  # output: 2
  ```

`for item in comtainer`循环中，`item`也是指向`contain`的一个元素指向的对象。

赋值（其他情形也一样）后更改变量导致的行为则和变量类型是否可变有关：

> A class is immutable if each **object** of that class has a fixed value upon instantiation that cannot subsequently be changed. For example, the float class is immutable. Once an instance has been created, its value cannot be changed (although an **identifier** referencing that object can be reassigned to a different value).
>
> *Data Structures and Algorithms in Python*

immutable or mutable 是针对 object 而言的，而非 identifier，immutable 指的是 identifier 指向的对象不可 mutate，赋值只是重新指向，不是 mutate。

在使用`*`运算符重复列表时，重复的元素是原始列表中相同对象的引用。这一点在处理可变对象（如列表）时尤其重要，因为修改一个地方会影响到其他引用相同对象的地方。