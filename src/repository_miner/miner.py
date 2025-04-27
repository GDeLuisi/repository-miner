from .git import Git
from .utility import execute_command
from .helper import cmd_builder,log_builder,rev_list_builder,get_head_commit,is_dir_a_repo,is_git_available
from .exceptions import *
from .data_typing import *
from functools import partial
from typing import Iterable,Optional,Generator
from datetime import datetime
class RepoMiner():
    def __init__(self,path:str):
        self.git=Git(path)
        self.path=path
        
    def log(self,from_commit:Optional[str]=None,to_commit:Optional[str]=None,pretty:Optional[str]=None,merges:bool=False,max_count:Optional[int]=None,skip:Optional[int]=None,author:Optional[str]=None,follow:Optional[str]=None,since:Optional[datetime]=None,to:Optional[datetime]=None,extra_args:Optional[Iterable[str]]=[])->str:
        if not from_commit:
            from_commit=get_head_commit(self.path)
        return self.git.log(log_builder(self.path,from_commit,to_commit,pretty,merges,max_count,skip,author,follow,since,to,*extra_args))
    
    def rev_list(self,from_commit:Optional[str]=None,to_commit:Optional[str]=None,pretty:Optional[str]=None,merges:bool=False,max_count:Optional[int]=None,skip:Optional[int]=None,author:Optional[str]=None,since:Optional[datetime]=None,to:Optional[datetime]=None,extra_args:Optional[Iterable[str]]=[])->str:
        if not from_commit:
            from_commit=get_head_commit(self.path)
        return self.git.rev_list(rev_list_builder(self.path,from_commit,to_commit,pretty,merges,max_count,skip,author,since,to,*extra_args))
    
    def local_branches(self):
        branches=self.git.branch("-l").split("\n")
        for branch in branches:
            name=branch.strip("*").strip()
            yield Head(name,self.git.rev_parse(name))
    
    def remote_branches(self):
        branches=self.git.branch("-r").split("\n")
        for branch in branches:
            name=branch.strip("*").strip()
            yield Head(name,self.git.rev_parse(name))