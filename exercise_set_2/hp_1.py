# hp_1.py

# accounts is the accounts data list used for this project.
accounts = [
    ['Sly', 'Brockbank', 'sbrockbank0@patch.com', '118', '5/21/2021'],
    ['Modesta', 'Petegre', 'mpetegre1@kickstarter.com', '135', '10/12/2020'],
    ['Karine', 'Woollons', 'kwoollons2@moonfruit.com', '194', '3/26/2021'],
    ['Kendricks', 'Vockings', 'kvockings3@state.tx.us', '162', '11/18/2020'],
    ['Nedda', 'Karpeev', 'nkarpeev4@uol.com.br', '91', '6/22/2021'],
    ['Dino', 'Snowman', 'dsnowman5@marketwatch.com', '199', '10/9/2021'],
    ['Margarette', 'Clampton', 'mclampton6@yolasite.com', '126', '5/12/2021'],
    ['Standford', 'McGrann', 'smcgrann7@goo.ne.jp', '59', '3/11/2021'],
    ['Wilt', 'Vasyunichev', 'wvasyunichev8@senate.gov', '76', '10/16/2021'],
    ['Conchita', 'Poupard', 'cpoupard9@icq.com', '117', '4/5/2021']
]


def get_username(email):
    '''Returns the username portion of the input argument email. Accounts for
    invalid emails and returns a lowercase username'''

    # Delete pass and insert your code (optionally replace this with code from
    # ex_1_2.py
    if isinstance(email, str):
        if '@' in email:
            email_parts = email.split('@')
            return email_parts[0].lower()
        else:
            return None
    else:
        return None


def convert_list(accounts):
    '''Converts a list of lists to a list of dictionaries with keys
    first_name, last_name, username, email, login_count, last_login
    '''
    # Delete the pass keyword here and insert your code.
    accounts_list = list()
    for i in range(len(accounts)):
        account_dict = dict()
        account = accounts[i]
        username = get_username(account[2])

        account_dict['first_name'] = account[0]
        account_dict['last_name'] = account[1]
        account_dict['username'] = username
        account_dict['email'] = account[2]
        account_dict['login_count'] = account[3]
        account_dict['last_login'] = account[4]

        accounts_list.append(account_dict)
    return accounts_list


def get_usernames(account_list):
    '''Accepts a list of dictionaries with keys first_name, last_name,
    username, email, login_count, last_login. This function returns a list of
    usernames collected from each dictionary in the list'''
    # Delete the pass keyword here and insert your code
    username_list = [account['username'] for account in account_list]
    return username_list


def average_logins(account_list):
    '''Accepts a list of dictionaries with keys first_name, last_name,
    username, email, login_count, last_login. This function collects the
    login_counts from all dictionary elements in the list and returns the
    average login count.'''

    # Delete the pass keyword below and insert your code.
    login_count_list = [int(account['login_count']) for account in account_list]
    average = sum(login_count_list) / len(login_count_list)
    return average


def print_details():
    '''This function calls convert_list to convert accounts to a list
    of dictionaries.  Then it prints the following results obtained by
    calling the support functions get_usernames and average_logins:

    Print the following to the screen:

    - the list of usernames returned from get_usernames
    - the average login_count

    Print values with a format of your choosing.'''

    # delete the pass keyword below and insert your code
    accounts_list = convert_list(accounts)
    username_list = get_usernames(accounts_list)
    print("List of usernames:")
    print(username_list)
    average = average_logins(accounts_list)
    print("\nAverage Logins: ")
    print(average)
