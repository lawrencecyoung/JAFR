# Testing Meeting Description
Missing dot point Scheduled: 18:00 27/08/23
- Scheduled: in Meeting Description Scheduled: 18:00 27/08/23
        - Has indentation before  Scheduled: 18:00 27/08/23
-       Scheduled: 18:00 27/08/23  
-  Scheduled:Scheduled:Scheduled:Scheduled: is invalid Scheduled: 18:00 27/08/23      
- Dash-in-Description Scheduled: 18:00 27/08/23
-Missing space characterScheduled: 18:00 27/08/23
- Duplicates should show up twice Scheduled: 18:00 27/08/23
- Duplicates should show up twice Scheduled: 18:00 27/08/23
- Special characters !@#$%^&*()_+{}|~:"<>? Scheduled: 18:00 27/08/23

# Testing Date
- Invalid year format DD/MM/YYYY Scheduled: 18:00 27/08/2023
- Swapped format MM/DD/YY Scheduled: 18:00 08/27/23
- Invalid separator DD-MM-YY Scheduled: 18:00 27-08-23
- DD/M/YY Scheduled: 18:00 25/8/23
- Negative Date Numbers Scheduled: 18:00 -27/-08/23
- Missing scheduled string 25/08/23 
- Invalid month format Scheduled: 18:00 27/Aug/23
- Impossible day date format Scheduled: 18:00 32/08/23
- Impossible month date format Scheduled: 18:00  27/13/23
- Missing date Scheduled: 18:00 

# Testing Time
- Invalid hour value Scheduled: 24:00 27/08/23
- Edge Valid hour value Scheduled: 23:59 27/08/23
- Edge Valid hour value Scheduled: 00:00 27/08/23
- Invalid Minute value Scheduled: 13:60 27/08/23
- Edge Valid Minute value Scheduled: 13:00 27/08/23
- Edge Valid Minute value Scheduled: 13:59 27/08/23
- Invalid format 12-hour time Scheduled: 1:00pm 27/08/23
- Invalid format 12-hour time Scheduled: 1:00am 27/08/23
- Invalid format HH:MM:SS Scheduled: 1:00:23 27/08/23
- Invalid format MM:HH Scheduled: 15:60 27/08/23
- Invalid separator HH-MM Scheduled: 15-59 27/08/23
- Missing time Scheduled: 27/08/23

# Checking Date Boundaries
- Meeting due yesterday Scheduled: 18:00 24/08/23
- Meeting due today Scheduled: 18:00 27/08/23
- Meeting due tomorrow Scheduled: 18:00 28/08/23
- Meeting due in two days Scheduled: 18:00 29/08/23
- Meeting due in three days Scheduled: 18:00 30/08/23
- Meeting due in four days Scheduled: 18:00 31/08/23
- Meeting due in five days Scheduled: 18:00 01/09/23
- Meeting due in six days Scheduled: 18:00 02/09/23
- Meeting due in the next week Scheduled: 18:00 03/09/23
- Meeting due in the one week and one day Scheduled: 18:00 04/09/23

# Incorrect Format
- Meeting description Scheduled: 27/08/23 18:00
- Scheduled: 18:00 27/08/23 Meeting description 
- 27/08/23 Meeting description Scheduled: 18:00 

