class Fancy:
    MOD = 10**9 + 7
    
    def __init__(self):
        self.seq = []
        self.mul = 1  
        self.add = 0  
        self.history = []  
    def append(self, val: int) -> None:
        # store value with current state
        self.history.append((val, self.mul, self.add))
    
    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD
    
    def multAll(self, m: int) -> None:
        self.mul = (self.mul * m) % self.MOD
        self.add = (self.add * m) % self.MOD
    
    def getIndex(self, idx: int) -> int:
        if idx >= len(self.history):
            return -1
        
        val, mul0, add0 = self.history[idx]
       
        inv_mul0 = pow(mul0, self.MOD - 2, self.MOD)
       
        res = (val * self.mul * inv_mul0 + (self.add - add0 * self.mul * inv_mul0) % self.MOD) % self.MOD
        return res