import random
import string


if __name__ == "__main__":
    # todo: 如何增加游戏难度？
    num = random.sample(string.digits, 4)
    times = 50 # 游戏次数 
    while True:
        times -= 1
        a = 0
        b = 0
        user_in = input("请输入4位数字: ")
        if len(user_in) != 4:
            print("请输入4位数字")
            continue
        else:
            for c in user_in:
                if not c.isdigit():
                    print("必须输入数字: `{}` 不是数字".format(c))
                    continue
            
            # todo: 思考有其他方法?
            for index, c in enumerate(user_in):
                if c in num:
                    if num.index(c) == index:
                        a += 1
                    else:
                        b += 1
        if a == 4:
            print("恭喜猜中: 答案是: {}".format("".join(num)))
            break

        if times <= 1:
            print("游戏次数已用完")
            break

        print("猜测结果：{}A{}B, 离成功又近一步了, 加油!!!".format(a, b))