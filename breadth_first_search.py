from collections import deque

def person_is_seller(person, mango):
    return mango == person


def bfs(name):  # var graph is hast-table with key-value elements that consists of person and his friends
    mango = "bob"
    queue = deque()
    queue += graph[name]
    searched = []
    while queue:
        person = queue.popleft()
        if not person in searched:
            if person_is_seller(person, mango):
                print(person + " is a seller")
                return True
            else:
                queue += graph[person]
                searched.append(person)
    return False
graph = {"you": ["Nastya", "Sergey", "Katya"], "Nastya": ["Artem", "Masha"], "Sergey": ["Vova", "Petya"],
         "Katya":["Valentina", "Anna"], "Artem":[], "Masha":[], "Vova":[], "Petya":[], "Valentina":[], "Anna":[]}
bfs("you")
graph = {"you": ["alice", "bob", "claire"], "bob": ["anuj", "peggy"], "alice": ["peggy"], "claire": ["thom", "johny"],
         "anuj": [], "peggy": [], 'thom': [], 'jonny': []}
bfs("you")