# patterns


def pattern(a, b, c, case):
    match case:
        # AはBの何倍
        case 1:
            print(a / b)

        # AはBの何%
        case 2:
            print((a * b) * 100)

        #Aに占めるBの割合何%
        case 3:
            print((b / a) * 100)

        #AからBにかけての増加率
        case 4:
            print((b / a) + 1)

        #AからBにかけての減少率
        case 5:
            print((b / a) - 1)

        #AのB%はいくつ
        case 6:
            print(a * (b / 100))

        #AがBのC倍の時、Bはいくつ鬱
        case 7:
            print(a / c)

        #AがBのC%の時、Bはいくつ鬱
        case 8:
            print(a / (c / 100))

        #AからB%増加するといくつ
        case 9:
            print(a * (1 + (b / 100)))

        #AからB%減少するといくつ
        case 10:
            print(a * (1 - (b / 100)))

        #Aを１として時のB
        case 11:
            print(b / a)

        #Aを１00として時のB
        case 11:
            print((b / a) * 100)

        #AをCとした時のB
        case 11:
            print((b / a) * c)


pattern(670, 742, 0, 1)