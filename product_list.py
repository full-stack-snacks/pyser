import javascript
from random import shuffle


def handle_product_choice(product):
    this = javascript.this()
    votes = dict(this.tallies).get(product, 0)
    this.tallies[product] = votes + 1

    prods = this.products[:]
    shuffle(prods)
    this.working_products = prods[:3]


props = ["products"]
methods = {"handle_product_choice": handle_product_choice}


def data(*args):
    return {"working_products": [], "tallies": {}}


template = """

<ul class="flex gap-x-16 p-8 border border-8 border-gray-700 rounded">
    <li v-for="prod in working_products" :key="prod" class="flex-1">
        <product :info='prod' :product_choice="handle_product_choice" />
    </li>
</ul>
<p>{{ tallies }}</p>
<p>{{ winner }}</p>

"""


def created():
    this = javascript.this()
    prods = this.products[:]
    shuffle(prods)
    this.working_products = prods[:3]


def winner(*args):
    tallies = dict(javascript.this().tallies)
    if not tallies:
        return "..."

    return max(tallies, key=tallies.get)


computed = {"winner": winner}


options = {
    "props": props,
    "methods": methods,
    "data": data,
    "template": template,
    "created": created,
    "computed": computed,
}
