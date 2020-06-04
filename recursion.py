# 递归
# 尾递归？


def tell_what_row(n):
    if n == 1:
        return 1
    return tell_what_row(n-1)+1


# 可以设置的全局变量供递归调用
# deep = 0
# 记录已经计算的数
has_solved_list = {}

def step_count_recursion(n):
    """递归求解台阶问题
    递推公式：f(n) = f(n-1) + f(n-2)
    不要考虑多层级调用，而是要关注当前问题与拆解处理的子问题之间的关系即可
    这个关系就是递推公式展示的关系
    从符合逻辑的角度去看，终止条件设置成f(1)=1,f(2)=2。因为如果设置f(2)=f(1)+f(0)，这样f(0)是1就很奇怪。
    增加一个递归深度限制,并且借此机会实验了python的变量作用域。参考链接：https://www.runoob.com/python3/python3-namespace-scope.html
    """
    # global deep
    # print(id(deep), deep)
    # deep += 1
    global has_solved_list
    if n == 1:
        return 1
    if n == 2:
        return 2

    if n in has_solved_list.keys():
        print(n)
        return has_solved_list[n]

    ret = step_count_recursion(n-1) + step_count_recursion(n-2)
    has_solved_list[n] = ret
    return ret


def step_count(n):
    """上面用递归求解这个问题时，想用一个字典在各个子调用中共享已有的计算结果
    但由于递归编程技巧有限的原因，使用了全局变量进行共享，现在更习惯引入另外一个函数，通过传参可变元素来实现
    """
    solved_list = {}
    return step_count_r(n, solved_list)


def step_count_r(n, solved_list):
    # 递归终止条件，实际上就是斐波那契数列数列，但是这里考虑到实际意义，所以f(0)被认为是无效的
    if n == 1:
        return 1
    if n == 2:
        return 2

    if n in solved_list:
        return solved_list[n]

    res = step_count_r(n - 1, solved_list) + step_count_r(n - 2, solved_list)
    solved_list[n] = res
    return res


def step_count_iteration(n):
    """使用迭代的方式求解
    怎么去设置变量和写出迭代公式：
    设置这样三个变量，并且三者关系为：
    ret = pre + prepre
    对比递归公式：f(n) = f(n-1) + f(n-2)
    f(n+1) = f(n) + f(n-1)
    则ret = pre + prepre
    prepre = pre
    pre = ret
    """
    if n == 1:
        return 1
    if n == 2:
        return 2

    pre = 2
    prepre = 1
    for i in range(0, n-2):
        ret = pre + prepre
        prepre = pre
        pre = ret

    return ret


def test_step_count_iteration():
    print(step_count_iteration(7))


def test_step_count_recursion():
    print(step_count_recursion(7))


if __name__ == "__main__":
    # print(tell_what_row(10))
    # test_step_count_recursion()
    test_step_count_iteration()
    # print(id(deep), deep)
    # print("*******")
    # test_step_count_recursion()
    # print("*******")
    # print(id(deep), deep)
    # a = 1
    # print(id(a), a)
    # a += 1
    # print(id(a), a)
    # lp = [1] * 3
    # print("list: ")
    # print(id(lp), lp)
    # lp[0] = 2
    # print(id(lp), lp)
    print(step_count(7))