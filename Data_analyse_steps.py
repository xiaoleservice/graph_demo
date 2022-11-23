import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.figure_factory as FF
import re
from PIL import Image

@st.cache
def get_origin_data(url):
    excel_file = url
    sheet_name = '第一页'
    df = pd.read_excel(excel_file, header=0)
    df = df.fillna({'deviceName': '其他'})
    df = df.fillna({'问题分类': '其他未标注问题'})
    return df


st.set_page_config(page_title='小米运动健康反馈数据分析 - 计步专项')

# st.header('小米穿戴反馈数据分析')
st.markdown('# 小米运动健康反馈数据分析 - 计步专项')
# st.subheader('Feedback 反馈平台数据')
st.markdown('##### *适用于 Feedback 反馈平台原始数据（Coded by lizhengpei）*')

st.markdown('### 1. 上传数据原始文件')
file = st.file_uploader('上传文件', type=['xls', 'xlsx'])

# df_origin = get_origin_data('0621_0627_wearable_feedback-1624957035081.xls')
if file:
    df_origin = get_origin_data(file)
    df = df_origin.copy()

    st.markdown('### 2. 数据筛选')

    # feedback_type = df['反馈类型'].unique().tolist()
    # print(df)
    problem_type = df['问题分类'].unique().tolist()
    device_type = df['deviceName'].unique().tolist()
    device_type = sorted(device_type)
    app_versions = df['App版本'].unique().tolist()
    app_versions = sorted(app_versions)

    # type_selection = st.multiselect('反馈类型：', feedback_type, default='bug')
    device_selection = st.multiselect('设备型号', device_type, default=['小米手环7 Pro', 'Xiaomi Watch S1 Pro', '小米手环7', '小米手环7 NFC版'])
    version_selection = st.multiselect('App版本：', app_versions, default=['3.2.0', '3.3.0', '3.3.1', '3.4.0', '3.4.1', '3.4.2', '3.5.0', '3.5.3', '3.6.0', '3.6.1', '3.7.0', '3.7.1', '3.8.0', '3.8.1', '3.8.2', '3.9.2'])

    # if not type_selection:
    #     st.error("请选择至少一个反馈类型！")
    ways = st.selectbox('选择筛选方法', ['问题分类', '问题分类 - 二级', '反馈内容关键词'])
    accessible = st.radio('可回访性', ['是', '否'], index=1)
    # ways = st.radio('选择筛选方法', ['具体问题', '具体问题(标注)', '反馈内容关键词'])

    if ways in ['问题分类 - 二级', '问题分类']:
        type_problem_selection = st.multiselect(ways, problem_type)

        if not type_problem_selection:
            st.error("请选择至少一个具体问题！")
        reg = '1(3[0-9]|4[5,7]|5[0,1,2,3,5,6,7,8,9]|6[2,5,6,7]|7[0,1,7,8]|8[0-9]|9[1,8,9])\d{8}$'
        # mask1 = df['反馈类型'].isin(type_selection)
        if accessible == '是':
            mask2 = ((df[ways].isin(type_problem_selection)) & (df['App版本'].isin(version_selection)) & (df['反馈内容'].str.findall(reg)))
        else:
            mask2 = ((df[ways].isin(type_problem_selection)) & (
                df['App版本'].isin(version_selection)))
        button_begin = st.button('检索数据')
        if button_begin:
            number_of_result2 = df[mask2].shape[0]

            st.markdown(f'*检索到数据：{number_of_result2} 条*')

            df_grouped = df[mask2].groupby(by=['deviceName']).count()[['反馈ID']]
            df_grouped = df_grouped.rename(columns={'反馈ID': '计数'})
            df_grouped = df_grouped.reset_index()
            bar_chart = px.bar(df_grouped.sort_values('计数', ascending=False), x='deviceName', y='计数', text='计数',
                               template='plotly_white', title='各机型反馈占比')

            pie_chart = px.pie(df_grouped, title='各机型反馈占比', values='计数', names='deviceName')

            col1, col2 = st.columns(2)

            with col1:
                st.plotly_chart(bar_chart)
            with col2:
                st.plotly_chart(pie_chart)

            df_grouped_system = df[mask2].groupby(by=['反馈平台']).count()[['反馈ID']]
            df_grouped_system = df_grouped_system.rename(columns={'反馈ID': '计数'})
            df_grouped_system = df_grouped_system.reset_index()
            bar_chart_system = px.bar(df_grouped_system.sort_values('计数', ascending=False), x='反馈平台', y='计数', text='计数',
                               template='plotly_white', title='各平台反馈占比')

            pie_chart_system = px.pie(df_grouped_system, title='各平台反馈占比', values='计数', names='反馈平台')

            col3, col4 = st.columns(2)
            with col3:
                st.plotly_chart(bar_chart_system)
            with col4:
                st.plotly_chart(pie_chart_system)

            df_grouped_version = df[mask2].groupby(by=['App版本']).count()[['反馈ID']]
            df_grouped_version = df_grouped_version.rename(columns={'反馈ID': '计数'})
            df_grouped_version = df_grouped_version.reset_index()
            bar_chart_version = px.bar(df_grouped_version.sort_values('计数', ascending=False), x='App版本', y='计数',
                                      text='计数',
                                      template='plotly_white', title='各App版本反馈占比')

            pie_chart_version = px.pie(df_grouped_version, title='各App版本反馈占比', values='计数', names='App版本')

            col5, col6 = st.columns(2)
            with col5:
                st.plotly_chart(bar_chart_version)
            with col6:
                st.plotly_chart(pie_chart_version)

            df_grouped_cat = df[mask2].groupby(by=['问题分类']).count()[['反馈ID']]
            df_grouped_cat = df_grouped_cat.rename(columns={'反馈ID': '计数'})
            df_grouped_cat = df_grouped_cat.reset_index()
            bar_chart_cat = px.bar(df_grouped_cat.sort_values('计数', ascending=False), x='问题分类', y='计数',
                                       text='计数',
                                       template='plotly_white', title='各问题分类占比')

            pie_chart_cat = px.pie(df_grouped_cat, title='各问题分类占比', values='计数', names='问题分类')

            col9, col10 = st.columns(2)
            with col9:
                st.plotly_chart(bar_chart_cat)
            with col10:
                st.plotly_chart(pie_chart_cat)

            df_grouped_cat2 = df[mask2].groupby(by=['问题分类 - 二级']).count()[['反馈ID']]
            df_grouped_cat2 = df_grouped_cat2.rename(columns={'反馈ID': '计数'})
            df_grouped_cat2 = df_grouped_cat2.reset_index()
            bar_chart_cat2 = px.bar(df_grouped_cat2.sort_values('计数', ascending=False), x='问题分类 - 二级', y='计数',
                                   text='计数',
                                   template='plotly_white', title='各二级分类占比')

            pie_chart_cat2 = px.pie(df_grouped_cat2, title='各二级分类占比', values='计数', names='问题分类 - 二级')

            col11, col12 = st.columns(2)
            with col11:
                st.plotly_chart(bar_chart_cat2)
            with col12:
                st.plotly_chart(pie_chart_cat2)






















            col7, col8 = st.columns(2)

            with col7:
                st.markdown('#### 日趋势')
                df['反馈时间'] = pd.to_datetime(df['反馈时间'])

                df_date = df[mask2].set_index(df[mask2]['反馈时间'], drop=True)
                df_date_day = df_date.resample('D').count()
                df_date_day = df_date_day[['反馈ID']]
                df_date_day = df_date_day.reset_index()
                df_date_day = df_date_day.rename(columns={'反馈ID': '反馈量', })
                plot1 = px.line(df_date_day, x='反馈时间', y='反馈量', title='日反馈趋势', )
                st.plotly_chart(plot1)
            with col8:
                st.markdown('#### 周趋势')
                df_date_week = df_date.resample('W-SUN').count()
                df_date_week = df_date_week[['反馈ID']]
                df_date_week = df_date_week.reset_index()
                df_date_week = df_date_week.rename(columns={'反馈ID': '反馈量', })
                # print(df_date_week)
                plot2 = px.line(df_date_week, x='反馈时间', y='反馈量', title='周反馈趋势')
                st.plotly_chart(plot2)

            # fig5 = FF.create_table(df_date_week, index=False)
            # st.plotly_chart(fig5)

            st.markdown('### 筛选后数据')
            st.dataframe(df[mask2][['反馈时间', '具体问题', '反馈内容', 'deviceName', 'App版本', '反馈平台']])
            # st.markdown('### 回访数据')
            print(df[mask2]['反馈内容'].str.split(';'))
            # df[mask2]['联系方式'] = df[mask2]['反馈内容'].str.split(';')[-1]
            df_contack = df[mask2]['反馈内容'].str.split(';', expand=True)
            # st.dataframe(df[mask2][['反馈ID', '反馈时间', '反馈内容']])
            # st.dataframe(df_contack)
            # origin_after_data_button = st.button('显示完整筛选后数据')
            # if origin_after_data_button:
            #     st.markdown('### 筛选后原始数据')
            #     st.dataframe(df[mask2])
            # origin_data_button = st.button('显示完整原始数据')
            # if origin_data_button:
            #     st.markdown('### 原始数据')
            #     st.dataframe(df)
    elif ways == '反馈内容关键词':
        keywords = st.text_input('输入反馈内容关键词')
        button_start = st.button('检索')
        reg = '1(3[0-9]|4[5,7]|5[0,1,2,3,5,6,7,8,9]|6[2,5,6,7]|7[0,1,7,8]|8[0-9]|9[1,8,9])\d{8}$'
        if button_start:
            if accessible == '否':
                mask2 = ((df['反馈内容'].str.contains(keywords)) & df['App版本'].isin(version_selection))
            else:
                mask2 = ((df['反馈内容'].str.contains(keywords)) & df['App版本'].isin(version_selection) & (df['反馈内容'].str.findall(reg)))
            number_of_result2 = df[mask2].shape[0]

            st.markdown(f'*检索到数据：{number_of_result2} 条*')

            df_grouped = df[mask2].groupby(by=['deviceName']).count()[['反馈ID']]
            df_grouped = df_grouped.rename(columns={'反馈ID': '计数'})
            df_grouped = df_grouped.reset_index()
            bar_chart = px.bar(df_grouped.sort_values('计数', ascending=False), x='deviceName', y='计数', text='计数',
                               template='plotly_white')

            pie_chart = px.pie(df_grouped, title='各机型反馈占比', values='计数', names='deviceName')

            st.plotly_chart(bar_chart)
            st.plotly_chart(pie_chart)

            st.markdown('#### 日趋势')
            df['反馈时间'] = pd.to_datetime(df['反馈时间'])
            df_date = df[mask2].set_index(df[mask2]['反馈时间'], drop=True)
            df_date_day = df_date.resample('D').count()
            df_date_day = df_date_day[['反馈ID']]
            df_date_day = df_date_day.reset_index()
            df_date_day = df_date_day.rename(columns={'反馈ID': '反馈量', })
            plot1 = px.line(df_date_day, x='反馈时间', y='反馈量', title='日反馈趋势')
            st.plotly_chart(plot1)

            st.markdown('#### 周趋势')
            df_date_week = df_date.resample('W-SUN').count()
            df_date_week = df_date_week[['反馈ID']]
            df_date_week = df_date_week.reset_index()
            df_date_week = df_date_week.rename(columns={'反馈ID': '反馈量', })
            # print(df_date_week)
            plot2 = px.line(df_date_week, x='反馈时间', y='反馈量', title='周反馈趋势')
            st.plotly_chart(plot2)

            fig5 = FF.create_table(df_date_week, index=False)
            st.plotly_chart(fig5)

            st.markdown('### 筛选后数据')
            st.dataframe(df[mask2][['反馈时间', '反馈ID', '具体问题(标注)', '反馈内容', 'deviceName', 'App版本']])
            origin_after_data_button = st.button('显示完整筛选后数据', key='11')
            if origin_after_data_button:
                st.markdown('### 筛选后原始数据')
                st.dataframe(df[mask2])
            # origin_data_button = st.button('显示完整原始数据', key='22')
            # if origin_data_button:
            #     st.markdown('### 原始数据')
            #     st.dataframe(df)

    else:
        st.info('请选择筛选方法')
else:
    st.info('未上传文件')



