# 找出近似解的方法就是使用贪婪算法，贪婪算法的概念就是选择最好的物品，最好可能是 重量最大、价值最大、或者是 价值重量比 最大。
# 所以贪婪算法，需要我们根据选择的"最好"方式进行多次测试
# 我们需要根据选择的"最好"方式，对数据进行排序，然后计算在阈值范围内最优解

class Item(object):

    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def get_weight(self):
        return self.weight

    def __repr__(self):
        return f"{self.name}:{self.weight}:{self.value}"


def value(item):
    return item.get_value()


def weight_inverse(item):
    return 1 / item.get_weight()


def density(item):
    return item.get_value() / item.get_weight()


# 贪婪算法
def greedy(items, max_weight, sort_func):
    """
    贪婪算法的具体实现
    :param items: 物品列表
    :param max_weight: 最大的阈值
    :param sort_func:  "最好"的方式，也就是排序方法
    :return:
    """

    sorted_items = sorted(items, key=sort_func, reverse=True)
    weight_sum = 0
    max_value = 0
    result = []
    for item in sorted_items:
        weight_sum = weight_sum + item.get_weight()
        if weight_sum > max_weight:
            break
        max_value = max_value + item.get_value()
        result.append(item)
    return result, max_value


if __name__ == "__main__":
    names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer']
    values = [175, 90, 20, 50, 10, 200]
    weights = [10, 9, 4, 2, 1, 20]
    Items = []

    for i in range(len(values)):
        Items.append(Item(names[i], values[i], weights[i]))

    print(greedy(items=Items, max_weight=20, sort_func=value))
    print(greedy(items=Items, max_weight=20, sort_func=weight_inverse))
    print(greedy(items=Items, max_weight=20, sort_func=density))
