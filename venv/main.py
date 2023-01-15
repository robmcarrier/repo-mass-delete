import requests as req

headers = {"Authorization": "Bearer {{your token}}"}
r = req.get("https://api.github.com/users/{{your username}}/repos?per_page=100", headers=headers)
json_response = r.json()
repoList = []

for i in json_response:
    name = ''
    try:
        name = i['name']
    except:
        continue
    #     The repos I wanted to delete all end with 000
    if name.endswith('000'):
        repoList.append('\'https://api.github.com/repos/{{your username}}/' + i['name'] + "\'")


print('repoList = [' + ', '.join(repoList) + ']')
