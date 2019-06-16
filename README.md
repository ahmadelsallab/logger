
# Logger
In machine learning you perform many experiments until you settle on a good model. During this journey you have a lot of checkpoints, visualizations, results,...etc.

The logger helps you to organize and keep track of:
- The experiments results
- TODO: The model checkpoints
- TODO: Different visualizations and curves



# Requirements

``` 
pip install requirements.txt
```


# Install


```python
!pip install git+https://github.com/ahmadelsallab/logger.git
    
```

    Collecting git+https://github.com/ahmadelsallab/logger.git
      Cloning https://github.com/ahmadelsallab/logger.git to /tmp/pip-req-build-hldj1x3x
        Complete output from command python setup.py egg_info:
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/home/ahmad/anaconda3/lib/python3.6/tokenize.py", line 452, in open
            buffer = _builtin_open(filename, 'rb')
        FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pip-req-build-hldj1x3x/setup.py'
        
        ----------------------------------------
    [31mCommand "python setup.py egg_info" failed with error code 1 in /tmp/pip-req-build-hldj1x3x/[0m
    [33mYou are using pip version 10.0.1, however version 19.1.1 is available.
    You should consider upgrading via the 'pip install --upgrade pip' command.[0m


___or alternatively clone the repo inside your project___


```python
!git clone https://github.com/ahmadelsallab/logger.git
```

# Usage
More use cases under tests/test_experiment.py

## Log new experiment result
In general any experiment is composed of:
- meta_data: name, purpose, file, commit,...etc
- config: mostly the hyperparameters, and any other configuration like the used features. For deep learning, config can be further divided into: data, model, optimizer, learning hyper parameters
- results: metrics, best model file, comment,..etc




Suppose all your previous records are in 'results_old.csv'.

And now you want to log a new experiment.


```python
from logger.experiments import Experiment

exp_meta_data = {'name': 'experiment_1',
            'purpose': 'test my awesome model',
             'date': 'today'
            }

exp_config = {'model_arch': '100-100-100'
          'learning_rate': 0.0001,
          'epochs': 2
          'optimizer': 'Adam'
         }

exp_results = {'val_acc': 0.95, 
         'F1': 0.92
         'Comment': 'Best model'}

experiment = Experiment(csv_file='results_old.csv', meta_data=meta_data, config=config, results=results)


```

__Note that__

you can add or remove experiment parameters. In that case, if you add a parameter, old records will have NaN for those. If you delete some parameters, they will remain in the old records, but will be NaN in the new logged one.

Now Write CSV of the results


```python
experiment.to_csv('results.csv')
```

## Alternatively, you could init the Experiment with the old records, and later log one or more experiment


```python
from logger.experiments import Experiment

# Load the old records
experiment = Experiment(csv_file='results_old.csv')

# TODO: perform you experiment

# Now log the new experiment data
exp_meta_data = {'name': 'experiment_1',
            'purpose': 'test my awesome model',
             'date': 'today'
            }

exp_config = {'model_arch': '100-100-100'
          'learning_rate': 0.0001,
          'epochs': 2
          'optimizer': 'Adam'
         }

exp_results = {'val_acc': 0.95, 
         'F1': 0.92
         'Comment': 'Best model'}

experiment.log_experiment(meta_data=meta_data, config=config, results=results)

# Export the whole result
experiment.to_csv('results.csv')
```

## You can init an emtpy experiment, or with a certain csv, and add or change the old records csv.

__But in this case, the records will be modified not appended or updated.__


```python
from logger.experiments import Experiment
# Init empty experiment
experiment = Experiment() # or Experiment(csv_file="another_results.csv")

# Update with another
experiment.from_csv(csv_file='results_old.csv')

# Now log the new experiment data
exp_meta_data = {'name': 'experiment_1',
            'purpose': 'test my awesome model',
             'date': 'today'
            }

exp_config = {'model_arch': '100-100-100'
          'learning_rate': 0.0001,
          'epochs': 2
          'optimizer': 'Adam'
         }

exp_results = {'val_acc': 0.95, 
         'F1': 0.92
         'Comment': 'Best model'}

experiment.log_experiment(meta_data=meta_data, config=config, results=results)

# Export the whole result
experiment.to_csv('results.csv')
```

## Other use cases

- You can load old records from pandas.DataFrame instead of csv using orig_df in the Experiment constructor
```
df = pd.read_csv('results.old.csv')
experiment = Experiment(orig_df=df)
```

- You can log experiment using yaml files, either in init or using ```from_yaml``` method



# Known issues

https://github.com/ahmadelsallab/logger/issues

# Future developments
- JSON Support
- xlsx support
- The model checkpoints
- Different visualizations and curves
- Upload the result file to gdrive for online updates and sharing

