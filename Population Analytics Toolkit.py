"""
This is the project of CITS1401 Python written by Wiz Zhang(SID:23210735).
This program read CSV file, after reading the file, the program would output the following information:
   1.The country name which has minimum and maximum population in a specific region which has positive net change in population.
   2.Calculate the average and standard deviation of population for a specific region.
   3.Calculate the density of population for each country in a specific region.
   4.Calculate the correlation between population and land area for all the countries in a specific region.
I try to use the same loop to calculate value as much as possible, but not separate them into 4 functions so I can reduce loop times.
"""
def main(csvfile,region):
    #Change the function to the project required function
    MaxMin,stdvAverage,density,corr = process_data(csvfile, region)
    return MaxMin,stdvAverage,density,corr
def process_data(csvfile, region):
    #Open and read the csv file
    with open(csvfile, 'r', encoding='utf-8') as file:
        data = file.readlines()
    #Initialize variables for Question1
    max_population,min_population,max_population_country,min_population_country = 0,float('inf'),"",""
    #Initialize variables for Question2
    sum_population,countries_nums, average_population,variance= 0,0,0,0
    #Initialize variables for Question3
    density_for_all_countries,country_density =[],[]
    #Initialize variables for Question4
    sum_population,sum_land_area,countries_nums,average_population,average_land_area,covariance_numerator,variance_population,variance_land_area,correlation = 0,0,0,0,0,0,0,0,0
    #Iterate through the data and process each row
    for line in data[1:]:
        row = line.strip().split(",")
        if row[5] == region:
            #Check if the population growth is greater than zero
            if int(row[3]) > 0:
                population = int(row[1])
                #Find the country with max and min population
                if population > max_population:
                    max_population = population
                    max_population_country = row[0]
                if population < min_population:
                    min_population = population
                    min_population_country = row[0]
            #Calculate the sum of population and land area
            sum_population += int(row[1])
            sum_land_area += int(row[4])
            countries_nums +=1
            #Calculate the population density for each country
            country_density=round(float( float(row[1])/float(row[4]) ),4)
            density_for_all_countries.append([row[0],country_density])
     # Sort the density_for_all_countries list
    n = len(density_for_all_countries)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            #If the current element has a greater density value, update max_idx
            if density_for_all_countries[j][1] > density_for_all_countries[max_idx][1]:
                max_idx = j
        #Swap the elements at indices i and max_idx
        density_for_all_countries[i], density_for_all_countries[max_idx] = density_for_all_countries[max_idx], density_for_all_countries[i]
    #Calculate the average population and land area       
    average_population = round(float(sum_population / countries_nums), 4)
    average_land_area = round(float(sum_land_area / countries_nums), 4)
    #Reset the variables' value
    sum_population=0
    countries_nums=0
    #Iterate through the data again for variance and correlation calculation
    for line in data[1:]:
        row = line.strip().split(",")
        if row[5] == region:
            population=int(row[1])
            sum_population += population
            countries_nums +=1
            #Calculate variance and covariance components
            variance += (population-average_population)**2
            covariance_numerator += (int(row[1]) - average_population) * (int(row[4]) - average_land_area)
            variance_population += (int(row[1]) - average_population)**2
            variance_land_area += (int(row[4]) - average_land_area)**2
    #Calculate correlation
    correlation = round(float(covariance_numerator / (variance_population * variance_land_area)**0.5), 4)
    variance = float(variance / (countries_nums -1 ))
    stdv_population = round (variance ** 0.5, 4)
    stdvAverage = [average_population, stdv_population]
    MaxMin=[max_population_country, min_population_country]
    #return the results
    return MaxMin,stdvAverage,density_for_all_countries,correlation
 



