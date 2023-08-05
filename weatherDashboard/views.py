import time
from django.shortcuts import render, redirect

import json
import pandas as pd
from django.http import JsonResponse


def get_data(request):
    AWS_S3_BUCKET = "o2afiles"
    AWS_ACCESS_KEY_ID = "AKIAQ4OQCD35ZJDZWCE5"
    AWS_SECRET_ACCESS_KEY = "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"
    
    df = pd.read_csv(
        f"s3://{AWS_S3_BUCKET}/weather.csv",
        storage_options={
            "key": AWS_ACCESS_KEY_ID,
            "secret": AWS_SECRET_ACCESS_KEY,
        }
    )
    
    df_hourly = pd.read_csv(
        f"s3://{AWS_S3_BUCKET}/hourly_weather.csv",
        storage_options={
            "key": AWS_ACCESS_KEY_ID,
            "secret": AWS_SECRET_ACCESS_KEY,
        }
    )
        
    hourly_temp_list = df_hourly["temp_moy"].tolist()
    hours = df_hourly["hour"].tolist()
    
    df_daily = pd.read_csv(
        f"s3://{AWS_S3_BUCKET}/daily_weather.csv",
        storage_options={
            "key": AWS_ACCESS_KEY_ID,
            "secret": AWS_SECRET_ACCESS_KEY,
        }
    )
        
    daily_temp_list = df_daily["temp_moy"].tolist()
    days = df_daily["date"].tolist()
    
    temp_list = df["temp"].tolist()
    hum_list = df["hum"].tolist()
    wsp_list = df["wsp"].tolist()
    prec_list = df["prec"].tolist()
            
    times = [15, 30, 45, 60, 15, 30, 45, 60, 15, 30, 45, 60, 15, 30, 45, 60, 15, 30, 45, 60]
    
    df_forecast = pd.read_csv(
        f"s3://{AWS_S3_BUCKET}/predictions.csv",
        storage_options={
            "key": AWS_ACCESS_KEY_ID,
            "secret": AWS_SECRET_ACCESS_KEY,
        }
    )
    ens = df["ens"].tolist()
    times2Hours = [15, 30, 45, 60, 15, 30, 45, 60, 15, 30, 45, 60]
    last_forecasts = []

    for column in df_forecast.columns:
        last_forecast = df_forecast[column].iloc[-1]
        last_forecasts.append(last_forecast)
        
    
    
    return JsonResponse({
        'hours': hours, 
        'hourly_temp_list': hourly_temp_list, 
        'days': days, 
        'daily_temp_list': daily_temp_list,
        'temp_list': temp_list[-20:],
        'hum_list': hum_list[-20:],
        'wsp_list': wsp_list[-20:],
        'prec_list': prec_list[-20:], 
        'times': times,
        'last_forecasts': last_forecasts,
        'ens': ens[-20:],
        'times2Hours': times2Hours        
        })
    

def view_base(request):
    AWS_S3_BUCKET = "o2afiles"
    AWS_ACCESS_KEY_ID = "AKIAQ4OQCD35ZJDZWCE5"
    AWS_SECRET_ACCESS_KEY  = "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"
    

    df = pd.read_csv(
        f"s3://{AWS_S3_BUCKET}/weather.csv",
        storage_options={
            "key": AWS_ACCESS_KEY_ID,
            "secret": AWS_SECRET_ACCESS_KEY,
        }
    )
    
    df_pred = pd.read_csv(
        f"s3://{AWS_S3_BUCKET}/predictions.csv",
        storage_options={
            "key": AWS_ACCESS_KEY_ID,
            "secret": AWS_SECRET_ACCESS_KEY,
        }
    ) 
    df_hourly = pd.read_csv(
        f"s3://{AWS_S3_BUCKET}/hourly_weather.csv",
        storage_options={
            "key": AWS_ACCESS_KEY_ID,
            "secret": AWS_SECRET_ACCESS_KEY,
        }
    )
    
    df_daily = pd.read_csv(
        f"s3://{AWS_S3_BUCKET}/daily_weather.csv",
        storage_options={
            "key": AWS_ACCESS_KEY_ID,
            "secret": AWS_SECRET_ACCESS_KEY,
        }
    )
    
    df_forecast = pd.read_csv(
        f"s3://{AWS_S3_BUCKET}/predictions.csv",
        storage_options={
            "key": AWS_ACCESS_KEY_ID,
            "secret": AWS_SECRET_ACCESS_KEY,
        }
    )
    
    last_forecasts = []

    for column in df_forecast.columns:
        last_forecast = df_forecast[column].iloc[-1]
        last_forecasts.append(last_forecast)

    firstEightForecasts = last_forecasts[:8]

    # Extract the "temp" column into a list
    temp_list = df["temp"].tolist()
    mean_temp = int(sum(temp_list)/len(temp_list))
    hum_list = df["hum"].tolist()
    mean_hum = int(sum(hum_list)/len(hum_list))
    wsp_list = df["wsp"].tolist()
    mean_wsp = int(sum(wsp_list)/len(wsp_list))
    prec_list = df["prec"].tolist()
    mean_prec = int(sum(prec_list)/len(prec_list))
    
    hourly_temp_list = df_hourly["temp_moy"].tolist()
    hours = df_hourly["hour"].tolist()
    
    daily_temp_list = df_daily["temp_moy"].tolist()
    days = df_daily["date"].tolist()
        
    timestamps = df["timestamp"].tolist()
    times = [15, 30, 45, 60, 15, 30, 45, 60, 15, 30, 45, 60, 15, 30, 45, 60, 15, 30, 45, 60]
    
    ens = df["ens"].tolist()
    times2Hours = [15, 30, 45, 60, 15, 30, 45, 60, 15, 30, 45, 60]
    

    # Pass the temp_list to the view_base template
    return render(request, "home.html", {
        'temp_list': temp_list[-20:], 
        'mean_temp': mean_temp, 
        'hum_list': hum_list[-20:],
        'wsp_list': wsp_list[-20:],
        'prec_list': prec_list[-20:], 
        'mean_wsp': mean_wsp, 
        'mean_hum':mean_hum, 
        'mean_prec': mean_prec, 
        'times':times, 
        'timestamps':timestamps,
        'hourly_temp_list':hourly_temp_list,
        'daily_temp_list':daily_temp_list,
        'hours': hours,
        'days':days,
        'firstEightForecasts': firstEightForecasts,
        'ens': ens[-20:],
        'times2Hours': times2Hours
        })

def view_forecast(request):
    AWS_S3_BUCKET = "o2afiles"
    AWS_ACCESS_KEY_ID = "AKIAQ4OQCD35ZJDZWCE5"
    AWS_SECRET_ACCESS_KEY  = "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"
    
    df_forecast = pd.read_csv(
        f"s3://{AWS_S3_BUCKET}/predictions.csv",
        storage_options={
            "key": AWS_ACCESS_KEY_ID,
            "secret": AWS_SECRET_ACCESS_KEY,
        }
    )
    
    last_forecasts = []

    for column in df_forecast.columns:
        last_forecast = df_forecast[column].iloc[-1]
        last_forecasts.append(last_forecast)

    lastFourForecasts = last_forecasts[-4:]
    
    times = [15, 30, 45, 60, 15, 30, 45, 60, 15, 30, 45, 60, 15, 30, 45, 60, 15, 30, 45, 60]
    
    times3hours = [15, 30, 45, 60, 15, 30, 45, 60, 15, 30, 45, 60]

    # Pass the temp_list to the view_base template
    return render(request, "forecast.html", {
                                        'times': times,
                                        'last_forecasts': last_forecasts,
                                        'times3hours': times3hours,
                                        'lastFourForecasts': lastFourForecasts
                                        })


def view_humidity(request):

    
    return render(request, "humidity.html") 

def view_temperature(request):
    AWS_S3_BUCKET = "o2afiles"
    AWS_ACCESS_KEY_ID = "AKIAQ4OQCD35ZJDZWCE5"
    AWS_SECRET_ACCESS_KEY  = "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"
    
    df_hourly = pd.read_csv(
        f"s3://{AWS_S3_BUCKET}/hourly_weather.csv",
        storage_options={
            "key": AWS_ACCESS_KEY_ID,
            "secret": AWS_SECRET_ACCESS_KEY,
        }
    )
    
    df_daily = pd.read_csv(
        f"s3://{AWS_S3_BUCKET}/daily_weather.csv",
        storage_options={
            "key": AWS_ACCESS_KEY_ID,
            "secret": AWS_SECRET_ACCESS_KEY,
        }
    )
    
    hourly_temp_list = df_hourly["temp_moy"].tolist()
    hours = df_hourly["hour"].tolist()
    # hours = hours.sort
    
    daily_temp_list = df_daily["temp_moy"].tolist()
    days = df_daily["date"].tolist()
            
    times = [15, 30, 45, 60, 15, 30, 45, 60, 15, 30, 45, 60, 15, 30, 45, 60, 15, 30, 45, 60]

    return render(request, "temperature.html", {
        'hourly_temp_list':hourly_temp_list,
        'daily_temp_list':daily_temp_list,
        'hours': hours,
        'days':days,
        'times': times,
        })

def view_wind(request):

    
    return render(request, "wind.html")

def view_precipitation(request):

    
    return render(request, "precipitation.html")

    
def view_chart(request):

    
    return render(request, "chartTest.html")
