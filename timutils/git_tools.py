"""print git versioning info from working directory

written by Travis O'Brien, modified by Timothy W. Hilton
"""
import git


def print_cwd_git_version():
    """print git branch and revision hash from current working directory
    """
    try:
        _repo = git.Repo(search_parent_directories=True)
        _git_sha = _repo.head.object.hexsha
        _git_short_sha = _repo.git.rev_parse(_git_sha, short=7)
        try:
            _git_branch = _repo.active_branch
        except TypeError as e:
            if 'detached' in str(e):
                branch_str = "detached head;"
            else:
                raise
        else:
            branch_str = "On branch {}".format(_git_branch)
        print("{} at rev {}".format(branch_str, _git_short_sha))
    except git.InvalidGitRepositoryError:
        print("No git repository detected.")
