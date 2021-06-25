import time
from math import floor, ceil
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px


def start_not_zero(value_max, value_min):
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
    print('计算过程如下：')
    print('1. 当前数据最小值为：{}，最大值为：{}'.format(value_min, value_max))
    value_range = value_max - value_min
    print('2. 数值区间为：{}'.format(value_range))
    temp_value = value_range / 3
    print('3. temp_value 值 为：{}'.format(temp_value))
    temp_value = ceil(temp_value)
    while temp_value % 3 != 0:
        temp_value = temp_value + 1
    print('4. 向上以3取整结果为：{}'.format(temp_value))
    axis_max = value_max
    axis_min = value_min

    n = 0
    while axis_max % temp_value != 0:
        n = n + 1
        axis_max = axis_max + 1
    print('5. 坐标轴最大值为：{} + {} = {}'.format(value_max, n, axis_max))

    m = 0
    while axis_min % temp_value != 0:
        m = m + 1
        axis_min = axis_min - 1
    print('6. 坐标轴最小值为：{} - {} = {}'.format(value_min, m, axis_min))
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
        print('最大值修正值为 {}'.format(axis_max))
        axis_each = axis_range / 4
        for i in range(5):
            result.append(axis_min + i * axis_each)
    print('计算完毕，均分获得最终坐标轴结果...')
    return result


def start_with_zero(value_max):
    result = []

    print('计算过程如下: ')
    print('----------------------------------')
    x = value_max / 4
    print('1. x 值 为：{}'.format(x))
    x = ceil(x)
    while x % 4 != 0:
        x = x + 1
    print('2. 向上以3取整结果为：{}'.format(x))
    axis_max = value_max

    n = 0
    while axis_max % x != 0:
        n = n + 1
        axis_max = axis_max + 1
    print('3. 坐标轴最大值为：{} + {} = {}'.format(value_max, n, axis_max))
    range_value = axis_max / 4
    for i in range(3, -1, -1):
        result.append(axis_max - i * range_value)
    print('----------------------------------')
    print('计算完毕，均分获得最终坐标轴结果...')
    return result


def speed_graph(value_max, value_min):
    range_val = value_max - value_min
    temp = range_val / 3
    temp = ceil(temp)
    while temp % 3 != 0:
        temp = temp + 1
    print(temp)
    axis_max = value_max
    axis_min = value_min

    n = 0
    while axis_max % temp != 0:
        n = n + 1
        axis_max = axis_max + 1
    print('坐标轴最大值为：{} + {} = {}'.format(value_max, n, axis_max))

    m = 0
    while axis_min % temp != 0:
        m = m + 1
        axis_min = axis_min - 1
        if axis_min <= 0:
            axis_min = 0
            m = value_min
            break
    print('坐标轴最小值为：{} - {} = {}'.format(value_min, m, axis_min))
    axis_range = axis_max - axis_min
    result = []

    if axis_min != 0:
        axis_each = float(axis_range / 4)
        for i in range(5):
            secs = axis_min + i * axis_each
            min_res = floor(secs / 60)
            sec_res = int(secs % 60)
            res_str = '{}:{}'.format(min_res, sec_res)
            result.append(res_str)
    else:
        axis_each = axis_range / 5
        print(axis_each)
        for i in range(6):
            secs = axis_min + i * axis_each
            min_res = floor(secs / 60)
            sec_res = int(secs % 60)
            res_str = '{}:{}'.format(min_res, sec_res)
            result.append(res_str)
    return result


def speed_graph2(value_max, value_min):

    axis_max = value_max
    axis_min = value_min

    n = 0
    while axis_max % 20 != 0:
        n = n + 1
        axis_max = axis_max + 1
    print('坐标轴最大值为：{} + {} = {}'.format(value_max, n, axis_max))

    m = 0
    while axis_min % 20 != 0:
        m = m + 1
        axis_min = axis_min - 1
        if axis_min <= 0:
            axis_min = 0
            m = value_min
            break
    print('坐标轴最小值为：{} - {} = {}'.format(value_min, m, axis_min))
    axis_range = axis_max - axis_min
    result = []

    if axis_min != 0:
        axis_each = float(axis_range / 4)
        for i in range(5):
            secs = axis_min + i * axis_each
            min_res = floor(secs / 60)
            sec_res = int(secs % 60)
            res_str = '{}:{}'.format(min_res, sec_res)
            result.append(res_str)
    else:
        axis_each = axis_range / 5
        print(axis_each)
        for i in range(6):
            secs = axis_min + i * axis_each
            min_res = floor(secs / 60)
            sec_res = int(secs % 60)
            res_str = '{}:{}'.format(min_res, sec_res)
            result.append(res_str)
    return result


def draw_plot_1(value_x, value_y, y_ticks):
    series_count = 4
    plt.figure(1, figsize=(8, 5))
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
        plt.plot(value_x[i], value_y[i], linewidth=2, color='#E35A5A')   # 折线
        # plt.subplot(10, 2, 2 * i + 2)
        # plt.yticks(y_ticks)
        # plt.xticks([0, 3, 6, 9], ['0(min)', '3', '6', '9'])
        # c = np.mean(value_y[i])
        # plt.axhline(y=c, color="gray", ls='--', lw=2, alpha=0.5)
        # ax = plt.gca()
        # ax.yaxis.tick_right()
        # if min(value_y[i]) != 0:
        #     ax.set_ylim(y_ticks[0] - 0.5 * (y_ticks[1] - y_ticks[0]),
        #                 y_ticks[-1] + 0.5 * (y_ticks[1] - y_ticks[0]))
        # else:
        #     ax.set_ylim(y_ticks[0], y_ticks[-1] + 0.5 * (y_ticks[1] - y_ticks[0]))
        # ax.set_xlim(0, 10)
        # plt.scatter(value_x[i], value_y[i], s=15)
    # plt.show()
    st.pyplot(plt)

# 起点一定为0
def draw_plot_2(value_x, value_y, y_ticks, type=1, color='#61CE86'):
    series_count = 4
    plt.figure(1, figsize=(8, 5))
    for i in range(series_count):
        plt.subplot(series_count / 2, 2, i + 1)
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
        fill_aera_y = value_y[i].tolist()
        fill_aera_y.insert(0, 0)
        fill_aera_y.append(0)
        if type == 1:
            plt.fill(fill_aera_x, fill_aera_y, color=color)
            plt.plot(value_x[i], value_y[i], linewidth=2, color=color)   # 折线
        elif type == 2:
            plt.scatter(value_x[i], value_y[i], s=15)
        elif type == 3:
            plt.bar(value_x[i], value_y[i], 1, color=color)
    st.pyplot(plt)


def draw_plot_3(value_x, value_y, y_ticks):
    series_count = 4
    plt.figure(1, figsize=(8, 5))
    for i in range(series_count):
        plt.subplot(int(series_count / 2), 2, i + 1)
        plt.yticks(y_ticks)
        plt.xticks([0, 3, 6, 9], ['0(min)', '3', '6', '9'])
        c = np.mean(value_y[i])
        plt.axhline(y=c, color="gray", ls='--', lw=2, alpha=0.5)
        ax = plt.gca()
        ax.yaxis.tick_right()
        ax.set_ylim(y_ticks[0] - 0.5 * (y_ticks[1] - y_ticks[0]),
                    y_ticks[-1] + 0.5 * (y_ticks[1] - y_ticks[0]))
        ax.set_xlim(0, 10)
        fill_aera_x = value_x[i].tolist()
        fill_aera_x.insert(0, 0)
        fill_aera_x.append(10)
        fill_aera_y = value_y[i].tolist()
        fill_aera_y.insert(0, y_ticks[0] - 0.5 * (y_ticks[1] - y_ticks[0]))
        fill_aera_y.append(y_ticks[0] - 0.5 * (y_ticks[1] - y_ticks[0]))
        plt.fill(fill_aera_x, fill_aera_y, color='#5FCEFF')
        plt.plot(value_x[i], value_y[i], linewidth=2, color='#5FCEFF')   # 折线
    st.pyplot(plt)



def generate_bar_data(max_val, min_val):
    value_x_result = []
    value_y_result = []
    for i in range(10):
        if min_val != max_val:
            demo_value_y = np.random.randint(min_val, max_val, 10)
        else:
            demo_value_y = [min_val] * 10
        demo_value_y[3] = min_val
        demo_value_y[-3] = max_val
        demo_value_x = np.arange(0.5, 9.6, 1)
        value_x_result.append(demo_value_x)
        value_y_result.append(demo_value_y)
    return value_x_result, value_y_result


def generate_data(max_val, min_val):
    value_x_result = []
    value_y_result = []
    for i in range(10):
        if min_val != max_val:
            demo_value_y = np.random.randint(min_val, max_val, 51)
        else:
            demo_value_y = [min_val] * 51
        demo_value_y[3] = min_val
        demo_value_y[-3] = max_val
        demo_value_x = np.arange(0, 10.1, 0.2)
        value_x_result.append(demo_value_x)
        value_y_result.append(demo_value_y)
    return value_x_result, value_y_result


def heart_rate_graph():
    min_val = value_selection[0]
    max_val = value_selection[1]
    result_list = start_not_zero(max_val, min_val)
    str_val = '##### 方案一坐标轴计算结果：' + str(result_list)
    st.markdown(str_val)
    with st.spinner('生成数据...'):
        time.sleep(0.5)
        demo_value_x, demo_value_y = generate_data(max_val, min_val)
    with st.spinner('绘制中...'):
        draw_plot_1(demo_value_x, demo_value_y, result_list)


def latitude_graph():
    min_val = value_selection[0]
    max_val = value_selection[1]
    result_list = start_below_zero(max_val, min_val)
    st.write("选择了", value_selection)
    str_val = '##### 方案一坐标轴计算结果：' + str(result_list)
    st.markdown(str_val)
    with st.spinner('生成数据...'):
        time.sleep(0.5)
        demo_value_x, demo_value_y = generate_data(max_val, min_val)
    with st.spinner('绘制中...'):
        draw_plot_3(demo_value_x, demo_value_y, result_list)


def start_by_zero_graph(type=1, color='#61CE86'):
    min_val = value_selection[0]
    max_val = value_selection[1]
    result_list = start_with_zero(max_val)
    str_val = '##### 方案一坐标轴计算结果：' + str(result_list)
    st.markdown(str_val)
    with st.spinner('生成数据...'):
        time.sleep(0.5)
        if type == 1 or type == 2:
            demo_value_x, demo_value_y = generate_data(max_val, min_val)
        elif type == 3:
            demo_value_x, demo_value_y = generate_bar_data(max_val, min_val)
    with st.spinner('绘制中...'):
        draw_plot_2(demo_value_x, demo_value_y, result_list, type, color)


def for_speed_graph_1():
    try:
        min_val_min, min_val_sec = map(int, input('输入最快配速：').split(':'))
        max_val_min, max_val_sec = map(int, input('输入最慢配速：').split(':'))
        min_value = min_val_min * 60 + min_val_sec
        max_value = max_val_min * 60 + max_val_sec
        if max_value < min_value:
            print('数值关系错误！')
    except Exception as e:
        print('数值输入错误！')
    result_list = speed_graph(max_value, min_value)
    print(result_list)


def for_speed_graph_2():
    try:
        min_val_min, min_val_sec = map(int, input('输入最快配速：').split(':'))
        max_val_min, max_val_sec = map(int, input('输入最慢配速：').split(':'))
        min_value = min_val_min * 60 + min_val_sec
        max_value = max_val_min * 60 + max_val_sec
        if max_value < min_value:
            print('数值关系错误！')
    except Exception as e:
        print('数值输入错误！')
    result_list = speed_graph2(max_value, min_value)
    print(result_list)


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


# 起点一定不小于0：心率
# 起点一定为0：速度、阻力、划频（游泳）、Swolf（游泳）、步频、起跳高度、频率（跳绳）、频率（划船机）、踏频（室内单车）
# 起点可能小于0：海拔
# 配速相关：配速（游泳）、配速（非游泳）

if selection == '心率':
    st.markdown(f'### 2. 选取数据范围')
    if st.button('随机生成'):
        random_value = np.random.randint(0, 220, 2)
        random_value.sort()
        value_selection = st.slider('数值范围', min_value=0, max_value=220, value=(int(random_value[0]), int(random_value[1])))
    else:
        value_selection = st.slider('数值范围', min_value=0, max_value=220, value=(60, 140))
    heart_rate_graph()
elif selection == '海拔':
    st.markdown(f'### 2. 选取数据范围')
    if st.button('随机生成'):
        random_value = np.random.randint(300, 400, 2)
        random_value.sort()
        value_selection = st.slider('数值范围', min_value=-3000, max_value=3500,
                                    value=(int(random_value[0]), int(random_value[1])))
    else:
        value_selection = st.slider('数值范围', min_value=-3000, max_value=3500, value=(281, 300))
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
    start_by_zero_graph()
elif selection == '阻力':
    st.markdown(f'### 2. 选取数据范围')
    if st.button('随机生成'):
        random_value = np.random.randint(0, 60, 2)
        random_value.sort()
        value_selection = st.slider('数值范围', min_value=0, max_value=60,
                                    value=(int(random_value[0]), int(random_value[1])))
    else:
        value_selection = st.slider('数值范围', min_value=0, max_value=60, value=(12, 24))
    start_by_zero_graph(3)
elif selection == '步频':
    st.markdown(f'### 2. 选取数据范围')
    if st.button('随机生成'):
        random_value = np.random.randint(0, 300, 2)
        random_value.sort()
        value_selection = st.slider('数值范围', min_value=0, max_value=300,
                                    value=(int(random_value[0]), int(random_value[1])))
    else:
        value_selection = st.slider('数值范围', min_value=0, max_value=300, value=(45, 135))
    start_by_zero_graph(2)
elif selection == 4:
    for_speed_graph_1()
elif selection == 5:
    for_speed_graph_2()
elif selection == '划频（游泳）':
    st.markdown(f'### 2. 选取数据范围')
    if st.button('随机生成'):
        random_value = np.random.randint(0, 40, 2)
        random_value.sort()
        value_selection = st.slider('数值范围', min_value=0, max_value=40,
                                    value=(int(random_value[0]), int(random_value[1])))
    else:
        value_selection = st.slider('数值范围', min_value=0, max_value=40, value=(2, 17))
    start_by_zero_graph(3, '#1CC3DF')
elif selection == 'Swolf（游泳）':
    st.markdown(f'### 2. 选取数据范围')
    if st.button('随机生成'):
        random_value = np.random.randint(0, 40, 2)
        random_value.sort()
        value_selection = st.slider('数值范围', min_value=0, max_value=40,
                                    value=(int(random_value[0]), int(random_value[1])))
    else:
        value_selection = st.slider('数值范围', min_value=0, max_value=40, value=(2, 17))
    start_by_zero_graph(3, '#5188E0')
else:
    st.warning('未完成')
