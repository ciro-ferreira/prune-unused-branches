import pdb
import sys

import customFilters
from git import Repo, remote

def pruneBranchs(repo):
    
    # Retrieving repository
    re = Repo(repo)
    # Getting heads
    repo_heads = re.heads 

    # Filter unused branchs
    branch_names = [x for x in map(customFilters.filter_names, repo_heads) if x is not None]
    #remote.delete(Repo, branch_names, force=True)

def delete_branch(branches):
    print("deleting remote branch: %s" % branches.remote_head)
    remote.push(refspec=(":%s" % branches.remote_head)) # remote_head = the branch you want to delete Example: "origin/my-branch"

pruneBranchs(sys.argv[1])