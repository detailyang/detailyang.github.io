import json

def toLink(repo):
    return '<a href="{url}">{name}</a>: {desc}'.format(url=repo['url'], name=repo['name'], desc=repo['desc'])

with open('./projects.json') as f:
    repos = json.load(f)
    repos = map(toLink, repos)
    projects = "\r\n       ".join(repos)

with open('./index.html.tpl', 'rw') as f:
    html = f.read()
    html = html.replace('###PROJECTS###', projects)
    print(html)

