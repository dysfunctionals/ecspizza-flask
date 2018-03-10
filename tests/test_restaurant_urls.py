# Copyright 2014 SolidBuilds.com. All rights reserved
#
# Authors: Ling Thio <ling.thio@gmail.com>

from __future__ import print_function  # Use print() instead of print
from flask import url_for


def test_page_urls(client):

    response = client.get(url_for('restaurants.index'), follow_redirects=True)
    assert response.status_code==200