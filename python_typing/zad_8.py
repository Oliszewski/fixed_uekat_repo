import requests
import argparse


class Brewery:
    def __init__(self, name: str, city: str, state: str, brewery_type: str):
        self.name = name
        self.city = city
        self.state = state
        self.brewery_type = brewery_type

    def __str__(self) -> str:
        return f"🍺 {self.name} | City: {self.city}, {self.state} | Type: {self.brewery_type}"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--city", type=str, help="Filter breweries by city")
    args = parser.parse_args()

    url = "https://api.openbrewerydb.org/v1/breweries"
    params = {"per_page": 20}

    if args.city:
        params["by_city"] = args.city

    try:
        response = requests.get(url, params=params)
        data = response.json()

        brewery_list = []

        for item in data:
            b = Brewery(
                name=item.get("name", "Unknown"),
                city=item.get("city", "Unknown"),
                state=item.get("state_province", "Unknown"),
                brewery_type=item.get("brewery_type", "Unknown"),
            )
            brewery_list.append(b)

        print(f"Found {len(brewery_list)} breweries:")
        for brewery in brewery_list:
            print(brewery)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
