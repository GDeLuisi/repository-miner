from  dataclasses import dataclass,field
from datetime import date
from time import strptime
from typing import Literal,get_args,Iterable,Optional,Union,Generator,Callable
import json
from pathlib import Path

@dataclass
class Author():
    email:str
    name:str
    commits_authored:list[str]=field(default_factory=lambda: [])
    def __hash__(self):
        return hash(repr(self.name)+repr(self.email))
    def __eq__(self, value):
        if not isinstance(value,Author):
            raise TypeError(f"Expected value of type <Author>, received {type(value)}")
        return self.name==value.name and self.email==value.email
    def __str__(self):
        return f"Name: {self.name} , Email: {self.email}"
    def __repr__(self):
        return  f"Name: {self.name} , Email: {self.email} , Commits: {self.commits_authored}"
    
@dataclass
class CommitInfo():
    commit_hash:str
    abbr_hash:str
    tree:str
    refs:str
    subject:str
    author_name:str
    author_email:str
    date:date
    def __hash__(self):
        return hash(self.commit_hash)
@dataclass
class Head():
    name:str
    hash:str
    def __hash__(self):
        return hash(self.hash)

@dataclass
class Blob():
    hash:str
    name:str
    path:str
    size:int
    def __hash__(self):
        return hash(self.hash)

@dataclass
class Tree():
    hash:str
    def iterate_tree(self):
        raise NotImplementedError()
    def __hash__(self):
        return hash(self.hash)
    
class TreeImpl(Tree):
    def __init__(self,hash:str,iter_function:Callable[...,Generator[Union[Tree,Blob],None,None]]):
        super().__init__(hash)
        self.iter_func=iter_function
    def iterate_tree(self)->Generator[Union[Tree,Blob],None,None]:
        return self.iter_func()