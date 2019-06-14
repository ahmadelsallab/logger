import pandas as pd
import warnings
import yaml
class Experiment:
    # TODO: add **kwargs to support any experiment parameters other than the given ones. It should be a dict.
    def __init__(self, meta_data=None, config=None, results=None, csv_file=None, orig_df=None, yaml_file=None):
        """
        :param meta_data: the current experiment meta_data
        :type meta_data: dict
        :param config: the current experiment config/hyper parameters
        :type config: dict
        :param results: the current experiment results
        :type results: dict
        :param csv_file: full file path of the old experiments params as csv. If given it overrides orig_df
        :type csv_file: string
        :param orig_df: the old experiments params as DataFrame. This df will be merged to new experiment, new columns will be added with NaN in old records, but old wont be deleted.
        :type orig_df: DataFrame
        :param yaml_file: full file path of the current experiment yaml. Must have meta_data, config and results. If given, it overrides the other args.
        :type yaml_file: string

        """

        # Load old experiments
        if csv_file:
            self.from_csv(csv_file)

        elif orig_df is not None:
            self.from_df(orig_df)

        else: # No records exist

            self.df = pd.DataFrame()
            warnings.warn(UserWarning("No old experiments records given. It's OK if this is the first record or you will add later using from_csv or from_df. Otherwise, old records they will be overwritten"))

        # Log an experiment if yaml or exp attribs given is given
        if yaml_file or (meta_data and config and results):
            self.log_experiment(meta_data, config, results, yaml_file)

    def __str__(self):
        # FIXME
        return self.df

    def __repr__(self):
        # FIXME:
        return self.df

    def __iter__(self):
        return self.df.items()

    def __add__(self, other):
        # FIXME
        self.df = pd.concat([self.df, other.df], axis=0, ignore_index=True, sort=False)

    def from_csv(self, csv_file):
        self.df = pd.read_csv(csv_file)


    def from_df(self, old_df):
        self.df = old_df

    def log_experiment(self, meta_data=None, config=None, results=None, yaml_file=None):

        # Build the log experiment df
        exp_df = self.exp_to_df(meta_data, config, results, yaml_file)

        # Append the current experiment to old records
        self.df = pd.concat([self.df, exp_df], axis=0, ignore_index=True, sort=False)

    def exp_to_df(self, meta_data=None, config=None, results=None, yaml_file=None):
        if yaml_file:
            exp_df = self.from_yaml(yaml_file)

        else:
            # Load experiments data:
            assert isinstance(meta_data, dict), "Meta data must a dictionary."
            assert isinstance(config, dict), "Config must a dictionary."
            assert isinstance(results, dict), "Results must a dictionary."

            # Concatenate all experiment parameters (meta, config and results) along their columns. This will be one entry DataFrame.
            exp_df = pd.concat([pd.DataFrame([meta_data]), pd.DataFrame([config]), pd.DataFrame([results])], axis=1)

        return exp_df

    def to_csv(self, csv_file):
        """
        Writes the whole experiment data frame to csv_file
        Warning: if the csv_file has old experiments they will be overwritten.
        To avoid that, first load the old experiments records using from_csv method.

        :param csv_file: full file path
        :type csv_file: string
        :return:
        :rtype:
        """
        with open(csv_file, mode='w', newline='\n') as f:
            self.df.to_csv(f, index=False, sep=",", line_terminator='\n', encoding='utf-8')
        #self.df.to_csv(csv_file, index=False, line_terminator='\n')

    def from_yaml(self, yaml_file):
        """
        Convert yaml file into df
        :param yaml_file:
        :type yaml_file:
        :return: experiment data frame
        :rtype: DataFrame
        """
        with open(yaml_file, 'r') as f:
            exp_df = pd.DataFrame(yaml.load(f), index=[0])
        return exp_df
    def to_yaml(self, meta_data, config, results, yaml_file):
        """ Write yaml from experiment df

        :param meta_data: exp_df meta
        :type meta_data: DataFrame
        :param config: exp_df config
        :type config: DataFrame
        :param results: exp_df results
        :type results: DataFrame
        :param yaml_file: the output file to save yaml (full path)
        :type yaml_file: string
        :return:
        :rtype:
        """


        exp_df = self.exp_to_df(meta_data, config, results, yaml_file=None)
        with open(yaml_file, 'wt') as f:
            yaml.dump(exp_df.iloc[-1].to_dict(), f, default_flow_style=False)

        return exp_df

