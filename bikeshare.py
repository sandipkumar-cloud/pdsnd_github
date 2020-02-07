import time
import pandas as pd
import numpy as np
# The data here is a stripped down version of real data from a company
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
    city_index = 0
    city_list = ['chicago', 'new york city', 'washington']
    while city_index == 0:
            city = input("Enter a valid city name to analyze: ")
            city = city.lower()
            print(" you have selected the city, {}!".format(city))
            if city in city_list:
                city_index = 1            
               
    # TO DO: get user input for month (all, january, february, ... , june)
    month_index = 0
    month_list = ['january', 'february', 'march', 'april', 'may', 'june']
    while month_index == 0:
            month = input("Enter a valid month to analyze: ")
            month = month.lower()
            print(" you have selected month: {}".format(month))
            if month in month_list:
                month_index = 1
            elif month == 'all':
                month_index = 2

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_index = 0
    day_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while day_index == 0:
            day = input("Enter a valid day to analyze: ")
            day = day.lower()
            print(" you have selected day: {}".format(day))
            if day in day_list:
                day_index = 1
            elif day == 'all':
                day_index = 2

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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    df.head()

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('Most Popular Month:', most_common_month)

    # TO DO: display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print('Most Popular Day of week:', most_common_day_of_week)

    # TO DO: display the most common start hour
    hour = df['Start Time'].dt.hour
    most_common_hour = hour.mode()[0]
    print('Most Popular Start Hour:', most_common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station:', most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('Most Common End Station:', most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    start_end=df['Start Station']+' to '+df['End Station']
    most_common_start_end_station = start_end.mode()[0]
    print('Most Common Trip from Start to End:', most_common_start_end_station)    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    
    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time) 
    
    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print('Average Travel Time:', average_travel_time) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types:', user_types) 


    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_types = df['Gender'].value_counts()
        print('Counts of Gender:', gender_types) 
    else:
        print('Gender data not available for this city')

            

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        print('Earliest birth year:', earliest_birth_year) 
        
        recent_birth_year = df['Birth Year'].max()
        print('Most recent birth year:', recent_birth_year) 
        
        most_common_birth_year = df['Birth Year'].mode()[0]
        print('Most common birth year:', most_common_birth_year)         
    else:
        print('Birth Year data not available for this city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        preview_index = 0
        while preview_index == 0:
            preview = input('\nWould you like to see the first 5 lines of raw data? Enter yes or no.\n')
            if preview.lower() == 'yes':
                print("The first 5 lines of raw data are:")
                print(df.head())
            else:
                preview_index = 1


        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
