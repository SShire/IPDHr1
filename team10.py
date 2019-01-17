####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Kyle' # Only 10 chars displayed.
strategy_name = 'Random Strategy'
strategy_description = 'Choose random beweteen collude and betray'
    
import random
a = ["Collude", "Betray", "Collude","Collude", "Betray", "Collude"]
print(random.choice(a))
