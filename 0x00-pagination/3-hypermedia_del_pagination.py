#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict:
        """
        Deletion-resilient hypermedia pagination

        Parameters:
            index (int): index of the first item in the current page
                - given page 3 with page_size 20, index should be 60
                    if no items were deleted.
            page_size (int): number of items per page

        Requirements:
            - Use assert to verify that index is in a valid range.
            - If index 0, page_size 10,
                then should return rows indexed 0 to 9 included.
            - If next request is for index (10) with page_size 10,
                but rows 3, 6 and 7 were deleted,
                the user should still receive rows indexed 10 to 19 included.
        Returns:
            Dict: {index: List[dataset], next_index: int, page_size: int, data: List}
        """
        assert type(index) == int, "Index must be an integer"
        assert index >= 0, "Index must be positive"

        indexed_dataset = self.indexed_dataset()
        dataset_size = len(indexed_dataset)

        assert index < dataset_size, "Index out of range"

        data = []
        curr_index = index

        while len(data) < page_size and curr_index < dataset_size:
            if curr_index in indexed_dataset:
                data.append(indexed_dataset[curr_index])
            curr_index += 1

        next_index = curr_index

        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data,
        }
