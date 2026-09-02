import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\Zone Tech\Downloads\students.csv')

number = df['city'].value_counts()

plt.bar(number.index, number.values, color = "teal")
plt.xlabel("Cites")
plt.ylabel("Students")
plt.title("Number of Students per city")
plt.show()


plt.bar(number.index, number.values, color = "purple")
plt.xlabel("Cites")
plt.ylabel("Students")
plt.title("Number of Students per city")
plt.show()