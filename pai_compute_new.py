import pandas as pd
import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.figure_factory as FF
import re
from PIL import Image

st.set_page_config(page_title='元气值计算')
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
# st.header('小米穿戴反馈数据分析')
st.markdown('# 元气值计算模拟工具')
# st.subheader('Feedback 反馈平台数据')
st.markdown('##### *适用于元气值数据计算（Coded by Lizhengpei @ Xiaomi）*')

# st.markdown('### 1. 上传数据原始文件')
# file = st.file_uploader('上传文件', type=['xls', 'xlsx'])

# df_origin = get_origin_data('0621_0627_wearable_feedback-1624957035081.xls')
st.markdown('### 1. 数据录入')
st.markdown("> 单位：分钟")

def f(x):
    y = 127.23722*(1-math.exp(-x/104.64574))
    return y

def f1(x):
    # if x <= 3:
    #     y = 4 * x
    # else:
    #     y = 120 / (1 + 9 * math.exp(-0.03*x))
    y = 126.28284694515 - 126.282901842748 * math.exp(-0.010002338008324 * x)
    return y

a = np.arange(500)
b = []
c = []
for i in a:
    b.append(f1(i))
    c.append(f(i))
plt.plot(a, b)
plt.plot(a, c)
plt.show()

def f_lmh(low, medium, high, prev_pai):  # 七日低、七日中、七日高、之前已获得的七日pai值
    final_score = high + low/12 + medium/2
    y = 127.23722*(1-np.exp(-final_score/104.64574))  # 七日累计元气值
    y_today = y - prev_pai
    try:
        low_score = (low/12/final_score) * y_today
    except Exception as e:
        low_score = 0
    try:
        medium_score = (medium/2/final_score) * y_today
    except Exception as e:
        medium_score = 0
    try:
        high_score = (high/final_score) * y_today
    except Exception as e:
        high_score = 0
    y = np.floor(y)
    y_today = np.floor(y_today)
    medium_score = np.floor(medium_score)
    high_score = np.floor(high_score)
    low_score = y_today - medium_score - high_score
    return [y, y_today, low_score, medium_score, high_score]  # 七日pai、当日获得pai、当日低、当日中、当日高

def f1_lmh(low, medium, high, prev_pai):  # 取整：中、高向下取整，低 = 总 - （中_整 + 高_整）
    final_score = high + low/12 + medium/2
    y = 126.282901842748 - 126.282901842748 * math.exp(-0.010002338008324 * final_score)
    y_today = y - prev_pai
    try:
        low_score = (low / 12 / final_score) * y_today
    except Exception as e:
        low_score = 0
    try:
        medium_score = (medium / 2 / final_score) * y_today
    except:
        medium_score = 0
    try:
        high_score = (high / final_score) * y_today
    except:
        high_score = 0
    y = np.floor(y)
    y_today = np.floor(y_today)
    medium_score = np.floor(medium_score)
    high_score = np.floor(high_score)
    low_score = y_today - medium_score - high_score
    return [y, y_today, low_score, medium_score, high_score]  # 七日pai、当日获得pai、当日低、当日中、当日高


col1, col2, col3, col4 = st.columns([2, 5, 5, 5])
with col2:
    day1_small = st.number_input('较小强度', 0, 1440, 30, key='day1_1')
with col3:
    day1_middle = st.number_input('中等强度', 0, 1440, 30, key='day1_2')
with col4:
    day1_high = st.number_input('较大强度', 0, 1440, 30, key='day1_3')
with col1:
    st.markdown("\n")
    st.markdown("\n")
    st.markdown("\n第一天：")

col1, col2, col3, col4 = st.columns([2, 5, 5, 5])
with col1:
    st.markdown("\n")
    st.markdown("\n")
    st.markdown("\n第二天：")
with col2:
    day2_small = st.number_input('较小强度', 0, 1440, 30, key='day2_1')
with col3:
    day2_middle = st.number_input('中等强度', 0, 1440, 30, key='day2_2')
with col4:
    day2_high = st.number_input('较大强度', 0, 1440, 30, key='day2_3')

col1, col2, col3, col4 = st.columns([2, 5, 5, 5])
with col1:
    st.markdown("\n")
    st.markdown("\n")
    st.markdown("\n第三天：")
with col2:
    day3_small = st.number_input('较小强度', 0, 1440, 30, key='day3_1')
with col3:
    day3_middle = st.number_input('中等强度', 0, 1440, 30, key='day3_2')
with col4:
    day3_high = st.number_input('较大强度', 0, 1440, 30, key='day3_3')

col1, col2, col3, col4 = st.columns([2, 5, 5, 5])
with col1:
    st.markdown("\n")
    st.markdown("\n")
    st.markdown("\n第四天：")
with col2:
    day4_small = st.number_input('较小强度', 0, 1440, 30, key='day4_1')
with col3:
    day4_middle = st.number_input('中等强度', 0, 1440, 30, key='day4_2')
with col4:
    day4_high = st.number_input('较大强度', 0, 1440, 30, key='day4_3')

col1, col2, col3, col4 = st.columns([2, 5, 5, 5])
with col1:
    st.markdown("\n")
    st.markdown("\n")
    st.markdown("\n第五天：")
with col2:
    day5_small = st.number_input('较小强度', 0, 1440, 30, key='day5_1')
with col3:
    day5_middle = st.number_input('中等强度', 0, 1440, 30, key='day5_2')
with col4:
    day5_high = st.number_input('较大强度', 0, 1440, 30, key='day5_3')

col1, col2, col3, col4 = st.columns([2, 5, 5, 5])
with col1:
    st.markdown("\n")
    st.markdown("\n")
    st.markdown("\n第六天：")
with col2:
    day6_small = st.number_input('较小强度', 0, 1440, 30, key='day6_1')
with col3:
    day6_middle = st.number_input('中等强度', 0, 1440, 30, key='day6_2')
with col4:
    day6_high = st.number_input('较大强度', 0, 1440, 30, key='day6_3')

col1, col2, col3, col4 = st.columns([2, 5, 5, 5])
with col1:
    st.markdown("\n")
    st.markdown("\n")
    st.markdown("\n第七天：")
with col2:
    day7_small = st.number_input('较小强度', 0, 1440, 30, key='day7_1')
with col3:
    day7_middle = st.number_input('中等强度', 0, 1440, 30, key='day7_2')
with col4:
    day7_high = st.number_input('较大强度', 0, 1440, 30, key='day7_3')

col1, col2, col3, col4 = st.columns([2, 4, 4, 4])
with col3:
    compute = st.button('计算元气值')

if compute:
    flag = 0
    day1_pai = f_lmh(day1_small, day1_middle, day1_high, 0)
    if day1_pai[0] > 80:
        flag = 1
        while(day1_pai[1] > 80):
            if day1_high >= 1:
                day1_high -= 1
                day1_pai = f_lmh(day1_small, day1_middle, day1_high, 0)
                if day1_pai[1] > 80 and day1_middle >= 1:
                    day1_middle -= 1
                    day1_pai = f_lmh(day1_small, day1_middle, day1_high, 0)
                    if day1_pai[1] > 80 and day1_small >= 1:
                        day1_small -= 1
                        day1_pai = f_lmh(day1_small, day1_middle, day1_high, 0)

    day2_pai = f_lmh(day1_small + day2_small, day1_middle + day2_middle, day1_high + day2_high, day1_pai[0])
    if day2_pai[1] > 80:
        flag = 1
        while(day2_pai[1] > 80):
            if day2_high >= 1:
                day2_high -= 1
                day2_pai = f_lmh(day1_small + day2_small, day1_middle + day2_middle, day1_high + day2_high, day1_pai[0])
                if day2_pai[1] > 80 and day2_middle >= 1:
                    day2_middle -= 1
                    day2_pai = f_lmh(day1_small + day2_small, day1_middle + day2_middle, day1_high + day2_high, day1_pai[0])
                    if day2_pai[1] > 80 and day2_small >= 1:
                        day2_small -= 1
                        day2_pai = f_lmh(day1_small + day2_small, day1_middle + day2_middle, day1_high + day2_high, day1_pai[0])
    day3_pai = f_lmh(day1_small + day2_small + day3_small, day1_middle + day2_middle + day3_middle, day1_high + day2_high + day3_high, day2_pai[0])
    if day3_pai[1] > 80:
        flag = 1
        while (day3_pai[1] > 80):
            if day3_high >= 1:
                day3_high -= 1
                day3_pai = f_lmh(day1_small + day2_small + day3_small, day1_middle + day2_middle + day3_middle, day1_high + day2_high + day3_high, day2_pai[0])
                if day3_pai[1] > 80 and day3_middle >= 1:
                    day3_middle -= 1
                    day3_pai = f_lmh(day1_small + day2_small + day3_small, day1_middle + day2_middle + day3_middle, day1_high + day2_high + day3_high, day2_pai[0])
                    if day3_pai[1] > 80 and day3_small >= 1:
                        day3_small -= 1
                        day3_pai = f_lmh(day1_small + day2_small + day3_small, day1_middle + day2_middle + day3_middle, day1_high + day2_high + day3_high, day2_pai[0])

    day4_pai = f_lmh(day1_small + day2_small + day3_small + day4_small, day1_middle + day2_middle + day3_middle + day4_middle, day1_high + day2_high + day3_high + day4_high, day3_pai[0])
    if day4_pai[1] > 80:
        flag = 1
        while (day4_pai[1] > 80):
            if day4_high >= 1:
                day4_high -= 1
                day4_pai = f_lmh(day1_small + day2_small + day3_small + day4_small, day1_middle + day2_middle + day3_middle + day4_middle, day1_high + day2_high + day3_high + day4_high, day3_pai[0])
                if day4_pai[1] > 80 and day4_middle >= 1:
                    day4_middle -= 1
                    day4_pai = f_lmh(day1_small + day2_small + day3_small + day4_small, day1_middle + day2_middle + day3_middle + day4_middle, day1_high + day2_high + day3_high + day4_high, day3_pai[0])
                    if day4_pai[1] > 80 and day4_small >= 1:
                        day4_small -= 1
                        day4_pai = f_lmh(day1_small + day2_small + day3_small + day4_small, day1_middle + day2_middle + day3_middle + day4_middle, day1_high + day2_high + day3_high + day4_high, day3_pai[0])

    day5_pai = f_lmh(day1_small + day2_small + day3_small + day4_small + day5_small, day1_middle + day2_middle + day3_middle + day4_middle + day5_middle, day1_high + day2_high + day3_high + day4_high + day5_high, day4_pai[0])
    if day5_pai[1] > 80:
        flag = 1
        while (day5_pai[1] > 80):
            if day5_high >= 1:
                day5_high -= 1
                day5_pai = f_lmh(day1_small + day2_small + day3_small + day4_small + day5_small, day1_middle + day2_middle + day3_middle + day4_middle + day5_middle, day1_high + day2_high + day3_high + day4_high + day5_high, day4_pai[0])
                if day5_pai[1] > 80 and day5_middle >= 1:
                    day5_middle -= 1
                    day5_pai = f_lmh(day1_small + day2_small + day3_small + day4_small + day5_small, day1_middle + day2_middle + day3_middle + day4_middle + day5_middle, day1_high + day2_high + day3_high + day4_high + day5_high, day4_pai[0])
                    if day5_pai[1] > 80 and day5_small >= 1:
                        day5_small -= 1
                        day5_pai = f_lmh(day1_small + day2_small + day3_small + day4_small + day5_small, day1_middle + day2_middle + day3_middle + day4_middle + day5_middle, day1_high + day2_high + day3_high + day4_high + day5_high, day4_pai[0])

    day6_pai = f_lmh(day1_small + day2_small + day3_small + day4_small + day5_small + day6_small, day1_middle + day2_middle + day3_middle + day4_middle + day5_middle + day6_middle, day1_high + day2_high + day3_high + day4_high + day5_high + day6_high, day5_pai[0])
    if day6_pai[1] > 80:
        flag = 1
        while (day6_pai[1] > 80):
            if day6_high >= 1:
                day6_high -= 1
                day6_pai = f_lmh(day1_small + day2_small + day3_small + day4_small + day5_small + day6_small, day1_middle + day2_middle + day3_middle + day4_middle + day5_middle + day6_middle, day1_high + day2_high + day3_high + day4_high + day5_high + day6_high, day5_pai[0])
                if day6_pai[1] > 80 and day6_middle >= 1:
                    day6_middle -= 1
                    day6_pai = f_lmh(day1_small + day2_small + day3_small + day4_small + day5_small + day6_small, day1_middle + day2_middle + day3_middle + day4_middle + day5_middle + day6_middle, day1_high + day2_high + day3_high + day4_high + day5_high + day6_high, day5_pai[0])
                    if day6_pai[1] > 80 and day6_small >= 1:
                        day6_small -= 1
                        day6_pai = f_lmh(day1_small + day2_small + day3_small + day4_small + day5_small + day6_small, day1_middle + day2_middle + day3_middle + day4_middle + day5_middle + day6_middle, day1_high + day2_high + day3_high + day4_high + day5_high + day6_high, day5_pai[0])

    day7_pai = f_lmh(day1_small + day2_small + day3_small + day4_small + day5_small + day6_small + day7_small,
                     day1_middle + day2_middle + day3_middle + day4_middle + day5_middle + day6_middle + day7_middle,
                     day1_high + day2_high + day3_high + day4_high + day5_high + day6_high + day7_high, day6_pai[0])
    if day7_pai[1] > 80:
        flag = 1
        while day7_pai[1] > 80:
            if day7_high >= 1:
                day7_high -= 1
                day7_pai = f_lmh(
                    day1_small + day2_small + day3_small + day4_small + day5_small + day6_small + day7_small,
                    day1_middle + day2_middle + day3_middle + day4_middle + day5_middle + day6_middle + day7_middle,
                    day1_high + day2_high + day3_high + day4_high + day5_high + day6_high + day7_high, day6_pai[0])
                if day7_pai[1] > 80 and day6_middle >= 1:
                    day7_middle -= 1
                    day7_pai = f_lmh(
                        day1_small + day2_small + day3_small + day4_small + day5_small + day6_small + day7_small,
                        day1_middle + day2_middle + day3_middle + day4_middle + day5_middle + day6_middle + day7_middle,
                        day1_high + day2_high + day3_high + day4_high + day5_high + day6_high + day7_high, day6_pai[0])
                    if day7_pai[1] > 80 and day7_small >= 1:
                        day7_small -= 1
                        day7_pai = f_lmh(
                            day1_small + day2_small + day3_small + day4_small + day5_small + day6_small + day7_small,
                            day1_middle + day2_middle + day3_middle + day4_middle + day5_middle + day6_middle + day7_middle,
                            day1_high + day2_high + day3_high + day4_high + day5_high + day6_high + day7_high,
                            day6_pai[0])

    st.markdown("#### 产品侧拟合曲线参考值")
    if flag == 1:
        st.warning("请注意，当前输入数据存在超限(80)情况，由于无法得到当天超限时间点，以下数据经过逆推处理，故以下数据项仅供参考，可能存在一定误差！")

    df = pd.DataFrame(columns=["天数", "7日累计元气值", "当天获取", "当天较小强度获取", "当天中等强度获取", "当天较大强度获取"])
    list1 = [1, int(day1_pai[0]), day1_pai[1], day1_pai[2], day1_pai[3], day1_pai[4]]
    df.loc[len(df)] = list1
    list2 = [2, day2_pai[0], day2_pai[1], day2_pai[2], day2_pai[3], day2_pai[4]]
    df.loc[len(df)] = list2
    list3 = [3, day3_pai[0], day3_pai[1], day3_pai[2], day3_pai[3], day3_pai[4]]
    df.loc[len(df)] = list3
    list4 = [4, day4_pai[0], day4_pai[1], day4_pai[2], day4_pai[3], day4_pai[4]]
    df.loc[len(df)] = list4
    list5 = [5, day5_pai[0], day5_pai[1], day5_pai[2], day5_pai[3], day5_pai[4]]
    df.loc[len(df)] = list5
    list6 = [6, day6_pai[0], day6_pai[1], day6_pai[2], day6_pai[3], day6_pai[4]]
    df.loc[len(df)] = list6
    list7 = [7, day7_pai[0], day7_pai[1], day7_pai[2], day7_pai[3], day7_pai[4]]
    df.loc[len(df)] = list7

    # df.index = df.index + 1
    # st.dataframe(df.astype(int))
    # print(df)

    bar_chart = px.bar(df, x="天数", y=["7日累计元气值", "当天获取", "当天较小强度获取", "当天中等强度获取", "当天较大强度获取"], title="数据柱状图")
    line_chart = px.line(df, x="天数",
                         y=["7日累计元气值", "当天获取", "当天较小强度获取", "当天中等强度获取", "当天较大强度获取"],
                         title="数据折线图")
    st.plotly_chart(bar_chart)
    st.plotly_chart(line_chart)
    
    
    
    
    
    
    # 算法侧结果
    flag = 0
    day1_pai = f1_lmh(day1_small, day1_middle, day1_high, 0)
    if day1_pai[0] > 80:
        flag = 1
        while (day1_pai[1] > 80):
            if day1_high >= 1:
                day1_high -= 1
                day1_pai = f1_lmh(day1_small, day1_middle, day1_high, 0)
                if day1_pai[1] > 80 and day1_middle >= 1:
                    day1_middle -= 1
                    day1_pai = f1_lmh(day1_small, day1_middle, day1_high, 0)
                    if day1_pai[1] > 80 and day1_small >= 1:
                        day1_small -= 1
                        day1_pai = f1_lmh(day1_small, day1_middle, day1_high, 0)

    day2_pai = f1_lmh(day1_small + day2_small, day1_middle + day2_middle, day1_high + day2_high, day1_pai[0])
    if day2_pai[1] > 80:
        flag = 1
        while (day2_pai[1] > 80):
            if day2_high >= 1:
                day2_high -= 1
                day2_pai = f1_lmh(day1_small + day2_small, day1_middle + day2_middle, day1_high + day2_high, day1_pai[0])
                if day2_pai[1] > 80 and day2_middle >= 1:
                    day2_middle -= 1
                    day2_pai = f1_lmh(day1_small + day2_small, day1_middle + day2_middle, day1_high + day2_high,
                                     day1_pai[0])
                    if day2_pai[1] > 80 and day2_small >= 1:
                        day2_small -= 1
                        day2_pai = f1_lmh(day1_small + day2_small, day1_middle + day2_middle, day1_high + day2_high,
                                         day1_pai[0])
    day3_pai = f1_lmh(day1_small + day2_small + day3_small, day1_middle + day2_middle + day3_middle,
                     day1_high + day2_high + day3_high, day2_pai[0])
    if day3_pai[1] > 80:
        flag = 1
        while (day3_pai[1] > 80):
            if day3_high >= 1:
                day3_high -= 1
                day3_pai = f1_lmh(day1_small + day2_small + day3_small, day1_middle + day2_middle + day3_middle,
                                 day1_high + day2_high + day3_high, day2_pai[0])
                if day3_pai[1] > 80 and day3_middle >= 1:
                    day3_middle -= 1
                    day3_pai = f1_lmh(day1_small + day2_small + day3_small, day1_middle + day2_middle + day3_middle,
                                     day1_high + day2_high + day3_high, day2_pai[0])
                    if day3_pai[1] > 80 and day3_small >= 1:
                        day3_small -= 1
                        day3_pai = f1_lmh(day1_small + day2_small + day3_small, day1_middle + day2_middle + day3_middle,
                                         day1_high + day2_high + day3_high, day2_pai[0])

    day4_pai = f1_lmh(day1_small + day2_small + day3_small + day4_small,
                     day1_middle + day2_middle + day3_middle + day4_middle,
                     day1_high + day2_high + day3_high + day4_high, day3_pai[0])
    if day4_pai[1] > 80:
        flag = 1
        while (day4_pai[1] > 80):
            if day4_high >= 1:
                day4_high -= 1
                day4_pai = f1_lmh(day1_small + day2_small + day3_small + day4_small,
                                 day1_middle + day2_middle + day3_middle + day4_middle,
                                 day1_high + day2_high + day3_high + day4_high, day3_pai[0])
                if day4_pai[1] > 80 and day4_middle >= 1:
                    day4_middle -= 1
                    day4_pai = f1_lmh(day1_small + day2_small + day3_small + day4_small,
                                     day1_middle + day2_middle + day3_middle + day4_middle,
                                     day1_high + day2_high + day3_high + day4_high, day3_pai[0])
                    if day4_pai[1] > 80 and day4_small >= 1:
                        day4_small -= 1
                        day4_pai = f1_lmh(day1_small + day2_small + day3_small + day4_small,
                                         day1_middle + day2_middle + day3_middle + day4_middle,
                                         day1_high + day2_high + day3_high + day4_high, day3_pai[0])

    day5_pai = f1_lmh(day1_small + day2_small + day3_small + day4_small + day5_small,
                     day1_middle + day2_middle + day3_middle + day4_middle + day5_middle,
                     day1_high + day2_high + day3_high + day4_high + day5_high, day4_pai[0])
    if day5_pai[1] > 80:
        flag = 1
        while (day5_pai[1] > 80):
            if day5_high >= 1:
                day5_high -= 1
                day5_pai = f1_lmh(day1_small + day2_small + day3_small + day4_small + day5_small,
                                 day1_middle + day2_middle + day3_middle + day4_middle + day5_middle,
                                 day1_high + day2_high + day3_high + day4_high + day5_high, day4_pai[0])
                if day5_pai[1] > 80 and day5_middle >= 1:
                    day5_middle -= 1
                    day5_pai = f1_lmh(day1_small + day2_small + day3_small + day4_small + day5_small,
                                     day1_middle + day2_middle + day3_middle + day4_middle + day5_middle,
                                     day1_high + day2_high + day3_high + day4_high + day5_high, day4_pai[0])
                    if day5_pai[1] > 80 and day5_small >= 1:
                        day5_small -= 1
                        day5_pai = f1_lmh(day1_small + day2_small + day3_small + day4_small + day5_small,
                                         day1_middle + day2_middle + day3_middle + day4_middle + day5_middle,
                                         day1_high + day2_high + day3_high + day4_high + day5_high, day4_pai[0])

    day6_pai = f1_lmh(day1_small + day2_small + day3_small + day4_small + day5_small + day6_small,
                     day1_middle + day2_middle + day3_middle + day4_middle + day5_middle + day6_middle,
                     day1_high + day2_high + day3_high + day4_high + day5_high + day6_high, day5_pai[0])
    if day6_pai[1] > 80:
        flag = 1
        while (day6_pai[1] > 80):
            if day6_high >= 1:
                day6_high -= 1
                day6_pai = f1_lmh(day1_small + day2_small + day3_small + day4_small + day5_small + day6_small,
                                 day1_middle + day2_middle + day3_middle + day4_middle + day5_middle + day6_middle,
                                 day1_high + day2_high + day3_high + day4_high + day5_high + day6_high, day5_pai[0])
                if day6_pai[1] > 80 and day6_middle >= 1:
                    day6_middle -= 1
                    day6_pai = f1_lmh(day1_small + day2_small + day3_small + day4_small + day5_small + day6_small,
                                     day1_middle + day2_middle + day3_middle + day4_middle + day5_middle + day6_middle,
                                     day1_high + day2_high + day3_high + day4_high + day5_high + day6_high, day5_pai[0])
                    if day6_pai[1] > 80 and day6_small >= 1:
                        day6_small -= 1
                        day6_pai = f1_lmh(day1_small + day2_small + day3_small + day4_small + day5_small + day6_small,
                                         day1_middle + day2_middle + day3_middle + day4_middle + day5_middle + day6_middle,
                                         day1_high + day2_high + day3_high + day4_high + day5_high + day6_high,
                                         day5_pai[0])

    day7_pai = f1_lmh(day1_small + day2_small + day3_small + day4_small + day5_small + day6_small + day7_small,
                     day1_middle + day2_middle + day3_middle + day4_middle + day5_middle + day6_middle + day7_middle,
                     day1_high + day2_high + day3_high + day4_high + day5_high + day6_high + day7_high, day6_pai[0])
    if day7_pai[1] > 80:
        flag = 1
        while day7_pai[1] > 80:
            if day7_high >= 1:
                day7_high -= 1
                day7_pai = f1_lmh(
                    day1_small + day2_small + day3_small + day4_small + day5_small + day6_small + day7_small,
                    day1_middle + day2_middle + day3_middle + day4_middle + day5_middle + day6_middle + day7_middle,
                    day1_high + day2_high + day3_high + day4_high + day5_high + day6_high + day7_high, day6_pai[0])
                if day7_pai[1] > 80 and day6_middle >= 1:
                    day7_middle -= 1
                    day7_pai = f1_lmh(
                        day1_small + day2_small + day3_small + day4_small + day5_small + day6_small + day7_small,
                        day1_middle + day2_middle + day3_middle + day4_middle + day5_middle + day6_middle + day7_middle,
                        day1_high + day2_high + day3_high + day4_high + day5_high + day6_high + day7_high, day6_pai[0])
                    if day7_pai[1] > 80 and day7_small >= 1:
                        day7_small -= 1
                        day7_pai = f1_lmh(
                            day1_small + day2_small + day3_small + day4_small + day5_small + day6_small + day7_small,
                            day1_middle + day2_middle + day3_middle + day4_middle + day5_middle + day6_middle + day7_middle,
                            day1_high + day2_high + day3_high + day4_high + day5_high + day6_high + day7_high,
                            day6_pai[0])

    st.markdown("#### 算法侧拟合曲线参考值")
    if flag == 1:
        st.warning(
            "请注意，当前输入数据存在超限(80)情况，由于无法得到当天超限时间点，以下数据经过逆推处理，故以下数据项仅供参考，可能存在一定误差！")

    df = pd.DataFrame(
        columns=["天数", "7日累计元气值", "当天获取", "当天较小强度获取", "当天中等强度获取", "当天较大强度获取"])
    list1 = [1, int(day1_pai[0]), day1_pai[1], day1_pai[2], day1_pai[3], day1_pai[4]]
    df.loc[len(df)] = list1
    list2 = [2, day2_pai[0], day2_pai[1], day2_pai[2], day2_pai[3], day2_pai[4]]
    df.loc[len(df)] = list2
    list3 = [3, day3_pai[0], day3_pai[1], day3_pai[2], day3_pai[3], day3_pai[4]]
    df.loc[len(df)] = list3
    list4 = [4, day4_pai[0], day4_pai[1], day4_pai[2], day4_pai[3], day4_pai[4]]
    df.loc[len(df)] = list4
    list5 = [5, day5_pai[0], day5_pai[1], day5_pai[2], day5_pai[3], day5_pai[4]]
    df.loc[len(df)] = list5
    list6 = [6, day6_pai[0], day6_pai[1], day6_pai[2], day6_pai[3], day6_pai[4]]
    df.loc[len(df)] = list6
    list7 = [7, day7_pai[0], day7_pai[1], day7_pai[2], day7_pai[3], day7_pai[4]]
    df.loc[len(df)] = list7

    # df.index = df.index + 1
    # st.dataframe(df.astype(int))
    # print(df)

    bar_chart = px.bar(df, x="天数",
                       y=["7日累计元气值", "当天获取", "当天较小强度获取", "当天中等强度获取", "当天较大强度获取"],
                       title="数据柱状图")
    line_chart = px.line(df, x="天数",
                       y=["7日累计元气值", "当天获取", "当天较小强度获取", "当天中等强度获取", "当天较大强度获取"],
                       title="数据折线图")
    st.plotly_chart(bar_chart)
    st.plotly_chart(line_chart)











































    # st.markdown("第一天:")
    # st.markdown("七日元气值 {}，当天获取 {} 元气，其中，较小强度获取 {} 元气，中等强度获取 {} 元气，较大强度获取 {} 元气。".format(day1_pai[0], int(day1_pai[1]), int(day1_pai[2]), int(day1_pai[3]), int(day1_pai[4])))
    # st.markdown("第二天:")
    # st.markdown(
    #     "七日元气值 {}，当天获取 {} 元气，其中，较小强度获取 {} 元气，中等强度获取 {} 元气，较大强度获取 {} 元气。".format(
    #         day2_pai[0], int(day2_pai[1]), int(day2_pai[2]), int(day2_pai[3]), int(day2_pai[4])))

    # st.markdown("第三天:")
    # st.markdown(
    #     "七日元气值 {}，当天获取 {} 元气，其中，较小强度获取 {} 元气，中等强度获取 {} 元气，较大强度获取 {} 元气。".format(
    #         day3_total_pai[0], int(day3_pai[0]), int(day3_pai[1]), int(day3_pai[2]), int(day3_pai[3])))
    #
    # st.markdown("第四天:")
    # st.markdown(
    #     "七日元气值 {}，当天获取 {} 元气，其中，较小强度获取 {} 元气，中等强度获取 {} 元气，较大强度获取 {} 元气。".format(
    #         day4_total_pai[0], int(day4_pai[0]), int(day4_pai[1]), int(day4_pai[2]), int(day4_pai[3])))
    #
    # st.markdown("第五天:")
    # st.markdown(
    #     "七日元气值 {}，当天获取 {} 元气，其中，较小强度获取 {} 元气，中等强度获取 {} 元气，较大强度获取 {} 元气。".format(
    #         day5_total_pai[0], int(day5_pai[0]), int(day5_pai[1]), int(day5_pai[2]), int(day5_pai[3])))
    #
    # st.markdown("第六天:")
    # st.markdown(
    #     "七日元气值 {}，当天获取 {} 元气，其中，较小强度获取 {} 元气，中等强度获取 {} 元气，较大强度获取 {} 元气。".format(
    #         day6_total_pai[0], int(day6_pai[0]), int(day6_pai[1]), int(day6_pai[2]), int(day6_pai[3])))
    #
    # st.markdown("第七天:")
    # st.markdown(
    #     "七日元气值 {}，当天获取 {} 元气，其中，较小强度获取 {} 元气，中等强度获取 {} 元气，较大强度获取 {} 元气。".format(
    #         day7_total_pai[0], int(day7_pai[0]), int(day7_pai[1]), int(day7_pai[2]), int(day7_pai[3])))

