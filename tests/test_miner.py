from repository_miner.git import *
from repository_miner import RepoMiner
from repository_miner import execute_command,cmd_builder
from pytest import fixture
from pathlib import Path
from subprocess import check_output
main_path=Path.cwd()
@fixture
def git():
    return RepoMiner(main_path.as_posix())

def test_log(git):
    t=execute_command(cmd_builder("log",main_path.as_posix()))
    res=git.log()
    assert t==res
    # print(res)

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