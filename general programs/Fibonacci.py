def fibonacci (n):
  if n <= 1:
    return n
  return fibonacci(n-1) + fibonacci (n-2)
x = 3
print(f'o fibonacci de pos {x} eh: {fibonacci(x)}')
print(f'o fibonacci de pos {7} eh: {fibonacci(7)}')