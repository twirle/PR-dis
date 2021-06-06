from numpy import true_divide
import pandas as pd

cars = {'brand': ['honda', 'toyoya', ' ford'],
        'price': [22000, 25000, 27000]}

cars_df = pd.DataFrame(cars, columns=['brand', 'price'], index=[
                       'car 1', 'car 2', 'car 3'])
year = [2010, 2011, 2008]
cars_df['year'] = year

cars_df.insert(1, 'model', ['civic', 'prius', 'focus'], True)
# newcar1 = {'brand': 'hyundai', 'model': 'avante', 'year': 2010}
# cars_df = cars_df.append(newcar1, ignore_index=True)

cars_df.loc['car 4'] = ['hyundai', 'avante', 20000, 2010]

cars_df['discount'] = 0.1 * cars_df['price']
cars_df['discount price'] = 0.9 * cars_df['price']

print(cars_df)
print(cars['brand'])
