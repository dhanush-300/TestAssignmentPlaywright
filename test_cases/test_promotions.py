import allure
from web_pages.promotions_page import PromotionsPage


def test_promotions_filters(page):
    promo = PromotionsPage(page)

    promo.open_promotions()

    with allure.step("Verify promo cards visible"):
        assert promo.get_promo_cards() > 0

    categories = ["sports", "casino", "all"]

    for cat in categories:
        with allure.step(f"Apply filter: {cat}"):
            promo.apply_filter(cat)
            assert promo.get_promo_cards() > 0