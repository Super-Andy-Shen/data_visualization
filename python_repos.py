from asyncio.staggered import staggered_race
import requests
import json
url ='https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept':'application/vnd.github.v3+json'}
r = requests.get(url,headers=headers)
print(f"Status code:{r.status_code}")

response_dict = r.json()
github_api ="github_api.json"
with open(github_api,'w') as f:
    json.dump(response_dict,f,indent=4)
print(f"Total repositories:{response_dict['total_count']}")

repo_dicts = response_dict['items']
print(f"Repositories returned:{len(repo_dicts)}")

repo_dict = repo_dicts[0]
#print(f"\nKeys:{len(repo_dict)}")
#for key in sorted(repo_dict.keys()):
#   print(key)
#print(response_dict.keys())

print("\nSelected info :")
print(f"Name:{repo_dict['name']}")
print(f"Owner:{repo_dict['owner']['login']}")
print(f"Stars:{repo_dict['stargazers_count']}")
print(f"Repository:{repo_dict['html_url']}")
print(f"Created:{repo_dict['created_at']}")
print(f"updated:{repo_dict['updated_at']}")
print(f"Description:{repo_dict['description']}")