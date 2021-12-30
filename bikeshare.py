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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        cities = ['chicago','new york city','washington']
        city = input ("Would you like to see the data for chicago, new york city or washington?\n").lower()
        if city in cities:
            break
        else:
            print('This city is not valid, please choose between [chicago,new york city,washington]\n')
            
    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        months = ['january','february','march','april','may','june','all']
        month = input("Which Month (all, january, ... june)?\n").lower()
        if month in months:
            break
        else:
            print('This month is not valid, please choose between [january, february, march, april, may, june, all]\n')
     
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    while True:
        days = ['saturday','sunday','monday','tuesday','wednesday','thursday','friday','all']
        day = input("Which day? (all, monday, tuesday, ... sunday)\n").lower()
        if day in days:
            break
        else:
            print('This day is not valid, please choose between [saturday, sunday, monday, tuesday, wednesday, thursday, friday, all]\n')


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

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('Most Popular Month:', most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('Most Day Of Week:', most_common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most  commonly start station:', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most coomonly end station:', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination']=df['Start Station']+" "+"to"+" "+ df['End Station']
    most_combination_station = df['combination'].mode()[0]
    print("The most frequent combination of start and end stations is: \n", most_combination_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:\n', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:\n', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_of_user_types= df['User Type'].value_counts()
    print("User types are:\n",count_of_user_types)

    
    # TO DO: Display counts of gender
    if city != 'washington':
        counts_of_gender= df['Gender'].value_counts()
        print("The counts of both genders are:\n",counts_of_gender)


    # TO DO: Display earliest, most recent, and most common year of birth
        earliest= int(df['Birth Year'].min())
        print("The oldest user is born of the year: \n",earliest)
    
        most_recent= int(df['Birth Year'].max())
        print("The youngest user is born of the year:\n",most_recent)
    
        most_common= int(df['Birth Year'].mode()[0])
        print("Most users are born of the year:\n",most_common)
    else:
        print("Sorry washington doesn't have does not include the column gender")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_raw_data(df) :
    display_raw_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?\n").lower()
    start = 0
    while view_data == 'yes':
        print(df.iloc[start:start + 5])
        start+= 5
        view_display = input("Do you wish to continue?: Yes OR No \n").lower()
        if view_display== 'no':
            break
        
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_raw_data = input("Would you like to view 5 rows of individual trip data? Please enter yes or no?\n").lower()
        start = 0
        while display_raw_data == 'yes':
            print(df.iloc[start:start + 5])
            start+= 5
            display_raw_data = input("Do you wish to continue?: Yes OR No \n").lower()
            if display_raw_data== 'no':
                break
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
