class RollingHashMap:
    def __init__(self, x, a=7, p=1009):
        self.a = a
        self.seqlen = len(x)
        n = self.seqlen - 1
        self.p = p
        u = 0
        for c in x:
            u += ord(c)*(self.a ** n)
            n -= 1
        self.r = u % p

    def append(self, c):
        self.r = (self.r * self.a + ord(c)) % self.p

    def skip(self, c):
        self.r -= ord(c) * ((self.a**self.seqlen) % self.p)
        self.r = self.r % self.p

    def __str__(self):
        return str(self.r)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.r == other.r


class SubString:
    def __init__(self, string):
        self.string = string

    def substringcheck(self, substring):

        rs = RollingHashMap(x=substring)
        rt = RollingHashMap(x=self.string[:len(substring)])

        if rt == rs:
            if substring == self.string[:len(substring)]:
                return True

        for i in range(len(substring), len(self.string)):
            rt.append(self.string[i])
            rt.skip(self.string[i - len(substring)])

            if rs == rt:
                if substring == self.string[i-len(substring)+1: i+1]:
                    return True
        return False


if __name__ == '__main__':
    t = "This is a sample text"
    s = "samp"
    h = SubString(string=t)
    print(h.substringcheck(substring=s))

