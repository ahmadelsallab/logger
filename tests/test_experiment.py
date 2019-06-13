import unittest
from unittest import TestCase
from experiment import Experiment
import pandas as pd

class TestExperiment(TestCase):

    def test__init_no_old_exp_no_logged_exp(self):

        with self.assertWarns(Warning):
            experiment = Experiment()

    def test__init_from_csv(self):
        experiment = Experiment(csv_file='results_old.csv')

        old_df = pd.read_csv('results_old.csv')

        assert old_df.equals(experiment.df)

    def test__init_from_yaml(self):
        # TODO: when yaml is supported
        '''
        experiment = Experiment(csv_file='results_old.csv')

        old_df = pd.read_csv('results_old.csv')

        assert old_df.equals(experiment.df)
        '''
        self.fail()

    def test__init_old_exp_incomplete_exp(self):
        self.fail()

    def test__init_no_old_exp_incomplete_exp(self):
        self.fail()


    def test__init_old_exp_complete_exp(self):
        self.fail()

    def test__init_no_old_exp_complete_exp(self):
        self.fail()

    def test_from_csv(self):
        experiment = Experiment()
        experiment.from_csv(csv_file='results_old.csv')
        old_df = pd.read_csv('results_old.csv')

        assert old_df.equals(experiment.df)

    def test_from_df(self):

        old_df = pd.read_csv('results_old.csv')
        experiment = Experiment()
        experiment.from_df(old_df)

        assert old_df.equals(experiment.df)

    def test_log_experiment(self):
        self.fail()

    def test_exp_to_df(self):
        self.fail()

    def test_to_csv(self):
        experiment = Experiment(csv_file='results_old.csv')
        experiment.to_csv('results.csv')
        df = pd.read_csv('results.csv')

        #self.assertAlmostEquals(df, experiment.df)
        assert df.equals(experiment.df)

    def test_from_yaml(self):
        self.fail()

    def test_to_yaml(self):
        self.fail()
'''
if __name__ == '__main__':
    unittest.main()
'''