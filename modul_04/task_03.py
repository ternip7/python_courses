from collections import deque

def person_is_seller(name):
    return name[-1] == 'm'


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        person = search_queue.popleft()

        if not person in searched:
            if person_is_seller(person):
                print(person + ' is a mango')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anju', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anju'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []
print(graph)

search('you')