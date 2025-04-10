import random

stream = [random.randint(1, 9) for _ in range(23)]
n = len(stream)

def count_occurence(stream, pos):
  element = stream[pos-1]
  return sum(1 for elem in stream[pos-1:] if elem == element)

x0 = random.randint(1, n)
x1 = random.randint(1, n)
x2 = random.randint(1, n)

data = {'x': [x0, x1, x2], 'x.ele': [stream[x0-1], stream[x1-1], stream[x2-1]]}
data['x.val'] = [count_occurence(stream, x) for x in data['x']]
data['n(2*x.val-1)'] = [n * (2*val-1) for val in data['x.val']]
average = sum(data['n(2*x.val-1)']) / len(data['n(2*x.val-1)'])

import pandas as pd
print(pd.DataFrame(data))
print("Result = ", average)