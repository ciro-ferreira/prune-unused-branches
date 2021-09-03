import re

def filter_names(repo):
    if repo.name.startswith('feature/') or repo.name.startswith('hotfix/'):
        return repo