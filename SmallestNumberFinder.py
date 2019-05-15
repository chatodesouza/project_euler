class SmallestNumberFinder:
    print("***** " + "SMALLEST NUMBER THAT CAN BE DIVIDED INTO ALL NUMBERRS BETWEEN X AND Y" + " *****")
    a = int(input("Enter the X value: "))
    # a = 1

    b = int(input("Enter the Y value: "))
    # b = 20
    print("CALCULATING...")
    c = 0
    x = b

    while (c == 0):
        x += 1
        for i in range(a, b + 1):
            if x % i == 0:
                if i == b:
                    c = x
                    print("Smallest number that is divided into any number between " + str(a) + " and " + str(
                        b) + ": " + str(c))
                    break
            else:
                break
