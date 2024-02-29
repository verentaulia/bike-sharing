import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set(style='dark')

# Menyiapkan daily_rent_df
def create_daily_rent_df(df):
    daily_rent_df = df.groupby(by='dteday').agg({
        'count': 'sum'
    }).reset_index()
    return daily_rent_df

# Menyiapkan daily_casual_rent_df
def create_daily_casual_rent_df(df):
    daily_casual_rent_df = df.groupby(by='dteday').agg({
        'casual': 'sum'
    }).reset_index()
    return daily_casual_rent_df

# Menyiapkan daily_registered_rent_df
def create_daily_registered_rent_df(df):
    daily_registered_rent_df = df.groupby(by='dteday').agg({
        'registered': 'sum'
    }).reset_index()
    return daily_registered_rent_df
    

# Menyiapkan holiday_rent_df
def create_holiday_rent_df(df):
    holiday_rent_df = df.groupby(by='holiday').agg({
        "casual": "sum",
        "registered": "sum",
        "count": "sum"
    })
    holiday_rent_df = holiday_rent_df.reset_index()
    holiday_rent_df = pd.melt(holiday_rent_df,
                                      id_vars=['holiday'],
                                      value_vars=['casual', 'registered'],
                                      var_name='type_of_rides',
                                      value_name='jumlah')
    return holiday_rent_df


# Menyiapkan weekday_rent_df
def create_weekday_rent_df(df):
    weekday_rent_df = df.groupby(by='weekday').agg({
        "casual": "sum",
        "registered": "sum",
        "count": "sum"
    })
    weekday_rent_df = weekday_rent_df.reset_index()
    weekday_rent_df = pd.melt(weekday_rent_df,
                                      id_vars=['weekday'],
                                      value_vars=['casual', 'registered'],
                                      var_name='type_of_rides',
                                      value_name='jumlah')
    
    weekday_rent_df['weekday'] = pd.Categorical(weekday_rent_df['weekday'],
                                             categories=['Sun','Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
                                             ordered=True)
    weekday_rent_df = weekday_rent_df.sort_values('weekday')
    return weekday_rent_df
 
    
# Menyiapkan workingday_rent_df
def create_workingday_rent_df(df):
    workingday_rent_df = df.groupby(by='workingday').agg({
        "casual": "sum",
        "registered": "sum",
        "count": "sum"
    })
    workingday_rent_df = workingday_rent_df.reset_index()
    workingday_rent_df = pd.melt(workingday_rent_df,
                                      id_vars=['workingday'],
                                      value_vars=['casual', 'registered'],
                                      var_name='type_of_rides',
                                      value_name='jumlah')
    
    return workingday_rent_df

# Menyiapkan month_rent_df
def create_month_rent_df(df):
    month_rent_df = df.resample(rule='ME', on='dteday').agg({
        "casual": "sum",
        "registered": "sum",
        "count": "sum"
    })
    month_rent_df.index = month_rent_df.index.strftime('%b-%y')
    month_rent_df = month_rent_df.reset_index()
    month_rent_df.rename(columns={
        "dteday": "yearmonth",
        "count": "total_rides",
        "casual": "casual_rides",
        "registered": "registered_rides"
    }, inplace=True)
    
    return month_rent_df

# Menyiapkan season_rent_df
def create_season_rent_df(df):
    season_rent_df = df.groupby(by='season').agg({
        "casual": "sum",
        "registered": "sum",
        "count": "sum"
    })
    season_rent_df = season_rent_df.reset_index()
    season_rent_df = pd.melt(season_rent_df,
                                      id_vars=['season'],
                                      value_vars=['casual', 'registered'],
                                      var_name='type_of_rides',
                                      value_name='jumlah')
    
    return season_rent_df

# Menyiapkan weather_rent_df
def create_weather_users_df(df):
    weather_users_df = df.groupby(by='weather').agg({
        "casual": "sum",
        "registered": "sum",
        "count": "sum"
    })
    weather_users_df = weather_users_df.reset_index()
    weather_users_df = pd.melt(weather_users_df,
                                      id_vars=['weather'],
                                      value_vars=['casual', 'registered'],
                                      var_name='type_of_rides',
                                      value_name='jumlah')
    
    return weather_users_df

# Menyiapkan hourly_rent_df
def create_hourly_rent_df(df):
    hourly_rent_df = hr_df.groupby(by=['hr','workingday']).agg({
        "cnt": "sum"
    })
    hourly_rent_df = hourly_rent_df.reset_index()

    
    return hourly_rent_df

#Menyiapkan RFM Analysis
def create_rfm_df(df):
    rfm_df = day_df.groupby(by="weekday", as_index=False).agg({
        "dteday": "max",
        "instant": "nunique",
        "count": "sum"
    })
    rfm_df.columns = ["weekday", "max_order_timestamp", "frequency", "monetary"]
    rfm_df["max_order_timestamp"] = rfm_df["max_order_timestamp"].dt.date
    recent_date = day_df["dteday"].dt.date.max()
    rfm_df["recency"] = rfm_df["max_order_timestamp"].apply(lambda x: (recent_date - x).days)
    rfm_df.drop("max_order_timestamp", axis=1, inplace=True)
    return rfm_df

#menyiapkan data
day_df=pd.read_csv("https://raw.githubusercontent.com/verentaulia/bike-sharing/master/dashboard/day_df.csv")
day_df.head()

hr_df=pd.read_csv("https://raw.githubusercontent.com/verentaulia/bike-sharing/master/dashboard/hr_df.csv")
hr_df.head()

day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hr_df['dteday'] = pd.to_datetime(hr_df['dteday'])

    
# Membuat komponen filter
min_date = pd.to_datetime(day_df['dteday']).dt.date.min()
max_date = pd.to_datetime(day_df['dteday']).dt.date.max()
 
with st.sidebar:
    st.image("https://raw.githubusercontent.com/verentaulia/bike-sharing/4f625891172bf390a7c982138a7397f5dd994dab/dashboard/capital_bikeshare.png")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value= min_date,
        max_value= max_date,
        value=[min_date, max_date]
    )

main_df = day_df[(day_df['dteday'] >= str(start_date)) & 
                (day_df['dteday'] <= str(end_date))]

# Menyiapkan dataframe
daily_rent_df = create_daily_rent_df(main_df)
daily_casual_rent_df = create_daily_casual_rent_df(main_df)
daily_registered_rent_df = create_daily_registered_rent_df(main_df)
holiday_rent_df = create_holiday_rent_df(main_df)
weekday_rent_df = create_weekday_rent_df(main_df)
workingday_rent_df = create_workingday_rent_df(main_df)
month_rent_df = create_month_rent_df(main_df)
season_rent_df = create_season_rent_df(main_df)
hourly_rent_df = create_hourly_rent_df(main_df)
weather_users_df = create_weather_users_df(main_df)
rfm_df = create_rfm_df(main_df)

# Membuat Dashboard secara lengkap

# Membuat judul
st.header('Bike Sharing Dashboard 🚲')


#jumlah penyewaan harian
st.subheader('Daily Rentals')
col1, col2, col3 = st.columns(3)

with col1:
    daily_rent_casual = daily_casual_rent_df['casual'].sum()
    st.metric('Casual User', value= daily_rent_casual)

with col2:
    daily_rent_registered = daily_registered_rent_df['registered'].sum()
    st.metric('Registered User', value= daily_rent_registered)
 
with col3:
    daily_rent_total = daily_rent_df['count'].sum()
    st.metric('Total User', value= daily_rent_total)

# jumlah penyewaan bulanan
st.subheader('Monthly Rentals')
fig, ax = plt.subplots(figsize=(24, 8))
ax.plot(
    month_rent_df["yearmonth"],
    month_rent_df['registered_rides'],
    marker='o', 
    linewidth=2,
    color='tab:blue'
)

ax.plot(
    month_rent_df["yearmonth"],
    month_rent_df['casual_rides'],
    marker='o', 
    linewidth=2,
    color='tab:orange'
)

for index, row in month_rent_df.iterrows():
    ax.text(index, row['registered_rides'], str(row['registered_rides']), ha='center', va='bottom', fontsize=12)
    ax.text(index, row['casual_rides'], str(row['casual_rides']), ha='center', va='bottom', fontsize=12)

ax.tick_params(axis='x', labelsize=25, rotation=45)
ax.tick_params(axis='y', labelsize=20)
ax.set_ylabel("Jumlah Sepeda Disewakan", fontsize=18)
ax.set_xlabel(None)
ax.set_title("Jumlah Penyewaan pada Tahun 2011 dan 2012", loc="center",fontsize=35)
ax.legend(title='type of rides',labels=['registered rides','casual rides'] )
st.pyplot(fig)

#jumlah penyewaan holiday, workingday dan weekday
st.subheader('Holiday, Workingday and Weekday Rentals')

col1, col2 = st.columns(2)
 
with col1:
    # Berdasarkan holiday
    fig, ax = plt.subplots(figsize=(20,10))

    sns.barplot(
        x='holiday', 
        y='jumlah', 
        data=holiday_rent_df, 
        order=holiday_rent_df['holiday'], 
        hue='type_of_rides',
        palette='Set2',
        ax=ax
    )

    ax.set_title("Number of Bikeshare Rides Based on Holiday", loc="center", fontsize=30)
    ax.set_xlabel(None)
    ax.set_ylabel("Total rides")
    ax.tick_params(axis='y', labelsize=25)
    ax.tick_params(axis='x', labelsize=20)
    ax.legend(title='type of rides')
    st.pyplot(fig)
 
with col2:
    #Berdasarkan workingday
    fig, ax = plt.subplots(figsize=(20,10))
    sns.barplot(
        x='workingday', 
        y='jumlah', 
        data=workingday_rent_df, 
        order=workingday_rent_df['workingday'], 
        hue='type_of_rides',
        palette='Set2',
        ax=ax
    )

    ax.set_title("Number of Bikeshare Rides Based on Workingday", loc="center", fontsize=30)
    ax.set_xlabel(None)
    ax.set_ylabel("Total rides")
    ax.tick_params(axis='y', labelsize=25)
    ax.tick_params(axis='x', labelsize=20)
    ax.legend(title='type of rides')
    st.pyplot(fig)



# Berdasarkan weekday
fig, ax = plt.subplots(figsize=(20,8))
sns.barplot(
    x='weekday', 
    y='jumlah', 
    data=weekday_rent_df, 
    order=weekday_rent_df['weekday'],
    hue='type_of_rides',
    palette='Set2',
    ax=ax
    )

ax.set_title("Number of Bikeshare Rides Based on Weekday", loc="center", fontsize=30)
ax.set_xlabel(None)
ax.set_ylabel("Total rides")
ax.tick_params(axis='y', labelsize=25)
ax.tick_params(axis='x', labelsize=20)
ax.legend(title='type of rides')
st.pyplot(fig)

#Jumlah Penyewaan Berdasarkan Season
st.subheader('Seasonly Rentals')

fig, ax = plt.subplots(figsize=(20,10))
sns.barplot(
    x='season', 
    y='jumlah', 
    data=season_rent_df, 
    order=season_rent_df['season'],
    hue='type_of_rides',
    palette='Set2',
    ax=ax
    )

ax.set_title("Number of Bikeshare Rides Based on Season", loc="center", fontsize=30)
ax.set_xlabel(None)
ax.set_ylabel("Total rides")
ax.tick_params(axis='y', labelsize=25)
ax.tick_params(axis='x', labelsize=20)
ax.legend(title='type of rides')
st.pyplot(fig)

#Jumlah Penyewaan Berdasarkan Weather
st.subheader('Weatherly Rentals')

fig, ax = plt.subplots(figsize=(20,10))
sns.barplot(
    x='weather', 
    y='jumlah', 
    data=weather_users_df, 
    order=weather_users_df['weather'],
    hue='type_of_rides',
    palette='Set2',
    ax=ax
    )

ax.set_title("Number of Bikeshare Rides Based on Weather", loc="center", fontsize=30)
ax.set_xlabel(None)
ax.set_ylabel("Total rides")
ax.tick_params(axis='y', labelsize=25)
ax.tick_params(axis='x', labelsize=20)
ax.legend(title='type of rides')
st.pyplot(fig)

# jumlah penyewaan per jam
st.subheader('Hourly Rentals')

fig, ax = plt.subplots(figsize=(20, 5))
sns.lineplot(
    data=hourly_rent_df,
    x='hr',
    y='cnt',
    hue='workingday',
    palette='bright'
)

ax.tick_params(axis='x', labelsize=25, rotation=45)
ax.tick_params(axis='y', labelsize=20)
ax.set_ylabel("Jumlah Sepeda Disewakan", fontsize=18)
ax.set_xlabel(None)
ax.set_title("Jumlah Penyewaan per Jam", loc="center",fontsize=35)
ax.set_xticks(hourly_rent_df['hr'].unique())
ax.set_xticklabels(hourly_rent_df['hr'].unique())
ax.legend(title='day')
st.pyplot(fig)


#RFM Analysis

st.subheader("Best Customer Based on RFM Parameters (day)")
col1, col2, col3 = st.columns(3)

with col1:
    avg_recency = round(rfm_df.recency.mean(), 1)
    st.metric("Average Recency (days)", value=avg_recency)

with col2:
    avg_frequency = round(rfm_df.frequency.mean(), 2)
    st.metric("Average Frequency", value=avg_frequency)

with col3:
    avg_frequency = format_currency(rfm_df.monetary.mean(), "AUD", locale='es_CO') 
    st.metric("Average Monetary", value=avg_frequency)

fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(35, 15))
colors = ["#90CAF9", "#90CAF9", "#90CAF9", "#90CAF9", "#90CAF9","#90CAF9", "#90CAF9"]

sns.barplot(y="recency", x="weekday", data=rfm_df.sort_values(by="recency", ascending=True).head(7), palette=colors, hue="weekday", legend=False, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("By Recency (days)", loc="center", fontsize=50)
ax[0].tick_params(axis='y', labelsize=25)
ax[0].tick_params(axis ='x', labelsize=30, rotation=45)

sns.barplot(y="frequency", x="weekday", data=rfm_df.sort_values(by="frequency", ascending=False).head(7), palette=colors, hue="weekday", legend=False, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].set_title("By Frequency", loc="center", fontsize=50)
ax[1].tick_params(axis='y', labelsize=25)
ax[1].tick_params(axis='x', labelsize=30, rotation=45)

sns.barplot(y="monetary", x="weekday", data=rfm_df.sort_values(by="monetary", ascending=False).head(7), palette=colors, hue="weekday", legend=False, ax=ax[2])
ax[2].set_ylabel(None)
ax[2].set_xlabel(None)
ax[2].set_title("By Monetary", loc="center", fontsize=50)
ax[2].tick_params(axis='y', labelsize=25)
ax[2].tick_params(axis='x', labelsize=30, rotation=45)

st.pyplot(fig)

st.caption('Copyright (c) Aulia Verent Amriawati 2023')
