from vector import Vector

def test(ok, arguments, expected, expected_shape):
    print(f'testing: {arguments}, {expected}')
    print(f'{repr(arguments)}')
    worked = 1
    try:
        v = Vector(arguments)
    except TypeError as e:
        worked = 0
        print(f"Didn't work: {e}")
        #raise(e)
    if (not worked):
        if (not ok):
            print('OKK')
        else:
            print('KKO')
        print()
        return 
    print("vector: ", v)
    if (v.values == expected):
        print("OK")
    else:
        print("KO")
    print(f'Shape: {v.shape} Expected: {expected_shape}')
    if (v.shape == expected_shape):
        print("OK")
    else:
        print("KO")

test(1, [[1.0], [2.0], [3.0]], [1.0, 2.0, 3.0], (3, 1))

test(0, [[]], None, (1, 3))
test(0, [[],[]], None, (1, 3))

test(1, [[1.0, 2.0, 3.0]], [1.0, 2.0, 3.0], (1, 3))
test(1, [[1.0], [2.0], [3.0]], [1.0, 2.0, 3.0], (3, 1))
test(0, [[1.0, 5.0], [2.0], [3.0]], [1.0, 2.0, 3.0], (3, 1))
test(0, [[], [2.0], [3.0]], [1.0, 2.0, 3.0], (3, 1))
test(0, [['a'], [2.0], [3.0]], [1.0, 2.0, 3.0], (3, 1))
test(1, 3, [0.0, 1.0, 2.0], (3, 1))
test(1, (3, 6), [3.0, 4.0, 5.0], (3, 1))

print('\n\n')

def testDotProduct(va, vb, expected):
    vr = Vector.dot(va, vb)

    print(f'dot product between: {va} --- {vb}')
    print(f'result = {vr} expected = {expected}')
    if (vr != expected):
        print("KO")
    else:
        print("OK")

    print("testing transpose")
    shape =  va.shape
    va.T()
    if (shape[0] == va.shape[1] and shape[1] == va.shape[0]):
        print("OK");
    else:
        print("KO");
    print()

v0 = Vector([[0.0, 0.0, 0.0, 0.0]])
v1 = Vector([[1.0, 1.0, 1.0, 1.0]])
v2 = Vector([[2.0, 2.0, 2.0, 2.0]])
v3 = Vector([[1.0, 2.0, 3.0, 4.0]])
v4 = Vector([[2.0, 3.0, 4.0, 5.0]])
v5 = Vector([[2.0, 3.0, 5.0]])

testDotProduct(v0, v1, sum([0.0, 0.0, 0.0, 0.0]))
testDotProduct(v1, v2, sum([2.0, 2.0, 2.0, 2.0]))
testDotProduct(v3, v4, sum([2.0, 6.0, 12.0, 20.0]))

print('sum sub')
print(v1 + v2)
print(v2 - v3)
print('mult')
print(v3 * 3)
print(3 * v3 )
print('div')
print(v4 / 4)
print(4 / v4 )