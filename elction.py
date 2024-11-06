import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
# data = pd.read_csv('election_results_2024.csv')
data = pd.read_csv('election_results_2024.csv', encoding='latin1')


# Display the first few rows of the dataframe
# print(data.head())

# Get a summary of the dataset
# print(data.info())

# Check for missing values
# print(data.describe())

print(data.isnull().sum())

# Drop rows with missing values
# data = data.dropna()

# Convert Margin to integer
# data['Margin'] = data['Margin'].astype(int)

# winning_candidates = data['Leading Party'].value_counts()
# print(winning_candidates)

# leading_candidates = data[['Constituency', 'Leading Candidate', 'Leading Party']]
# print(leading_candidates)

# top 10 parties
# plt.figure(figsize=(12, 6))
# sns.countplot(x='Leading Party', data=data, order=data['Leading Party'].value_counts().index[:10])
# plt.title('Number of Constituencies Won by Each Party')
# plt.xticks(rotation=45)

# plt.ylabel('Number of Constituencies')
# plt.show()

# Candidate won by highest margin
# top_candidate = data.groupby("Leading Candidate")['Margin'].sum().sort_values(ascending=False).head(10)

# # Convert to DataFrame for plotting
# top_candidate_df = top_candidate.reset_index()

# # Plotting the bar chart
# plt.figure(figsize=(12, 6))
# sns.barplot(data=top_candidate_df, x='Leading Candidate', y='Margin')

# # Rotate x-axis labels for readability
# plt.xticks(rotation=20)

# # Remove scientific notation on y-axis
# plt.ticklabel_format(style='plain', axis='y')

# # Display the plot
# plt.show()


# # Candidate won by lowest margin
# top_candidate = data.groupby("Leading Candidate")['Margin'].sum().sort_values(ascending=False).tail(10)

# # Convert to DataFrame for plotting
# top_candidate_df = top_candidate.reset_index()

# # Plotting the bar chart
# plt.figure(figsize=(12, 6))
# sns.barplot(data=top_candidate_df, x='Leading Candidate', y='Margin')

# # Rotate x-axis labels for readability
# plt.xticks(rotation=20)

# # Remove scientific notation on y-axis
# plt.ticklabel_format(style='plain', axis='y')

# # Display the plot
# plt.show()

# Distribution of top 5 Leading Party Wins
# leading_party_counts = data['Leading Party'].value_counts().head(5)
# plt.figure(figsize=(8, 8))
# leading_party_counts.plot.pie(autopct='%1.1f%%', startangle=90)
# plt.title('Distribution of top 5 Leading Party Wins')
# plt.ylabel('')
# plt.show()

# Top Constituencies by Margin
# top_constituencies = data[['Constituency', 'Margin']].sort_values(by='Margin', ascending=False).head(10)
# plt.figure(figsize=(10, 6))
# sns.barplot(data=top_constituencies, y='Constituency', x='Margin', orient='h')
# plt.title('Top 10 Constituencies by Winning Margin')
# plt.xlabel('Winning Margin')
# plt.show()

# print(data.head(5))
# print(data.info())

# Top Constituencies by Margin
# top_city=data.groupby(["Constituency","Leading Party"])['Margin'].sum().sort_values(ascending=False).head(10)
# print(top_city)