# Tim Lucas
# 2025-06-17

STATE_TAX_RATE = .051
#problem = County tax rate incorrectly set to 2.5%; corrected to 2.4%
COUNTY_TAX_RATE = .024

def main():
    print('This program will calculate your taxes!\n')

    sale = float(input('How much is the cost of your purchase? '))
    #problem = state_tax not initialized.; corrected by initializing state_tax and
	#assigned the value returned by calculate state tax
    state_tax = calculate_state_tax(sale, STATE_TAX_RATE)
    #problem = parameters in incorrect order. corrected = place in correct order
    county_tax = calculate_county_tax(sale, COUNTY_TAX_RATE)
	 
    total_cost = sale + state_tax + county_tax

    print('\nSale amount: $', format(sale, '.2f'), sep = '')
    print('State tax  : $', format(state_tax, '.2f'), sep = '')
    print('County tax : $', format(county_tax, '.2f'), sep = '')
    print('Total cost : $', format(total_cost, '.2f'), sep = '')

def calculate_state_tax(sales_amount, tax_rate):
	return(sales_amount * tax_rate)
	
def calculate_county_tax(amount, rate):
	#problem = function does not return anything. corrected = added statement to 
	#return calculated value
    return(amount * rate)
    
main()
