from fastapi import FastAPI
from tools import UkhaanTable


ukhaans = UkhaanTable()

nepali_lists = ukhaans.nepali()
roman_lists = ukhaans.roman()
meaning_lists = ukhaans.meaning()
example_lists = ukhaans.example()


app = FastAPI()

@app.get("/ukhaantukkas")
def main_page():
    return {
        'Nepali': nepali_lists,
        'Roman': roman_lists,
        'Meaning': meaning_lists,
        'Example': example_lists,
        }


@app.get("/ukhaantukkas/nepali")
def nepali():
    return {
        "Nepali": nepali_lists,
    }


@app.get("/ukhaantukkas/roman")
def roman():
    return {
        'Roman': roman_lists,
    }


@app.get("/ukhaantukkas/meaning")
def meaning():
    return {
        'Meaning': meaning_lists,
    }


@app.get("/ukhaantukkas/example")
def example():
    return {
        'Example': example_lists,
    }

