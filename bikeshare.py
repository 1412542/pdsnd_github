import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_LIST = {'january' : 1 ,
              'february' : 2,
              'march' : 3,
              'april' : 4,
              'may' : 5,
              'june' : 6 }
DAY_LIST = {'monday' : 0,
            'tuesday' : 1,
            'wednesday' : 2,
            'thursday' : 3,
            'friday' : 4,
            'saturday' : 5,
            'sunday' : 6 }

ALL_STR = 'all'

def get_key_from_value_in_dictionary(dictionary, value):
    """Find the key in a dictionary by value """
    
    # list out keys and values separately
    key_list = list(dictionary.keys())
    val_list = list(dictionary.values())
 
    # print key with val 100
    position = val_list.index(value)
    return key_list[position]
              
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
    city = "";
    while (city not in CITY_DATA):
        print('Please input one of three city name (chicago, new york city, washington): ')
        city = input().lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    
    month = "";
    while (month not in MONTH_LIST and month != ALL_STR):
        print('\nPlease input a name of the month {January, February, March, April, May, June} to filter by, or "all" to apply no month filter: ')
        month = input().lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = "";
    while (day not in DAY_LIST and day != ALL_STR):
        print('\nPlease input a name of the day of week to filter by, or "all" to apply no day filter: ')
        day = input().lower()

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
    
    ## convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    ## extract month and day from the Start Time column 
    df['Month'] = df['Start Time'].dt.month
    df['Day Name'] = df['Start Time'].dt.dayofweek
    df['Hour'] = df['Start Time'].dt.hour
    
    if (month != ALL_STR):
        df = df[df['Month'] == MONTH_LIST[month]]
              
    if (day != ALL_STR):
        df = df[df['Day Name'] == DAY_LIST[day]]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_month = df['Month'].value_counts().index.tolist()[0]
    print('\nThe most common month is: %s' % get_key_from_value_in_dictionary(MONTH_LIST, most_month))

    # TO DO: display the most common day of week
    most_day_of_week = df['Day Name'].value_counts().index.tolist()[0]
    print('\nThe most common day of week is: %s' % get_key_from_value_in_dictionary(DAY_LIST, most_day_of_week))

    # TO DO: display the most common start hour
    most_hour = df['Hour'].value_counts().index.tolist()[0]
    print('\nThe most common start hour is: %s' % most_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start_station = df['Start Station'].value_counts().index.tolist()[0]
    print ('\nThe most common start station is: %s' % most_start_station)
    
    # TO DO: display most commonly used end station
    most_end_station = df['End Station'].value_counts().index.tolist()[0]
    print ('\nThe most common end station is: %s' % most_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    # Select the 'name' and 'age' columns
    df['trip'] = df['Start Station'] + '_' + df['End Station']
    most_combination_stations = df['trip'].mode()[0]
    print ('\nThe most frequent combination of start station and end station trip is: %s' % most_combination_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print ('\nThe total travel time is: %s' % total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print ('\nThe total travel time is: %s' % mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nCounts of user types:');
    for idx, name in enumerate(user_types.index.tolist()): 
        print('\n {0}: {1}'.format(name, user_types[idx]) )

    # TO DO: Display counts of gender
    is_gender_exists = 'Gender' in df.columns
    if not is_gender_exists:
        print('\nGender information is not provided in this data.')
    else:
        gender = df['Gender'].value_counts()
        print('\nCounts of gender:');
        for idx, name in enumerate(gender.index.tolist()): 
            print('\n {0}: {1}'.format(name, gender[idx]))

    # TO DO: Display earliest, most recent, and most common year of birth
    is_birth_exists = 'Birth Year' in df.columns
    if not is_birth_exists:
        print('\nBirth Year information is not provided in this data.')
    else: 
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()[0]
        print('\nThe earliest Birth Year: ', int(earliest_birth_year))
        print('\nThe most recent Birth Year: ', int(most_recent_birth_year))
        print('\nThe most common Birth Year: ', int(most_common_birth_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def show_data(df):
    """Show some rows of data upon request."""

    print('\nShow data...\n')
    start_time = time.time()
    
    print('\nWould you like to view 5 rows of individual trip data? Enter yes or no?')
    is_show = input().lower()
    
    df = df.sort_values('Start Time')
    row_count = df.shape[0]
    start_loc = 0
    while (is_show == 'yes'):
        end_loc = start_loc + 5
        print(df[start_loc:end_loc])
        start_loc = end_loc
        
        if (start_loc >= row_count):
            print('All data were showed, so we will stop displaying data here!')
            break
            
        is_show = input("Do you wish to continue?: ").lower()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print (df.shape)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
