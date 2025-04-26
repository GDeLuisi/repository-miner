from repository_miner.git import *
from repository_miner import RepoMiner
from pytest import fixture
from pathlib import Path
@fixture
def git():
    return RepoMiner(Path.cwd().as_posix())

def test_log(git):
    res=git.log()
    print(res)