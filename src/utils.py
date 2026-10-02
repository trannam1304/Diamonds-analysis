import matplotlib.pyplot as plt
import seaborn as sns

def set_plotting_style():
    """Thiết lập chuẩn style biểu đồ đồng nhất cho cả nhóm."""
    sns.set_theme(style='whitegrid', palette='muted')
    plt.rcParams['figure.figsize'] = (10, 6)
    plt.rcParams['font.size'] = 11
    plt.rcParams['axes.titlesize'] = 14
    plt.rcParams['axes.labelsize'] = 12
