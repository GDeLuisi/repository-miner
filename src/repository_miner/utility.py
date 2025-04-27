import subprocess
from math import floor,ceil
from typing import Iterable

def execute_command(command:str)->str:
    return subprocess.check_output(command,shell=True,text=True).strip()

def create_batches(it:Iterable,n:int)->Iterable[Iterable]:
    """create batches of n items for batch using the items in the iterable

    Args:
        it (Iterable): iterable from which batches are created
        n (int): number of items for each batch

    Raises:
        ValueError: If iterable is empty or None and if the number of items for batch is not correct

    Returns:
        Iterable[Iterable]: Iterable containing the batches
    """
    if not n:
        raise ValueError("n must be at least 1")
    if not it:
        raise ValueError("Iterable cannot be None or empty")
    batches=[]
    tmp=list(it)
    n_items=len(tmp)
    if n_items==0:
        raise ValueError("Iterable must not be empty")
    for i in range(0,n_items,n):
        batches.append(tmp[i:i+n])
    return tuple(batches)