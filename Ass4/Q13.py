import matplotlib.pyplot as plt

# Sample data
math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]

# Create a scatter plot
plt.scatter(math_marks, science_marks, color='blue')

# Add titles and labels
plt.title('Scatter Plot: Mathematics vs Science Marks')
plt.xlabel('Mathematics Marks')
plt.ylabel('Science Marks')

# Show the plot
plt.show()
