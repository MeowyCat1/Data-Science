import numpy as np

numbers = [5, 6, 5, 6, 7, 8]
npnumbers = np.array(numbers, float)
print(npnumbers)
print(npnumbers.ndim)
print(npnumbers.shape)
print(npnumbers.size)

twod = np.zeros((5, 5), float)

print(twod)
print(twod.ndim)
print(twod.shape)
print(twod.size)

ones = np.ones((100, 100), float)

print(ones)
print(ones.ndim)
print(ones.shape)
print(ones.size)

fancyarray = np.arange(1, 501, 1)

randomiser = np.random.default_rng()

print(type(fancyarray))
print(fancyarray)

twodfancy = fancyarray.reshape((100,5))

print(np.linspace(0, 999, 12))

print(randomiser.integers(0, 99999, 10))

wibbly = randomiser.permutation(fancyarray)

print(wibbly)

print(randomiser.permutation(twodfancy))

wibbly.sort()
print(wibbly)

print(wibbly / 5)

print((wibbly + 2)[:10])

print(wibbly[299:400:2])