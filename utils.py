#!/usr/bin/python3
'''
Description:
Utils file which has the analysis methods to parse the data
'''
import os
import math
import numpy as np


def plotme(plt, plot_id, plot_name, plot_path='../Final_Plots', show_flag=True, pdf_only=True):
    if show_flag:
        print('Showing Plot {}_{}'.format(plot_id, plot_name))
        plt.show()
    else:
        if not pdf_only:
            ax = plt.gca()

            if not os.path.exists('{}/png/'.format(plot_path)):
                os.makedirs('{}/png/'.format(plot_path))
            plt.savefig('{}/png/{}_{}.png'.format(plot_path, plot_id, plot_name), format='png', dpi=300,
                        bbox_inches='tight',
                        pad_inches=0.02)
            if not os.path.exists('{}/pdf/'.format(plot_path)):
                os.makedirs('{}/pdf/'.format(plot_path))
            plt.savefig('{}/pdf/{}_{}.pdf'.format(plot_path, plot_id, plot_name), format='pdf', dpi=300,
                        bbox_inches='tight',
                        pad_inches=0.5)
            # Save it with rasterized points
            ax.set_rasterization_zorder(1)
            if not os.path.exists('{}/eps/'.format(plot_path)):
                os.makedirs('{}/eps/'.format(plot_path))
            plt.savefig('{}/eps/{}-{}.eps'.format(plot_path, plot_id, plot_name), dpi=300, rasterized=True,
                        bbox_inches='tight',
                        pad_inches=0.02)
        else:
            if not os.path.exists('{}/pdf/'.format(plot_path)):
                os.makedirs('{}/pdf/'.format(plot_path))
            plt.savefig('{}/pdf/{}_{}.pdf'.format(plot_path, plot_id, plot_name), format='pdf', dpi=300,
                        bbox_inches='tight',
                        pad_inches=0.02)
        print('Saved Plot {}_{}'.format(plot_id, plot_name))

def V_t(df, window=5):
    smoothed_data = df.groupby(df.index // window).mean()
    return smoothed_data.diff().abs().mean()

def get_smooth_metric(df, window=5, flag='nonOverlap'):
    # Smoothness - Timeseries change rate: sup(sum(|r{t}-r{t-1}|))

    # Calculate the non-overlapping rolling mean using groupby
    #     print(time_series.columns.tolist())
    if 'Lon' in df.columns.tolist():
        df = df.drop(columns=['Lon', 'Lat'])
    if flag == 'nonOverlap':
        smoothed_data = df.groupby(df.index // window).mean()  # .dropna().values
        #         smoothness_index = (smoothed_data.diff().abs().mean(), smoothed_data.std())
        smoothness_index = (smoothed_data.diff().abs().mean(), smoothed_data.diff().abs().std())
    elif flag == 'overlap':
        #         smoothed_data = time_series.groupby(time_series.columns.tolist()).rolling(window).mean()# .dropna().values
        smoothness_index = (df.rolling(window).mean().dropna().diff().abs().fillna(0).mean(),
                            df.rolling(window).mean().dropna().diff().abs().fillna(0).std())
    return smoothness_index