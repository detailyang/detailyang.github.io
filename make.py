import json

def toLink(repo):
    return '<a href="{url}">{name}</a>: {desc}'.format(url=repo['url'], name=repo['name'], desc=repo['desc'])

with open('./projects.json') as f:
    repos = json.load(f)
    repos = [r for r in repos if 'zan' not in r['name'] and 'yz' not in r['name']]
    repos = map(toLink, repos)
    projects = "\r\n       ".join(repos)

with open('./contributes.json') as f:
    repos = json.load(f)
    repos = [r for r in repos if 'zan' not in r['name'] and 'yz' not in r['name']]
    repos = map(toLink, repos)
    contributes = "\r\n       ".join(repos)

with open('./index.html.tpl', 'r') as f:
    html = f.read()
    html = html.replace('###PROJECTS###', projects)
    html = html.replace('###CONTRIBUTES###', contributes)
    print(html)

