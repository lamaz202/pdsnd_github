import time
import pandas as pd
import numpy as np

CITIES = {'chicago': 'chicago.csv',
             'new york': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hi good morning Let\'s explore some US bikeshare data')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input('Choose the one you want from chicago,new york or washington :').lower()
    while city not in CITIES:
        city = input('im sorry there is no information,Please Try Again : ').lower()


    # TO DO: get user input for month (all, january, february, ... , june)

    month = input('Enter the month you want From the first six months :').lower()

    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september',
              'october', 'november', 'december']
    while month not in months:
        month = input('im sorry there is no information,Please Try Again : ').lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day = input('Enter the day you want:').lower()
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']
    while day not in days:
        day = input('im sorry there is no information,Please Try Again : ').lower()


    print('-' * 40)

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
    df = pd.read_csv(CITIES[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['month'] = df['Start Time'].dt.month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
                  'november', 'december',]
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):

    """Displays statistics on the most frequent times of travel."""
    print('Calculating The Most Frequent Times of Travel')
    start_time = time.time()
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    co_month = df['month'].mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september',
              'october', 'november', 'december']

    print('The most common month:', months[co_month - 1])

    # TO DO: display the most common day of week

    df['day_of_week'] = df['Start Time'].dt.dayofweek
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']
    co_day = df['day_of_week'].mode()[0]
    print('The most common day:', days[co_day])


    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    co_hour = df['hour'].mode()[0]
    print('The most common Start Hour:', co_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def station_stats(df):

    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    str = df['Start Station'].mode()[0]
    print(f'most commonly used start station is: {str}')

    # TO DO: display most commonly used end station

    en = df['End Station'].mode()[0]
    print(f'most commonly used end station is: {en}')

    # TO DO: display most frequent combination of start station and end station trip

    comp = df['Start Station'] + ' -------> ' + df['End Station']
    comp = comp.mode()[0]
    print(f'the most Famous start station and end station is: {comp}')

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-' * 40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total = df['Trip Duration'].sum()
    print(f'Total trip duration is : {total}sec')

    # TO DO: display mean travel time

    mean = df['Trip Duration'].mean()
    print(f'the mean travel time is: {mean}sec')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')

    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        the_gender = df['Gender'].value_counts()
        print(the_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('here the Earliest year of Birth:', df['Birth Year'].min())
        print('here the Most Recent year of Birth:', df['Birth Year'].max())
        print('here the Most Common year of Birth:', df['Birth Year'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-' * 40)



def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        x = 0
        while True:
            raw = input("do you want to see the raw data ? , pleses enter 'y' if yes and enter 'n' if no .").lower()
            if raw == 'y':
                print(df.rund[x: x + 5])
                x += 5
            elif raw == 'n':
                break
            else:
                print("there is no data , You entered the wrong entry try again")


        restart = input('Would you like to restart? Enter yes or no.').lower()
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

