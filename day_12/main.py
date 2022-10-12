from math import ceil, log


class Mask(object):
    def __init__(self, mask, by_host_number=False):
        self.mask = []
        self.CIDR = 0

        if by_host_number:
            mask = self.get_mask(mask)

        if type(mask) == type("str"):
            self.mask = mask.split(".")
            self.mask = list(map(int, self.mask))
            self.CIDR = self.CIDR_mask()
        elif type(mask) == type(1):
            self.CIDR = mask
            self.mask = self.decimal_mask()
        elif type(mask) == type([]):
            self.mask = mask
            self.CIDR = self.CIDR_mask()
        else:
            raise ValueError("Mask must be int|str|list")

        if len(self.mask) != 4:
            raise ValueError("Incorrect format")

    def __str__(self):
        return ".".join(map(str, self.mask))

    def CIDR_mask(self) -> int:
        return 30 - self.count_hosts()

    def get_mask(self, hosts: int) -> int:
        return 32 - ceil(log(hosts + 2, 2))

    def decimal_mask(self) -> list:
        M = [0]*4
        i = 0
        mask = self.CIDR
        while mask > 8:
            mask = mask - 8
            M[i] = int(2**8) - 1
            i += 1

        M[i] = int(2**8 - 2**(8-mask))
        return M

    def count_hosts(self):
        hosts = map(lambda x: int(log(256 - x, 2)), self.mask)
        return 2**sum(hosts) - 2

    def get_class(self):
        classes = {
            "A": (0, 8),
            "B": (9, 16),
            "C": (17, 32),
        }

        for key, val in classes.items():
            if val[0] <= self.CIDR <= val[1]:
                return key


if __name__ == "__main__":
    A = Mask(30, True)
    print("mask:", A, f"/{int(A.CIDR)}")
    print("host:", A.count_hosts())
    print("class:", A.get_class())

    B = Mask(8190, True)
    print("\nmask:", B, f"/{int(B.CIDR)}")
    print("host:", B.count_hosts())
    print("class:", B.get_class())

    B = Mask(8)
    print("\nmask:", B, f"/{int(B.CIDR)}")
    print("host:", B.count_hosts())
    print("class:", B.get_class())

