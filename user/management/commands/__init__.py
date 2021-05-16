# from abc import ABC
#
#
# class A(ABC):
#
#     pass
#
#
# def hello(self, name='world'):
#     print(f'hello {name}')
#
#
# # 创建一个新的类型
# # 第一个参数是类型的名称，第二个参数是继承的父类的集合(元祖), 第三个参数是函数名和方法的绑定(字典)
# Hello = type('Hello', (object, ), dict(hello=hello))
#
# print(type(Hello))
#
# h = Hello()
# print(type(h))
#
# h.hello()
#
#
# class ListMetaClass(type):
#
#     def __new__(cls, name, bases, attrs):
#         print('enter')
#         attrs['add'] = lambda self, value: self.append(value)
#         return type.__new__(cls, name, bases, attrs)
#
#
# class MyList(list, metaclass=ListMetaClass):
#     pass
#
#
# mylist = MyList()
# mylist.add(2)
# print(mylist)
#
#
# # 编写一个简单的ORM框架
# class Field(object):
#
#     def __init__(self, name, column_type):
#         self.name = name
#         self.column_type = column_type
#
#     def __str__(self):
#         return f'<{self.__class__.__name__}:{self.name}>'
#
#
# class StringField(Field):
#
#     def __init__(self, name):
#         super(StringField, self).__init__(name, 'varchar(100)')
#
#
# class IntegerField(Field):
#
#     def __init__(self, name):
#         super(IntegerField, self).__init__(name, 'bigint')
#
#
# class ModelMetaClass(type):
#
#     def __new__(cls, name, bases, attrs):
#
#         if name == 'Model':
#             return type.__new__(cls, name, bases, attrs)
#
#         print(f'Found Model {name}')
#
#         mappings = dict()
#
#         for key, value in attrs.items():
#             if isinstance(value, Field):
#                 print('Found mapping: %s ==> %s' % (key, value))
#                 mappings[key] = value
#
#         for k in mappings.keys():
#             attrs.pop(k)
#
#         attrs['__mappings__'] = mappings
#         attrs['__table__'] = name
#
#         return type.__new__(cls, name, bases, attrs)
#
#
# class Model(dict, metaclass=ModelMetaClass):
#
#     def __init__(self, **kwargs):
#         super(Model, self).__init__(**kwargs)
#
#     def __getattr__(self, item):
#         try:
#             return self[item]
#         except KeyError:
#             raise AttributeError(r"'Model' object has no attribute '%s'" % item)
#
#     def __setattr__(self, key, value):
#         self[key] = value
#
#     def save(self):
#         fields = []
#         params = []
#         args = []
#         for k, v in self.__mappings__.items():
#             fields.append(v.name)
#             params.append('?')
#             args.append(getattr(self, k, None))
#         sql = f'insert into {self.__table__} ({",".join(fields)}) values ({",".join(params)})'
#         print('SQL: %s' % sql)
#         print('ARGS: %s' % str(args))
#
#
# class User(Model):
#     # 定义类的属性到列的映射：
#     id = IntegerField('id')
#     name = StringField('username')
#     email = StringField('email')
#     password = StringField('password')
#
# # 创建一个实例：
# u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# # 保存到数据库：
# u.save()
