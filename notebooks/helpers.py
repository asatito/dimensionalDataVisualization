from pandas import DataFrame
from plotnine import *


def make_df(features, target=None):
    """
    Helper function to turn a feature matrix and a target vector into a pandas
    DataFrame. Assumes that the feature matrix has two columns. The target
    vector is optional.
    """
    
    df = DataFrame(features[:,0:2], columns=['x', 'y'])
    if target is not None:
        df['target'] = target
        
    return df


def plot(df):
    """
    Helper function to plot a pandas DataFrame using the plotnine package.
    Assumes that the columns are named x, y, and target. The target column
    is optional.
    """
    
    if 'target' in df.columns:
        g = (ggplot(df, aes('x', 'y', color='factor(target)')) +
             geom_point() +
             labs(color='target')
            )
    else:
        g = ggplot(df, aes('x', 'y')) + geom_point()
        
    return g