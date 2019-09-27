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
        _git_branch = _repo.active_branch
        print("On branch {} at rev {}".format(_git_branch, _git_short_sha))
    except git.InvalidGitRepositoryError:
        print("No git repository detected.")
