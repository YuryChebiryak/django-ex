__author__ = 'yurychebiryak'
from project.settings import base_url

navContext = {
         'main' : base_url + "main",
         'submit' : base_url + "submit",
         'donate' : base_url + "donate",
         'recent' : base_url + "recent",
         }

def uniteContexts(a, b):
    return { x: a[x] if x in a else b[x] for x in list(a.keys()) + list(b.keys()) }
