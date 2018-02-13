ramit = {
  "name": "Ramit",
  "email": "ramit@gmail.com",
  "interests": ["movies", "tennis"],
  "friends": [
    {
      "name": "Jasmine",
      "email": "jasmine@yahoo.com",
      "interests": ["photography", "tennis"]
    },
    {
      "name": "Jan",
      "email": "jan@hotmail.com",
      "interests": ["movies", "tv"]
    }
  ]
}

print(ramit["email"])   # prints ramit's email
print(ramit["interests"][0])    # prints first of Ramit's interests
print(ramit["friends"][0]["email"]) # prints Jasmine's email address
print(ramit["friends"][1]["interests"][1])