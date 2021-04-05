import json
import os
import pickle

import numpy as np


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

    @staticmethod
    def weighted_pct(bool_list, weights):
        """ Takes a list of boolean values and a list of weights associated by index. Returns the percent of the
        weighted population listed a True in the boolean list. """

        numerator = 0
        for val, weight in zip(bool_list, weights):
            numerator += val * weight
        denominator = sum(weights)

        return numerator / denominator * 100

    @staticmethod
    def weighted_average(values_list, weights):
        """ Takes a list of values and a list of weights associated by index. Returns the weighted average of the 
        values. """

        numerator = 0
        for val, weight in zip(values_list, weights):
            numerator += val * weight
        denominator = sum(weights)

        return numerator / denominator

    @staticmethod
    def weighted_median(values_list, weights):
        """ Takes a list of values and a list of weights associated by index. Returns the weighted median of the 
        values. """
        values_list, weights = np.array(values_list).squeeze(), np.array(weights).squeeze()
        s_values_list, s_weights = map(np.array, zip(*sorted(zip(values_list, weights))))
        midpoint = 0.5 * sum(s_weights)
        if any(weights > midpoint):
            w_median = (values_list[weights == np.max(weights)])[0]
        else:
            cs_weights = np.cumsum(s_weights)
            idx = np.where(cs_weights <= midpoint)[0][-1]
            if cs_weights[idx] == midpoint:
                w_median = np.mean(s_values_list[idx : idx + 2])
            else:
                w_median = s_values_list[idx + 1]
        return w_median

    @staticmethod
    def weighted_quantiles(values_list, quantiles, sample_weight=None):
        """ Takes an list of values, a list of quantiles to generate, and a list of weights corresponding to values.
        Identifies the value splitting the quantile within the weighted distribution. Returns a dictionary of quantiles
        and their associated values. """

        values_list = np.array(values_list)
        quantiles = np.array(quantiles)
        if sample_weight is None:
            sample_weight = np.ones(len(values_list))
        sample_weight = np.array(sample_weight)

        assert np.all(quantiles >= 0) and np.all(quantiles <= 1), "quantiles should be in [0, 1]"

        sorter = np.argsort(values_list)
        values_list = values_list[sorter]
        sample_weight = sample_weight[sorter]

        weighted_quantiles = np.cumsum(sample_weight) - 0.5 * sample_weight
        weighted_quantiles /= np.sum(sample_weight)
        quantile_values = np.interp(quantiles, weighted_quantiles, values_list)

        return {quan: val for quan, val in zip(quantiles, quantile_values)}
