from repository_miner.git import *
from repository_miner import RepoMiner
from repository_miner import execute_command,cmd_builder
from pytest import fixture
from pathlib import Path
from subprocess import check_output
main_path=Path.cwd()
test_path=main_path.parent.joinpath("pandas")
@fixture
def git():
    return RepoMiner(main_path.as_posix())

def test_log(git):
    res=git.retrieve_commits()
    t=check_output(f"git -C {main_path.as_posix()} log --pretty=format:%H",text=True,shell=True).splitlines()
    for i,c in enumerate(res):
        print(c.commit_hash,t[i])
        assert c.commit_hash == t[i]
    
def test_count(git):
    res=git.n_commits()
    t=int(execute_command(cmd_builder("rev-list",main_path.as_posix(),"HEAD","--count")))
    assert t==res
    
def test_local_branches(git):
    res=check_output(f"git -C {main_path.as_posix()} branch -l",text=True,shell=True).split("\n")[:-1]
    res=list(map(lambda a: a.strip("*").strip(),res))
    heads=list(git.local_branches())
    res_hashes=[]
    for hashes in map(lambda a: execute_command(cmd_builder("rev-parse",main_path.as_posix(),a)),res):
        res_hashes.append(hashes)
    assert len(res)==len(heads)
    assert set(res)==set(map(lambda h:h.name,heads))
    assert set(res_hashes)==set(map(lambda h:h.hash,heads))
    for head in heads:
        res=len(check_output(f"git -C {main_path.as_posix()} log {head.name} --pretty='format:%h'",text=True,shell=True).splitlines())
        assert res==len(list(head.traverse_commits()))

def test_tree(git):
    tree = git.tree("HEAD")
    t=check_output(f"git -C {main_path.as_posix()} ls-tree HEAD -r -t --format=%(objectname)",text=True,shell=True).split("\n")[:-1]
    t.sort()
    traverse=list(tree.traverse())
    traverse.sort(key=lambda a:a.hash)
    t_hash=[i.hash for i in traverse]
    assert t_hash  == t
        
def test_author(git):
    git.authors()