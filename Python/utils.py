"""Utils functions"""
import os
def check_path(path):
    path = "Graph SVG"
    if not os.path.exists(path):
        os.makedirs(path)