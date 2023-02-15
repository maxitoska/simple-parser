from fake_useragent import UserAgent
import requests
import json

ua = UserAgent()


def collect_data(cat_type=2):
    offset = 0
    items_size = 60
    result = []
    count = 0
    is_data = True

    while is_data:
        for item in range(offset, offset + items_size, 60):

            url = f"https://cs.money/1.0/market/sell-orders?limit=60&maxPrice=" \
                  f"10000&minPrice=2000&offset={item}&type={cat_type}"
            response = requests.get(
                url=url,
                headers={"user-agent": f"{ua.random}"}
            )
            offset += items_size

            data = response.json()

            if data.get("error") == 2:
                return 'Data were collected'

            items = data.get("items")

            for i in items:
                item_3d = {}
                item_screenshot = {}
                item_preview = {}
                if i["pricing"].get("discount") is not None and i["pricing"].get("discount") > 0.2:
                    item_full_name = i["asset"]["names"].get("full")
                    item_steam_image = i["asset"]["images"].get("steam")
                    if "screenshot" in i["asset"]["images"]:
                        item_screenshot = i["asset"]["images"].get("screenshot")
                    if "preview" in i["asset"]["images"]:
                        item_preview = i["asset"]["images"].get("preview")
                    if "3d" in i["links"]:
                        item_3d = i["links"].get("3d")
                    item_price = i["pricing"].get("computed")
                    item_discount = i["pricing"].get("discount")

                    result.append(
                        {
                            "full_name": item_full_name,
                            "steam_image": item_steam_image,
                            "screenshot": item_screenshot,
                            "preview": item_preview,
                            "3d": item_3d,
                            "price": item_price,
                            "discount": item_discount,
                        }
                    )

            count += 1

            if len(items) < 60:
                is_data = False

        with open("result.json", "w", encoding="utf-8") as file:
            json.dump(result, file, indent=4, ensure_ascii=False)


def main():
    collect_data()


if __name__ == "__main__":
    main()
