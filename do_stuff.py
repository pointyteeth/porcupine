import urllib2
import json

user = raw_input()
#user = 'gausanka'

x = urllib2.urlopen("https://api.github.com/users/" + user).read()
repos = urllib2.urlopen("https://api.github.com/users/" + user + "/repos").read()

x = json.loads(x)
repos = json.loads(repos)

a = {}
a['user'] = user
a['avatar'] = x['avatar_url']
a['followers'] = int(x['followers'])
a['repos'] = []
for i in repos:
    z = {}
    z['name'] = i['name']
    z['description'] = i['description']
    z['url'] = i['url']
    z['size'] = int(i['size'])
    z['watchers_count'] = int(i['watchers_count'])
    z['forks'] = int(i['forks'])
    a['repos'].append(z)
a['total_repo_size'] = sum(z['size'] for z in a['repos'])
a['total_repo_watchers'] = sum(z['watchers_count'] for z in a['repos'])

print json.dumps(a, indent = 4)
   
