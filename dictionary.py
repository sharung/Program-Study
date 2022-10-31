# ## Dictionary
# buku = {
#     "judul":"Lord of the rings",
#     "tema":"Merebutkan kembali kerajaan",
#     "penerbit":"Erlangga"
# }
# # print(buku["judul"])
# print(buku["judul"])
# buku["halaman"] = 12
# for i in buku.keys():
#     print(i)

"""
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for score in student_scores:
    # student_grades[score]
    scores = student_scores[score]
    if scores >= 91 and scores <= 100:
        student_scores[score] = "Outstanding"
    elif scores >= 81 and scores <= 90:
        student_scores[score] = "Exceeds Expectations"
    elif scores >= 71 and scores <= 80:
        student_scores[score] = "Acceptable"
    else:
        student_scores[score] = "Fail"

    student_grades = student_scores
# 🚨 Don't change the code below 👇
print(student_grades)
"""

# #Nesting 
# capitals = {
#   "France": "Paris",
#   "Germany": "Berlin",
# }

# #Nesting a List in a Dictionary

# travel_log = {
#   "France": ["Paris", "Lille", "Dijon"],
#   "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }

# #Nesting Dictionary in a Dictionary

# travel_log = {
#   "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#   "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
# }

# #Nesting Dictionaries in Lists

# travel_log = [
# {
#   "country": "France", 
#   "cities_visited": ["Paris", "Lille", "Dijon"], 
#   "total_visits": 12,
# },
# {
#   "country": "Germany",
#   "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#   "total_visits": 5,
# },
# ]

"""
# Dictionery list

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country,visitor,cities):
  travel_log.append({
    "country": country,
    "visits": visitor,
    "cities": cities  
  })

def input_beda(country, visit, city):
    new_detail = {}
    new_detail["country"] = country
    new_detail["visits"] = visit
    new_detail["cities"] = city
    travel_log.append(new_detail)


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
"""
player_bit = []

game = True
while game:
    bid_player = {}
    bid_player["player"] = "joko"
    bid_player["bid"] = "100"
    player_bit.append(bid_player)

add = input("")
print(player_bit)

    # for i in player_bit:

    #     print(i["bid"])








