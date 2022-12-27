from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


def test_basic_duckduckgo_search(browser):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    PHRASE = "seal animal"

    search_page.load()
    search_page.search(PHRASE)

    WebDriverWait(browser, 10).until(expected_conditions.title_contains(PHRASE))
    assert PHRASE == result_page.search_input_value()

    for title in result_page.result_link_titles():
        assert PHRASE.lower().split(" ")[0] in title.lower()
