country_code = {"india": "0091",
                "nepal": "00977",
                "china": "0086",}

print("Country code for india -")
print(country_code.get("india", "not found"))

print("country code for nepal -")
print(country_code.get("nepal", "not found"))