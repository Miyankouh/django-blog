from . import jalali
from django.utils import timezone


def persian_numbers_converter(mystr):
   numbers = {
      "0":"۰",
      "1":"۱",
      "2":"۲",
      "3":"۳",
      "4":"۴",
      "5":"۵",
      "6":"۶",
      "7":"۷",
      "8":"۸",
      "9":"۹",
      
   }

   for e, p in numbers.items():
      mystr = mystr.replace(e,p)
   return mystr


def jalali_converter(time):
   # persian_months
   jmonths = ['فروردین','اردیبهشت','خرداد','تیر','مرداد','شهریور','مهر','ابان','اذر','دی','بهمن','اسفند']


   time = timezone.localtime(time)

   # persian_time
   time_to_str = "{},{},{}".format(time.year, time.month, time.day)
   time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()
   
   # chang time_to_tuple to time_to_list For use in persian_months
   time_to_list = list(time_to_tuple)

   # persian_months
   for index, month in enumerate(jmonths):
      if time_to_list[1] == index + 1:
         time_to_list[1] = month
         break
   
   output = "{} {} {}, ساعت {}:{}".format(
      time_to_list[2],
      time_to_list[1],
      time_to_list[0],
      time.hour,
      time.minute,
   )
   return  persian_numbers_converter(output)
    
    		