# function is a first class object

def double_decker():
    print('starting double decker')

    def inner_func():
        print('inside the inner function')
        return 400
    return inner_func

# print(double_decker())
# print('\n')
# print(double_decker()())


def do_something(work):
    print('work started')
    # print(work)
    work()
    print('work ended')

# do_something('doing assignment')

def coding():
    print('solving problems')

do_something(coding)