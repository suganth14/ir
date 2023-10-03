A = [[0,0,0,1,0,0,0,0],
     [0,0,1,0,1,0,0,0],
     [1,0,0,0,0,0,0,0],
     [0,1,1,0,0,0,0,0],
     [0,1,1,1,0,1,0,0],
     [0,0,1,0,0,0,0,1],
     [1,0,1,0,0,0,0,0],
     [1,0,0,0,0,0,0,0]]

def calculateAuth(auth,hub):
  for j in range(len(A[0])):
    cnt = 0
    for i in range(len(A)):
      if A[i][j] == 1:
        cnt += hub[i]
    auth[j] = cnt
  # normalize
  total = sum(auth)
  auth = [auth[i]/total for i in range(len(auth))]
  return auth

def calculateHub(auth,hub):
  for i in range(len(A)):
    cnt = 0
    for j in range(len(A[0])):
      if A[i][j] == 1:
        cnt += auth[j]
    hub[i] = cnt
  # normalize
  total = sum(hub)
  hub = [hub[i]/total for i in range(len(hub))]
  return hub

def findDiff(arr1,arr2):
  val = 0
  for ele1,ele2 in zip(arr1,arr2):
    val=max(abs(ele1-ele2),val)
  return val

auth = [1]*len(A)
hub = [1]*len(A)

while(True):
  old_hub = hub.copy()
  old_auth = auth.copy()
  newAuth = calculateAuth(auth.copy(),hub.copy())
  newHub = calculateHub(auth.copy(),hub.copy())
  auth = [round(newAuth[i],2) for i in range(len(newAuth))]
  hub = [round(newHub[i],2) for i in range(len(newHub))]
  max_diff1 = findDiff(old_hub,hub)
  max_diff2 = findDiff(old_auth,auth)
  if max_diff1<0.01 and max_diff2<0.01:
    break
print(auth)
print(hub)

