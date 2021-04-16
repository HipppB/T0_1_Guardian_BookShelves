import os
from pathlib import Path
import json

def get_project_root() -> Path:
    return Path(__file__).parent.parent
    # renvoie au chemin du dossier racine on l'utilise dans tous les acces au fichiers

def loadBook(book):
    Books = []
    fileList = os.listdir(os.path.join(get_project_root(), 'Books', book))
    for p in fileList:
        page = json.load(open(os.path.join(get_project_root(), 'Books', book, p)))
        Books.append(page)
    return Books

def indexedBook():
    bookList = []
    fileList = os.listdir(os.path.join(get_project_root(), 'Books'))
    for b in fileList:
        page = json.load(open(os.path.join(get_project_root(), 'Books', b, 'Page0.json')))
        bookString = (str(page["ID"]) + '. ' + page["book"])
        bookList.append(bookString)
    return bookList 
    # ["1. bookTitle1","2. bookTitle2"]
def listPage():
    fileList = os.listdir(os.path.join(get_project_root(), 'books'))
    return fileList 
    # ["bookTitle1","bookTitle2"]

def listPages(book):
    pageList = []
    fileList = os.listdir(os.path.join(get_project_root(), 'Books', book))
    for p in fileList:
        page = json.load(open(os.path.join(get_project_root(), 'Books', book, p)))
        pageString = (str(page["ID"]) + '. ' + page["title"])
        pageList.append(pageString)
    return pageList 
    # ["0. PageName", "1. PageName"]

def loadPage(book, page):
    Page = json.load(open(os.path.join(get_project_root(), 'Books', book, page)))
    return Page
    # Dictionnary of the page in python format

def pageNumber(book):
    num = len(listPages(book)[1])
    return num

