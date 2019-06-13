from experiment import Experiment
import pandas as pd

class DLExperiment(Experiment):

    def _init_(self, yaml_file=None, meta_data=None, config=None, results=None):
        """

        :param yaml_file:
        :type yaml_file:
        :param meta_data:
        :type meta_data:
        :param config:
        :type config:
        :param results:
        :type results:
        :return:
        :rtype:
        """

        if yaml_file:
            self.parse_yaml(yaml_file)
        elif meta_data:
            '''meta_data is supposed to be dict: {'Name': , 'Description': , 'Run File':, 'Commit':}'''
            assert isinstance(meta_data, dict)
            self.meta_df = pd.DataFrame(meta_data)
        elif config:
            assert isinstance(config, dict)
        elif results:
            assert isinstance(results, dict)
        return

    def __str__(self):

        return 0

    def build_hier_df(self, level1_col_names, level2_dfs):
        """ Utility to restore a 2 level hierarichal indexed df, from many flat dfs

        :param level1_col_names: the higher level columns names
        :type level1_col_names: list of strings
        :param level2_dfs: the data frames to be used to build the 2 level column indexed df
        :type level2_dfs: list of DataFrames
        :return: merged hierarichal data frame
        :rtype: pd.DataFrame
        """
        level1_cols = []
        for level1_col_name, level2_df in zip(level1_col_names, level2_dfs):
            level1_cols.extend([level1_col_name for col in level2_df.columns])
        merged = pd.concat(level2_dfs, axis=1)
        merged.columns = [level1_cols, merged.columns]

        return merged

    def parse_yaml(self, yaml_file):
        # TODO: read yaml file and fill in the proper dfs
        return
    def from_csv(self):

        return 0

    def to_csv(self):

        return 0

    def save(self):

        return 0

    def load(self):

        return 0

    def from_yaml(self):

        return 0

    def to_yaml(self):

        return 0
