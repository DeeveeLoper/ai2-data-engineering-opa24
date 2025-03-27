from read_data import read_data

df = read_data()

approved = df.query("Beslut == 'Beviljad'")
#approvet = df[df["Beslut"] == "Bevilja"]

# culculate kpis for all school
number_approved =len(approved)
total_applications = len(df)
approved_precentage = f"{number_approved*100/total_applications:.1f}%"

# calculate kpis for on school
def provider_kpis(provider):
    applied = df.query(f"`Utbildningsanordnare administrativ enhet` == '{provider}'")
    applications = len(applied)
    approved = len(applied.query("Beslut=='Beviljad'"))
    
    return applications, approved

if __name__ == '__main__':
    # for testing purpose
    print(number_approved)
    print(total_applications)
    print(approved_precentage)