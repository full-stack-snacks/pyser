import javascript
from browser import window
from components import button_counter

Vue = window.Vue


def data(*args):
    return {"total": 0}


def update_total(*args):
    this = javascript.this()
    this.total += 1


app = Vue.createApp(
    {
        "data": data,
        "methods": {
            "update_total": update_total,
        },
        "template": """
            <h2>{{  total }}</h2>
            <div class="flex flex-col gap-8 w-1/2 mx-auto py-8">
                <button-counter :update_total="update_total"></button-counter>
                <button-counter :update_total="update_total"></button-counter>
                <button-counter :update_total="update_total"></button-counter>
            </div>
        """,
    }
)

app.component("button-counter", button_counter)

vm = app.mount("#app")
