class GitNotFoundException(Exception):
    def __init__(self, *args):
        super().__init__(*args)

class GitCmdError(Exception):
    def __init__(self, *args):
        super().__init__(*args)
    
class NotGitRepositoryError(Exception):
    def __init__(self, *args):
        super().__init__(*args)
