class Moon:
    # Basic class to create a moon object that can cycle using __iter__ and __next__
    def __init__(self):
        self.cameFrom = "NEW"
        self.state_n = 0
    def __iter__(self):
        return self
    def __next__(self):
        value = self.evaluateMoonPhase() # on 0 -> new moon or full moon and on 4 -> must be HALF
        self.state_n += self.order()
        return value
    def evaluateMoonPhase(self):
        if not (self.state_n % 8):
            if (self.state_n // 8) % 2:
                self.cameFrom = "FULL"
                return "FULL"
            self.cameFrom = 'NEW'
            return "NEW"
        elif not (self.state_n % 4): return "HALF"
        return self.state_n % 8
    def order(self):
        if self.cameFrom is "NEW": return 1
        elif self.cameFrom is "FULL": return -1
    


if __name__ == "__main__":
    # main test -> change x for higher or lower values of moon cycles
    a = Moon()
    for x,y in enumerate(a):
        print(f"The moon is currently at cycle: {y}. \t|| Time passes....")
        if x == 20: break
