
athletes = {}
events = {}
countries = {}


def add_athlete(name, country_name):
    if name not in athletes:
        country = get_or_create_country(country_name)
        athletes[name] = {
            'name': name,
            'country': country,
            'performances': []
        }
        print(f"Athlete added: {name}, Country: {country_name}")
    else:
        print(f"Athlete {name} already exists")


def add_event(event_name, date):
    if event_name not in events:
        events[event_name] = {
            'name': event_name,
            'date': date,
            'results': []
        }
        print(f"Event added: {event_name}, Date: {date}")
    else:
        print(f"Event {event_name} already exists")


def record_performance(athlete_name, event_name, result, medal_type=None):
    if athlete_name in athletes and event_name in events:
        athlete = athletes[athlete_name]
        event = events[event_name]

        event['results'].append({'athlete': athlete_name, 'result': result})
        athlete['performances'].append({'event': event_name, 'result': result})

        if medal_type:
            add_medal(athlete['country'], medal_type)

        print(f"Recorded performance: {athlete_name} in {event_name}, Result: {result}, Medal: {medal_type}")
    else:
        print("Athlete or Event does not exist")


def get_or_create_country(country_name):
    if country_name not in countries:
        countries[country_name] = {'name': country_name, 'medals': {'Gold': 0, 'Silver': 0, 'Bronze': 0}}
    return countries[country_name]


def add_medal(country, medal_type):
    if medal_type in country['medals']:
        country['medals'][medal_type] += 1

def view_medal_count_by_country():
    
    print(f"{'Country':<20} {'Gold':<10} {'Silver':<10} {'Bronze':<10} {'Total':<10}")
    print("-" * 60)  
    
    for country_name, country in countries.items():
        gold_medals = country['medals']['Gold']
        silver_medals = country['medals']['Silver']
        bronze_medals = country['medals']['Bronze']
        total_medals = gold_medals + silver_medals + bronze_medals
        
      
        print(f"{country_name:<20} {gold_medals:<10} {silver_medals:<10} {bronze_medals:<10} {total_medals:<10}")



def search_athlete_performance(athlete_name):
    if athlete_name in athletes:
        athlete = athletes[athlete_name]
        print(f"Athlete: {athlete_name}, Country: {athlete['country']['name']}")
        for performance in athlete['performances']:
            print(f"Event: {performance['event']}, Result: {performance['result']}")
    else:
        print("Athlete does not exist")


def view_event_details(event_name):
    if event_name in events:
        event = events[event_name]
        print(f"Event: {event_name}, Date: {event['date']}")
        print(f"{'Athlete':<20} {'Result':<15}")
        print("-" * 35)
        for result in event['results']:
            print(f"{result['athlete']:<20} {result['result']:<15}")
    else:
        print(f"Event {event_name} not found.")


def view_statistics():
    total_events = len(events)
    total_athletes = len(athletes)
    total_medals = sum(sum(country['medals'].values()) for country in countries.values())

    print(f"Total Events: {total_events}")
    print(f"Total Athletes: {total_athletes}")
    print(f"Total Medals Distributed: {total_medals}")


def exit_system():
    print("Saving changes and exiting the system.")
    exit()


def main_menu():
    while True:
        print("\nOlympic Data Explorer")
        print("1. Add Details")
        print("2. View Details")
        print("3. View Medal Count by Country")
        print("4. Search Athlete Performance")
        print("5. View Event Details")
        print("6. View Statistics")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            athlete_name = input("Enter athlete's name: ")
            country_name = input("Enter country: ")
            add_athlete(athlete_name, country_name)

            event_name = input("Enter event name: ")
            date = input("Enter event date (YYYY-MM-DD): ")
            add_event(event_name, date)

            result = input("Enter performance result: ")
            medal_type = input("Enter medal type (Gold/Silver/Bronze or leave blank): ")
            record_performance(athlete_name, event_name, result, medal_type)

        elif choice == '2':
            event_name = input("Enter event name to view details: ")
            view_event_details(event_name)
        elif choice == '3':
            view_medal_count_by_country()
        elif choice == '4':
            athlete_name = input("Enter athlete's name to search: ")
            search_athlete_performance(athlete_name)
        elif choice == '5':
            event_name = input("Enter event name to view details: ")
            view_event_details(event_name)
        elif choice == '6':
            view_statistics()
        elif choice == '7':
            exit_system()
        else:
            print("Invalid choice, please try again.")


main_menu()
