from Chef import Chef

myChef = Chef()
myChef.make_chicken()


class ChineseChef(Chef):

    def make_chinese_dish(self):
        print("The chef makes a chinese dish")


chineseChef = ChineseChef()
chineseChef.make_salad()
chineseChef.make_chinese_dish()