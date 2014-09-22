import numpy as np
import pandas
import matplotlib.pyplot as plt

datamap = {
    1: 'real bad',
    2: 'bad',
    3: 'meh',
    4: 'good',
    5: 'way good'
}


df = pandas.DataFrame(data=np.random.choice(range(1,6), size=37), columns=['score'])
df['rating'] = df.score.map(datamap.get)

fig, ax = plt.subplots()
df.rating.value_counts().plot(kind='bar', ax=ax)
## alternatively:
# df.groupby(by='rating').count().plot(kind='bar', ax=ax)
fig.tight_layout()