from gql import gql

CURRENTMONTHINCOME = gql(
    """ 
        query CurrentMonthIncome($date: String) {
            currentMonthIncome(date: $date) {
                total
                remainder
                percent_remainder
                expenses_count
                user {
                    currency
                }
            }
        }
    """
)

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
