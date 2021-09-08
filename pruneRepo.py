import os, shutil, sys
from git import *

def clone_repo (remote_url, local_path, branch):                               # Clone a remote repo
    print("Cloning repo %s" % remote_url)
    if os.path.isdir(local_path) is True:
        shutil.rmtree(local_path)
    Repo.clone_from(remote_url, local_path, branch=branch)

def delete_remote_branches(remote_url, main_branch, branches):
    cur_dir = os.path.dirname(__file__)
    # local_path="%s/%s" % (cur_dir, 'repoToPrune')
    local_path=f'{cur_dir}/repoToPrune'

    clone_repo(
        remote_url=remote_url,
        local_path=local_path,
        branch=main_branch
    )
    repo = Repo(local_path)                  
    assert not repo.bare   
    remote = repo.remote()
    for repo_branch in repo.references:
        delete = False   
        for branch in branches:
            if repo_branch.name.find(branch) >= 0:
                delete = True
        if delete:
            print(f'deleting remote branch: {repo_branch.remote_head}')
            remote.push(refspec=(f':{repo_branch.remote_head}'))
            #remote.push(refspec=(":%s" % repo_branch.remote_head))
        

delete_remote_branches('git@github.com:ciro-ferreira/repoToPrune.git', 'release/spiderman', ['hotfix/'])