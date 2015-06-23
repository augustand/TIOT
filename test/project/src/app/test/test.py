# print "567##fcf".split("##")[-1] == "fcf"

class Hello():
    def __init__(self):
        print repr(self)+"##"+self.__class__.__name__
    pass

# print Hello().__class__.__name__

list = []
list.append(Hello())
list.append((Hello()))
print list
print list[0] == list[1]


# ss={"hello":1}
# print ss["hello"]

# print "cc".__class__.__name__
# print [].__class__.__name__

# print repr(" 22 32 11 22 44".replace(" ","\x"))

print repr(str(bytearray.fromhex("FF FF F1 06 07 F0")))