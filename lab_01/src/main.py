import graph as g

def MainMenu():
    print("------------ Меню ---------------")
    print("1 - Равномерное распределение")
    print("2 - Нормальное распределение")
    print("0 - Выйти")

def GraphUniform():
    print("\nВведите отрезок для равномерного распределения: ")
    a = float(input("a = "))
    b = float(input("b = "))

    g.DrawUniformDistrGraphs(a, b)
    
def GraphNormal():
    print("\nВведите отрезок для нормального распределения: ")
    mean = float(input("m = "))
    sigma = float(input("sigma = "))
    
    g.DrawNormalDistrGraphs(mean, sigma)

choice = -1;
while (choice != 0):
    MainMenu()
    choice = int(input("Выбор: "))

    if choice == 1:
        GraphUniform()
    else:
        GraphNormal()