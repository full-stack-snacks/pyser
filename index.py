from browser import window
from cookie_sales import sales_data, calculate_hourly_totals
from javascript import this

from table_components import (
    table_body,
    table_data,
    table_element,
    table_footer,
    table_header,
)

Vue = window.Vue


def root():
    """
    Brython/Vue Component
    """

    def data(*args):
        return sales_data

    computed = {"totals": lambda _: calculate_hourly_totals(this().stands)}

    template = """
    <div class="p-8">
    <table-element>
        <thead>
        <tr class="bg-green-400">
            <table-header>Location</table-header>
            <table-header v-for="time_slot in hours">
                {{time_slot}}
            </table-header>
            <table-header>Totals</table-header>
        </tr>
        </thead>
        <table-body :stands="stands" />
        <table-footer :sales="totals" />
    </table-element>
    </div>

    """

    return {
        "data": data,
        "template": template,
        "computed": computed,
    }


app = Vue.createApp(root())

app.component("table-element", table_element())
app.component("table-header", table_header())
app.component("table-footer", table_footer())
app.component("table-data", table_data())
app.component("table-body", table_body())

vm = app.mount("#app")
