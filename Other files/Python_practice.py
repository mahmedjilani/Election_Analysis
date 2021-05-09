# counties = ["Arapahoe","Denver","Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])

# counties = ["Arapahoe","Denver","Jefferson"]
# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not the list of counties.")

# if "Arapahoe" in counties or "El Paso" in counties:
#     print("Arapahoe and El Paso are in the list of counties.")
# else:
#     print("Arapahoe or El Paso is not in the list of counties.")

# if "Arapahoe" in counties and "El Paso" not in counties:
#    print("Only Arapahoe is in the list of counties.")
# else:
#    print("Arapahoe is in the list of counties and El Paso is not in the list of counties")

# for county in counties:
#     print(county)

# numbers = [0, 1, 2, 3, 4]
# for num in numbers:
#     print(num)    

# for num in range(5):
#     print(num)


# for j in range(len(counties)):
#     print(counties[j])

# counties_tuple = ("Arapahoe","Denver","Jefferson")

# for i in range(len(counties_tuple)):
#     print (counties_tuple[i])

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},{"county":"Denver", "registered_voters": 463353},{"county":"Jefferson", "registered_voters": 432438}]
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# for i in range(len(voting_data)):
#     print(voting_data[i])


# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)

for county_dict in voting_data:
    print(county_dict['county'])        

# for county in counties_dict.keys():
#     print(county)

# for voters in counties_dict.values():
#     print(voters)

# for county, voters in counties_dict.items():
#     print (county, 'county has', voters, 'registered voters')


