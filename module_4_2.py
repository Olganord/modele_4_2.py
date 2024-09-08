def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()


test_function()


#  inner_function()
""" При попытке вызова вложенной функции в области видимости родительской возникает ошибка:
    имя "inner_function" (вложенной) не определено, Вы имели в виду "test_function" (родительская)?
    module_4_2.py", line 10, in <module>
    inner_function()
    ^^^^^^^^^^^^^^
NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
Process finished with exit code 1"""
