# cleaning string data

name_1 = "PRIYA SHARMA" 
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"

salary_1 = "$82,500"
salary_2 = "$74,000"

#lowercase names
print(name_1.lower())
print(name_2.lower())
print(name_3.lower())

#Title case names
print(name_1.title())
print(name_2.title())
print(name_3.title())

# remove the dollar sign
clean_salary_1 = salary_1.replace("$","")
clean_salary_2 = salary_2.replace("$", "")