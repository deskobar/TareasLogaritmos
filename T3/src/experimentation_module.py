from .file_module import generate_file, search_username_in_file

def generate_experiment(Q):
    result = {}
    bloom_filter, L_file = generate_file(m, k, n)
    for _ in range(0, Q):
        username_query = generate_random_query()
        response = 'NOT FOUND'
        if bloom_filter.check(username_query) == 1:
            element = search_username_in_file(username_query, L_file)
            if element != '':
                response = element
        result[username_query] = response
    print(response)
    return result

def generate_random_query():
    return 'ugjalpxop'

generate_experiment(1)