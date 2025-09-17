def hanoi(n, a, b, c):
    if n == 1:
        print(a, "->", c)
        return
    hanoi(n - 1, a, c, b)
    hanoi(1, a, b, c)
    hanoi(n - 1, b, a, c)
k = input('请输入a柱的盘子数量: ')
num = int(k)
print('将 ',num,' 个盘子从a柱移动到c柱:')
hanoi(num, "a", "b", "c")