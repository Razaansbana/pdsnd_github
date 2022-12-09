import time
import pandas as pd
import numpy as np
import datetime as dt

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        try:
            city = str(input('Name of the city to analyze: ').lower())
            df = pd.read_csv(CITY_DATA[city])
            break
        except KeyError:
            print('\nPlease only choose from Chicago, Washington and New York City')

    # TO DO: get user input for month (all, january, february, ... , june)
    month_list = ['january', 'february', 'march', 'april', 'may', 'june','all']
    while True:
        try:
            month = input(('\nName of the month to filter by, or "all" to apply no month filter: ').lower())
            month_index = month_list.index(month)
            break
        except:
            print('\nPlease only choose one month from Janurary to June or select all')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_list = ['Monday', 'Tuesday', 'Wednesday','Thursday','Friday','Saturday','Sunday','All']
    while True:
        try:
            day = input('\nName of the day of week to filter by, or "all" to apply no day filter:').capitalize()
            day_index = day_list.index(day)
            break
        except:
            print('\nPlease type in Monday, Tuesday.... or all')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    #filter by month
    if month != "all":
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month']==month]

    #filter by day
    if day != "All":
        df = df[df['day_of_week']==day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('most common month: ',most_common_month)

    # TO DO: display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print('most common day of week: ',most_common_day_of_week)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print('most common hour: ',most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start_station = df['Start Station'].mode()[0]
    print('most commonly used start station: ', most_start_station)

    # TO DO: display most commonly used end station
    most_end_station = df['End Station'].mode()[0]
    print('most commonly used end station: ', most_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_start_end = df.groupby(['Start Station','End Station']).size().idxmax()
    print('\nmost frequent combination of start station and end station: ', most_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("total travel time: ", df['Trip Duration'].sum()/3600/24, ' days.')

    # TO DO: display mean travel time
    print("\nmean travel time: ", df['Trip Duration'].mean()/60 ,' minutes.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\ncounts of user types:\n ', user_types)

    # TO DO: Display counts of gender
    if city != 'washington':
        df.dropna(axis = 0)
        gender_counts = df['Gender'].value_counts()
        print('\ncounts of gender: \n', gender_counts)
    else:
        print('\nNo gender information for Washington')

    # TO DO: Display earliest, most recent, and most common year of birth
    if city != 'washington':
        df.dropna(axis = 0)
        earliest = int(df['Birth Year'].min())
        print('\nearliest year of birth: ', earliest)
        most_recent = int(df['Birth Year'].max())
        print('\nmost recent year of birth: ', most_recent)
        most_common = int(df['Birth Year'].mode()[0])
        print('\nmost common year of birth: ', most_common)
    else:
        print('No birth year information for Washington')

    answer_list = ['yes','no']
    i = 0
    j = 10
    while True:
        try:
            answer = input(('would you like to see 10 rows of data? yes/no ').lower())
            answer_index = answer_list.index(answer)
            if answer == 'yes':
                print(df[i:j])
                i += 10
                j += 10
                continue
            else:
                break
        except:
            print('Please only enter yes/no')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():

    while True:

        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)




if __name__ == "__main__":
	main()
