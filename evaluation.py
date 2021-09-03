#Imports
import sys
import pandas as pd
import numpy as np
import json

# set df and dictionary 
df = pd.read_json('df_parties.json')
dict = {"Ley_1" : "1",
       "Ley_2" : "1",
       "Ley_3" : "1",
       "Ley_4" : "0.33",
       "Ley_5" : "1",
       "Ley_6" : "1",
       "Ley_7" : "1",
       "Ley_8" : "1",
       "Ley_9" : "1",
       "Ley_10" : "1"}


def main(dict):
    congresistas = {"01":{"AP":1.0,"APP":1.0,"FA":1.0,"FP":0.3333333333,"FREPAP":1.0,"PM":1.0,"PP":1.0,"SP":1.0,"UPP":0.7846153846},"02":{"AP":1.0,"APP":1.0,"FA":1.0,"FP":1.0,"FREPAP":1.0,"PM":1.0,"PP":1.0,"SP":1.0,"UPP":0.8769230769},"03":{"AP":1.0,"APP":1.0,"FA":0.475,"FP":1.0,"FREPAP":1.0,"PM":0.775,"PP":1.0,"SP":1.0,"UPP":0.9538461538},"04":{"AP":1.0,"APP":1.0,"FA":1.0,"FP":0.6285714286,"FREPAP":1.0,"PM":1.0,"PP":1.0,"SP":1.0,"UPP":1.0},"05":{"AP":1.0,"APP":1.0,"FA":0.9,"FP":0.2153846154,"FREPAP":1.0,"PM":0.4,"PP":1.0,"SP":1.0,"UPP":1.0},"06":{"AP":1.0,"APP":0.97,"FA":0.8285714286,"FP":1.0,"FREPAP":1.0,"PM":1.0,"PP":1.0,"SP":0.4,"UPP":0.7},"07":{"AP":0.1714285714,"APP":0.0526315789,"FA":1.0,"FP":0.1333333333,"FREPAP":0.0769230769,"PM":0.0,"PP":0.2444444444,"SP":0.4,"UPP":0.7142857143},"08":{"AP":0.4347826087,"APP":1.0,"FA":1.0,"FP":0.0769230769,"FREPAP":1.0,"PM":1.0,"PP":1.0,"SP":1.0,"UPP":1.0},"09":{"AP":0.9565217391,"APP":1.0,"FA":1.0,"FP":1.0,"FREPAP":1.0,"PM":0.0,"PP":1.0,"SP":1.0,"UPP":1.0},"10":{"AP":0.9130434783,"APP":1.0,"FA":0.9142857143,"FP":0.2727272727,"FREPAP":0.9333333333,"PM":1.0,"PP":0.9454545455,"SP":1.0,"UPP":0.6666666667},"11":{"AP":0.0139217391,"APP":0.0185714286,"FA":0.0203571429,"FP":0.0207142857,"FREPAP":0.008,"PM":0.03625,"PP":0.0134090909,"SP":0.0192857143,"UPP":0.0123076923},"Resultado":{"AP":0,"APP":0,"FA":0,"FP":0,"FREPAP":0,"PM":0,"PP":0,"SP":0,"UPP":0}}
    
    #create dfs
    df = pd.DataFrame(congresistas)
    voter_s = create_user(dict)

    
    dictionary = {}
    for i in get_result_gen(voter_s, df):
        dictionary[i[0]] = i[1]

    calculation_s = pd.Series(dictionary)
    calculation_s.sort_values(ascending=False, inplace=True)
    result = create_json(calculation_s, 3)
    return result

def create_user(dict):
    """Create a pd.serie for the user using the dictionary"""
    arr = list()  
    
    # Extract the information from the dictionary
    for i in range(len(dict)):
        vote = dict.get("Ley_" + str(i+1))
        if(vote):
            number = float(vote)
            arr.append(number) 
    
    return pd.Series(arr)

def get_result_gen(voter_s, df):
    # The last column is for absenties
    row_length = len(df)
    
    # Get every substraction per row.
    for i in range(len(df)):
        row_result = get_row_result(voter_s, df.iloc[i,:])
        party_name = df.iloc[i,:].name
        yield [party_name, row_result]
        
def get_row_result(voter_s, row):
    """Given a voter series and a row, this returns the affinity minus the absenties"""
    row_without_absenties = row.iloc[:-2]
    row_without_absenties.reset_index(drop=True, inplace=True)
    affinity_mean = get_absolute_mean(voter_s, row_without_absenties)
    punishment = row.iloc[-2]
    result = affinity_mean - punishment
    return result
    
def get_absolute_mean(voter_s, row_laws):
    """gets 1 row and gets the affinity mean"""
    return 1-abs(row_laws - voter_s).mean()

def create_json(calculation_s, number_of_parties):
    dict = {}
    for i in range(number_of_parties):
        array = []
        array.append(calculation_s.index[i])
        array.append(calculation_s.iloc[i])
        dict["resultado_" + str(i+1)] = array
    return dict

print(main(dict))