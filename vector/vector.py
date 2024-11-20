class Vector():
    def __init__(self, values):
        if (type(values) == list):
            self._listInit_(values)
        elif (type(values) == tuple or type(values) == int):
            self._tupleIntInit_(values)
        else:
            raise TypeError("Must provide a list a tuple or an int")

    def _tupleIntInit_(self, values):
        if (isinstance(values, int)):
            self.values = [float(v) for v in range(values)]
            self.shape = (values, 1)
        elif (isinstance(values, tuple)):
            if (not isinstance(values[0], int) or not isinstance(values[1], int) or values[0] > values[1]):
                raise AssertionError("Must provide a tuple of ints (a, b) where a < b")
            self.values = [float(v) for v in range(values[0], values[1])]
            self.shape = (values[1] - values[0], 1)

    def _listInit_(self, values):
        self.shape = (len(values), 0)
        # It's a col
        if (self.shape[0] > 1):
            for v in values: 
                if (not isinstance(v, list) or len(v) != 1 or not isinstance(v[0], float)): 
                    raise TypeError("Must provide a vector of floats with size 1xN or Nx1")
            self.values = [v[0] for v in values]
            self.shape = (self.shape[0], 1);
        # It's a row
        else:
            self.shape = (self.shape[0], len(values[0]))
            if (self.shape[1] == 0):
                raise TypeError("Must provide a vector of floats with size 1xN or Nx1")
            for v in values[0]:
                if (not isinstance(v, float)):
                   raise TypeError("Must provide a vector of floats with size 1xN or Nx1")
            self.values = values[0]

    def __str__(self):
        if (self.shape[0] == 1):
            string = "[["
            string +=  "], [".join([str(v) for v in self.values])
            string += "]]"
        else: 
            string = "[["
            string +=  ", ".join([str(v) for v in self.values])
            string += "]]"
        return (string)
    def __rep__(self):
            return (self.__str__())
    @staticmethod
    def dot(a ,b):
        if (not isinstance(a, Vector) or not isinstance(b, Vector)):
            raise TypeError("Must provide two vectors of the same shape")
        if (a.shape != b.shape):
            raise AssertionError("The vectors must have the same shape")
        result = []
        for x, y in zip(a.values, b.values):
            result.append(x * y)
        v = Vector([result])
        v.shape = a.shape
        return (sum(v.values))
        
    def T(v):
        shape = (v.shape[1], v.shape[0])
        v.shape = shape
    def __add__(A, B):
        result = [float(a + b) for a, b in zip(A.values, B.values)] 
        result = Vector([result])
        result.shape = A.shape
        return (result)
    def __sub__(A, B):
        result = [a - b for a, b in zip(A.values, B.values)] 
        result = Vector([result])
        result.shape = A.shape
        return (result)
    def __mul__(V, n):
        result = [v * n for v in V.values]
        result = Vector([result])
        result.shape = V.shape
        return (result)
    def __rmul__(V, n):
        result = [v * n for v in V.values]
        result = Vector([result])
        result.shape = V.shape
        return (result)
    def __truediv__(V, n):
        result = [v / n for v in V.values]
        result = Vector([result])
        result.shape = V.shape
        return (result)
    def __rtruediv__(V, n):
        result = [v / n for v in V.values]
        result = Vector([result])
        result.shape = V.shape
        return (result)
