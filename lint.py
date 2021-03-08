import sys
import os
import subprocess
import pycodestyle


class LinterFormatter:
    """ Automates linting and formatting of directory:
        Steps:
            pycodestyle: for checking the style
            pyflakes: for fast static analysis.
            black: for formatting
            pylint: for everything else.
    """

    def __init__(self):
        """ Defines files and folders to ignore """
        self.files_to_exclude = {"pylintrc", "pycodestyle", "black", "chromedriver"}
        self.folders_to_exlude = {".git", "__pycache__", "migrations"}

    def run_script(self, argv):
        """ Primary Entry point of MyLinter """

        if argv == "lint":
            sources = self.collect_sources()
            self.run_pyflakes(sources=sources)
            self.run_pycodestypes(sources=sources)
            self.run_pylint(sources=sources)
        elif argv == "format":
            sources = self.collect_sources()
            self.run_black(sources=sources)
        elif argv == "git_actions":
            sources = self.collect_sources()
            self.run_pyflakes(sources=sources)
            self.run_pylint(sources=sources)
        elif not argv:
            sources = self.collect_sources()
            self.run_black(sources=sources)
            self.run_pyflakes(sources=sources)
            self.run_pycodestypes(sources=sources)
            self.run_pylint(sources=sources)

    def collect_sources(self):
        """ Parses through current directory and returns all absolute file paths of files not excluded by:
        files_to_exclude, folders_to_exlude
        """
        root_dir = os.getcwd()
        sources = []
        for subdir, dirs, files in os.walk(root_dir):  # pylint: disable=unused-variable
            current_dir = subdir.replace(root_dir, "")
            if not any(folder in current_dir for folder in self.folders_to_exlude):
                for file in files:
                    if file not in self.files_to_exclude:
                        file_name_list = file.split(".")
                        if file_name_list[1] == "py":
                            sources.append(os.path.join(subdir, file))
        return sources

    @staticmethod
    def run_pycodestypes(sources):
        """ Takes a list of absolute file paths, checks files against some of the style conventions in PEP 8"""
        print("Checking for Style")
        pycodestyle.StyleGuide(
            ignore=["E203", "W503", "E402", "E266", "E231", "W291"], max_line_length=119
        ).check_files(sources)

    @staticmethod
    def run_black(sources):
        """ Takes a list of absolute file paths, auto formats code """
        print("Auto Formating ")
        cmd = ["black", "-l 119"]
        cmd.extend(sources)
        subprocess.call(cmd)

    @staticmethod
    def run_pyflakes(sources):
        """ Takes a list of absolute file paths, checks source code for errors """
        print("Checking for Errors")
        cmd = ["pyflakes"]
        cmd.extend(sources)
        subprocess.call(cmd)

    @staticmethod
    def run_pylint(sources):
        """ Takes a list of absolute file paths, checks for linting errors """
        print("Checking for Linting Errors ")
        cmd = ["pylint"]
        cmd.extend(sources)
        subprocess.call(cmd)


if __name__ == "__main__":
    mylint = LinterFormatter()
    if len(sys.argv) > 1:
        mylint.run_script(sys.argv[1])
    else:
        mylint.run_script(None)
