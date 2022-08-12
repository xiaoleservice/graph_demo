import time
from math import floor, ceil
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go


# Zepp 速度
def zepp_speed_km_ticks(value_max, value_min):
    A = value_max
    B = value_min
    A = int(np.ceil(A))
    B = int(np.floor(B))
    # 省略处理？
    X = A * 1000
    Y = B * 1000
    C = (X - Y) / 3
    D = C / 500
    D = int(np.ceil(D))
    ticks_interval = 500 * D
    ticks_interval_km = ticks_interval / 1000
    skip_val = X
    while skip_val % 500 != 0:
        skip_val = skip_val + 1
    skip_val_km = skip_val / 1000
    if A - B <= 3:
        result_ticks = [A - 3, A - 2, A - 1, A]
    else:
        result_ticks = [skip_val_km - 3 * ticks_interval_km,
                        skip_val_km - 2 * ticks_interval_km,
                        skip_val_km - 1 * ticks_interval_km,
                        skip_val_km]
    return result_ticks


def start_above_zero(value_max, value_min):
    if value_max < value_min:
        st.error('最大值最小值关系错误！')
    # st.markdown('#### 方案一')
    # st.write('计算过程如下：')
    # st.markdown('1. 当前数据最小值为：{}，最大值为：{}'.format(value_min, value_max))
    value_range = value_max - value_min
    # st.write('2. 数值区间为：{}'.format(value_range))
    temp_value = value_range / 3
    # st.write('3. temp_value 值 为：{}'.format(temp_value))
    temp_value = ceil(temp_value)
    while temp_value % 3 != 0:
        temp_value = temp_value + 1
    # st.write('4. 向上以3取整结果为：{}'.format(temp_value))
    axis_max = value_max
    axis_min = value_min

    n = 0
    if temp_value != 0:
        while axis_max % temp_value != 0:
            n = n + 1
            axis_max = axis_max + 1
    else:
        pass
    # st.write('5. 坐标轴最大值为：{} + {} = {}'.format(value_max, n, axis_max))

    m = 0
    if temp_value != 0:
        while axis_min % temp_value != 0:
            m = m + 1
            axis_min = axis_min - 1
            if axis_min <= 0:
                axis_min = 0
                m = value_min
                break
    else:
        pass
    # st.write('6. 坐标轴最小值为：{} - {} = {}'.format(value_min, m, axis_min))
    axis_range = axis_max - axis_min
    result = []

    if axis_min != 0:
        axis_each = float(axis_range / 3)
        for i in range(4):
            result.append(axis_min + i * axis_each)
    else:
        while axis_range % 4 != 0:
            axis_max = axis_max + 1
            axis_range = axis_max - axis_min
        # print('最大值修正值为 {}'.format(axis_max))
        axis_each = axis_range / 4
        for i in range(5):
            result.append(axis_min + i * axis_each)
    # print('----------------------------------')
    # print('计算完毕，均分获得最终坐标轴结果...')
    return result


def start_below_zero(value_max, value_min):
    if value_max < value_min:
        print('最大值最小值关系错误！')
        return
    # print('计算过程如下：')
    # print('1. 当前数据最小值为：{}，最大值为：{}'.format(value_min, value_max))
    value_range = value_max - value_min
    # print('2. 数值区间为：{}'.format(value_range))
    temp_value = value_range / 3
    # print('3. temp_value 值 为：{}'.format(temp_value))
    temp_value = ceil(temp_value)
    while temp_value % 3 != 0:
        temp_value = temp_value + 1
    # print('4. 向上以3取整结果为：{}'.format(temp_value))
    axis_max = value_max
    axis_min = value_min

    n = 0
    if temp_value != 0:
        while axis_max % temp_value != 0:
            n = n + 1
            axis_max = axis_max + 1
    else:
        pass
    # print('5. 坐标轴最大值为：{} + {} = {}'.format(value_max, n, axis_max))

    m = 0
    if temp_value != 0:
        while axis_min % temp_value != 0:
            m = m + 1
            axis_min = axis_min - 1
    else:
        pass
    # print('6. 坐标轴最小值为：{} - {} = {}'.format(value_min, m, axis_min))
    axis_range = axis_max - axis_min
    result = []

    if axis_min != 0:
        axis_each = float(axis_range / 3)
        for i in range(4):
            result.append(axis_min + i * axis_each)
    else:
        while axis_range % 4 != 0:
            axis_max = axis_max + 1
            axis_range = axis_max - axis_min
        # print('最大值修正值为 {}'.format(axis_max))
        axis_each = axis_range / 4
        for i in range(5):
            result.append(axis_min + i * axis_each)
    # print('计算完毕，均分获得最终坐标轴结果...')
    return result


def start_with_zero(value_max):
    result = []

    # print('计算过程如下: ')
    # print('----------------------------------')
    x = value_max / 4
    print('1. x 值 为：{}'.format(x))
    x = ceil(x)
    while x % 4 != 0:
        x = x + 1
    print('2. 向上以4取整结果为：{}'.format(x))
    axis_max = value_max

    n = 0
    while axis_max % x != 0:
        n = n + 1
        axis_max = axis_max + 1
    print('3. 坐标轴最大值为：{} + {} = {}'.format(value_max, n, axis_max))
    range_value = axis_max / 4
    for i in range(3, -1, -1):
        result.append(axis_max - i * range_value)
    # print('----------------------------------')
    # print('计算完毕，均分获得最终坐标轴结果...')
    return result


def start_with_zero_upgrade(value_max):
    result = []

    axis_max = value_max

    n = 0
    while axis_max % 20 != 0:
        n = n + 1
        axis_max = axis_max + 1
    # print('3. 坐标轴最大值为：{} + {} = {}'.format(value_max, n, axis_max))
    range_value = axis_max / 4
    for i in range(3, -1, -1):
        result.append(axis_max - i * range_value)
    # print('----------------------------------')
    # print('计算完毕，均分获得最终坐标轴结果...')
    return result


def speed_graph(value_max, value_min):
    range_val = value_max - value_min
    temp = range_val / 3
    temp = ceil(temp)
    while temp % 3 != 0:
        temp = temp + 1
    # print(temp)
    axis_max = value_max
    axis_min = value_min

    n = 0
    if temp != 0:
        while axis_max % temp != 0:
            n = n + 1
            axis_max = axis_max + 1
    else:
        pass
    # print('坐标轴最大值为：{} + {} = {}'.format(value_max, n, axis_max))

    m = 0
    if temp != 0:
        while axis_min % temp != 0:
            m = m + 1
            axis_min = axis_min - 1
            if axis_min <= 0:
                axis_min = 0
                m = value_min
                break
    else:
        pass
    # print('坐标轴最小值为：{} - {} = {}'.format(value_min, m, axis_min))
    axis_range = axis_max - axis_min
    result_num = []
    result = []

    if axis_min != 0:
        axis_each = float(axis_range / 3)
        for i in range(4):
            secs = axis_min + i * axis_each
            result_num.append(secs)
            min_res = floor(secs / 60)
            sec_res = int(secs % 60)
            res_str = '{}\'{}\'\''.format(min_res, sec_res)
            result.append(res_str)
    else:
        axis_each = axis_range / 4
        # print(axis_each)
        for i in range(5):
            secs = axis_min + i * axis_each
            result_num.append(secs)
            min_res = floor(secs / 60)
            sec_res = int(secs % 60)
            res_str = '{}\'{}\'\''.format(min_res, sec_res)
            result.append(res_str)
    # print(result_num)
    # print(result)
    return result_num, result


def speed_graph2(value_max, value_min):
    axis_max = value_max
    axis_min = value_min

    n = 0
    # while axis_max % 30 != 0:
    #     n = n + 1
    #     axis_max = axis_max + 1
    # print('坐标轴最大值为：{} + {} = {}'.format(value_max, n, axis_max))

    m = 0
    while axis_min % 30 != 0:
        m = m + 1
        axis_min = axis_min - 1
        if axis_min <= 0:
            axis_min = 0
            m = value_min
            break
    # print('坐标轴最小值为：{} - {} = {}'.format(value_min, m, axis_min))
    axis_range = axis_max - axis_min
    result = []
    result_num = []

    if axis_min != 0:
        axis_each = float(axis_range / 3)

        while floor(axis_each) % 30 != 0:
            axis_each = floor(axis_each) + 1
        for i in range(4):
            secs = axis_min + i * axis_each
            result_num.append(secs)
            min_res = floor(secs / 60)
            sec_res = int(secs % 60)
            res_str = '{}:{}'.format(min_res, sec_res)
            result.append(res_str)
    else:
        axis_each = axis_range / 4
        while floor(axis_each) % 30 != 0:
            axis_each = floor(axis_each) + 1
        print(axis_each)
        for i in range(5):
            secs = axis_min + i * axis_each
            result_num.append(secs)
            min_res = floor(secs / 60)
            sec_res = int(secs % 60)
            res_str = '{}:{}'.format(min_res, sec_res)
            result.append(res_str)
    print(result_num)
    print(result)
    return result_num, result


def speed_graph3(value_max, value_min):
    axis_max = value_max
    axis_min = value_min

    n = 0
    while axis_max % 20 != 0:
        n = n + 1
        axis_max = axis_max + 1
    # print('坐标轴最大值为：{} + {} = {}'.format(value_max, n, axis_max))

    m = 0
    while axis_min % 20 != 0:
        m = m + 1
        axis_min = axis_min - 1
        if axis_min <= 0:
            axis_min = 0
            m = value_min
            break
    # print('坐标轴最小值为：{} - {} = {}'.format(value_min, m, axis_min))
    axis_range = axis_max - axis_min
    result = []
    result_num = []

    if axis_min != 0:
        axis_each = float(axis_range / 4)
        for i in range(5):
            secs = axis_min + i * axis_each
            result_num.append(secs)
            min_res = floor(secs / 60)
            sec_res = int(secs % 60)
            res_str = '{}:{}'.format(min_res, sec_res)
            result.append(res_str)
    else:
        axis_each = axis_range / 5
        # print(axis_each)
        for i in range(6):
            secs = axis_min + i * axis_each
            result_num.append(secs)
            min_res = floor(secs / 60)
            sec_res = int(secs % 60)
            res_str = '{}:{}'.format(min_res, sec_res)
            result.append(res_str)
    return result_num, result


def draw_plot_speed(value_x, value_y, y_ticks, type=1, color='#FF0000'):
    series_count = 2
    if type == 1:
        plt.figure(1, figsize=(8, 2.5))
    elif type == 3:
        plt.figure(1, figsize=(8, 2.5))
    y_ticks_labels = []
    for i in range(len(y_ticks)):
        secs = y_ticks[i]
        minutes_val = floor(secs / 60)
        seconds_val = int(secs % 60)
        y_ticks_labels.append('{}\'{}\"'.format(minutes_val, seconds_val))
    for i in range(series_count):
        if type == 1:
            plt.subplot(int(series_count / 2), 2, i + 1)
        elif type == 3:
            plt.subplot(int(series_count / 2), 2, i + 1, facecolor=color)
        plt.yticks(y_ticks, y_ticks_labels)
        plt.xticks([0, 3, 6, 9], ['0(min)', '3', '6', '9'])
        c = np.mean(value_y[i])
        plt.axhline(y=c, color="gray", ls='--', lw=2, alpha=0.5)
        ax = plt.gca()
        ax.yaxis.tick_right()
        if min(y_ticks) != 0:
            ax.set_ylim(y_ticks[0] - 0.5 * (y_ticks[1] - y_ticks[0]),
                        y_ticks[-1] + 0.5 * (y_ticks[1] - y_ticks[0]))
        else:
            ax.set_ylim(y_ticks[0], y_ticks[-1] + 0.5 * (y_ticks[1] - y_ticks[0]))
        ax.set_xlim(0, 10)
        fill_aera_x = value_x[i].tolist()
        fill_aera_x.insert(0, 0)
        fill_aera_x.append(10)
        ax.invert_yaxis()
        if type == 1:
            if not isinstance(value_y[i], list):
                fill_aera_y = value_y[i].tolist()
                fill_aera_y.insert(0, y_ticks[-1] + 0.5 * (y_ticks[1] - y_ticks[0]))
                fill_aera_y.append(y_ticks[-1] + 0.5 * (y_ticks[1] - y_ticks[0]))
                plt.fill(fill_aera_x, fill_aera_y, color=color)
            else:
                plt.fill([0, 10, 10, 0], [y_ticks[-1] + 0.5 * (y_ticks[1] - y_ticks[0]) + 10,
                                          y_ticks[-1] + 0.5 * (y_ticks[1] - y_ticks[0]), value_y[i][0], value_y[i][0]],
                         color='#E35A5A')
            plt.plot(value_x[i], value_y[i], linewidth=2, color=color)  # 折线
        elif type == 3:
            plt.bar(value_x[i], value_y[i], 1, color='w')
    st.pyplot(plt)


def draw_plot_1(value_x, value_y, y_ticks):
    series_count = 2
    plt.figure(1, figsize=(8, 2.5))
    for i in range(series_count):
        plt.subplot(int(series_count / 2), 2, i + 1)
        plt.yticks(y_ticks)
        plt.xticks([0, 3, 6, 9], ['0(min)', '3', '6', '9'])
        c = np.mean(value_y[i])
        plt.axhline(y=c, color="gray", ls='--', lw=2, alpha=0.5)
        ax = plt.gca()
        ax.yaxis.tick_right()
        if min(value_y[i]) != 0:
            ax.set_ylim(y_ticks[0] - 0.5 * (y_ticks[1] - y_ticks[0]),
                        y_ticks[-1] + 0.5 * (y_ticks[1] - y_ticks[0]))
        else:
            ax.set_ylim(y_ticks[0], y_ticks[-1] + 0.5 * (y_ticks[1] - y_ticks[0]))
        ax.set_xlim(0, 10)
        fill_aera_x = value_x[i].tolist()
        fill_aera_x.insert(0, 0)
        fill_aera_x.append(10)
        if not isinstance(value_y[i], list):
            fill_aera_y = value_y[i].tolist()
            fill_aera_y.insert(0, 0)
            fill_aera_y.append(0)
            plt.fill(fill_aera_x, fill_aera_y, color='#E35A5A')
        else:
            plt.fill([0, 10, 10, 0], [value_y[i][0], value_y[i][0], 0, 0], color='#E35A5A')
        plt.plot(value_x[i], value_y[i], linewidth=2, color='#E35A5A')  # 折线
    st.pyplot(plt)


# 起点一定为0
def draw_plot_2(value_x, value_y, y_ticks, type=1, color='#61CE86'):
    series_count = 2
    plt.figure(1, figsize=(8, 2.5))
    for i in range(series_count):
        plt.subplot(int(series_count / 2), 2, i + 1)
        plt.yticks(y_ticks)
        plt.xticks([0, 3, 6, 9], ['0(min)', '3', '6', '9'])
        c = np.mean(value_y[i])
        plt.axhline(y=c, color="gray", ls='--', lw=2, alpha=0.5)
        ax = plt.gca()
        ax.yaxis.tick_right()
        ax.set_ylim(0, y_ticks[-1] + 0.5 * (y_ticks[1] - y_ticks[0]))
        ax.set_xlim(0, 10)
        fill_aera_x = value_x[i].tolist()
        fill_aera_x.insert(0, 0)
        fill_aera_x.append(10)
        if not isinstance(value_y[i], list) and type == 1:
            fill_aera_y = value_y[i].tolist()
            fill_aera_y.insert(0, 0)
            fill_aera_y.append(0)
            plt.fill(fill_aera_x, fill_aera_y, color=color)
            plt.plot(value_x[i], value_y[i], linewidth=2, color=color)  # 折线
        elif type == 1:
            plt.fill([0, 10, 10, 0], [value_y[i][0], value_y[i][0], 0, 0], color=color)
            plt.plot(value_x[i], value_y[i], linewidth=2, color=color)
        elif type == 2:
            plt.scatter(value_x[i], value_y[i], s=9, color=color)
        elif type == 3:
            plt.bar(value_x[i], value_y[i], 1, color=color)
    st.pyplot(plt)


def draw_plot_3(value_x, value_y, y_ticks):
    series_count = 2
    plt.figure(1, figsize=(8, 2.5))
    for i in range(series_count):
        plt.subplot(int(series_count / 2), 2, i + 1)
        plt.yticks(y_ticks)
        plt.xticks([0, 3, 6, 9], ['0(min)', '3', '6', '9'])
        c = np.mean(value_y[i])
        ax = plt.gca()
        ax.yaxis.tick_right()
        ax.set_ylim(y_ticks[0] - 0.5 * (y_ticks[1] - y_ticks[0]),
                    y_ticks[-1] + 0.5 * (y_ticks[1] - y_ticks[0]))
        ax.set_xlim(0, 10)
        fill_aera_x = value_x[i].tolist()
        fill_aera_x.insert(0, 0)
        fill_aera_x.append(10)
        if not isinstance(value_y[i], list):
            fill_aera_y = value_y[i].tolist()
            fill_aera_y.insert(0, y_ticks[0] - 0.5 * (y_ticks[1] - y_ticks[0]))
            fill_aera_y.append(y_ticks[0] - 0.5 * (y_ticks[1] - y_ticks[0]))
            plt.fill(fill_aera_x, fill_aera_y, color='#5FCEFF')
        else:
            plt.fill([0, 10, 10, 0], [value_y[i][0], value_y[i][0], 0, 0], color='#5FCEFF')
        plt.plot(value_x[i], value_y[i], linewidth=2, color='#5FCEFF')  # 折线
        plt.axhline(y=c, color="gray", ls='--', lw=2, alpha=0.5)
    st.pyplot(plt)


def generate_bar_data(max_val, min_val):
    value_x_result = []
    value_y_result = []
    for i in range(10):
        if min_val != max_val:
            demo_value_y = np.random.randint(min_val, max_val, 21)
        else:
            demo_value_y = [min_val] * 21
        demo_value_y[3] = min_val
        demo_value_y[-3] = max_val
        demo_value_x = np.arange(0, 10.1, 0.5)
        value_x_result.append(demo_value_x)
        value_y_result.append(demo_value_y)
    return value_x_result, value_y_result


def get_heart_data():
    value_heart_y = [86, 96, 85, 87, 98, 100, 99, 99, 100, 105, 106, 107, 100, 99, 98, 96, 96, 96, 97, 96, 106, 109,
                     113, 114, 113, 113, 111, 107, 105, 102, 101, 102, 102, 108, 110, 109, 105, 105, 104, 104, 104, 102,
                     103, 101, 106, 113, 114, 114, 108, 110, 111, 115, 118, 117, 118, 117, 118, 119, 121, 121, 117, 115,
                     113, 110, 108, 111, 114, 110, 108, 106, 105, 101, 100, 110, 111, 110, 107, 106, 107, 108, 113, 114,
                     111, 112, 114, 115, 119, 118, 111, 108, 107, 104, 105, 102, 101, 103, 103, 106, 106, 110, 114, 117,
                     118, 112, 113, 112, 118, 119, 120, 121, 122, 126, 136, 136, 137, 139, 136, 135, 134, 130, 128, 131,
                     129, 124, 125, 118, 116, 117, 116, 123, 126, 128, 132, 138, 130, 131, 134, 144, 144, 137, 136, 134,
                     131, 128, 126, 123, 120, 119, 118, 117, 120, 123, 126, 129, 135, 126, 122, 123, 118, 123, 125, 126,
                     130, 133, 129, 127, 130, 137, 140, 144, 148, 148, 141, 140, 137, 131, 130, 134, 133, 128, 122, 120,
                     117, 113, 121, 117, 116, 99, 97, 99, 96, 98, 101, 102, 101, 99, 98, 98, 97, 93]
    value_heart_x = np.arange(0, 10.1, 0.05)

    value_heart_y = [86, 98, 100, 100, 96, 106, 113, 105, 102, 105, 104, 106, 108, 118, 118, 117, 108, 108, 100, 107, 113, 114, 111, 105, 103, 114, 113, 120, 136, 136, 128, 125, 116, 132, 134, 136, 126, 118, 126, 122, 125, 129, 140, 141, 130, 122, 121, 97, 101, 98, 97]
    value_heart_x = np.arange(0, 10.1, 0.2)

    # value_heart_y = [86, 85, 98, 99, 100, 106, 100, 98, 96, 97, 106, 113, 113, 111, 105, 101, 102, 110, 105, 104, 104,
    #                  103, 106, 114, 108, 111, 118, 118, 118, 121, 117, 113, 108, 114, 108, 105, 100, 111, 107, 107, 113,
    #                  111, 114, 119, 111, 107, 105, 101, 103, 106, 114, 118, 113, 118, 120, 122, 136, 137, 136, 134, 128,
    #                  129, 125, 116, 116, 126, 132, 130, 134, 144, 136, 131, 126, 120, 118, 120, 126, 135, 122, 118, 125,
    #                  130, 129, 130, 140, 148, 141, 137, 130, 133, 122, 117, 121, 116, 97, 96, 101, 101, 98, 97]
    # value_heart_x = np.arange(0, 10.1, 0.1)

    value_heart_y = [86, 96, 85, 87, 98, 100, 99, 99, 100, 105, 106, 107, 100, 99, 98, 96, 96, 96, 97, 96, 106, 109,
                     113, 114, 113, 113, 111, 107, 105, 102, 101, 102, 102, 108, 110, 109, 105, 105, 104, 104, 104, 102,
                     103, 101, 106, 113, 114, 114, 108, 110, 111, 115, 118, 117, 118, 117, 118, 119, 121, 121, 117, 115,
                     113, 110, 108, 111, 114, 110, 108, 106, 105, 101, 100, 110, 111, 110, 107, 106, 107, 108, 113, 114,
                     111, 112, 114, 115, 119, 118, 111, 108, 107, 104, 105, 102, 101, 103, 103, 106, 106, 110, 114, 117,
                     118, 112, 113, 112, 118, 119, 120, 121, 122, 126, 136, 136, 137, 139, 136, 135, 134, 130, 128, 131,
                     129, 124, 125, 118, 116, 117, 116, 123, 126, 128, 132, 138, 130, 131, 134, 144, 144, 137, 136, 134,
                     131, 128, 126, 123, 120, 119, 118, 117, 120, 123, 126, 129, 135, 126, 122, 123, 118, 123, 125, 126,
                     130, 133, 129, 127, 130, 137, 140, 144, 148, 148, 141, 140, 137, 131, 130, 134, 133, 128, 122, 120,
                     117, 113, 121, 117, 116, 99, 97, 99, 96, 98, 101, 102, 101, 99, 98, 98, 97, 93, 86, 85, 98, 99, 100, 106, 100, 98, 96, 97, 106, 113, 113, 111, 105, 101, 102, 110, 105, 104, 104,
                      103, 106, 114, 108, 111, 118, 118, 118, 121, 117, 113, 108, 114, 108, 105, 100, 111, 107, 107, 113,
                      111, 114, 119, 111, 107, 105, 101, 103, 106, 114, 118, 113, 118, 120, 122, 136, 137, 136, 134, 128,
                      129, 125, 116, 116, 126, 132, 130, 134, 144, 136, 131, 126, 120, 118, 120, 126, 135, 122, 118, 125,
                      130, 129, 130, 140, 148, 141, 137, 130, 133, 122, 117, 121, 116, 97, 96, 101, 101, 98, 97]
    value_heart_x = np.arange(0, 10.1, 0.0375)
    return value_heart_x, value_heart_y

def get_scatter_data():
    value_heart_y = [86, 96, 85, 87, 98, 100, 99, 99, 100, 105, 106, 107, 100, 99, 98, 96, 96, 96, 97, 96, 106, 109,
                     113, 114, 113, 113, 111, 107, 105, 102, 101, 102, 102, 108, 110, 109, 105, 105, 104, 104, 104, 102,
                     103, 101, 106, 113, 114, 114, 108, 110, 111, 115, 118, 117, 118, 117, 118, 119, 121, 121, 117, 115,
                     113, 110, 108, 111, 114, 110, 108, 106, 105, 101, 100, 110, 111, 110, 107, 106, 107, 108, 113, 114,
                     111, 112, 114, 115, 119, 118, 111, 108, 107, 104, 105, 102, 101, 103, 103, 106, 106, 110, 114, 117,
                     118, 112, 113, 112, 118, 119, 120, 121, 122, 126, 136, 136, 137, 139, 136, 135, 134, 130, 128, 131,
                     129, 124, 125, 118, 116, 117, 116, 123, 126, 128, 132, 138, 130, 131, 134, 144, 144, 137, 136, 134,
                     131, 128, 126, 123, 120, 119, 118, 117, 120, 123, 126, 129, 135, 126, 122, 123, 118, 123, 125, 126,
                     130, 133, 129, 127, 130, 137, 140, 144, 148, 148, 141, 140, 137, 131, 130, 134, 133, 128, 122, 120,
                     117, 113, 121, 117, 116, 99, 97, 99, 96, 98, 101, 102, 101, 99, 98, 98, 97, 93]
    value_heart_x = np.arange(0, 10.1, 0.05)
    #
    # value_heart_y = [86, 98, 100, 100, 96, 106, 113, 105, 102, 105, 104, 106, 108, 118, 118, 117, 108, 108, 100, 107, 113, 114, 111, 105, 103, 114, 113, 120, 136, 136, 128, 125, 116, 132, 134, 136, 126, 118, 126, 122, 125, 129, 140, 141, 130, 122, 121, 97, 101, 98, 97]
    # value_heart_x = np.arange(0, 10.1, 0.2)
    #
    # # value_heart_y = [86, 85, 98, 99, 100, 106, 100, 98, 96, 97, 106, 113, 113, 111, 105, 101, 102, 110, 105, 104, 104,
    # #                  103, 106, 114, 108, 111, 118, 118, 118, 121, 117, 113, 108, 114, 108, 105, 100, 111, 107, 107, 113,
    # #                  111, 114, 119, 111, 107, 105, 101, 103, 106, 114, 118, 113, 118, 120, 122, 136, 137, 136, 134, 128,
    # #                  129, 125, 116, 116, 126, 132, 130, 134, 144, 136, 131, 126, 120, 118, 120, 126, 135, 122, 118, 125,
    # #                  130, 129, 130, 140, 148, 141, 137, 130, 133, 122, 117, 121, 116, 97, 96, 101, 101, 98, 97]
    # # value_heart_x = np.arange(0, 10.1, 0.1)
    #
    # value_heart_y = [86, 96, 85, 87, 98, 100, 99, 99, 100, 105, 106, 107, 100, 99, 98, 96, 96, 96, 97, 96, 106, 109,
    #                  113, 114, 113, 113, 111, 107, 105, 102, 101, 102, 102, 108, 110, 109, 105, 105, 104, 104, 104, 102,
    #                  103, 101, 106, 113, 114, 114, 108, 110, 111, 115, 118, 117, 118, 117, 118, 119, 121, 121, 117, 115,
    #                  113, 110, 108, 111, 114, 110, 108, 106, 105, 101, 100, 110, 111, 110, 107, 106, 107, 108, 113, 114,
    #                  111, 112, 114, 115, 119, 118, 111, 108, 107, 104, 105, 102, 101, 103, 103, 106, 106, 110, 114, 117,
    #                  118, 112, 113, 112, 118, 119, 120, 121, 122, 126, 136, 136, 137, 139, 136, 135, 134, 130, 128, 131,
    #                  129, 124, 125, 118, 116, 117, 116, 123, 126, 128, 132, 138, 130, 131, 134, 144, 144, 137, 136, 134,
    #                  131, 128, 126, 123, 120, 119, 118, 117, 120, 123, 126, 129, 135, 126, 122, 123, 118, 123, 125, 126,
    #                  130, 133, 129, 127, 130, 137, 140, 144, 148, 148, 141, 140, 137, 131, 130, 134, 133, 128, 122, 120,
    #                  117, 113, 121, 117, 116, 99, 97, 99, 96, 98, 101, 102, 101, 99, 98, 98, 97, 93, 86, 85, 98, 99, 100, 106, 100, 98, 96, 97, 106, 113, 113, 111, 105, 101, 102, 110, 105, 104, 104,
    #                   103, 106, 114, 108, 111, 118, 118, 118, 121, 117, 113, 108, 114, 108, 105, 100, 111, 107, 107, 113,
    #                   111, 114, 119, 111, 107, 105, 101, 103, 106, 114, 118, 113, 118, 120, 122, 136, 137, 136, 134, 128,
    #                   129, 125, 116, 116, 126, 132, 130, 134, 144, 136, 131, 126, 120, 118, 120, 126, 135, 122, 118, 125,
    #                   130, 129, 130, 140, 148, 141, 137, 130, 133, 122, 117, 121, 116, 97, 96, 101, 101, 98, 97]
    # value_heart_x = np.arange(0, 10.1, 0.0375)
    return value_heart_x, value_heart_y


def generate_data(max_val, min_val):
    value_x_result = []
    value_y_result = []

    for i in range(10):
        if min_val != max_val:
            demo_value_y = np.random.randint(min_val, max_val, 101)
        else:
            demo_value_y = [min_val] * 101
        demo_value_y[3] = min_val
        demo_value_y[-3] = max_val
        demo_value_x = np.arange(0, 10.1, 0.1)
        value_x_result.append(demo_value_x)
        value_y_result.append(demo_value_y)
    return value_x_result, value_y_result


# graph_type   1-折线  2-散点   3-段
# limtype    1-心率等大于等于0   2-海拔等可小于0  3-低点一定等于0
def draw_plotly_graph(x_values, y_values, y_ticks, limtype=1, graph_type=1, line_color='#F54F66', fillcolor='#FFEBEB',
                      speed_type=0):
    average_val = np.mean(y_values)
    yaxis_range = []
    time_label = []
    if speed_type != 0:
        for i in range(len(y_ticks)):
            secs = y_ticks[i]
            min_res = floor(secs / 60)
            sec_res = int(secs % 60)
            res_str = '{}\'{}\'\''.format(min_res, sec_res)
            time_label.append(res_str)
    if len(time_label) != 0:
        y_label = time_label
    else:
        y_label = y_ticks

    if limtype == 1:
        if speed_type == 1:
            if min(y_ticks) != 0:
                yaxis_range = [y_ticks[-1] + 0.5 * (y_ticks[1] - y_ticks[0]),
                               y_ticks[0] - 0.5 * (y_ticks[1] - y_ticks[0])]
            else:
                yaxis_range = [y_ticks[-1] + 0.5 * (y_ticks[1] - y_ticks[0]), y_ticks[0]]
        else:
            if min(y_ticks) != 0:
                yaxis_range = [y_ticks[0] - 0.5 * (y_ticks[1] - y_ticks[0]),
                               y_ticks[-1] + 0.5 * (y_ticks[1] - y_ticks[0])]
            else:
                yaxis_range = [y_ticks[0], y_ticks[-1] + 0.5 * (y_ticks[1] - y_ticks[0])]
    elif limtype == 2:
        yaxis_range = [y_ticks[0] - 0.5 * (y_ticks[1] - y_ticks[0]), y_ticks[-1] + 0.5 * (y_ticks[1] - y_ticks[0])]
    elif limtype == 3:
        yaxis_range = [0, y_ticks[-1] + 0.5 * (y_ticks[1] - y_ticks[0])]
    elif limtype == 4:
        if min(y_ticks) > 0:
            yaxis_range = [y_ticks[0] - 0.5 * (y_ticks[1] - y_ticks[0]),
                           y_ticks[-1] + 0.5 * (y_ticks[1] - y_ticks[0])]
        else:
            yaxis_range = [0, y_ticks[-1] + 0.5 * (y_ticks[1] - y_ticks[0])]
    elif limtype == 'zepp':
        yaxis_range = [y_ticks[0], y_ticks[-1]]
    elif limtype == 9:
        yaxis_range = [0, 230]
    go_average = go.Scatter(
        x=x_values,
        y=[average_val] * len(x_values),
        line=dict(dash='dash', color='#000000'),
        opacity=0.3,
        hoverinfo='none',
        showlegend=False
    )
    if graph_type == 1:
        go_val = go.Scatter(
            x=x_values,
            y=y_values,
            mode='lines',
            hoverinfo='y',
            fillcolor=fillcolor,
            # fill='tozeroy',
            line=dict(shape='linear', color=line_color, width=4),  # spline,hv,vh,linear,hvh,vhv
            showlegend=False,
            hoveron='points'
        )
        low_val_num = yaxis_range[0]
        go_down = go.Scatter(
            x=x_values,
            y=[low_val_num] * len(x_values),
            line=dict(dash='dash', color='#000000', width=0),
            opacity=0.1,
            fillcolor=fillcolor,
            fill='tonexty',
            hoverinfo='none',
            showlegend=False
        )

        fig = go.Figure([go_val, go_down, go_average])
    elif graph_type == 2:
        go_val = go.Scatter(
            x=x_values,
            y=y_values,
            mode='markers',
            hoverinfo='y',
            marker=dict(color=line_color),
            showlegend=False,
            hoveron='points'
        )
        fig = go.Figure([go_val, go_average])
    elif graph_type == 3:
        go_val = go.Scatter(
            x=x_values,
            y=y_values,
            mode='lines',
            hoverinfo='y',
            fillcolor=fillcolor,
            # fill='tozeroy',
            line=dict(shape='hv', color=line_color),  # spline,hv,vh,linear,hvh,vhv
            showlegend=False,
            hoveron='points'
        )
        low_val_num = yaxis_range[0]
        go_down = go.Scatter(
            x=x_values,
            y=[low_val_num] * len(x_values),
            line=dict(dash='dash', color='#000000', width=0),
            opacity=0.1,
            fillcolor=fillcolor,
            fill='tonexty',
            hoverinfo='none',
            showlegend=False
        )
        fig = go.Figure([go_val, go_down, go_average])

    fig.update_layout(
        yaxis=dict(
            tickmode='array',
            tickvals=y_ticks,
            ticktext=y_label,
            range=yaxis_range,
            showgrid=True,
            # gridcolor='#CDCDCD',
            # gridwidth=0.1,
            zeroline=False,
            showline=False,
            linecolor='#A3A3A3',
            linewidth=2,
            side='right'
        ),
        xaxis=dict(
            tickmode='array',
            tickvals=[0, 3, 6, 9],
            ticktext=['0(分钟)', '3', '6', '9'],
            range=[0, 10],
            showgrid=False,
            showline=False,
            zeroline=False,
            linecolor='#A3A3A3',
            linewidth=2,
        ),
        dragmode=False,
        height=400,
        margin=dict(t=30, b=20)
    )
    return fig


def heart_rate_graph():
    min_val = value_selection[0]
    max_val = value_selection[1]
    result_list = start_above_zero(max_val, min_val)
    # str_val = '##### 方案一坐标轴计算结果：' + str(result_list)
    # st.markdown(str_val)
    with st.spinner('生成数据...'):
        time.sleep(0.5)
        demo_value_x, demo_value_y = get_heart_data()
    with st.spinner('绘制中...'):
        # draw_plot_1(demo_value_x, demo_value_y, result_list)
        st.markdown('### 可交互视图（试验）- 0625')
        st.markdown('#### 方案一（' + str(result_list)[1:-1] + '）')
        fig1 = draw_plotly_graph(demo_value_x, demo_value_y, result_list)
        mifit_case1 = [40, 80, 120, 160, 200]
        fig2 = draw_plotly_graph(demo_value_x, demo_value_y, mifit_case1, 9, 1)
        st.plotly_chart(fig1)
        st.markdown('#### 方案二（' + str(mifit_case1)[1:-1] + '）')
        st.plotly_chart(fig2)
        st.success('绘制完成')


def zepp_latitude_ticks(max_val, min_val):
    A = min_val
    min_axis = int(np.floor(A))
    while min_axis % 5 != 0:
        min_axis = min_axis - 1
    axis_max = min_axis
    interval = 0
    if max_val - min_val <= 30:
        ticks_interval = 10
        return [min_axis,
                min_axis + 1 * ticks_interval,
                min_axis + 2 * ticks_interval,
                min_axis + 3 * ticks_interval]
    else:
        m = max_val  # m为数据的最大值
        print(m)
        while m >= axis_max:
            interval = interval + 5
            axis_max = min_axis + interval * 3
        return [min_axis,
                min_axis + 1 * interval,
                min_axis + 2 * interval,
                min_axis + 3 * interval]


def latitude_graph():
    min_val = value_selection[0]
    max_val = value_selection[1]
    result_list = start_below_zero(max_val, min_val)
    zepp_case = zepp_latitude_ticks(max_val, min_val)
    st.write("选择了", value_selection)
    # str_val = '##### 方案一坐标轴计算结果：' + str(result_list)
    # st.markdown(str_val)
    with st.spinner('生成数据...'):
        time.sleep(0.5)
        demo_value_x, demo_value_y = generate_data(max_val, min_val)
    with st.spinner('绘制中...'):
        # draw_plot_3(demo_value_x, demo_value_y, result_list)
        st.markdown('### 可交互视图（试验）- 0625')
        st.markdown('#### 方案一（' + str(result_list)[1:-1] + '）')
        fig1 = draw_plotly_graph(demo_value_x[0], demo_value_y[0], result_list, limtype=2, line_color='#30C1FF',
                                 fillcolor='#30C1FF')  # fillcolor='#2FC8E4'
        st.plotly_chart(fig1)
        st.markdown('#### 方案二（' + str(zepp_case)[1:-1] + '）')
        fig2 = draw_plotly_graph(demo_value_x[0], demo_value_y[0], zepp_case, limtype=4, line_color='#30C1FF',
                                 fillcolor='#30C1FF')  # fillcolor='#2FC8E4'
        st.plotly_chart(fig2)
        st.success('绘制完成')


def zepp_stroke_fre_swim_ticks(max_val, min_val):
    A = max_val
    B = A / 3
    C = int(np.ceil(B))
    while C % 5 != 0:
        C = C + 1
    result = [0, C, 2 * C, 3 * C]
    return result


def zepp_stroke_fre_swim_ticks_upgrade(max_val, min_val):
    A = max_val
    B = A / 4
    C = int(np.ceil(B))
    while C % 5 != 0:
        C = C + 1
    result = [0, C, 2 * C, 3 * C, 4 * C]
    return result


def zepp_running_cadence_ticks(max_val, min_val):
    A = max_val
    B = min_val
    C = A
    Z = B
    while C % 10 != 0:
        C = C + 1
    while Z % 10 != 0:
        Z = Z - 1
    D = (C - Z) / 3
    E = D / 5
    F = int(np.ceil(E))
    if C - Z <= 60:
        ticks_interval = 20
    else:
        ticks_interval = F * 5
    result = [Z,
              Z + 1 * ticks_interval,
              Z + 2 * ticks_interval,
              Z + 3 * ticks_interval]
    return result


def start_by_zero_graph(type=1, color='#61CE86', sport='sudu'):
    min_val = value_selection[0]
    max_val = value_selection[1]
    with st.spinner('生成数据...'):
        time.sleep(0.5)
        if type == 1 or type == 2:
            demo_value_x, demo_value_y = generate_data(max_val, min_val)
        elif type == 3:
            demo_value_x, demo_value_y = generate_bar_data(max_val, min_val)
    with st.spinner('绘制中...'):
        result_list = start_with_zero(max_val)
        # str_val = '##### 方案一坐标轴计算结果：' + str(result_list)
        # st.markdown(str_val)
        #
        # draw_plot_2(demo_value_x, demo_value_y, result_list, type, color)
        st.markdown('### 可交互视图（试验）- 0625')
        st.markdown('#### 方案一（' + str(result_list)[1:-1] + '）')
        fig1 = draw_plotly_graph(demo_value_x[0], demo_value_y[0], result_list, limtype=3, line_color=color,
                                 fillcolor=color, graph_type=type)  # fillcolor='#2FC8E4'
        st.plotly_chart(fig1)

        if sport == 'sudu':
            zepp_case = zepp_speed_km_ticks(max_val, min_val)
        elif sport == 'huapinyy' or sport == 'swolf':
            zepp_case = zepp_stroke_fre_swim_ticks(max_val, min_val)
            zepp_case_upgrade = zepp_stroke_fre_swim_ticks_upgrade(max_val, min_val)
        elif sport == 'bupin':
            zepp_case = zepp_running_cadence_ticks(max_val, min_val)

        if sport in ['sudu']:
            st.markdown('#### 方案二（' + str(zepp_case)[1:-1] + '）')
            fig2 = draw_plotly_graph(demo_value_x[0], demo_value_y[0], zepp_case, limtype=2, line_color=color,
                                     fillcolor=color, graph_type=type)  # fillcolor='#2FC8E4'
            st.plotly_chart(fig2)
        elif sport in ['huapinyy', 'swolf']:
            st.markdown('#### 方案二（' + str(zepp_case)[1:-1] + '）')
            fig2 = draw_plotly_graph(demo_value_x[0], demo_value_y[0], zepp_case, limtype=3, line_color=color,
                                     fillcolor=color, graph_type=type)  # fillcolor='#2FC8E4'
            st.plotly_chart(fig2)
            st.markdown('#### 方案二 + 改进（' + str(zepp_case_upgrade)[1:-1] + '）')
            fig3 = draw_plotly_graph(demo_value_x[0], demo_value_y[0], zepp_case_upgrade, limtype=3, line_color=color,
                                     fillcolor=color, graph_type=type)  # fillcolor='#2FC8E4'
            st.plotly_chart(fig3)
        elif sport in ['bupin']:
            st.markdown('#### 方案二（' + str(zepp_case)[1:-1] + '）')
            fig2 = draw_plotly_graph(demo_value_x[0], demo_value_y[0], zepp_case, limtype=1, line_color=color,
                                     fillcolor=color, graph_type=type)  # fillcolor='#2FC8E4'
            st.plotly_chart(fig2)
            upg = start_with_zero_upgrade(max_val)
            st.markdown('#### 方案一改进（' + str(zepp_case)[1:-1] + '）')
            fig3 = draw_plotly_graph(demo_value_x[0], demo_value_y[0], upg, limtype=3, line_color=color,
                                     fillcolor=color, graph_type=type)  # fillcolor='#2FC8E4'
            st.plotly_chart(fig3)
        st.success('绘制完成')


def zepp_pace_noswim(max_value, min_value):
    A = min_value
    B = max_value
    C = B - A
    if C >= 180:
        if C % 30 == 0:
            ticks_interval = 30 * int(C / 30)
        else:
            ticks_interval = 30 * int(np.ceil(C / 30))
    else:
        ticks_interval = 60
    if B >= 1500:
        result = [1500 - 3 * ticks_interval,
                  1500 - 2 * ticks_interval,
                  1500 - 1 * ticks_interval,
                  1500]
    else:
        while B % 30 != 0:
            B = B + 1
        result = [B - 3 * ticks_interval,
                  B - 2 * ticks_interval,
                  B - 1 * ticks_interval,
                  B]
    return result


def zepp_pace_swim(max_value, min_value):
    # A = max_value
    # B = min_value
    # if A - B <= 90 and A < 150:
    # st.warning('Zepp 方案说明不明确')
    pass


def for_speed_graph_1(type=1, color='#FF0000', yy=False):
    try:
        min_val_min, min_val_sec = map(int, speed_low.split(':'))
        max_val_min, max_val_sec = map(int, speed_high.split(':'))
        min_value = min_val_min * 60 + min_val_sec
        max_value = max_val_min * 60 + max_val_sec
        if max_value < min_value:
            print('数值关系错误！')
    except Exception as e:
        print('数值输入错误！')
    result_list = speed_graph(max_value, min_value)[0]
    result_list_2 = speed_graph2(max_value, min_value)[0]
    result_list_3 = speed_graph3(max_value, min_value)[0]
    if yy == False:
        zepp_case = zepp_pace_noswim(max_value, min_value)
    else:
        # zepp_case = zepp_pace_swim(max_value, min_value)
        # st.error('Zepp 方案说明待确认，结果暂不予展示')
        pass
    # str_val = '##### 方案一坐标轴计算结果：' + str(result_list)
    # st.markdown(str_val)
    with st.spinner('生成数据...'):
        time.sleep(0.5)
        if type == 1:
            demo_value_x, demo_value_y = generate_data(max_value, min_value)
        elif type == 3:
            demo_value_x, demo_value_y = generate_bar_data(max_value, min_value)
    with st.spinner('绘制中...'):
        st.markdown('#### 方案一（' + str(result_list)[1:-1] + '）')
        # draw_plot_speed(demo_value_x, demo_value_y, result_list, type=type, color='#2AC288')
        # print(result_list)
        fig1 = draw_plotly_graph(demo_value_x[0], demo_value_y[0], result_list, limtype=1, line_color='#2AC288',
                                 fillcolor='#2AC288', graph_type=type, speed_type=1)  # fillcolor='#2FC8E4'
        st.plotly_chart(fig1)

    # str_val = '##### 方案二坐标轴计算结果：' + str(result_list_2)
    # st.markdown(str_val)
    with st.spinner('绘制中...'):
        st.markdown('#### 方案二（' + str(result_list_2)[1:-1] + '）')
        # draw_plot_speed(demo_value_x, demo_value_y, result_list_2, type=type, color='#2AC288')
        fig2 = draw_plotly_graph(demo_value_x[0], demo_value_y[0], result_list_2, limtype=1, line_color='#2AC288',
                                 fillcolor='#2AC288', graph_type=type, speed_type=1)  # fillcolor='#2FC8E4'
        st.plotly_chart(fig2)

    # str_val = '##### 方案三坐标轴计算结果：' + str(result_list_3)
    # st.markdown(str_val)
    with st.spinner('绘制中...'):
        st.markdown('#### 方案三（' + str(result_list_3)[1:-1] + '）')
        # draw_plot_speed(demo_value_x, demo_value_y, result_list_3, type=type, color='#2AC288')
        fig3 = draw_plotly_graph(demo_value_x[0], demo_value_y[0], result_list_3, limtype=1, line_color='#2AC288',
                                 fillcolor='#2AC288', graph_type=type, speed_type=1)  # fillcolor='#2FC8E4'
        st.plotly_chart(fig3)

        try:
            st.markdown('#### 方案四（' + str(zepp_case)[1:-1] + '）')
            # draw_plot_speed(demo_value_x, demo_value_y, result_list_3, type=type, color='#2AC288')
            fig4 = draw_plotly_graph(demo_value_x[0], demo_value_y[0], zepp_case, limtype=1, line_color='#2AC288',
                                     fillcolor='#2AC288', graph_type=type, speed_type=1)  # fillcolor='#2FC8E4'
            st.plotly_chart(fig4)
        except Exception as e:
            st.error('方案说明待确认')


st.set_page_config(page_title='图表绘制模拟')
st.header('图表绘制方案模拟')
st.subheader('2021.06.24')

st.markdown(f'### 1. 选择图表类型')
selection = st.selectbox('图表类型',
                         ('心率',
                          '速度',
                          '配速（非游泳）',
                          '配速（游泳）',
                          '阻力',
                          '海拔',
                          '划频（游泳）',
                          'Swolf（游泳）',
                          '步频',
                          '起跳高度',
                          '频率（跳绳）',
                          '频率（划船机）',
                          '踏频（室内单车）'))

# 起点一定不小于0：心率 √
# 起点一定为0：速度 √、阻力 √、划频（游泳） √、Swolf（游泳） √、步频 √、起跳高度 √、频率（跳绳） √、频率（划船机） √、踏频（室内单车） √
# 起点可能小于0：海拔 √
# 配速相关：配速（游泳）、配速（非游泳）

if selection == '心率':
    st.markdown(f'### 2. 选取数据范围')
    if st.button('随机生成'):
        random_value = np.random.randint(0, 220, 2)
        random_value.sort()
        value_selection = st.slider('数值范围', min_value=0, max_value=220,
                                    value=(int(random_value[0]), int(random_value[1])))
    else:
        value_selection = st.slider('数值范围', min_value=0, max_value=220, value=(60, 140))
    st.info('已选定方案二')
    heart_rate_graph()
elif selection == '海拔':
    st.markdown(f'### 2. 选取数据范围')
    if st.button('随机生成'):
        random_value = np.random.randint(300, 400, 2)
        random_value.sort()
        value_selection = st.slider('数值范围', min_value=-100, max_value=300,
                                    value=(int(random_value[0]), int(random_value[1])))
    else:
        value_selection = st.slider('数值范围', min_value=-100, max_value=300, value=(281, 300))
    st.info('已选定方案一')
    latitude_graph()
elif selection == '速度':
    st.markdown(f'### 2. 选取数据范围')
    if st.button('随机生成'):
        random_value = np.random.randint(0, 200, 2)
        random_value.sort()
        value_selection = st.slider('数值范围', min_value=0, max_value=200,
                                    value=(int(random_value[0]), int(random_value[1])))
    else:
        value_selection = st.slider('数值范围', min_value=0, max_value=200, value=(12, 24))
    st.info('已选定方案一')
    start_by_zero_graph(sport='sudu')
elif selection == '阻力':
    st.markdown(f'### 2. 选取数据范围')
    if st.button('随机生成'):
        random_value = np.random.randint(0, 60, 2)
        random_value.sort()
        value_selection = st.slider('数值范围', min_value=0, max_value=60,
                                    value=(int(random_value[0]), int(random_value[1])))
    else:
        value_selection = st.slider('数值范围', min_value=0, max_value=60, value=(12, 24))
    st.info('已选定方案一')
    start_by_zero_graph(type=3, sport='zuli')
elif selection == '步频':
    st.markdown(f'### 2. 选取数据范围')
    if st.button('随机生成'):
        random_value = np.random.randint(0, 300, 2)
        random_value.sort()
        value_selection = st.slider('数值范围', min_value=0, max_value=300,
                                    value=(int(random_value[0]), int(random_value[1])))
    else:
        value_selection = st.slider('数值范围', min_value=0, max_value=300, value=(45, 135))
    st.info('已选定方案三（方案一改进）')
    start_by_zero_graph(2, sport='bupin')
elif selection == '配速（非游泳）' or selection == '配速（游泳）':
    st.markdown(f'### 2. 选取数据范围')
    col1, col2 = st.beta_columns(2)
    speed_low = col1.text_input('输入最快配速：', '3:10')
    speed_high = col2.text_input('输入最慢配速：', '8:10')
    if st.button('计算并绘制'):
        if selection == '配速（非游泳）':
            st.info('已选定方案二')
            for_speed_graph_1(1)
        else:
            st.info('已选定方案二')
            for_speed_graph_1(3, yy=True)
elif selection == '划频（游泳）':
    st.markdown(f'### 2. 选取数据范围')
    if st.button('随机生成'):
        random_value = np.random.randint(0, 40, 2)
        random_value.sort()
        value_selection = st.slider('数值范围', min_value=0, max_value=300,
                                    value=(int(random_value[0]), int(random_value[1])))
    else:
        value_selection = st.slider('数值范围', min_value=0, max_value=300, value=(2, 17))
    st.info('已选定方案三（方案二+改进）')
    start_by_zero_graph(3, '#1CC3DF', sport='huapinyy')
elif selection == 'Swolf（游泳）':
    st.markdown(f'### 2. 选取数据范围')
    if st.button('随机生成'):
        random_value = np.random.randint(0, 40, 2)
        random_value.sort()
        value_selection = st.slider('数值范围', min_value=0, max_value=300,
                                    value=(int(random_value[0]), int(random_value[1])))
    else:
        value_selection = st.slider('数值范围', min_value=0, max_value=300, value=(2, 17))
    st.info('已选定方案三（方案二+改进）')
    start_by_zero_graph(3, '#5188E0', sport='swolf')
elif selection == '起跳高度':
    st.markdown(f'### 2. 选取数据范围')
    if st.button('随机生成'):
        random_value = np.random.randint(0, 80, 2)
        random_value.sort()
        value_selection = st.slider('数值范围', min_value=0, max_value=80,
                                    value=(int(random_value[0]), int(random_value[1])))
    else:
        value_selection = st.slider('数值范围', min_value=0, max_value=80, value=(10, 30))
    st.info('已选定方案一')
    start_by_zero_graph(2, '#FF0000', sport='qitiaogaodu')
elif selection == '频率（划船机）' or selection == '踏频（室内单车）' or selection == '频率（跳绳）':
    st.markdown(f'### 2. 选取数据范围')
    if st.button('随机生成'):
        random_value = np.random.randint(0, 200, 2)
        random_value.sort()
        value_selection = st.slider('数值范围', min_value=0, max_value=300,
                                    value=(int(random_value[0]), int(random_value[1])))
    else:
        value_selection = st.slider('数值范围', min_value=0, max_value=300, value=(10, 50))
    st.info('已选定方案一')
    if selection == '频率（划船机）' or selection == '踏频（室内单车）':
        start_by_zero_graph(2, '#2BBD5C', sport='pinlv_hcj_dc')
    else:
        start_by_zero_graph(2, '#F5BF33', sport='pinlv_ts')
else:
    st.warning('未完成')
