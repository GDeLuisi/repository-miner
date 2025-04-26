from .utility import execute_command
from .helper import cmd_builder,log_builder,rev_list_builder,get_head_commit,is_dir_a_repo,is_git_available
from .exceptions import *
from functools import partial
from typing import Iterable,Optional
from datetime import datetime
class Git():
    def __init__(self,path:str):
        if not is_git_available():
            raise GitNotFoundException("Git not found")
        if not is_dir_a_repo(path):
            raise NotGitRepositoryError(f"Directory {path} is not a git repository")
        self.path=path

    def _execute_command(self,command:str,*args)->str:
        if len(args)==1 and not isinstance(args[0],str) and isinstance(args[0],Iterable):
            return execute_command(cmd_builder(command,self.path,*args[0]))
        return execute_command(cmd_builder(command,self.path,*args))
    
    def __getattr__(self, name:str):
        if name in self.__dict__ or name in self.__class__.__dict__:
            return getattr(self,name)
        name=name.replace("_","-")
        return partial(self._execute_command,name)