import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm


configs = ['SPA1_1', 'SPA1_2', 'SPA2', 'FRA1', 'FRA2', 'ITL1', 'ITL2', 'ITL3', 'GER1', 'GER2',
           'US1', 'US2', 'US3', 'US1_NoCA', 'US2_NoCA', 'US3_NoCA']

# Colors Definations
# get colors
cmap10 = plt.cm.tab10  # define the colormap
# extract all colors from the .jet map
colorlist10 = [cmap10(i) for i in range(cmap10.N)]

# get colors
cmap20 = plt.cm.tab20c  # define the colormap
# extract all colors from the .jet map
colorlist20 = [cmap20(i) for i in range(cmap20.N)]

# get colors
pastel2 = plt.cm.Pastel2  # define the colormap
# extract all colors from the .jet map
pastel2list = [pastel2(i) for i in range(pastel2.N)]

# get colors
paired = plt.cm.Paired  # define the colormap
# extract all colors from the .jet map
pairedlist = [paired(i) for i in range(paired.N)]

inferno = cm.get_cmap('inferno', 5)
infernolist = [inferno(i) for i in range(inferno.N)]

colors = {
    configs[0]: '#469990',
    configs[1]: '#808000',
    configs[2]: '#000075',
    configs[3]: '#dcbeff',
    configs[4]: '#000075',
    configs[5]: '#f58231',
    configs[6]: '#f58231',
    configs[7]: '#000000',
    configs[8]: '#f032e6',
    configs[9]: '#911eb4',
    configs[10]: '#3cb44b',
    configs[11]: '#9A6324',
    configs[12]: '#42d4f4',
    configs[13]: '#3cb44b',
    configs[14]: '#9A6324',
    configs[15]: '#42d4f4',
    'noShare': '#800000'
}
CONFIGS = ['SP11', 'SP12', 'SP2', 'FR1', 'FR2', 'IT1', 'IT2', 'IT3', 'GER1', 'GER2',
           'US1', 'US2', 'US3', 'US1_NoCA', 'US2_NoCA', 'US3_NoCA']
COLORS = {
    CONFIGS[0]: '#469990',
    CONFIGS[1]: '#808000',
    CONFIGS[2]: '#000075',
    CONFIGS[3]: '#dcbeff',
    CONFIGS[4]: '#800000',
    CONFIGS[5]: '#f58231',
    CONFIGS[6]: '#f58231',
    CONFIGS[7]: '#000000',
    CONFIGS[8]: '#f032e6',
    CONFIGS[9]: '#911eb4',
    CONFIGS[10]: '#3cb44b',
    CONFIGS[11]: '#9A6324',
    CONFIGS[12]: '#42d4f4',
    CONFIGS[13]: '#3cb44b',
    CONFIGS[14]: '#9A6324',
    CONFIGS[15]: '#42d4f4',
    'noShare': '#800000'
}

MARKERS = {
    configs[0]: 'X',
    configs[1]: '^',
    configs[2]: '1',
    configs[3]: '3',
    configs[4]: '>',
    configs[5]: 'd',
    configs[6]: '*',
    configs[7]: 'p',
    configs[8]: '<',
    configs[9]: 'o',
    configs[10]: 'v',
    configs[11]: '.',
    configs[12]: 'P'
}

HATCHES = {
    configs[0]: '/o',
    configs[1]: '\\|',
    configs[2]: '|*',
    configs[3]: '-\\',
    configs[4]: 'O.',
    configs[5]: 'x*',
    configs[6]: 'o-',
    configs[7]: 'O|',
    configs[8]: '+o',
    configs[9]: '*-',
    configs[10]: '///',
    configs[11]: 'o',
    configs[12]: 'X',
}

Clouds = {
    'france': 'Microsoft Azure',
    'Spain': 'Google',
    'Germany': 'Amazon AWS',
    'Italy': 'Google'
}

LS = ['--', ':', '-.', '-']
