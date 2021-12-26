from gql import gql

INCOMESTATS = gql(
    """
        query IncomeStats {
            incomeStats {
                income_total
                income_spent
                income_remainder
                currency
            }
        }
    """
)
