import random


def gen(mail, gmail="@gmail.com"):
    dump = []
    result = mail
    for i in range(random.randrange(1, len(mail)/2)):
        rand = random.randrange(1, len(mail)-1)
        result = result[:rand] + "." + result[rand:]
        dump.append(rand)

    while ".." in result:
        result = result.replace("..", ".")

    result = result + gmail

    return result

