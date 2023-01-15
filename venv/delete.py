import requests as req

# Paste here


headers = {"Authorization": "Bearer {{your token}}"}
for i in repoList:
    print(i)
    req.delete(i, headers=headers)
print('done')
