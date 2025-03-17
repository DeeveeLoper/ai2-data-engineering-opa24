# Calculate key metrics for higher vocational education applications

from read_data import read_data

# Load the dataset
df = read_data()

# Filter data to get only approved applications
approved = df.query("Beslut == 'Beviljad'")
# Calculate key metrics
number_approved = len(approved)
total_application = len(df)
approved_percentage = f"{number_approved / total_application*100:.1f}%"

# Print the calculated metrics for verification
print(number_approved)
print(total_application)
print(approved_percentage)

# Define function to calculate statistics for a specific provider
def provider_kpis(provider):
    # Filter data for the specified provider
    applied = df.query(f"`Utbildningsanordnare administrativ enhet` == '{provider}'")
    applications = len(applied)
    approved = len(applied.query("Beslut == 'Beviljad'"))
    
    return applications, approved

# Test the function with a sample provider
print(provider_kpis("TGA Utbildning AB"))