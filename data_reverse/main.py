import numpy

def data_reverse(data):
    if not data: return []
    result = []
    for byte in (numpy.array_split(data, (len(data) // 8))[::-1]):
        for bit in byte:
            result.append(bit)
    
    return result
            

def data_reverse_refactored(data):
  res = []
  
  for i in range(len(data)-8, -1, -8):
    res.extend(data[i:i+8])
  
  return res
     
        
    
