from selene import by, be, browser
from selene.support.shared.jquery_style import s


def test_github():
    browser.open("https://github.com")

    s(".header-search-button").click()
    s("#query-builder-test").send_keys("eroshenkoam/allure-example")
    s("#query-builder-test").press_enter()
    s(by.link_text("eroshenkoam/allure-example")).click()
    s("#issues-tab").click()

    s(by.partial_text("#76")).should(be.visible)
