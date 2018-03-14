def foo(k, u, d = {}):
  print(d)
  d[k] = u

foo("asdf", 3)
foo("qwer", 4)
foo("fff", 5)
