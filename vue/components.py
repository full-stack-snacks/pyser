import javascript


def button_counter_data(*args):
    return {"count": 0, "text_color": "text-gray-800"}


def button_counter_onClick(event):
    this = javascript.this()
    this.count += 1
    this.text_color = "text-red-800"
    this.update_total()


template = """

<button
    @click="button_counter_onClick"
    class="bg-yellow-300 py-4 rounded hover:bg-yellow-400 text-2xl"
    :class="text_color">
    You clicked me {{ count }} times.
</button>

"""

button_counter = {
    "data": button_counter_data,
    "props": ["update_total"],
    "template": template,
    "methods": {"spam": button_counter_onClick},
}
