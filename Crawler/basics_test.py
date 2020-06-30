try:
    a = 1/0
except Exception as e:
    print(e)


def func(b):
    try:
        b = b/0
    except Exception as e:
        print(e)


func(1)
