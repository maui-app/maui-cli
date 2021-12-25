from gql import gql

DAILYEXPENSES = gql(
    """
        query DailyExpenses($date: String!, $all: Boolean) {
            dailyExpenses(date: $date, all: $all) {
                expenses {
                    name
                    amount
                }
                sum
                pagination {
                    currentPage
                    maxPages
                }
            }
        }
    """
)

ADDEXPENSE = gql(
    """
        mutation AddExpense($name: String!, $amount: Float!, $date: String) {
            addExpense(name: $name, amount: $amount, date: $date) {
                sum
                errorId
                expense {
                    user {
                        currency
                    }
                }
            }
        }
    """
)
