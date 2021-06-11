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


def data_func():
    return {
        "count": 1,
    }


Vue.component(
    "button-counter-more",
    {
        "data": {data_func},
        "template": '<button v-on:click="count++">You clicked me {{ count }} times.</button>',
    },
)

app = Vue.new(
    {
        "el": "#app",
        "data": {"todos": todos.to_list()},
        "methods": {"add_node": add_node},
        "template": "<button-counter-more />",
    }
)


def data_func():
    return []
