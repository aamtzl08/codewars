def filter_list(l):
  return [i for i in l if isinstance(i, int)]

print(filter_list([1,2,'aasf','1','123',123]))