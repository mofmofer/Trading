# DataFrameを使う
import pandas as pd
import numpy as np

# 描画
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import Normalize

# K-分割交差検証とパラメータフィッティング
from sklearn.model_selection import GridSearchCV, StratifiedKFold
# Feature Warningを無視する
from warnings import simplefilter
# DataFrameのデータの統計を確認する
import pandas_profiling as ppf

# 学習モデル
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
# GridSearch用のパラメタ探索範囲と評価指標に関する自作パッケージ
from function.param import *

# astropy
from astropy.table import Table
import astropy.units as u
from astropy.coordinates import SkyCoord

threshold = 0.9

# Feature Warningを無視する
simplefilter(action='ignore', category=FutureWarning)

# シード値を設定しておく
np.random.seed(31415)

# プロット用のデータフレームを読み込む
FGL_plot = pd.read_csv("/Users/kawakami/Desktop/fight/STEP1/STEP1_5/data/FGL_unid_プロット用_閾値{}.csv".format(threshold), header=0).drop(["Unnamed: 0"], axis=1)
FGL_plot1 = FGL_plot[FGL_plot['label'] == 'PSRlike']
FGL_plot2 = FGL_plot[FGL_plot['label'] == 'AGNlike']

FGL_plot_AGN = pd.read_csv("/Users/kawakami/Desktop/fight/STEP1/STEP1_1/4FGL_AGN.csv", header=0).drop(["Unnamed: 0"], axis=1)
FGL_plot_PSR = pd.read_csv("/Users/kawakami/Desktop/fight/STEP1/STEP1_1/4FGL_PSR.csv", header=0).drop(["Unnamed: 0"], axis=1)

# 表示する画像サイズ
fig = plt.figure(figsize=(20, 10))
ax = fig.add_subplot(111, projection="aitoff")
plt.tick_params(labelsize=18)

# Astropy.Tableに変換
FGL_plot_astro1 = Table.from_pandas(FGL_plot1)
FGL_plot_astro2 = Table.from_pandas(FGL_plot2)
FGL_plot_astro_AGN = Table.from_pandas(FGL_plot_AGN)
FGL_plot_astro_PSR = Table.from_pandas(FGL_plot_PSR)

# unit(degree)をGLON,GLAT列に追加
FGL_plot_astro1['GLON'].unit = 'deg'
FGL_plot_astro1['GLAT'].unit = 'deg'
FGL_plot_astro2['GLON'].unit = 'deg'
FGL_plot_astro2['GLAT'].unit = 'deg'
FGL_plot_astro_AGN['GLON'].unit = 'deg'
FGL_plot_astro_AGN['GLAT'].unit = 'deg'
FGL_plot_astro_PSR['GLON'].unit = 'deg'
FGL_plot_astro_PSR['GLAT'].unit = 'deg'

#  ソースクラスのリスト
source_classes = ['']
coord1 = SkyCoord(FGL_plot_astro1["GLON"], FGL_plot_astro1["GLAT"], frame="galactic")  # type: SkyCoord
coord2 = SkyCoord(FGL_plot_astro2["GLON"], FGL_plot_astro2["GLAT"], frame="galactic")  # type: SkyCoord
coord3 = SkyCoord(FGL_plot_astro_AGN["GLON"], FGL_plot_astro_AGN["GLAT"], frame="galactic")  # type: SkyCoord
coord4 = SkyCoord(FGL_plot_astro_PSR["GLON"], FGL_plot_astro_PSR["GLAT"], frame="galactic")  # type: SkyCoord

# 描画
for source_class in source_classes:
    plot2 = ax.scatter(coord3.l.wrap_at(180 * u.degree).radian, coord3.b.radian, vmin=0, vmax=1, c='#4A593D', s=200, marker="+")
for source_class in source_classes:
    plot1 = ax.scatter(coord2.l.wrap_at(180 * u.degree).radian, coord2.b.radian, vmin=0, vmax=1, c='#B5CAA0', s=100, marker="+")

ax.grid(True)
ax.legend([plot1, plot2], ["AGNlike", "AGNness"], loc=1, prop={'size': 20}, title_fontsize =20)

plt.savefig("/Users/kawakami/Desktop/fight/STEP1/STEP1_7/AGNness_AGNlike.png".format(threshold), format='png', dpi=400)