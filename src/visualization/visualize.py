# Plot null values
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def plot_missing_data(df: pd.DataFrame):
    (
        df
        .isnull()
        .melt(value_name='missing')
        .pipe(
            lambda df: (
                sns.displot(
                    data=df,
                    y='variable',
                    hue='missing',
                    multiple='fill',
                    aspect=2
                )
            )
        )
    )


def plot_missing_data_heatmap(df: pd.DataFrame):
    (
        df
        .isnull()
        .transpose()
        .pipe(
            lambda df: sns.heatmap(data=df)
        )
    )
