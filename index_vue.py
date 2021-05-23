from browser import window
from javascript import this
from linked_list import LinkedList


Date = window.Date.new

Vue = window.Vue

todos = LinkedList(
    values=[
        {"text": "Learn JavaScript"},
        {"text": "Learn Vue"},
        {"text": "Build something awesome"},
    ]
)


def add_node(event):
    this().todos.push({"text": "do that thing"})
    todos.insert({"text": "do that thing"})
    # this().todos = LinkedList(values=[{"text": "no way"}]).to_list()
    # print(todos.to_list())


app = Vue.new(
    {
        "el": "#app",
        "data": {"todos": todos.to_list()},
        "methods": {"add_node": add_node},
    }
)
