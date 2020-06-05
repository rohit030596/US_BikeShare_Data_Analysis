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

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Hello! Let\'s explore some US bikeshare data! \nPlease enter city name \nNote that data of these cities are available(chicago, new york city, washington) :").lower()
    
   

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Please enter Month: ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please Enter Day: ").lower()

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
    if month != 'all':
       months = ['january','february','march','april','may','june','july','august','september','october','november','december']
       month = months.index(month) + 1
       df = df[df['month']== month]
    if day != 'all':
       df = df[df['day_of_week'] == day.title()]
     
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month_num = df['month'].mode()[0]
    months = ['january','february','march','april','may','june','july','august','september','october','november','december']
    popular_month = months[popular_month_num - 1].title()
    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day = df['day_of_week'].mode()[0]
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("\nMost common month:{} \n Most common day: {} \n Most common start hour : {}".format(popular_month,popular_day,popular_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_startstation = df['Start Station'].mode()[0]
    print("\nMost common start station : {}".format(popular_startstation))
    # TO DO: display most commonly used end station
    popular_endstation = df['End Station'].mode()[0]
    print("\nMost common End station : {}".format(popular_endstation))
    # TO DO: display most frequent combination of start station and end station trip
    popular_station = df.groupby(['Start Station','End Station']).size().sort_values(ascending=False)
    popular_combination = popular_station.index[0]
    print("\nMost common combination of start station and end station : {}".format(popular_combination))
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time = df['Trip Duration'].sum()
    print("Total travel time :",travel_time)
    # TO DO: display mean travel time
    mean_traveltime = df['Trip Duration'].mean()
    print("mean travel time is : ", mean_traveltime)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_users = df['User Type'].value_counts()
    print("COunt of user types : {}".format(counts_users))
    # TO DO: Display counts of gender
    if "Gender" in df:
       counts_gender = df['Gender'].value_counts()
       print("Counts of gender types : {}".format(counts_gender))
    else:
       print("Gender data doesn't exist") 
    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
       most_commonyear = df['Birth Year'].mode()[0] 
       most_recentyear = df['Birth Year'].max()
       earliest_year   = df['Birth Year'].min()
       print("Most common year : {} \nMost Recent year : {} \nEarliest Year : {}".format(most_commonyear,most_recentyear,earliest_year))
    else:
       print("Data Regarding birth year doesn't exist")
        
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
        user_input = input('\nDo you wish to see raw data? Enter yes or no.\n')
        df2 = pd.DataFrame()
        while user_input.lower() == 'yes':
            df2 = df2.append(df.head(5))
            print(df2)
            df = df[5:]
            user_input = input('\n Do you wish to see  more lines of raw data? Enter yes or no.\n')
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
