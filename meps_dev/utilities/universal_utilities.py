import json
import os
import pickle


class UniversalUtilityFunctions:
    """ Class that contains utility functions used throughout codebase. Set up as class for easier use of mock
    functions in testing. Contains the following:
        - load_data_from_file: loads pickle or json from path
        - write_data_to_file: writes data as pickle or json to path
    """

    @staticmethod
    def load_data_from_file(file_path, file_format=None, verbosity=0):
        """Loads a data object from a given file path"""

        if file_format:
            full_file_path = f"{file_path}.{file_format}"
        else:
            full_file_path = file_path
            file_format = file_path.split(".")[1]
        if isinstance(full_file_path, str):
            if not os.path.exists(full_file_path):
                raise AssertionError(f"File not found: {full_file_path}")
            opener = open  # can add ability to handle zipped files here
            mode = "rb" if file_format in {"pickle"} else "rt"
            file_reader = opener(full_file_path, mode)
        loaders = {
            "pickle": lambda file_reader: pickle.load(file_reader),
            "json": lambda file_reader: json.load(file_reader),
        }
        data = loaders[file_format](file_reader)
        if verbosity > 2:
            print(f"     File {full_file_path} loaded.")

        return data

    @staticmethod
    def write_data_to_file(data, output_file_path, output_file_format, verbosity=0):
        """ Takes a data object, writes and saves as a pickle or json. """

        full_path = output_file_path + "." + output_file_format
        if isinstance(full_path, str):
            if output_file_format not in {"pickle", "json"}:
                raise ValueError(f"Incompatible file format :{output_file_format}")
            # Create folder if not already present
            folder = os.path.dirname(full_path)
            if folder and not os.path.exists(folder):
                os.makedirs(folder)
            mode = "wb" if output_file_format == "pickle" else "wt"
            file_writer = open(full_path, mode)
        else:
            raise ValueError("full_path must be specified")

        writers = {
            "pickle": lambda file_writer: pickle.dump(data, file_writer, protocol=4),
            "json": lambda file_writer: json.dump(data, file_writer, indent=2),
        }
        writers[output_file_format](file_writer)
        file_writer.close()
        if verbosity > 2:
            print(f"     {full_path} saved.")
