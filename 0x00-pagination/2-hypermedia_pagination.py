#!/usr/bin/env python3
"""
Implementation of (get_hyper) function to paginate a database.
"""
import csv
import math
from typing import List
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


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return a page of the dataset

        Parameters:
            page (int): represents the starting index of the page
            page_size (int): represents the number of items per page

        Returns:
            List[List]

        Example:
        >>> server = Server()
        >>> server.get_page(1, 2)
        [['1', 'Male', 'MILO', '205'], ['2', 'Female', 'AMELIA', '172']]
        >>> server.get_page(2, 2)
        [['3', 'Male', 'OLIVER', '151'], ['4', 'Female', 'EMMA', '151']]
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        dataset = self.dataset()
        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Return a dictionary containing the following keys:
        - page_size: the length of the returned dataset page
        - page: the current page number
        - data: the dataset page
        - next_page: the next page number
        - prev_page: the previous page number
        - total_pages: the total number of pages in the dataset

        Parameters:
            page (int): represents the starting index of the page
            page_size (int): represents the number of items per page

        Returns:
            dict

        Example:
        >>> server = Server()
        >>> server.get_hyper(1, 2)
        {'page_size': 2, 'page': 1 , 'data': [['1', 'Male', 'MILO', '205'], ['2', 'Female', 'AMELIA', '172']], 'next_page': 2, 'prev_page': None, 'total_pages': 326}
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
