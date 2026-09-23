from pathlib import Path
import pandas as pd


INPUT_FILE = Path("employees.csv")
OUTPUT_FILE = Path("employees_above_threshold.csv")
SALARY_THRESHOLD = 70000


def load_data(filename):
    return pd.read_csv(filename)


def analyze_data(data):
    average_salary = data["salary"].mean()
    department_count = data["department"].value_counts()

    return average_salary, department_count


def filter_by_salary(data, threshold):
    return data[data["salary"] > threshold].copy()


def export_results(data, filename):
    data.to_csv(filename, index=False)


def main():
    try:
        data = load_data(INPUT_FILE)

        required_columns = {"name", "department", "salary"}

        if not required_columns.issubset(data.columns):
            missing = required_columns - set(data.columns)
            raise ValueError(
                f"Missing required columns: {', '.join(sorted(missing))}"
            )

        average_salary, department_count = analyze_data(data)
        filtered_data = filter_by_salary(data, SALARY_THRESHOLD)

        print("=" * 55)
        print("          EMPLOYEE DATA ANALYSIS")
        print("=" * 55)

        print(f"\nTotal Employees: {len(data)}")
        print(f"Average Salary : ₹{average_salary:,.2f}")

        print("\nDepartment Count")
        print("-" * 30)
        print(department_count)

        print(f"\nEmployees with salary above ₹{SALARY_THRESHOLD:,}")
        print("-" * 55)
        print(filtered_data.to_string(index=False))

        export_results(filtered_data, OUTPUT_FILE)

        print(f"\nFiltered results exported to: {OUTPUT_FILE}")

    except FileNotFoundError:
        print(f"Input file not found: {INPUT_FILE}")
    except pd.errors.EmptyDataError:
        print("The employee CSV file is empty.")
    except ValueError as error:
        print(f"Data error: {error}")
    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()
