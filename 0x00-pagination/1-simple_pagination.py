#!/usr/bin/env python3
"""1-simple_pagination module"""
import csv
import requests
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple containing the start and end index
    for the given page and page_size.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_URL = (
        "https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2020/5/"
        "7d3576d97e7560ae85135cc214ffe2b3412c51d7.csv?X-Amz-Algorithm=AWS4-"
        "HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240819%2Fus-"
        "east-1%2Fs3%2Faws4_request&X-Amz-Date=20240819T045937Z&X-Amz-"
        "Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ea161c9851"
        "320bec7b3703c67f48a093ba3e0a32d2e992f156aad90598668573"
    )

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def download_data(self) -> List[List]:
        """Downloads and caches the dataset from the URL."""
        if self.__dataset is None:
            response = requests.get(self.DATA_URL)
            response.raise_for_status()
            decoded_content = response.content.decode('utf-8').splitlines()
            reader = csv.reader(decoded_content)
            dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a page of the dataset based on page and page_size.
        """
        assert isinstance(page, int) and page > 0, (
            "Page number must be a positive integer"
        )


assert isinstance(page_size, int) and page_size > 0, (
    "Page size must be a positive integer"
)

dataset = self.download_data()
start_index, end_index = index_range(page, page_size)

return dataset[start_index:end_index] if start_index < len(
    dataset
) else []
