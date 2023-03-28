import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.ExcelFile("obes-phys-acti-diet-eng-2017-tab.xlsx")

data_age = data.parse('Table 6', skiprows=7, skipfooter=12)
data_age.rename(columns={u'Year4': u'Year', u'All persons5': u'Total'}, inplace=True)
data_age.drop(axis=1, columns={u'Unnamed: 1'}, inplace=True)
data_age.dropna(inplace=True)
data_age.set_index('Year', inplace=True)
data_age_minus_total = data_age.drop('Total', axis=1)

# data_age['Under 16'].plot(label="Under 16")
# data_age['35 to 44'].plot(label="35-44")

kids_values = data_age['Under 16'].values
x_axis = range(len(kids_values))
poly_degree = 3
curve_fit = np.polyfit(x_axis, kids_values, poly_degree)
poly_interp = np.poly1d(curve_fit)

poly_fit_values = []
for i in range(len(x_axis)):
    poly_fit_values.append(poly_interp(i))

plt.plot(x_axis, poly_fit_values, "-r", label = "Fitted")
plt.plot(x_axis, kids_values, "-b", label = "Orig")

plt.legend(loc="upper right")
plt.show()
plt.close()

x_axis2 = range(15)

poly_fit_values = []
for i in range(len(x_axis2)):
    poly_fit_values.append(poly_interp(i))

plt.plot(x_axis, kids_values, "-b", label = "Orig")
plt.plot(x_axis2, poly_fit_values, "-g", label = "Prediction")
plt.legend(loc="upper right")
plt.show()