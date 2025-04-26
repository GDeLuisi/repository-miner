import subprocess
from math import floor,ceil
from typing import Iterable

def execute_command(command:str)->str:
    return subprocess.check_output(command,shell=True,text=True)

def create_batches(it:Iterable,n:int)->Iterable[Iterable]:
    if not n:
        raise ValueError("n must be at least 1")
    if not it:
        raise ValueError("Iterable cannot be None or empty")
    batches=[]
    tmp=list(it)
    n_items=len(tmp)
    if n_items==0:
        raise ValueError("Iterable must not be empty")
    n_batches=ceil(n_items/n)
    for i in range(0,n_items,n):
        batches.append(tmp[i:i+n])
    return tuple(batches)