# Smart Parking Fee Management System in Python

## 1. Problem Statement
 Smart Parking Fee Management: Calculate charges from entry and exit times, vehicle categories, overnight parking, daily limits, and penalty conditions while validating time inputs. 
 
## 2. Algorithm

1. Start the program.
2. Define the hourly parking rates for bikes, cars, and trucks.
3. Read the vehicle category, entry time, and exit time.
4. Validate the vehicle category and time format.
5. Convert the entry and exit times into minutes.
6. If the exit time is earlier than the entry time, treat it as an overnight parking session.
7. Calculate the total parking duration in minutes.
8. Convert the duration into hours, rounding up any partial hour.
9. Calculate the parking fee using the vehicle's hourly rate.
10. If parking extends overnight, add the overnight penalty.
11. If parking exceeds 24 hours, apply the daily maximum limit for each 24-hour period.
12. Display the parking duration, base fee, penalties, and total fee.
13. Stop the program.

## 3. Flowchart 
```mermide
flowchart TD
    A([Start]) --> B[/Input vehicle and entry/exit times/]
    B --> C{Valid inputs?}
    C -- No --> D[Display Error]
    C -- Yes --> E[Calculate Parking Duration]
    E --> F[Calculate Fee and Penalty]
    F --> G[Apply Daily Fee Limit]
    G --> H[/Display Total Fee/]
    D --> I([Stop])
    H --> I
```

## 5. Sample Input

SMART PARKING FEE MANAGEMENT
Vehicle categories: Bike, Car, Truck
Enter vehicle category: Car
Enter entry time (HH:MM): 21:00
Enter exit time (HH:MM): 02:30


## 6. Sample Output

----- PARKING BILL -----
Vehicle: Car
Parking duration: 5 hours 30 minutes
Chargeable hours: 6
Hourly rate: Rs. 50
Base parking fee: Rs. 300
Overnight penalty: Rs. 50
Late-exit penalty: Rs. 0
------------------------
Total fee: Rs. 350

