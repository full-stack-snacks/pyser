"""
Brython/Vue Component
"""

import javascript


props = ["info", "product_choice"]
methods = {
    "click_handler": lambda _: javascript.this().product_choice(
        javascript.this().info
    )
}


def data(*args):
    return {"path": f"/busmall/assets/{javascript.this().info}.jpg"}


template = """

<div @click="click_handler">
    <img v-bind:src="path" />
    <p>{{info}}</p>
</div>

"""

options = {
    "props": props,
    "methods": methods,
    "data": data,
    "template": template,
}
