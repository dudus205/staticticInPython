import pandas as pd
import altair as alt

doc = pd.read_csv('worker.csv', usecols=['Hire Date'])

dwo = pd.DataFrame(doc)

data = pd.DataFrame(dwo.value_counts(ascending=False).iloc[:25])

chart = alt.Chart(data.reset_index().rename(columns={0: "counts"})).mark_bar().encode(
    x='counts',
    y='Hire Date', color='counts'
)

chart.save("chart1.png")
