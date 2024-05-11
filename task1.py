from queue import Queue

queue = Queue()

def generate_request():
    request_number = queue.qsize() + 1
    queue.put(request_number)
    return f'You are {request_number} in queue'

def process_request():
    if not queue.empty():
        return queue.get()
    else:
        return 'Queue is empty'

if __name__ == "__main__":
        while(True):
            command = input("Enter a command: ")

            match command:
                case "add":
                    print(generate_request())
                case "get":
                    print(process_request())
                case "exit":
                    print('Goodbye!')
                    break
                case _:
                    print('invalid command')