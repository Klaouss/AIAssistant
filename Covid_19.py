def Covid():
    import covid
    Covid = covid.Covid(source='worldometers')
    population_greece = int(Covid.get_status_by_country_name('Greece')['population'])
    list = Covid.list_countries()
    actve = Covid.get_total_active_cases()
    deaths = Covid.get_total_deaths()
    confirmed = Covid.get_total_confirmed_cases()
    recovered = Covid.get_total_recovered()

    Greece = Covid.get_status_by_country_name('Greece')


    print('There have been ',Greece['confirmed'], ' confirmed cases in Greece as if right now')
    print('From these, ',Greece['active'],' are active cases')
    percent_of_greece_infected =(int(Greece['confirmed']) / population_greece) * 100
    print(percent_of_greece_infected, '%  percent of Greece has been infected')


    percent_of_infected_dead = (int(Greece['deaths'])) / (int(Greece['confirmed']))*100
    print('The death rate of the infected in Greece is: ', percent_of_infected_dead, '%')




    



