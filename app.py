from fastapi import FastAPI
from tools import UkhaanTable


ukhaan = UkhaanTable()

nepali_lists = ukhaan.nepali()
roman_lists = ukhaan.roman()
meaning_lists = ukhaan.meaning()
example_lists = ukhaan.example()


app = FastAPI()

@app.get("/ukhaantukka")
def main_page():
    return {
        'Nepali': nepali_lists,
        'Roman': roman_lists,
        'Meaning': meaning_lists,
        'Example': example_lists,
        }


@app.get("/ukhaantukka/nepali")
def nepali():
    return {
        "Nepali": nepali_lists,
    }


@app.get("/ukhaantukka/roman")
def roman():
    return {
        'Roman': roman_lists,
    }


@app.get("/ukhaantukka/meaning")
def meaning():
    return {
        'Meaning': meaning_lists,
    }


@app.get("/ukhaantukka/example")
def example():
    return {
        'Example': example_lists,
    }

