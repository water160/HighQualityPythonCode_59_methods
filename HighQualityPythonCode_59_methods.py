import os
from urllib.parse import parse_qs


"""
《编写高质量Python代码的59个有效方法》——总结
"""

'''
第1章 用Pythonic方式来思考
'''
class HighQuality_1:
    """ 第1条：确认自己所用的Python版本
    """


class HighQuality_2:
    """ 第2条：遵循PEP 8风格指南
    """


class HighQuality_3:
    """ 第3条：了解bytes、str与unicode的区别
    3.1 Python3中：bytes是一种包含8位值的序列，str是一种包含Unicode字符的序列
    3.2 Python2中：str是一种包含8位值的序列，unicode是一种包含Unicode字符的序列
    3.3 保障操作的字符类型一致，要么是二进制流，要么是unicode字符序列；默认读写文件会使用unicode字符序列接收，读写时会使用二进制流操作，因此使用'wb'模式
    """


class HighQuality_4:
    """ 第4条：用辅助函数来取代复杂的表达式
    """
    def __init__(self):
        my_values = parse_qs("red=5&blue=0&green=", keep_blank_values=True)
        print("my_values: {}".format(repr(my_values)))
        
        blank = my_values.get('green', [''])[0]
        print("if string/list is null, then return False: {}".format(blank))
        
        green = self.get_first_int(my_values, 'green')
        print("default green is blank, now is : {}".format(green))

    def get_first_int(self, values, key, default=0):
        found = values.get(key, [''])
        if found[0]:
            found = int(found[0])
        else:
            found = default
        return found


class HighQuality_5:
    """ 第5条：了解切割序列的方法
    5.1 start或end索引产生越界不会报错，例如：first_twenty_items = a[:20]，限定输入序列的最大长度
    5.2 访问列表中的单个元素时，下标越界会报错，导致异常，例如：a[20]
    5.3 原列表切割后会产生一个全新的列表，例如：b = a[4:]，b为一个全新列表，在b上修改不会影响a
    5.4 对列表赋值时，如果使用切片操作，会把原列表在切片相关范围内的值替换成新值，且长度不同依然可以替换，例如：a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], a[2:7] = [99, 22, 14], print(a)打印结果为：a = ['a', 'b', 99, 22, 14, 'h']
    """


class HighQuality_6:
    """ 第6条：在单次切片操作内，不要同时指定start、end和stride
    6.1 单次切片操作内，不同时使用start, end, stride；如果确实需要执行这种操作，一般拆解为两条复制语句（步进切割+范围切割或反过来），提高程序可读性；如果内存用量很严格，不能使用两阶段切割法，则参考itertools模块中的islice方法
    6.2 尽量使用stride为正数，且不带start或end索引的切割操作，避免使用负数做为stride
    """


class HighQuality_7:
    """ 第7条：用列表推导式来取代map和filter
    由于需要采用lambda表达式，导致map和filter可读性较差
    """


class HighQuality_8:
    """ 第8条：不要使用含有两个以上表达式的列表推导
    建议使用if语句 + for循环替代，提高程序可读性
    """


class HighQuality_9:
    """ 第9条：用生成器表达式来改写数据量较大的列表推导
    """
    def __init__(self):
        list_number_ten = ['1','2','3','4','5','6','7','8','9','10']
        value = [len(x) for x in list_number_ten]
        print(value)

        # define the iterator
        it = (len(x) for x in list_number_ten)
        print("iterator is :", it)
        print(next(it))
        print(next(it))
        # define another iterator
        roots = ((x, x**0.5) for x in it)
        # 外围的迭代器前进时，会推动内部迭代器，使得执行循环、评估条件表达式、对接输入输出的逻辑都组合在一起
        print(next(roots))


class HighQuality_10:
    """ 第10条：尽量用enumerate取代range
    10.1 enumerate可以将各种迭代器包装为生成器，可以在遍历迭代器时获取每个元素的索引，便于输出；其中生成器每次产生一对输出值，前者表示循环下表，后者表示从迭代器中获取到的元素
    10.2 尽量用enumerate改写使用range与下标访问相结合的遍历方式
    10.3 可以给enumerate函数提供第二个参数，指定计数的初始值（默认为0）
    """
    def __init__(self):
        flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
        # 直接迭代flavor_list
        for flavor in flavor_list:
            print("%s is delicious" % flavor)
        # 使用range进行下标获取迭代
        for i in range(len(flavor_list)):
            flavor = flavor_list[i]
            print('%d: %s' % (i + 1, flavor))
        # 使用Python内置的enumerate遍历
        for i, flavor in enumerate(flavor_list):
            print('%d: %s' % (i + 1, flavor))
        # 可以指定enumerate函数计数的初始值，例如从10开始
        for i, flavor in enumerate(flavor_list, 10):
            print('%d: %s' % (i, flavor))


class HighQuality_11:
    """ 第11条：用zip函数同时遍历两个迭代器
    """


class HighQuality_12:
    """ 第12条：不要在for和while循环后面写else块
    """


class HighQuality_13:
    """ 第13条：合理利用try / except / else / finally结构中的每个代码块
    """


'''
第2章 函数
'''
class HighQuality_14:
    """ 第14条：尽量用异常来表示特殊情况，而不要返回None
    """


class HighQuality_15:
    """ 第15条：了解如何在闭包里使用外围作用域中的变量
    """


class HighQuality_16:
    """ 第16条：考虑用生成器来改写直接返回列表的函数
    """


class HighQuality_17:
    """ 第17条：在参数上面迭代时，要多加小心
    """


class HighQuality_18:
    """ 第18条：用数量可变的位置参数减少视觉杂讯
    """


class HighQuality_19:
    """ 第19条：用关键字参数来表达可循啊的行为
    """


class HighQuality_20:
    """ 第20条：用None和文档字符串来描述具有动态默认值的参数
    """


class HighQuality_21:
    """ 第21条：用只能以关键字形式指定的参数来确保代码明晰
    """


'''
第3章 类与继承
'''
class HighQuality_22:
    """ 第22条：尽量用辅助类来维护程序的状态，而不要用字典和元组
    """


class HighQuality_23:
    """ 第23条：简单的接口应该接受函数，而不是类的实例
    """


class HighQuality_24:
    """ 第24条：用@classmethod形式的多态去通用地构建对象
    """


class HighQuality_25:
    """ 第25条：用super初始化父类
    """


class HighQuality_26:
    """ 第26条：只在使用Mix-in组件制作工具类时进行多重继承
    """


class HighQuality_27:
    """ 第27条：多用public属性，少用private属性
    """


class HighQuality_28:
    """ 第28条：继承collections.abc以实现自定义的容器类型
    """


'''
第4章 元类及属性
'''
class HighQuality_29:
    """ 第29条：用纯属性取代get和set方法
    """


class HighQuality_30:
    """ 第30条：考虑用@property来替代属性重构
    """


class HighQuality_31:
    """ 第31条：用描述符来改写需要服用的@property方法
    """


class HighQuality_32:
    """ 第32条：用__getattr__、__getattribute__和__setattr__实现按需生成的属性
    """


class HighQuality_33:
    """ 第33条：用元类来验证子类
    """


class HighQuality_34:
    """ 第34条：用元类来注册子类
    """


class HighQuality_35:
    """ 第35条：用元类来注解类的属性
    """


'''
第5章 并发与并行
'''
class HighQuality_36:
    """ 第36条：用subprocess模块来管理子进程
    """


class HighQuality_37:
    """ 第37条：可以用线程来执行阻塞式I/O，但不要用它做平行计算
    """


class HighQuality_38:
    """ 第38条：在线程中使用Lock来防止数据竞争
    """


class HighQuality_39:
    """ 第39条：用Queue来协调各线程之间的工作
    """


class HighQuality_40:
    """ 第40条：考虑用协程来并发地运行多个函数
    """


class HighQuality_41:
    """ 第41条：考虑用concurrent.futures来实现真正的平行计算
    """


'''
第6章 内置模块
'''
class HighQuality_42:
    """ 第42条：用funtools.wraps定义函数修饰器
    """


class HighQuality_43:
    """ 第43条：考虑以contextlib和with语句来改写可复用的try / finally代码
    """


class HighQuality_44:
    """ 第44条：用copyreg实现可靠的pickle操作
    """


class HighQuality_45:
    """ 第45条：应该用datetime模块来处理本地时间，而不是用time模块
    """


class HighQuality_46:
    """ 第46条：使用内置算法与数据结构
    """


class HighQuality_47:
    """ 第47条：在重视精确度的场合，应该使用decimal
    """


class HighQuality_48:
    """ 第48条：学会安装由Python开发者社区所构建的模块
    """


'''
第7章 协作开发
'''
class HighQuality_49:
    """ 第49条：为每个函数、类和模块编写文档字符串
    """


class HighQuality_50:
    """ 第50条：用包来安排模块，并提供稳固的API
    """


class HighQuality_51:
    """ 第51条：为自编的模块定义根异常，以便将调用者与API相隔离
    """


class HighQuality_52:
    """ 第52条：用适当的方式打破循环依赖关系
    """


class HighQuality_53:
    """ 第53条：用虚拟环境隔离项目，并重建其依赖关系
    """


'''
第8章 部署
'''
class HighQuality_54:
    """ 第54条：考虑用模块级别的代码来配置不同的部署环境
    """


class HighQuality_55:
    """ 第55条：通过repr字符串来输出调试信息
    """


class HighQuality_56:
    """ 第56条：用unittest来测试全部代码
    """


class HighQuality_57:
    """ 第57条：考虑用pdb实现交互调试
    """


class HighQuality_58:
    """ 第58条：先分析性能，然后再优化
    """


class HighQuality_59:
    """ 第59条：用tracemalloc来掌握内存的使用及泄露情况
    """


if __name__ == "__main__":
    # high_quality_1 = HighQuality_1()
    # high_quality_2 = HighQuality_2()
    # high_quality_3 = HighQuality_3()
    # high_quality_4 = HighQuality_4()
    # high_quality_5 = HighQuality_5()
    # high_quality_6 = HighQuality_6()
    # high_quality_7 = HighQuality_7()
    # high_quality_8 = HighQuality_8()
    # high_quality_9 = HighQuality_9()
    high_quality_10 = HighQuality_10()
    # high_quality_11 = HighQuality_11()
    # high_quality_12 = HighQuality_12()
    # high_quality_13 = HighQuality_13()
    # high_quality_14 = HighQuality_14()
    # high_quality_15 = HighQuality_15()
    # high_quality_16 = HighQuality_16()
    # high_quality_17 = HighQuality_17()
    # high_quality_18 = HighQuality_18()
    # high_quality_19 = HighQuality_19()
    # high_quality_20 = HighQuality_20()
    # high_quality_21 = HighQuality_21()
    # high_quality_22 = HighQuality_22()
    # high_quality_23 = HighQuality_23()
    # high_quality_24 = HighQuality_24()
    # high_quality_25 = HighQuality_25()
    # high_quality_26 = HighQuality_26()
    # high_quality_27 = HighQuality_27()
    # high_quality_28 = HighQuality_28()
    # high_quality_29 = HighQuality_29()
    # high_quality_30 = HighQuality_30()
    # high_quality_31 = HighQuality_31()
    # high_quality_32 = HighQuality_32()
    # high_quality_33 = HighQuality_33()
    # high_quality_34 = HighQuality_34()
    # high_quality_35 = HighQuality_35()
    # high_quality_36 = HighQuality_36()
    # high_quality_37 = HighQuality_37()
    # high_quality_38 = HighQuality_38()
    # high_quality_39 = HighQuality_39()
    # high_quality_40 = HighQuality_40()
    # high_quality_41 = HighQuality_41()
    # high_quality_42 = HighQuality_42()
    # high_quality_43 = HighQuality_43()
    # high_quality_44 = HighQuality_44()
    # high_quality_45 = HighQuality_45()
    # high_quality_46 = HighQuality_46()
    # high_quality_47 = HighQuality_47()
    # high_quality_48 = HighQuality_48()
    # high_quality_49 = HighQuality_49()
    # high_quality_50 = HighQuality_50()
    # high_quality_51 = HighQuality_51()
    # high_quality_52 = HighQuality_52()
    # high_quality_53 = HighQuality_53()
    # high_quality_54 = HighQuality_54()
    # high_quality_55 = HighQuality_55()
    # high_quality_56 = HighQuality_56()
    # high_quality_57 = HighQuality_57()
    # high_quality_58 = HighQuality_58()
    # high_quality_59 = HighQuality_59()
    pass