import time
import pandas as pd
import numpy as np

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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('\nType the name of the city you want to explore its data. \n' +
                     '\nChicago. \nNew York City. \nWashington. \n')
        if city.lower() in CITY_DATA.keys():
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Specify the month of data to explore.'+ '\nAll, January, February, March, April, May, or June..\n')
        if month.lower() in ['all', 'january', 'february', 'march',
                             'april', 'may', 'june']:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Specify the day of data to explore. ' +
                    'All, Monday, Tuesday, Wednesday, Thursday, Friday, ' +
                    'Saturday, Sunday?\n')
        if day.lower() in ['all', 'monday', 'tuesday', 'wednesday', 'thursday',
                           'friday', 'saturday', 'sunday']:
            break

    print('-'*50)
    return city.lower(), month.lower(), day.lower()


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

    # convert  'Start Time' column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from 'Start Time' column to create new one
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('\nThe most common month of travel is: \n')
    print(df['month'].mode()[0])

    # display the most common day of week
    print('\nThe most common day of week for travel is: \n')
    print(df['day_of_week'].mode()[0])

    # display the most common start hour
    print('\nThe most common hour for travel is: \n')
    print(df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('\nThe most commonly used start station is: \n')
    print(df['Start Station'].mode()[0])

    # display most commonly used end station
    print('\nThe most commonly used end station is: ')
    print(df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    frequent_comb_stations = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print("The most frequent combination of start station and end station  is : \n" + str(frequent_comb_stations.split("||")))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    travel_time = df['Trip Duration'].sum()
    print('Total travel time is: \n' + str(travel_time))

    # display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print('The travel time average is: \n' + str(avg_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()


    # Display counts of user types
    count_user_types = df['User Type'].value_counts()
    print('The count of user types is: \n' + str(count_user_types))

    # Display counts of gender
    print('The gender count is: \n')
    try:
        print(df['Gender'].value_counts())
        #To handle null values in gender
    except:
        print('No gender data found')

    # Display earliest, most recent, and most common year of birth
    print('\nEarliest, Latest & Most Common Date of Birth:')
    try:
        print('Earliest: {}\nLatest: {}\nMost Common: {}'
              .format(df['Birth Year'].min(), df['Birth Year'].max(),
                      df['Birth Year'].mode()[0]))
    except:
        print('No birth year data found')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
