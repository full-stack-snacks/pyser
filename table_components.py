from javascript import this
from browser import window


def table_element():
    """
    Brython/Vue Component
    """

    template = """

    <table class="w-full m-auto text-lg bg-green-200 border border-collapse border-green-800 rounded-lg">
        <slot></slot>
    </table>

    """

    return {
        "template": template,
    }


def table_header():
    """
    Brython/Vue Component
    """

    template = """

    <th class="p-1 text-left border border-green-600">
        <slot></slot>
    </th>

    """

    return {
        "template": template,
    }


def table_footer():
    """
    Brython/Vue Component
    """
    props = ["sales"]
    template = """

    <tfoot>
        <tr class="bg-green-400">
            <table-header>Totals</table-header>
            <table-data v-for="shop_sales in sales">
                {{ shop_sales }}
            </table-data>
        </tr>
    </tfoot>

    """

    return {
        "props": props,
        "template": template,
    }


def table_data():
    """
    Brython/Vue Component
    """

    template = """

    <td class="px-3 py-2 text-right border border-green-600">
        <slot></slot>
    </td>

    """

    return {
        "template": template,
    }


def table_body():
    """
    Brython/Vue Component
    """
    props = ["stands"]
    methods = {
        "click_handler": lambda stand: window.alert(f"Delete {stand.location}")
    }
    template = """

    <tbody>
        <tr v-for="(stand,index) in stands" :key="stand.id" :class="{'bg-green-300': index % 2}" >

            <table-header>
                <div class="flex items-center justify-between gap-2 px-4">

                    <p>{{stand.location}}</p>

                    <svg @click="click_handler(stand)" class="w-6 h-6 text-red-400 text-xsm" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                    </svg>
                </div>
            </table-header>

            <table-data v-for="(amt,index) in stand.cookiesEachHour" :key="index">
                {{ amt }}
            </table-data>

            <table-data>{{stand.totalDailyCookies}}</table-data>
        </tr>

    </tbody>

    """

    return {
        "props": props,
        "methods": methods,
        "template": template,
    }
