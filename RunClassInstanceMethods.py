from StockClasses import Category

"""Create portfolio instance for short-term rental industry"""
short_term_rentals = Category("Short-term Rentals", ['EXPE', 'ABNB', 'BKNG', 'VCSA', 'SOND', 'ISPO'],
                              "Short-term Rental Equity Data")

"""push short-term rental data to Google Sheets"""
short_term_rentals.push_to_gsheet()

"""Set a new industry"""
# short_term_rentals.set_industry("Ice Cream")

"""Create portfolio instance for real estate industry"""
real_estate = Category("Real Estate", ['RDFN', 'COMP', 'Z', 'OPEN', 'OPAD', 'CBRE'],
                       "Real Estate Equity Data")

""""Push real estate data to Google Sheets"""
real_estate.push_to_gsheet()
