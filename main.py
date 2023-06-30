from functions_gene_sampling import *
from functions_generic import duval_factorization

import pandas as pd


# Create test strings
# Fib string of length 2584
fib_string = create_fib_string(18)
# Random string of length 2584
random_string = create_random_string(2584)
# Random string of length 2584
random_4_string = create_4_random_string(2584)
# Covid Gene of length 2584
with open('./data/Covid_gene.txt', 'r') as file:
    covid_string = file.read()
covid_string = covid_string[:2584]

distances = [8,16,32,64]
sample_lengths = [1000,400,200,100]

ds = []
ms = []
bwt_fib_runs = []
bbwt_fib_runs = []
ulw_fib_original = []
ulw_fib_concat = []
bwt_rand_runs = []
bbwt_rand_runs = []
ulw_rand_original = []
ulw_rand_concat = []
bwt_covid_runs = []
bbwt_covid_runs = []
ulw_covid_original = []
ulw_covid_concat = []
bwt_rand_4_runs = []
bbwt_rand_4_runs = []
ulw_rand_4_original = []
ulw_rand_4_concat = []

for d in distances:
    print(d)
    for m in sample_lengths:
        x = print(m, "+", end=" ")


        # Create a set of all phrases
        string = concat_string(fib_string,d,m)
        bwt_fib_runs.append(count_runs(bwt(string)))
        bbwt_fib_runs.append(count_runs(bbwt(string)))
        ulw_fib_original.append(len(set(duval_factorization(fib_string))))
        ulw_fib_concat.append(len(set(duval_factorization(string))))

        string = concat_string(random_string, d, m)
        bwt_rand_runs.append(count_runs(bwt(string)))
        bbwt_rand_runs.append(count_runs(bbwt(string)))
        ulw_rand_original.append(len(set(duval_factorization(random_string))))
        ulw_rand_concat.append(len(set(duval_factorization(string))))

        string = concat_string(covid_string, d, m)
        bwt_covid_runs.append(count_runs(bwt(string)))
        bbwt_covid_runs.append(count_runs(bbwt(string)))
        ulw_covid_original.append(len(set(duval_factorization(covid_string))))
        ulw_covid_concat.append(len(set(duval_factorization(string))))

        string = concat_string(random_4_string, d, m)
        bwt_rand_4_runs.append(count_runs(bwt(string)))
        bbwt_rand_4_runs.append(count_runs(bbwt(string)))
        ulw_rand_4_original.append(len(set(duval_factorization(random_4_string))))
        ulw_rand_4_concat.append(len(set(duval_factorization(string))))

        ds.append(d)
        ms.append(m)

# Create a dataframe of our test strings
df = pd.DataFrame()
df['d'] = ds
df['m'] = ms
df['fib bwt runs'] = bwt_fib_runs
df['fib bwbt runs'] = bbwt_fib_runs
df['fib original ulw'] = ulw_fib_original
df['fib concat ulw'] = ulw_fib_concat
df['rand-2 bwt runs'] = bwt_rand_runs
df['rand-2 bbwt runs'] = bbwt_rand_runs
df['rand-2 original ulw'] = ulw_rand_original
df['rand-2 concat ulw'] = ulw_rand_concat
df['covid bwt runs'] = bwt_covid_runs
df['covid bbwt runs'] = bbwt_covid_runs
df['covid original ulw'] = ulw_covid_original
df['covid concat ulw'] = ulw_covid_concat
df['rand-4 bwt runs'] = bwt_rand_4_runs
df['rand-4 bbwt runs'] = bbwt_rand_4_runs
df['rand-4 original ulw'] = ulw_rand_4_original
df['rand-4 concat ulw'] = ulw_rand_4_concat


# Write our DF to a CSV files
df.to_csv('data_gene_sampling_28657.csv', index=False)