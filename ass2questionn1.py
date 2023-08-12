question 1:
print("LIST AND TUPLES\n")


# part a:
temp=[25,30,27,22,28,33,29]
days=("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
temp_days=list(zip(temp,days))
print(temp_days)


# part b:
max_temp=max(temp)
print(f"\nthe maximum temperature is {max_temp}")
for i in temp_days:
  if i[0]==max_temp:
    print(f"the  day of max temp is {i[1]}")


# part c:
avg_temp=sum(temp)/len(temp)
print(f"the average temperature is {avg_temp}")
    