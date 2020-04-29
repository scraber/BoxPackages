from typing import Dict, List

from boxes import sizes


def compute_collective_box(total_boxes: int) -> int:
    """
    Auxiliary function.
    Calculates number of collective box to use
    based on sum of all three type of boxes

    Arguments:
        total_boxes {int} -- Sum of all three types of boxes

    Returns:
        int -- Number of collective boxes required for order
    """
    if total_boxes == 1:
        return 0
    return (
        total_boxes // sizes.COLLECTIVE_BOX + 1
        if total_boxes % sizes.COLLECTIVE_BOX
        else total_boxes // sizes.COLLECTIVE_BOX
    )


def optimize(small: int, medium: int, large: int, collective: int) -> List:
    """
    Auxiliary function
    Used in corner case for order size < 18

    Arguments:
        small {int} -- Quantity of small boxes
        medium {int} -- Quantity of medium boxes
        large {int} -- Quantity of large boxes
        collective {int} -- Quantity of collective boxes

    Returns:
        List -- List of box quantities [small, medium, large, collective]
    """
    if medium == 1 and large == 1:
        return [small, 0, medium + large, collective]

    if small == 1 and large == 1:
        return [0, small + large, 0, collective]

    return [small, medium, large, collective]


def pack_into_boxes(order_size: int, small=0, medium=0, large=0) -> List:
    """
    Packs desired product quantity into specific boxes

    Arguments:
        order_size {int} -- Order size to pack into boxes

    Keyword Arguments:
        small {int} -- Quantity of small boxes (default: {0})
        medium {int} -- Quantity of medium boxes (default: {0})
        large {int} -- Quantity of large boxes (default: {0})

    Returns:
        List -- List of box quantities [small, medium, large, collective]
    """
    if order_size <= 0:
        return optimize(
            small, medium, large, compute_collective_box(small + medium + large)
        )
    elif order_size > sizes.MEDIUM_BOX:
        return pack_into_boxes(order_size - sizes.LARGE_BOX, small, medium, large + 1)
    elif order_size > sizes.SMALL_BOX:
        return pack_into_boxes(order_size - sizes.MEDIUM_BOX, small, medium + 1, large)
    else:
        return pack_into_boxes(order_size - sizes.SMALL_BOX, small + 1, medium, large)


def summary_order_boxes(order_size: int) -> Dict:
    """
    Returns user friendly dictionary with specific order boxes

    Arguments:
        order_size {int} -- Order size

    Raises:
        ValueError: If order size is not in range of 1-100

    Returns:
        Dict -- Dictionary with required boxes for given order size
    """
    if not 1 <= order_size <= 100:
        raise ValueError("Order size must be in range of 1-100")

    small_box_qty, medium_box_qty, large_box_qty, collective_box_qty = pack_into_boxes(
        order_size
    )

    return {
        "small_box": small_box_qty,
        "medium_box": medium_box_qty,
        "large_box": large_box_qty,
        "collective_box": collective_box_qty,
    }
