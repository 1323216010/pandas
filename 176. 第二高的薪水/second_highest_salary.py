import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    sorted_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)

    if len(sorted_salaries) >= 2:
        return pd.DataFrame({'SecondHighestSalary': [sorted_salaries.iloc[1]]})
    else:
        return pd.DataFrame({'SecondHighestSalary': [None]})


employee_data = {
    'id': [1, 2, 3],
    'salary': [100, 200, 300]
}

employee = pd.DataFrame(employee_data)

result_df = second_highest_salary(employee)
print(result_df)
