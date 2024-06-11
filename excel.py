import pandas as pd

# Read Excel file
df = pd.read_excel('file.xlsx')

# Get column headers
headers = list(df.columns)

# Prompt user for search query
search_query = input("Enter search query (e.g. business name, address, description): ")

# Search for column matching search query
	for header in headers:    
		if search_query.lower() in header.lower():
       
# Display data for matching column        
			print(df[header])        
				break
			else:    
print("No matching column found.")