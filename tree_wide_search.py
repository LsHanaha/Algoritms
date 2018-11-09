from collections import deque
search_queue = deque()

graph = {}
graph["you"] = ["clare", 'alice', 'bob']
graph["alice"] = ["cherlie", 'billy', 'tom']
graph["clare"] = ["billy"]
graph["bob"] = []
graph["cherlie"] = []
graph["billy"] = []
graph["tom"] = []

search_queue += graph["you"] # добавляем в поиск своих друзей
scanned = []                 # Люди которых мы уже проверили

print(search_queue)

def person_is_seller(name):
    return name[-1] == 'm'

while search_queue:
    person = search_queue.popleft() #извлекаем левый элемент из деки
    if person not in scanned:
        scanned.append(person)
        if person_is_seller(person):
            print(person + ' is mango seller!')
            break
        else:
            search_queue += graph[person]
        if len(search_queue) == 0:
            print("There is no mango seller!")
    print(search_queue)






