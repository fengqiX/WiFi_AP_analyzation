import pandas as pd
import os
import datetime
import numpy as np
import matplotlib.pyplot as plt



def RF_Counter_func():
    path = r"C:\Users\fxiao\Documents\RF counters"
    listdir = os.listdir(path)
    df_result = pd.DataFrame()
    print(listdir)
    for file in listdir:
        # print(os.path.splitext(file))
        if 'csv' in os.path.splitext(file)[1]:
            fullPath = os.path.join(path, file)
            data = pd.read_csv(fullPath, error_bad_lines=False, skiprows=7)
            # print(pd.to_datetime(data["Time"]).dt.date)
            data["Time"] = pd.to_datetime(data["Time"],errors='ignore').dt.date
            # if data["Time"] == "2018-11-18":

            df_group = data.fillna(-1).groupby("Time")
            df_retry_total = df_group['Retry Count'].sum(skipna=False)
            df_frameCount_total = df_group['Tx Frame Count'].sum(skipna=False)
            df_RTS_success_count_total=df_group['RTS Success Count'].sum(skipna=False)
            df_RTS_failure_count_total = df_group['RTS Failure Count'].sum(skipna=False)
            df_Multiple_Retry_Count_total = df_group['Multiple Retry Count'].sum(skipna=False)
            print(df_retry_total)
            if 'Retry_total' in df_result:
                df_result['Retry_total']=df_result['Retry_total'].add(df_retry_total,fill_value = 0)
            else:
                df_result['Retry_total']=df_retry_total
            if 'FrameCount_total' in df_result:
                df_result['FrameCount_total']=df_result['FrameCount_total'].add(df_frameCount_total,fill_value = 0)
            else:
                df_result['FrameCount_total']=df_frameCount_total
            if 'RTS_Success_Count_total' in df_result:
                df_result['RTS_Success_Count_total']=df_result['RTS_Success_Count_total'].add(df_RTS_success_count_total,fill_value = 0)
            else:
                df_result['RTS_Success_Count_total']=df_RTS_success_count_total
            if 'RTS_Failure_Count_total' in df_result:
                df_result['RTS_Failure_Count_total']=df_result['RTS_Failure_Count_total'].add(df_RTS_failure_count_total,fill_value = 0)
            else:
                df_result['RTS_Failure_Count_total']=df_RTS_failure_count_total
            if 'Multiple_Retry_Count_total' in df_result:
                df_result['Multiple_Retry_Count_total'] = df_result['Multiple_Retry_Count_total'].add(df_Multiple_Retry_Count_total,fill_value = 0)
            else:
                df_result['Multiple_Retry_Count_total'] = df_Multiple_Retry_Count_total
    df_rate_result = pd.DataFrame()
    df_rate_result['Retry_Rate'] = df_result['Retry_total']/df_result['FrameCount_total']
    df_rate_result['Failure_Rate'] = df_result['RTS_Failure_Count_total']/(df_result['RTS_Failure_Count_total']+df_result['RTS_Success_Count_total'])

    # print(df_rate_result)
    # df_rate_result.to_excel('RF_Counters analyzed 2.xlsx',sheet_name='Sheet1')
    df_result.to_excel("RF_Counters Total 35.xlsx",sheet_name="Sheet1")
    print("Done!")
    # df_rate_result.plot()
    # plt.grid(True)
    # plt.show()

def RF_Wem_func():
    df_result = pd.DataFrame()
    path = r"C:\Users\fxiao\Documents\RF counters"
    listdir = os.listdir(path)
    for file in listdir:
        # print(os.path.splitext(file))
        print(os.path.splitext(file))
        if 'csv' in os.path.splitext(file)[1]:
            fullPath = os.path.join(path, file)
            data = pd.read_csv(fullPath, error_bad_lines=False, skiprows=7)
            data["Time"] = pd.to_datetime(data["Time"], errors='ignore').dt.date
            df_group = data.fillna(0).groupby("Time")
            df_Tx_Fragment_Count_total = df_group['Tx Fragment Count'].sum(skipna=False)
            df_Rx_Fragment_Count_total = df_group['Rx Fragment Count'].sum(skipna=False)
            df_FCS_Error_Count_total = df_group['FCS Error Count'].sum(skipna=False)
            df_Retry_Count_total = df_group['Retry Count'].sum(skipna=False)

            if 'Tx_Fragment_Count_total' in df_result:
                df_result['Tx_Fragment_Count_total'] = df_result['Tx_Fragment_Count_total'].add(df_Tx_Fragment_Count_total,fill_value = 0)
            else:
                df_result['Tx_Fragment_Count_total'] = df_Tx_Fragment_Count_total

            if 'Rx_Fragment_Count_total' in df_result:
                df_result['Rx_Fragment_Count_total'] = df_result['Rx_Fragment_Count_total'].add(df_Rx_Fragment_Count_total,fill_value = 0)
            else:
                df_result['Rx_Fragment_Count_total'] = df_Rx_Fragment_Count_total

            if 'FCS_Error_Count_total' in df_result:
                df_result['FCS_Error_Count_total'] = df_result['FCS_Error_Count_total'].add(df_FCS_Error_Count_total,fill_value = 0)
            else:
                df_result['FCS_Error_Count_total'] = df_FCS_Error_Count_total

            if 'Retry_Count_total' in df_result:
                df_result['Retry_Count_total'] = df_result['Retry_Count_total'].add(df_Retry_Count_total,fill_value = 0)
            else:
                df_result['Retry_Count_total'] = df_Retry_Count_total

        df_result.to_excel("RF Couters Wem33.xlsx",sheet_name="Sheet1")

if __name__ == "__main__":
    # 显示所有列
    pd.set_option('display.max_columns', None)
    # 显示所有行
    pd.set_option('display.max_rows', None)
    # 设置value的显示长度为100，默认为50
    pd.set_option('max_colwidth', 100)

    RF_Counter_func()
    # RF_Wem_func()