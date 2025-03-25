from read_data import read_data

# Load the data into a pandas DataFrame
df = read_data()

#Filter the DataFrame to get only approved applications
approved = df.query("Beslut == 'Beviljad'")
# Count the number of approved applications
number_approved = len(approved)
# Count total number of approved applications
total_applications = len(approved)

# Calculate the approval percentage and format it with on decimal place
approved_percentage = f"{number_approved / total_applications*100:.1f}%"

# Print the statics
print(number_approved)
print(total_applications)
print(approved_percentage)

def provider_kpis(provider):
    # Filter for a specific provider
    applied = df.query(f"`Utbildningsanordare administrativ enhet` == '{provider}'")
    # Count total applications from this provider
    applications = len(applied)
    # Count approved applications from this provider
    approved = len(applied.query("Beslut == 'Beviljad'"))
    # Returns both counts as a tuple
    return applications, approved

# Call the functionen for a specific provider and print the result
print(provider_kpis("TGA Utbildning AB"))

