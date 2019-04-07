from enum import Enum


class MessageCategory(Enum):
    ORDER_STATUS = "order_status"
    OTHERS = "others"
    CANCEL_ORDER = "cancel_order"
