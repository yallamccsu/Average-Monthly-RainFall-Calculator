
# List of all the months – we'll use this to make the prompts more user-friendly
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Ask how many years of rainfall data the user has
years = int(input("Enter the number of years: "))

# We’ll keep track of how much rain in total and how many months we’re talking about
total_rainfall = 0.0
total_months = years * 12  # 12 months per year

# Loop through each year one by one
for year in range(1, years + 1):
    print(f"\nFor year {year}:")

    # For each year, go through all 12 months
    for month in months:
        while True:
            try:
                # Ask the user how much it rained in a specific month
                rainfall = float(input(f"Enter the rainfall amount for {month}: "))

                # Don't let them enter a negative number – that doesn’t make sense
                if rainfall < 0:
                    print("Rainfall can't be negative – try again.")
                    continue

                # Add that month’s rainfall to the total
                total_rainfall += rainfall
                break
            except ValueError:
                # Catch when someone types something that's not a number
                print("That doesn’t look like a number. Try again!")

# Now that we have all the data, calculate the average rainfall per month
average_rainfall = total_rainfall / total_months

# Time to show the final results!
print(f"\nFor {total_months} months:")
print(f"Total rainfall: {total_rainfall:.2f} inches")
print(f"Average monthly rainfall: {average_rainfall:.2f} inches")
