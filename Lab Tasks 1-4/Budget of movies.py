movies=[
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]
added_movies=int(input("Enter the numbers of added movies"))
for i in range(added_movies):
    name=input("Enter the name of added movies: ")
    budget=int(input("Enter the budget of added movies: "))
    movies.append((name,budget))
    
Total_Budget=sum(budget for _,budget in movies)
Average_Budget=Total_Budget/len(movies)
print(f"total budget is: {Total_Budget}")
print(f"average budget is: {Average_Budget}")
High_Budget_Movies=[]
for name,budget in movies:
    if budget > Average_Budget:
        difference=budget - Average_Budget
        High_Budget_Movies.append((name, difference))
        print(f"{name} has a budget that is {difference} above the average")
        
print("High budget movies:", High_Budget_Movies)

    