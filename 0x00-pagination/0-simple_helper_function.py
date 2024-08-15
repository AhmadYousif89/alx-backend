#!/usr/bin/env python3
"""
Helper function (index_range) to paginate a dataset.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple containing the starting index and the ending index
    Page numbers are 1-indexed, i.e. the first page is page 1.

    Parameters:
        page: int
        page_size: int

    Returns:
        Tuple[int,int]

    Example:
    >>> index_range(0, 10)
    (0, 10)
    >>> index_range(3, 10)
    (20, 30)
    """
    page = 1 if page < 1 else page
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
