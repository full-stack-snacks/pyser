from browser import window

from product_list import options as product_list
from product import options as product

Vue = window.Vue


def data(*args):
    return {
        "products": [
            "bag",
            "banana",
            "bathroom",
            "boots",
            "breakfast",
            "bubblegum",
            "chair",
            "cthulhu",
            "dog-duck",
            "dragon",
            "pen",
            "pet-sweep",
            "scissors",
            "shark",
            "sweep",
            "tauntaun",
            "unicorn",
            "water-can",
            "wine-glass",
        ]
    }


app = Vue.createApp(
    {
        "data": data,
        "template": """
            <div class="p-8">
            <product-list :products="products" />
            </div>
        """,
    }
)

app.component("product-list", product_list)
app.component("product", product)

vm = app.mount("#app")
