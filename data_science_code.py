import pandas as panda
import matplotlib.pyplot as graphs

mode = input("1 for Normal mode or 2 for debug mode \n")

alldata_df = panda.read_csv('CarFuelConsumptionEmissionsData.csv', sep=',', dtype={'file' : str, 'year': int, 'manufacturer' : str, 'model' : str, 'description' : str, 'manufacturer' : str, 'manufacturer' : str})

alldata_df = alldata_df[['co_emissions','combined_metric', 'manufacturer', 'model', 'year']]

cleaned_df = alldata_df.dropna(subset=['combined_metric', 'co_emissions'])

cleaned_df = cleaned_df.loc[cleaned_df['co_emissions'] >= 1]

cleaned_df = cleaned_df.loc[cleaned_df['co_emissions'] <= 2500]

cleaned_df = cleaned_df.loc[cleaned_df['combined_metric'] >= 1]

cleaned_df = cleaned_df.loc[cleaned_df['combined_metric'] <= 25]

inefficient_df = cleaned_df[cleaned_df['combined_metric'] >= 10]

inefficient_count= len(inefficient_df) - 1

highemissions_df = cleaned_df[cleaned_df['co_emissions'] >= 200]

highemissions_count = len(highemissions_df) - 1

inefficient_highemissions_df = cleaned_df[(cleaned_df['combined_metric'] >= 10) & (cleaned_df['co_emissions'] >= 200)]

inefficient_highemissions_count = len(inefficient_highemissions_df) - 1

total_records = len(cleaned_df) - 1

#print("Full dataset:")
#print(alldata_df)
#print("inefficient_highemissions_df:")
#print(inefficient_highemissions_df)
print("Total records: " + str(total_records))
print("Total fuel inefficient: " + str(inefficient_count))
print("Total high emission: " + str(highemissions_count))
print("Total fuel inefficient, high emission cars: " + str(inefficient_highemissions_count))

# Support {a, b} = transactions with {a, b} / total transactions (fraction of a,b transactions)
support_rule = inefficient_highemissions_count/total_records
print("Support of rule: " + str(support_rule))

support_inefficient = inefficient_count/total_records
print("Support of fuel inefficient cars: " + str(support_inefficient))

support_highemissions = highemissions_count/total_records
print("Support of high emission cars: " + str(support_highemissions))

# Confidence = transactions with {a, b} / transactions with {a}
confidence = inefficient_highemissions_count/inefficient_count
print("Confidence of the rule: " + str(confidence))

# Lift method 1 = support of {a,b} / ( support of {a} * support  {b} )
lift = inefficient_highemissions_count/(support_inefficient*support_highemissions)
print("Lift of the rule (Method 1): " + str(lift))

# Lift method 2 = confidence / support of {b}
lift2 = confidence / support_highemissions
print("Lift of the rule (Method 2): " + str(lift2))

# conviction = ( 1 - support of {b} ) / ( 1 - confidence )
conviction = (1 - support_highemissions) / (1 - confidence)
print("Conviction of the rule: " + str(conviction))

if(mode == "2"):
	alldata_df.info()
	cleaned_df.info()
	inefficient_df.info()
	highemissions_df.info()
	inefficient_highemissions_df.info()
	print(alldata_df.head(5))
	print(cleaned_df.head(5))
	print(inefficient_df.head(5))
	print(highemissions_df.head(5))
	print(inefficient_highemissions_df.head(5))

#graph 1 bar(x, height, width=0.8, bottom=None, *, align='center', data=None, **kwargs)
fig = graphs.figure()
bargraph1 = fig.add_subplot()

bargraph1.bar(["Rule\nSupport", "Inefficient\nSupport", "High\nEmissions\nSupport","Confidence", "Lift 2", "conviction"],[support_rule,support_inefficient,support_highemissions,confidence,lift2,conviction], width=0.5, bottom=None, align='center', data=None,)

fig.savefig("Graph1.png")

#graph 2 barh(y, width, height=0.8, left=None, *, align='center', **kwargs)

fig = graphs.figure()
hbargraph1 = fig.add_subplot()

hbargraph1.barh(["Total Cars", "Total\nHigh\nEmissions\nCars", "Total\nInefficient\nCars","Total\nInefficient\nHigh\nEmissions\nCars"],[total_records,highemissions_count,inefficient_count,inefficient_highemissions_count], height=0.5, left=None, align='center', data=None,)

fig.savefig("Graph2.png")