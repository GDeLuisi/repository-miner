from repository_miner.git import *
from pytest import fixture
from pathlib import Path
@fixture
def git():
    return Git(Path.cwd().as_posix())
def test_any_cmd(git):
    res=git.rev_parse(["HEAD"])
    # print(res)
    
def test_rev_list(git):
    res=git.rev_list("HEAD")
    print([res])
    # print(res.split('\n'))

def test_log(git):
    res=git.log(r"--pretty='format:%ad'","--numstat")
    print([res])

