import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px

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
    month_rent_df = df.resample(rule='M', on='dteday').agg({
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
    hourly_rent_df = hr_df.groupby(by=['hr','weekday']).agg({
        "cnt": "sum"
    })
    hourly_rent_df = hourly_rent_df.reset_index()

    
    return hourly_rent_df

#menyiapkan data
day_df=pd.read_csv("day_df.csv")
day_df.head()

hr_df=pd.read_csv("hr_df.csv")
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

fig, ax = plt.subplots(figsize=(30, 20))
sns.lineplot(
    data=hourly_rent_df,
    x='hr',
    y='cnt',
    hue='weekday',
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


# Hitung Recency, Frequency, dan Monetary
current_date = day_df['dteday'].max()  # Tanggal analisis
day_df['recency'] = (current_date - day_df['dteday']).dt.days
day_df['frequency'] = day_df['count']
day_df['monetary'] = day_df['casual'] + day_df['registered']

# Segmentasi pelanggan berdasarkan Recency dan Frequency
bins_recency = [0, 7, 14, 30, 365]  # Tentukan batas-batas kategori Recency
bins_frequency = [0, 50, 100, 200, 500, 1000]  # Tentukan batas-batas kategori Frequency

day_df['recency_category'] = pd.cut(day_df['recency'], bins=bins_recency, labels=['Hari ini', 'Minggu lalu', '2 Minggu lalu', 'Bulan lalu'])
day_df['frequency_category'] = pd.cut(day_df['frequency'], bins=bins_frequency, labels=['Sangat Jarang', 'Jarang', 'Cukup Sering', 'Sering', 'Sangat Sering'])

# Visualisasi
st.header('RFM Analysis on Bike Sharing Dataset')
st.subheader('Segmentation based on Recency and Frequency')

# Scatter plot Recency vs Frequency
plt.figure(figsize=(10, 6))
sns.scatterplot(x='recency', y='frequency', data=day_df, hue='monetary', palette='viridis', size='monetary', sizes=(20, 200), alpha=0.8)
plt.xlabel('Recency (Days)')
plt.ylabel('Frequency')
plt.title('Recency vs Frequency')
st.pyplot()

# Tampilkan tabel hasil segmentasi
st.subheader('Segmentation Results')
st.write(day_df[['dteday', 'recency', 'frequency', 'monetary', 'recency_category', 'frequency_category']])
st.set_option('deprecation.showPyplotGlobalUse', False)

st.caption('Copyright (c) Aulia Verent Amriawati 2023')
