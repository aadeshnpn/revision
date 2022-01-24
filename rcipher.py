def rotationalCipher(input, rotation_factor):
  # Write your code here
  capA = ord('A')
  capZ = ord('Z')
  smallA = ord('a')
  smallZ = ord('z')
  output = ''
  print(input, rotation_factor)
  for i in input:
    if i.isnumeric():
      newval = int(i)+ rotation_factor % 10
      if newval >9:
        val = str(newval % 10)
      else:
        val = str(newval)
    elif i.isalpha():
      if i.isupper():
        newval = ord(i) + rotation_factor %26
        if newval > capZ:
          val = chr(capA-1 + (newval % capZ))
        else:
          val = chr(newval)
      else:
        newval = ord(i) + rotation_factor%26
        if newval > smallZ:
          val = chr(smallA-1 + (newval % smallZ))
        else:
          val = chr(newval)
    else:
      val = i
    output += val
  return output


## Contiguours Subarray
def count_subarrays(arr):
  # Write your code here
  N = len(arr)
  result = [1] * N
  stack = [-1]

  for i in range(N):
    while len(stack) > 1 and arr[stack[-1]] < arr[i]:
      stack.pop()
    result[i] += i - stack[-1] -1
    stack.append(i)

  stack=[N]
  for i in range(N-1, -1, -1):
    while len(stack) > 1 and arr[stack[-1]] < arr[i]:
      stack.pop()
    result[i] += stack[-1] -i -1
    stack.append(i)

  return result


##Passing Yearbook
def findSignatureCounts(arr):
  # Write your code here
  N = len(arr)
  res = [0] * N
  visited = set()
  for i in range(N):
    if i not in visited:
      j = i
      group = set([i])
      while arr[j]-1 != i:
        j = arr[j]-1
        group.add(j)
      visited.update(group)
      for k in group:
        res[k] = len(group)
  return res


import heapq
# Largest Triple Products

def findMaxProduct(arr):
  # Write your code here
  result = [-1] * len(arr)
  if len(arr) < 2:
    return result
  else:
    last3 = arr[:2]
    # print(last3)
    # last3 = heapq.heapify(first)
    heapq.heapify(last3)
    for i in range(2, len(arr)):
      if arr[i] > heapq.nsmallest(1,last3)[0]:
        if len(last3) >=3:
          heapq.heappop(last3)
        heapq.heappush(last3, arr[i])
      result[i] = last3[0] * last3[1] * last3[2]

  return result


## Balanced Split

def balancedSplitExists(arr):
  # Write your code here
  print(arr)
  sortedarr = sorted(arr)
  leftpsum = [0] * len(arr)
  rightpsum = [0] * len(arr)
  leftpsum[0] = sortedarr[0]
  rightpsum[len(arr)-1] = sortedarr[-1]

  for i in range(1, len(arr)):
    leftpsum[i] = leftpsum[i-1] + sortedarr[i]

  for j in range(len(arr)-2, -1, -1):
    rightpsum[j] = rightpsum[j+1] + sortedarr[j]

  for k in range(len(arr)-1):
    if leftpsum[k] == rightpsum[k+1]:
      if sortedarr[k] < sortedarr[k+1]:
        return True

  return False


## Magical candy bags

import math
def maxCandies(arr, k):
  # Write your code here
  # print(arr)
  eat = 0
  for i in range(k):
    heapq._heapify_max(arr)
    maxval = heapq.nlargest(1, arr)[0]
    # print(i, maxval)
    eat += maxval
    redval = math.floor(maxval/2)
    # print(redval)
    heapq.heappop(arr)
    heapq.heappush(arr, redval)
    # print(arr)
  return eat


## Encrypted Words

def findmiddle(R, s):
  if len(s) ==1:
    R.append(s)
  elif len(s) > 1:
    if len(s) % 2 ==0:
      mididx = (len(s)//2) -1
    else:
      mididx = int(len(s)//2)

    findmiddle(R, s[mididx])
    findmiddle(R, s[:mididx])
    findmiddle(R, s[mididx+1:])

def findEncryptedWord(s):
  # Write your code here
  R = []
  findmiddle(R, s)

  return ''.join(R)