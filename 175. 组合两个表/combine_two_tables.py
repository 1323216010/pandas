import pandas as pd

person_data = {
    'PersonId': [1, 2],
    'FirstName': ['Allen', 'Bob'],
    'LastName': ['Wang', 'Alice']
}
address_data = {
    'AddressId': [1, 2],
    'PersonId': [2, 3],
    'City': ['New York City', 'Leetcode'],
    'State': ['New York', 'California']
}

person = pd.DataFrame(person_data)
address = pd.DataFrame(address_data)


def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    combined = pd.merge(person, address[['PersonId', 'City', 'State']], on='PersonId', how='left')
    result = combined[['FirstName', 'LastName', 'City', 'State']]
    return result


result_df = combine_two_tables(person, address)
print(result_df)
