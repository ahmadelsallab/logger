
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
! pip install --upgrade git+https://github.com/ahmadelsallab/ml_logger.git
```

    Collecting git+https://github.com/ahmadelsallab/ml_logger.git
      Cloning https://github.com/ahmadelsallab/ml_logger.git to /tmp/pip-req-build-ccrtkamb
    Building wheels for collected packages: mllogger
      Running setup.py bdist_wheel for mllogger ... [?25ldone
    [?25h  Stored in directory: /tmp/pip-ephem-wheel-cache-swi794aj/wheels/87/e8/54/b5d82d55496a377ebe30a4b436616fe2bb006e9fc9055c6003
    Successfully built mllogger
    Installing collected packages: mllogger
      Found existing installation: mllogger 1.0
        Uninstalling mllogger-1.0:
          Successfully uninstalled mllogger-1.0
    Successfully installed mllogger-1.0
    [33mYou are using pip version 10.0.1, however version 19.1.1 is available.
    You should consider upgrading via the 'pip install --upgrade pip' command.[0m


___or alternatively clone the repo inside your project___


```python
!git clone https://github.com/ahmadelsallab/ml_logger.git
!cd ml_logger && pip install .
```

    Cloning into 'ml_logger'...
    remote: Enumerating objects: 74, done.[K
    remote: Counting objects: 100% (74/74), done.[K
    remote: Compressing objects: 100% (46/46), done.[K
    remote: Total 74 (delta 44), reused 49 (delta 25), pack-reused 0[K
    Unpacking objects: 100% (74/74), done.
    Processing /home/ahmad/Work/Logger/ml_logger/tests/ml_logger
    Building wheels for collected packages: mllogger
      Running setup.py bdist_wheel for mllogger ... [?25ldone
    [?25h  Stored in directory: /tmp/pip-ephem-wheel-cache-0mg36fxm/wheels/4f/c8/a5/a2a66360be84688ab6df5f949420a229abe1d786979b84bfe3
    Successfully built mllogger
    Installing collected packages: mllogger
      Found existing installation: mllogger 1.0
        Uninstalling mllogger-1.0:
          Successfully uninstalled mllogger-1.0
    Successfully installed mllogger-1.0
    [33mYou are using pip version 10.0.1, however version 19.1.1 is available.
    You should consider upgrading via the 'pip install --upgrade pip' command.[0m


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
from mllogger.experiments import Experiment

exp_meta_data = {'name': 'experiment_1',
            'purpose': 'test my awesome model',
             'date': 'today',
            }

exp_config = {'model_arch': '100-100-100',
          'learning_rate': 0.0001,
          'epochs': 2,
          'optimizer': 'Adam',
         }

exp_results = {'val_acc': 0.95, 
         'F1': 0.92,
         'Comment': 'Best model'}

experiment = Experiment(csv_file='results_old.csv', meta_data=exp_meta_data, config=exp_config, results=exp_results)


```

__Note that__

you can add or remove experiment parameters. In that case, if you add a parameter, old records will have NaN for those. If you delete some parameters, they will remain in the old records, but will be NaN in the new logged one.

Now Write CSV of the results


```python
experiment.to_csv('results.csv')
```

If you want to see the whole record:


```python
experiment.df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Purpose</th>
      <th>Description</th>
      <th>Run file</th>
      <th>Commit</th>
      <th>Features</th>
      <th>Train_test_split</th>
      <th>Size</th>
      <th>maxlen</th>
      <th>batch_size</th>
      <th>...</th>
      <th>Model file</th>
      <th>Comment</th>
      <th>date</th>
      <th>name</th>
      <th>purpose</th>
      <th>learning_rate</th>
      <th>model_arch</th>
      <th>optimizer</th>
      <th>F1</th>
      <th>val_acc</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>CNN1D_LSTM_Big</td>
      <td>Baseline CNN1D-LSTM Text only</td>
      <td>Big model</td>
      <td>jigsaw_simple_text_lstm_tokenizer.ipynb</td>
      <td>-</td>
      <td>comment_text</td>
      <td>0.2</td>
      <td>1804874.0</td>
      <td>317</td>
      <td>256.0</td>
      <td>...</td>
      <td>jigsaw_cnn_lstm_text_only.h5</td>
      <td>Same as small. Couldnt overfitIssue in model t...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>CNN1D_LSTM_Small</td>
      <td>Small CNN1D-LSTM Text only</td>
      <td>Small model</td>
      <td>jigsaw_simple_text_lstm_tokenizer.ipynb</td>
      <td>-</td>
      <td>comment_text</td>
      <td>0.2</td>
      <td>1804874.0</td>
      <td>317</td>
      <td>256.0</td>
      <td>...</td>
      <td>-</td>
      <td>No overfit. Needs bigger model</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>Small data CNN1D-LSTM Text only</td>
      <td>Big model Small data</td>
      <td>jigsaw_simple_text_lstm_tokenizer.ipynb</td>
      <td>-</td>
      <td>comment_text</td>
      <td>0.2</td>
      <td>20000.0</td>
      <td>317</td>
      <td>256.0</td>
      <td>...</td>
      <td>jigsaw_cnn_lstm_text_only.h5</td>
      <td>Also, loss not improving</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>LSTM_Big model_Small data</td>
      <td>Small data LSTM Text only</td>
      <td>LSTM Small data</td>
      <td>jigsaw_lstm.ipynb</td>
      <td>-</td>
      <td>comment_text</td>
      <td>0.2</td>
      <td>20000.0</td>
      <td>317</td>
      <td>256.0</td>
      <td>...</td>
      <td>jigsaw_lstm_1.h5</td>
      <td>Loss decreasing slowly, then aslo saturates</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>LSTM_Small model_Small data binary_crossentropy</td>
      <td>LSTM_Small model_Small data binary_crossentropy</td>
      <td>LSTM_Small model_Small data binary_crossentropy</td>
      <td>jigsaw_lstm.ipynb</td>
      <td>-</td>
      <td>comment_text</td>
      <td>0.2</td>
      <td>20000.0</td>
      <td>317/220</td>
      <td>256.0</td>
      <td>...</td>
      <td>jigsaw_lstm_1.h5</td>
      <td>Accuracy improved a lot. The targets have lots...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>LSTM_Big model_Small data binary_crossentropy</td>
      <td>LSTM_Small model_Small data binary_crossentropy</td>
      <td>LSTM_Small model_Small data binary_crossentropy</td>
      <td>jigsaw_lstm.ipynb</td>
      <td>-</td>
      <td>comment_text</td>
      <td>0.2</td>
      <td>20000.0</td>
      <td>317</td>
      <td>256.0</td>
      <td>...</td>
      <td>jigsaw_lstm_1.h5</td>
      <td>Accuracy improved a lot. The targets have lots...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>CNN1D_LSTM_Big binary_crossentropy</td>
      <td>Baseline CNN1D-LSTM Text only binary_crossentropy</td>
      <td>Big model binary_crossentropy</td>
      <td>jigsaw_simple_text_lstm_tokenizer.ipynb</td>
      <td>-</td>
      <td>comment_text</td>
      <td>0.2</td>
      <td>20000.0</td>
      <td>317</td>
      <td>256.0</td>
      <td>...</td>
      <td>jigsaw_cnn_lstm_text_only.h5</td>
      <td>Saturation as before \nBUT\nAccuracy improved ...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>LSTM_Huge model_Small data binary_crossentropy</td>
      <td>LSTM_Huge model_Small data binary_crossentropy</td>
      <td>LSTM_Huge model_Small data binary_crossentropy</td>
      <td>jigsaw_lstm.ipynb</td>
      <td>-</td>
      <td>comment_text</td>
      <td>0.2</td>
      <td>20000.0</td>
      <td>317</td>
      <td>256.0</td>
      <td>...</td>
      <td>jigsaw_lstm_1.h5</td>
      <td>Accuracy improved a lot. The targets have lots...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>LSTM_Huge model_Big data binary_crossentropy</td>
      <td>LSTM_Huge model_Big data binary_crossentropy</td>
      <td>LSTM_Huge model_Big data binary_crossentropy</td>
      <td>jigsaw_lstm.ipynb</td>
      <td>-</td>
      <td>comment_text</td>
      <td>0.2</td>
      <td>1804874.0</td>
      <td>317</td>
      <td>256.0</td>
      <td>...</td>
      <td>jigsaw_lstm_1.h5</td>
      <td>Accuracy improved a lot. The targets have lots...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>Best model</td>
      <td>today</td>
      <td>experiment_1</td>
      <td>test my awesome model</td>
      <td>0.0001</td>
      <td>100-100-100</td>
      <td>Adam</td>
      <td>0.92</td>
      <td>0.95</td>
    </tr>
  </tbody>
</table>
<p>10 rows × 32 columns</p>
</div>



## Alternatively, you could init the Experiment with the old records, and later log one or more experiment


```python
from mllogger.experiments import Experiment

# Load the old records
experiment = Experiment(csv_file='results_old.csv')

# TODO: perform you experiment

# Now log the new experiment data
exp_meta_data = {'name': 'experiment_1',
            'purpose': 'test my awesome model',
             'date': 'today',
            }

exp_config = {'model_arch': '100-100-100',
          'learning_rate': 0.0001,
          'epochs': 2,
          'optimizer': 'Adam',
         }

exp_results = {'val_acc': 0.95, 
         'F1': 0.92,
         'Comment': 'Best model'}

experiment.log_experiment(meta_data=exp_meta_data, config=exp_config, results=exp_results)

# Export the whole result
experiment.to_csv('results.csv')

experiment.df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Purpose</th>
      <th>Description</th>
      <th>Run file</th>
      <th>Commit</th>
      <th>Features</th>
      <th>Train_test_split</th>
      <th>Size</th>
      <th>maxlen</th>
      <th>batch_size</th>
      <th>...</th>
      <th>Model file</th>
      <th>Comment</th>
      <th>date</th>
      <th>name</th>
      <th>purpose</th>
      <th>learning_rate</th>
      <th>model_arch</th>
      <th>optimizer</th>
      <th>F1</th>
      <th>val_acc</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>CNN1D_LSTM_Big</td>
      <td>Baseline CNN1D-LSTM Text only</td>
      <td>Big model</td>
      <td>jigsaw_simple_text_lstm_tokenizer.ipynb</td>
      <td>-</td>
      <td>comment_text</td>
      <td>0.2</td>
      <td>1804874.0</td>
      <td>317</td>
      <td>256.0</td>
      <td>...</td>
      <td>jigsaw_cnn_lstm_text_only.h5</td>
      <td>Same as small. Couldnt overfitIssue in model t...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>CNN1D_LSTM_Small</td>
      <td>Small CNN1D-LSTM Text only</td>
      <td>Small model</td>
      <td>jigsaw_simple_text_lstm_tokenizer.ipynb</td>
      <td>-</td>
      <td>comment_text</td>
      <td>0.2</td>
      <td>1804874.0</td>
      <td>317</td>
      <td>256.0</td>
      <td>...</td>
      <td>-</td>
      <td>No overfit. Needs bigger model</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>Small data CNN1D-LSTM Text only</td>
      <td>Big model Small data</td>
      <td>jigsaw_simple_text_lstm_tokenizer.ipynb</td>
      <td>-</td>
      <td>comment_text</td>
      <td>0.2</td>
      <td>20000.0</td>
      <td>317</td>
      <td>256.0</td>
      <td>...</td>
      <td>jigsaw_cnn_lstm_text_only.h5</td>
      <td>Also, loss not improving</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>LSTM_Big model_Small data</td>
      <td>Small data LSTM Text only</td>
      <td>LSTM Small data</td>
      <td>jigsaw_lstm.ipynb</td>
      <td>-</td>
      <td>comment_text</td>
      <td>0.2</td>
      <td>20000.0</td>
      <td>317</td>
      <td>256.0</td>
      <td>...</td>
      <td>jigsaw_lstm_1.h5</td>
      <td>Loss decreasing slowly, then aslo saturates</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>LSTM_Small model_Small data binary_crossentropy</td>
      <td>LSTM_Small model_Small data binary_crossentropy</td>
      <td>LSTM_Small model_Small data binary_crossentropy</td>
      <td>jigsaw_lstm.ipynb</td>
      <td>-</td>
      <td>comment_text</td>
      <td>0.2</td>
      <td>20000.0</td>
      <td>317/220</td>
      <td>256.0</td>
      <td>...</td>
      <td>jigsaw_lstm_1.h5</td>
      <td>Accuracy improved a lot. The targets have lots...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>LSTM_Big model_Small data binary_crossentropy</td>
      <td>LSTM_Small model_Small data binary_crossentropy</td>
      <td>LSTM_Small model_Small data binary_crossentropy</td>
      <td>jigsaw_lstm.ipynb</td>
      <td>-</td>
      <td>comment_text</td>
      <td>0.2</td>
      <td>20000.0</td>
      <td>317</td>
      <td>256.0</td>
      <td>...</td>
      <td>jigsaw_lstm_1.h5</td>
      <td>Accuracy improved a lot. The targets have lots...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>CNN1D_LSTM_Big binary_crossentropy</td>
      <td>Baseline CNN1D-LSTM Text only binary_crossentropy</td>
      <td>Big model binary_crossentropy</td>
      <td>jigsaw_simple_text_lstm_tokenizer.ipynb</td>
      <td>-</td>
      <td>comment_text</td>
      <td>0.2</td>
      <td>20000.0</td>
      <td>317</td>
      <td>256.0</td>
      <td>...</td>
      <td>jigsaw_cnn_lstm_text_only.h5</td>
      <td>Saturation as before \nBUT\nAccuracy improved ...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>LSTM_Huge model_Small data binary_crossentropy</td>
      <td>LSTM_Huge model_Small data binary_crossentropy</td>
      <td>LSTM_Huge model_Small data binary_crossentropy</td>
      <td>jigsaw_lstm.ipynb</td>
      <td>-</td>
      <td>comment_text</td>
      <td>0.2</td>
      <td>20000.0</td>
      <td>317</td>
      <td>256.0</td>
      <td>...</td>
      <td>jigsaw_lstm_1.h5</td>
      <td>Accuracy improved a lot. The targets have lots...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>LSTM_Huge model_Big data binary_crossentropy</td>
      <td>LSTM_Huge model_Big data binary_crossentropy</td>
      <td>LSTM_Huge model_Big data binary_crossentropy</td>
      <td>jigsaw_lstm.ipynb</td>
      <td>-</td>
      <td>comment_text</td>
      <td>0.2</td>
      <td>1804874.0</td>
      <td>317</td>
      <td>256.0</td>
      <td>...</td>
      <td>jigsaw_lstm_1.h5</td>
      <td>Accuracy improved a lot. The targets have lots...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>Best model</td>
      <td>today</td>
      <td>experiment_1</td>
      <td>test my awesome model</td>
      <td>0.0001</td>
      <td>100-100-100</td>
      <td>Adam</td>
      <td>0.92</td>
      <td>0.95</td>
    </tr>
  </tbody>
</table>
<p>10 rows × 32 columns</p>
</div>



## You can init an emtpy experiment, or with a certain csv, and add or change the old records csv.

__But in this case, the records will be modified not appended or updated.__


```python
from mllogger.experiments import Experiment
# Init empty experiment
experiment = Experiment() # or Experiment(csv_file="another_results.csv")

# Update with another
experiment.from_csv(csv_file='results_old.csv')

# Now log the new experiment data
exp_meta_data = {'name': 'experiment_1',
            'purpose': 'test my awesome model',
             'date': 'today',
            }

exp_config = {'model_arch': '100-100-100',
          'learning_rate': 0.0001,
          'epochs': 2,
          'optimizer': 'Adam',
         }

exp_results = {'val_acc': 0.95, 
         'F1': 0.92,
         'Comment': 'Best model',}

experiment.log_experiment(meta_data=exp_meta_data, config=exp_config, results=exp_results)

# Export the whole result
experiment.to_csv('results.csv')

experiment.df
```

    /home/ahmad/anaconda3/lib/python3.6/site-packages/mllogger/experiments.py:33: UserWarning: No old experiments records given. It's OK if this is the first record or you will add later using from_csv or from_df. Otherwise, old records they will be overwritten
      warnings.warn(UserWarning("No old experiments records given. It's OK if this is the first record or you will add later using from_csv or from_df. Otherwise, old records they will be overwritten"))





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Purpose</th>
      <th>Description</th>
      <th>Run file</th>
      <th>Commit</th>
      <th>Features</th>
      <th>Train_test_split</th>
      <th>Size</th>
      <th>maxlen</th>
      <th>batch_size</th>
      <th>...</th>
      <th>Model file</th>
      <th>Comment</th>
      <th>date</th>
      <th>name</th>
      <th>purpose</th>
      <th>learning_rate</th>
      <th>model_arch</th>
      <th>optimizer</th>
      <th>F1</th>
      <th>val_acc</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>CNN1D_LSTM_Big</td>
      <td>Baseline CNN1D-LSTM Text only</td>
      <td>Big model</td>
      <td>jigsaw_simple_text_lstm_tokenizer.ipynb</td>
      <td>-</td>
      <td>comment_text</td>
      <td>0.2</td>
      <td>1804874.0</td>
      <td>317</td>
      <td>256.0</td>
      <td>...</td>
      <td>jigsaw_cnn_lstm_text_only.h5</td>
      <td>Same as small. Couldnt overfitIssue in model t...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>CNN1D_LSTM_Small</td>
      <td>Small CNN1D-LSTM Text only</td>
      <td>Small model</td>
      <td>jigsaw_simple_text_lstm_tokenizer.ipynb</td>
      <td>-</td>
      <td>comment_text</td>
      <td>0.2</td>
      <td>1804874.0</td>
      <td>317</td>
      <td>256.0</td>
      <td>...</td>
      <td>-</td>
      <td>No overfit. Needs bigger model</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>Small data CNN1D-LSTM Text only</td>
      <td>Big model Small data</td>
      <td>jigsaw_simple_text_lstm_tokenizer.ipynb</td>
      <td>-</td>
      <td>comment_text</td>
      <td>0.2</td>
      <td>20000.0</td>
      <td>317</td>
      <td>256.0</td>
      <td>...</td>
      <td>jigsaw_cnn_lstm_text_only.h5</td>
      <td>Also, loss not improving</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>LSTM_Big model_Small data</td>
      <td>Small data LSTM Text only</td>
      <td>LSTM Small data</td>
      <td>jigsaw_lstm.ipynb</td>
      <td>-</td>
      <td>comment_text</td>
      <td>0.2</td>
      <td>20000.0</td>
      <td>317</td>
      <td>256.0</td>
      <td>...</td>
      <td>jigsaw_lstm_1.h5</td>
      <td>Loss decreasing slowly, then aslo saturates</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>LSTM_Small model_Small data binary_crossentropy</td>
      <td>LSTM_Small model_Small data binary_crossentropy</td>
      <td>LSTM_Small model_Small data binary_crossentropy</td>
      <td>jigsaw_lstm.ipynb</td>
      <td>-</td>
      <td>comment_text</td>
      <td>0.2</td>
      <td>20000.0</td>
      <td>317/220</td>
      <td>256.0</td>
      <td>...</td>
      <td>jigsaw_lstm_1.h5</td>
      <td>Accuracy improved a lot. The targets have lots...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>LSTM_Big model_Small data binary_crossentropy</td>
      <td>LSTM_Small model_Small data binary_crossentropy</td>
      <td>LSTM_Small model_Small data binary_crossentropy</td>
      <td>jigsaw_lstm.ipynb</td>
      <td>-</td>
      <td>comment_text</td>
      <td>0.2</td>
      <td>20000.0</td>
      <td>317</td>
      <td>256.0</td>
      <td>...</td>
      <td>jigsaw_lstm_1.h5</td>
      <td>Accuracy improved a lot. The targets have lots...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>CNN1D_LSTM_Big binary_crossentropy</td>
      <td>Baseline CNN1D-LSTM Text only binary_crossentropy</td>
      <td>Big model binary_crossentropy</td>
      <td>jigsaw_simple_text_lstm_tokenizer.ipynb</td>
      <td>-</td>
      <td>comment_text</td>
      <td>0.2</td>
      <td>20000.0</td>
      <td>317</td>
      <td>256.0</td>
      <td>...</td>
      <td>jigsaw_cnn_lstm_text_only.h5</td>
      <td>Saturation as before \nBUT\nAccuracy improved ...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>LSTM_Huge model_Small data binary_crossentropy</td>
      <td>LSTM_Huge model_Small data binary_crossentropy</td>
      <td>LSTM_Huge model_Small data binary_crossentropy</td>
      <td>jigsaw_lstm.ipynb</td>
      <td>-</td>
      <td>comment_text</td>
      <td>0.2</td>
      <td>20000.0</td>
      <td>317</td>
      <td>256.0</td>
      <td>...</td>
      <td>jigsaw_lstm_1.h5</td>
      <td>Accuracy improved a lot. The targets have lots...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>LSTM_Huge model_Big data binary_crossentropy</td>
      <td>LSTM_Huge model_Big data binary_crossentropy</td>
      <td>LSTM_Huge model_Big data binary_crossentropy</td>
      <td>jigsaw_lstm.ipynb</td>
      <td>-</td>
      <td>comment_text</td>
      <td>0.2</td>
      <td>1804874.0</td>
      <td>317</td>
      <td>256.0</td>
      <td>...</td>
      <td>jigsaw_lstm_1.h5</td>
      <td>Accuracy improved a lot. The targets have lots...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>Best model</td>
      <td>today</td>
      <td>experiment_1</td>
      <td>test my awesome model</td>
      <td>0.0001</td>
      <td>100-100-100</td>
      <td>Adam</td>
      <td>0.92</td>
      <td>0.95</td>
    </tr>
  </tbody>
</table>
<p>10 rows × 32 columns</p>
</div>



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

