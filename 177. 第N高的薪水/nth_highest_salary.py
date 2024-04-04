import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    sorted_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)

    name = 'getNthHighestSalary(' + str(N) + ')'

    if N - 1 < 0:
        return pd.DataFrame({name: [None]})

    if len(sorted_salaries) >= N:
        return pd.DataFrame({name: [sorted_salaries.iloc[N - 1]]})
    else:
        return pd.DataFrame({name: [None]})


employee_data = {
    'id': [1, 2, 3],
    'salary': [100, 200, 300]
}

employee = pd.DataFrame(employee_data)

result_df = nth_highest_salary(employee, 2)
print(result_df)

result_df = nth_highest_salary(employee, 4)
print(result_df)
