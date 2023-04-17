def data_reverse(data):
  res = []
  print(data)
  for i in range(len(data)-8, -1, -8):
    res.extend(data[i:i+8])
    print(i)
    print(data[i:i+8])
  
  print()
  print()
  # return res



data = [[1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0], [1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1],[0,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1], [0,0,1,0,1,0,0,1,0,0,1,1,0,1,1,0]]

print([f"{data_reverse(test)}        "for test in data])

