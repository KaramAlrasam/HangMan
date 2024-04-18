
y=int(input("Input the year: ").strip())
# first we need to make sure the leap_year or not
if y%400==0:
  leap_year=True
elif y%100==0:
  leap_year=False
elif y%4==0:
  leap_year=True
else:
  leap_year=False

# create input for month
m=int(input("Input the month[1-12]: ").strip())
#These conditions to make sure from which month has 31,30,28,29 day
if m in(1,3,5,7,8,10,12):
  length_month=31
elif m==2:
  if leap_year:
    length_month=29
  else:
    length_month=28
else:
  length_month=30
#craete input for day.
d=int(input("Input the day[1-31]: ").strip())
if d<length_month:
  d+=1
else:
  d=1
  if m<12:
    m+=1
  else:
    m=1
    y+=1
print("The next date is [yyyy-mm-dd]: %i-%i-%i"%(y,m,d))
  