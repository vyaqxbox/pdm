#customer file

class customer:

    def __init__(self, first_name, last_name, purchases, alias, notes):
        self.first_name = first_name
        self.last_name = last_name
        self.purchases = purchases
        self.alis = alias
        self.notes = notes

function = customer(
"", #Customer First name
"", #Customer Last Name
"", #Phone Number
"", #Customer Alias
"", #Customer Notes
)

Derrick_Dero = customer(
"Derrick", #Customer First name
"Dero", #Customer Last Name
"", # Customer Phone Number
"derrick dero", #Customer Alias
"Test drove a Toyota Chaser. Very wreckless driver. Use caution when test driving", #Customer Notes
)

Undertaker_Undertaker = customer(
"Undertaker", #Customer First name
"Undertaker", #Customer Last Name
"Phone: 607-6719", #Customer Phone Number
"undertaker under taker", #Customer Alias
"Rides a KTM RC, came in looking at bikes. Member of MC", #Customer Notes
)

Hong_Dong = customer(
"Hong", #Customer First name
"Dong", #Customer Last Name
"", # Customer Phone Purchase(s)
"hong dong", #Customer Alias
"Looking at Lifted F-250", #Customer Notes
)

Joe_Momma = customer(
"Joe", #Customer First name
"Momma", #Customer Last Name
"", #Customer Phone Purchase(s)
"joe momma mom", #Customer Alias
"Newer member of city. Looking at 370z and a charger", #Customer Notes
)

Tiger_Woods = customer(
"Tiger", #Customer First name
"Woods", #Customer Last Name
"", #Customer Phone Purchase(s)
"tiger woods", #Customer Alias
"Came in with Julio. Will try to hit top speed on vehicle during test drive", #Customer Notes
)

Richard_Woodlock = customer(
"Richard", #Customer First name
"Woodlock", #Customer Last Name
"", #Phone Purchase(s)
"richard woodlock", #Customer Alias
"Pretty chill. High spender.", #Customer Notes
)

Tyrone_Tillman = customer(
"Tyrone", #Customer First name
"Tillman", #Customer Last Name
"", #Phone Purchase(s)
"tyrone tillman", #Customer Alias
"High spender. Good test driver, wanted Rolls Royce.", #Customer Notes
)

Kitt_Rxety = customer(
"Kitt", #Customer First name
"Rxety", #Customer Last Name
"Honda Integra", #Phone Purchase(s)
"kitt rxety", #Customer Alias
"Runs with julio.", #Customer Notes
)

Douglas_Dabz = customer(
"Douglas", #Customer First name
"Dabz", #Customer Last Name
"2000 BMW M3", #Phone Number
"douglas dabs", #Customer Alias
"", #Customer Notes
)

Luwig_Chick = customer(
"Luwig", #Customer First name
"Chick", #Customer Last Name
"", #Customer Purchases
"luwig chick", #Customer Alias
"Drove 2003 BMW M3", #Customer Notes
)

customers = [Derrick_Dero, Undertaker_Undertaker, Hong_Dong, Joe_Momma, Tiger_Woods,
Richard_Woodlock, Tyrone_Tillman, Kitt_Rxety, Douglas_Dabz, Luwig_Chick]
