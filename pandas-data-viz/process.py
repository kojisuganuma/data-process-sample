import pandas as pd

import json
import random


# 複数カラムへの分割
def split_name(x_df):
    fn = lambda x, idx: x.split(", ")[idx]
    return x_df.assign(
        FirstName=lambda x: x.Name.apply(fn, idx=0),
        LstName=lambda x: x.Name.apply(fn, idx=1),
    )


# json の展開
def json_expand(x_df):
    fn = lambda x, key: json.loads(x)[key]
    return x_df.assign(
        a=lambda df: df.json.apply(fn, key="a"),
        b=lambda df: df.json.apply(fn, key="b"),
    )


# 単一カラムマップ変換
def substitute_sex(x_df):
    mapping={'male':'M', 'female':'F'}
    x_df.Sex=x_df.Sex.map(mapping)
    return x_df


# 特定カラムを利用した null 値の補完
def replace_age_na(x_df):
    pclass_age_map = x_df.groupby(by=["Pclass"]).Age.mean().to_dict()
    cond = x_df.Age.isna()
    resp = x_df.loc[cond, "Pclass"].map(pclass_age_map)
    x_df.loc[cond, "Age"] = resp
    return x_df


def process_isna(x_df):
    process_mean = x_df.groupby(by=["PClass"]).Age.mean().to_dict()
    cond = x_df.Age.isna()
    resp = x_df.loc[cond, "PClass"].map(process_mean)
    x_df.loc[cond, "Age"] = resp
    return x_df


def replace_with_map(x_df):
    replace_map = {"Male": 0, "Female": 1}
    x_df.Age = x_df.Age.map(replace_map)
    return x_df

def expand_process(x_df):
    x_df.assign(
        a=lambda df: df.Age.apply(fn),
    )

def expand_process(x_df):
    fn = lambda x, key: json.loads(x)[key]
    x_df.assign(
        ajson=lambda df: df.json.apply(fn, key="hoge"),
        bjson=lambda df: df.json.apply(fn, key="fuga")
    )

def process_category_age(x_df):
    def process(x):
        if x < 10:
            return 0
        elif 10 <= x < 20:
            return 1
        elif 20 <= x < 30:
            return 2
        elif 30 <= x < 40:
            return 3
        elif 40 <= x < 50:
            return 4
        elif 50 <= x < 60:
            return 5
        elif 60 <= x:
            return 6

    return x_df.assign(
        new_category_age=lambda df: df.Age.apply(process)
    )

def complete_mean(x_df):
    mean_age = x_df.Age.mean()
    cond = x_df.Age.isna()
    resp = x_df.loc[cond, "Age"]
    x_df.loc[cond, "Age"] = mean_age
    return x_df
