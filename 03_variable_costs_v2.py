import pandas


# number checkers (checks number is valid )
def num_check(question, error, num_type):
    valid = False
    while not valid:
        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Function doesnt allow blanks for an answer
def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}. \nPlease Try again.\n".format(error))
            continue

        return response


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)

# gets expenses, returns list which has
# the data frame and a sub total
def get_expenses(var_fixed):
    # Set up dictionaries and lists

    item_list = []
    quantity_list = []
    price_list = []

    variable_dict = {
        "Item": item_list,
        "Quantity": quantity_list,
        "Price": price_list
    }

    item_name = ""
    while item_name.lower() != "xxx":

        print()
        # get name, quantity and item
        item_name = not_blank("Item name: ", "The compnent name cannot be blank.")

        if item_name.lower() == "xxx":
            break

        quantity = num_check("Quantity: ", "The amount must be a whole number more than zero", int)

        price = num_check("How much for a single item? $", "The price must be a number <more than 0>", float)

        # add item, quantity and price to lists
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index('Item')

    # Calculate cost of each component



# # main routine starts here
#
#
# # get user data
# product_name = not_blank("Product name: ", "The product name cannot be blank")

# loop to get component, quantity and price

    # add item, quantity and price to list
    item_list.append(item_name)
    quantity_list.append(quantity)
    price_list.append(price)

variable_frame = pandas.DataFrame(variable_dict)
variable_frame = variable_frame.set_index('Item')

# Calculator cost of each component
variable_frame['Cost'] = variable_frame['Quantity'] * variable_frame['Price']

# Find sub total
variable_sub = variable_frame['Cost'].sum()

# Currency Formatting (uses currency functions)
add_dollars = ['Price', 'Cost']
for item in add_dollars:
    variable_frame[item] = variable_frame[item].apply(currency)

# *** Printing Area ***

print()

print(variable_frame)

print()

print("Variable Costs: ${:.2f}".format(variable_sub))