import os


def find_directory(path: str) -> str:
    if os.path.isdir(path):
        return path
    elif os.path.exists(path):
        return os.path.dirname(path)
    else:
        parent_dir = os.path.dirname(path)

        if parent_dir == path:
            return ""
        else:
            return find_directory(parent_dir)


def assert_path(path: str):
    assert os.path.exists(path), "Entered path does not exist."
    assert os.path.isdir(path), f"Entered path is not a directory. Did you mean '{find_directory(path)}'?"


class PyStructure:
    def __init__(self, root_dir, ignores=None, use_gitignore=False):
        self.root_dir = root_dir
        self.ignores = ignores if ignores else []
        self.use_gitignore = use_gitignore

        if self.use_gitignore:
            self.ignores.extend(self._parse_gitignore())

    def _parse_gitignore(self):
        gitignore_path = os.path.join(self.root_dir, '.gitignore')
        ignore_list = ['.git']
        if os.path.exists(gitignore_path):
            with open(gitignore_path, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        if line.endswith("/"):
                            line = line[:-1]
                        ignore_list.append(line)
        return ignore_list

    def _should_ignore(self, path):
        relative_path = os.path.relpath(path, self.root_dir)
        for ignore in self.ignores:
            if ignore == relative_path or relative_path.startswith(ignore + os.sep):
                return True
        return False

    def _get_filtered_structure(self, current_dir):
        structure = []
        for item in sorted(os.listdir(current_dir)):
            path = os.path.join(current_dir, item)
            if not self._should_ignore(path):
                structure.append((item, path))
        return structure

    def _print_structure(self, current_dir, prefix=""):
        structure = self._get_filtered_structure(current_dir)
        for count, (item, path) in enumerate(structure):
            connector = "└── " if count == len(structure) - 1 else "├── "
            print(f"{prefix}{connector}{item}")

            if os.path.isdir(path):
                extension = "    " if count == len(structure) - 1 else "│   "
                self._print_structure(path, prefix + extension)

    def show_structure(self):
        print(f"Structure of '{self.root_dir}':")
        self._print_structure(self.root_dir)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Show project structure.')
    parser.add_argument('root_dir', type=str, help='Root directory of the project')
    parser.add_argument('--ignore', type=str, nargs='*', default=[], help='List of files or directories to ignore')
    parser.add_argument('--use-gitignore', action='store_true', help='Ignore directories and files from .gitignore')

    args = parser.parse_args()

    assert_path(args.root_dir)

    project = PyStructure(args.root_dir, args.ignore, args.use_gitignore)
    project.show_structure()
