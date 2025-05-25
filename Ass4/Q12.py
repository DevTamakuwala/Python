import matplotlib.pyplot as plt
import numpy as np

# 1. Bar Chart of Popularity of Programming Languages
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Create a bar chart
plt.figure(figsize=(10, 5))

# Plotting Bar Chart
plt.subplot(131)
plt.bar(languages, popularity, color=['blue', 'green', 'red', 'purple', 'orange', 'brown'])
plt.title('Popularity of Programming Languages')
plt.xlabel('Programming Languages')
plt.ylabel('Popularity (%)')

# 2. Bar Plot of Scores by Group and Gender
groups = ['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5']
men_means = [22, 30, 35, 35, 26]
women_means = [25, 32, 30, 35, 29]

# X-axis positions
x = np.arange(len(groups))
width = 0.35

# Plotting Bar Plot
plt.subplot(132)
rects1 = plt.bar(x - width/2, men_means, width, label='Men')
rects2 = plt.bar(x + width/2, women_means, width, label='Women')

# Add some text for labels, title and custom x-axis tick labels
plt.title('Scores by Group and Gender')
plt.xlabel('Groups')
plt.ylabel('Scores')
plt.xticks(x, groups)
plt.legend()

# 3. Pie Chart for Popularity of Programming Languages
plt.subplot(133)
plt.pie(popularity, labels=languages, autopct='%1.1f%%', startangle=90)
plt.title('Popularity of Programming Languages')

# Show the plots
plt.tight_layout()
plt.show()
