#########################################################
# Function :Output required dictionaries                #
# Argument :$csvfile                                    #
# Output   :dict1;dict2                                 #
# Date     :25-May-2023                                 #
# Author   :Wiz Zhang                                   #
# StudentID:23210735                                    #
# Project  :CITS-1401 Python Project2                   #
#########################################################
def main(csvfile):
    try:
        # Read csvfile
        with open(csvfile, 'r') as file:
            # Read header line
            headers = file.readline().strip().split(',')
            #Exception handling. Raise an exception if the file has no headers
            if not headers:
                raise EOFError("The header is empty.")
            # Create an empty list to store each row's data
            data = []
            # Iterate over each line in the csvfile
            for line in file:
                values = line.strip().split(',')
                row = {}
                # Add header and value into dictionary
                for header, value in zip(headers, values):
                    # Ensure Population;Net Change; Land Area are integers
                    if header.lower() in ['population', 'net change', 'land area']:
                        try:
                            value = int(value)
                        #Exception Handling. Skip the value if I cannot int it
                        except ValueError:
                            value = None
                    # Convert string values to lowercase match the requirement
                    row[header.lower()] = value.lower() if isinstance(value, str) else value 
                # keep adding data into dictionary
                if row['population'] is not None and row['land area'] is not None:
                    data.append(row)
    except FileNotFoundError:
        #Exception Handling. Print error text if csvfile doesn't exist
        print(f"Error: the file {csvfile} does not exist.")
        return {}, {}

    def task1(data):
        region_population = {}
        region_land_area = {}
        region_average_population = {}
        #Create dictionaries for regions' population;land area and average population
        for row in data:
            region = row['regions']
            population = row['population']
            land_area = row['land area']
            if region not in region_land_area:
                region_land_area[region] = []
            region_land_area[region].append(land_area)
            if region not in region_population:
                region_population[region] = []
            region_population[region].append(population)
            region_average_population[region] = sum(region_population[region]) / len(region_population[region])

        region_standard_error = {}
        region_cosine_similarity = {}
        #Calculate Standard Error and Cosine Similarity
        for region, populations in region_population.items():
            #Standard Error Calculation
            average = sum(populations) / len(populations)
            variance = sum((p - average) ** 2 for p in populations) / (len(populations) - 1)
            standard_deviation = variance ** 0.5
            standard_error = standard_deviation / (len(populations) ** 0.5)
            region_standard_error[region] = round(standard_error, 4)
            #Cosine Similarity Calculation
            population = [int(p) for p in region_population[region]]
            land_area = [int(l) for l in region_land_area[region]]
            dot_product = sum(p*q for p,q in zip(population, land_area))
            magnitude_population = sum([p**2 for p in population]) ** 0.5
            magnitude_land_area = sum([l**2 for l in land_area]) ** 0.5
            region_cosine_similarity[region] = round(dot_product / (magnitude_population * magnitude_land_area), 4)
        #Storage these two data into dict1 as required and return to main function
        dict1 = {}
        for region in region_population.keys():
            dict1[region] = [region_standard_error[region], region_cosine_similarity[region]]
        return dict1 #TASK1 DONE!

    def task2(data):
        region_population = {}
        region_net_change = {}
        region_land_area = {}
        #Get the required data for task2
        for row in data:
            region = row['regions']
            country = row['country']
            population = row['population']
            net_change = row['net change']
            land_area = row['land area']
            if region not in region_population:
                region_population[region] = {}
                region_net_change[region] = {}
                region_land_area[region] = {}
                
            #Put countries' population; net_change data into the region dictionary first, I don't need to calculate them
            region_population[region][country] = population
            region_net_change[region][country] = net_change
            region_land_area[region][country] = land_area
        
        region_percentage = {}
        region_density = {}
        region_rank = {}
        #Calculate Population Percentage, Density, Rank
        for region in region_population.keys():
            region_percentage[region] = {}
            region_density[region] = {}
            region_rank[region] = {}
            total_population = sum(region_population[region].values())
            for country in region_population[region].keys():
                density = round(region_population[region][country] / region_land_area[region][country], 4)
                percentage = round(region_population[region][country] / total_population * 100, 4)
                region_density[region][country] = density
                region_percentage[region][country] = percentage
            # 1st sort by alphabetical order (ascending)
            sorted_countries = sorted(region_percentage[region].items(), key=lambda item: item[0])
            # 2nd sort by density (descending)
            sorted_countries = sorted(sorted_countries, key=lambda item: region_density[region][item[0]], reverse=True)
            # 3rd sort by population (descending)
            sorted_countries = sorted(sorted_countries, key=lambda item: item[1], reverse=True)  
            for rank, country in enumerate(sorted_countries, 1):
                region_rank[region][country[0]] = rank
        #Store the data in dict2 as required and return it to main function
        dict2 = {}
        for region in region_population.keys():
            dict2[region] = {}
            for country in region_population[region].keys():
                dict2[region][country] = [region_population[region][country], region_net_change[region][country], region_percentage[region][country], region_density[region][country], region_rank[region][country]]
        return dict2 #TASK2 DONE!

    dict1 = task1(data)
    dict2 = task2(data)
    return dict1, dict2

'''
COMMENT:
I make the dictionaries for population and land area in main function so I don't need to do it again later
I also add some error handlings in main function that I thought it may happen.
'''

