import connexion
import six

from swagger_server.models.add_item import AddItem  # noqa: E501
from swagger_server.models.add_to_basket import AddToBasket  # noqa: E501
from swagger_server.models.assign_task import AssignTask  # noqa: E501
from swagger_server.models.feedback import Feedback  # noqa: E501
from swagger_server.models.new_customer import NewCustomer  # noqa: E501
from swagger_server.models.order import Order  # noqa: E501
from swagger_server.models.update_item import UpdateItem  # noqa: E501
from swagger_server import util


def api_add_item(body):  # noqa: E501
    """adds new menu items to the menu

     # noqa: E501

    :param body: adds new menu items to the menu
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = AddItem.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_add_to_basket(body):  # noqa: E501
    """make an order

     # noqa: E501

    :param body: Created user object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = AddToBasket.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_ask_for_help(table_id):  # noqa: E501
    """request help for specific table

     # noqa: E501

    :param table_id: table unique identifier
    :type table_id: str

    :rtype: str
    """
    return 'do some magic!'


def api_assign_task(body):  # noqa: E501
    """assign task to personel

     # noqa: E501

    :param body: assign task to personel
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = AssignTask.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_confirm_order(work_id):  # noqa: E501
    """chef confirms that he/she has received the order and has started working on it.

     # noqa: E501

    :param work_id: chef confirms that he/she has received the order and has started working on it
    :type work_id: str

    :rtype: str
    """
    return 'do some magic!'


def api_feedback(body):  # noqa: E501
    """give feedback on use

     # noqa: E501

    :param body: give feedback on use
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Feedback.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_get_orders(customer_id):  # noqa: E501
    """Get all orders

     # noqa: E501

    :param customer_id: User unique identifier
    :type customer_id: str

    :rtype: str
    """
    return 'do some magic!'


def api_new_customer(body):  # noqa: E501
    """updates new customer info

     # noqa: E501

    :param body: updates new customer info
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = NewCustomer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_order(body):  # noqa: E501
    """make an order

     # noqa: E501

    :param body: Created user object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Order.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_order_ready(work_id):  # noqa: E501
    """chef confirms that he/she has finished the order.

     # noqa: E501

    :param work_id: chef confirms that he/she has finished the order.
    :type work_id: str

    :rtype: str
    """
    return 'do some magic!'


def api_update_item(body):  # noqa: E501
    """updates menu items to the menu

     # noqa: E501

    :param body: updates menu items to the menu
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = UpdateItem.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
