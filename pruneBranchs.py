import os, shutil, sys
from git import *

def clone_repo (remote_url, local_path, branch):
    print("Cloning repo %s" % remote_url)
    if os.path.isdir(local_path) is True:
        shutil.rmtree(local_path)
    Repo.clone_from(remote_url, local_path, branch=branch)

def delete_remote_branches(remote_url, main_branch, branch):
    cur_dir = os.path.dirname(__file__)
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
        # for branch in branches:
        if repo_branch.name.find(branch) >= 0:
            print(f'deleting remote branch: {repo_branch.remote_head}')
            remote.push(refspec=(f':{repo_branch.remote_head}'))

# Usage:
#       $1 = github link to the repo
#       $2 = main branch
#       $3 = branch prefix
delete_remote_branches(sys.argv[1], sys.argv[2], sys.argv[3])
