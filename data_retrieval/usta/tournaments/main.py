"""A script that retrieves USTA tournament data."""
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# from dates import Dates
# from event import Event
# from facility import Facility
# from tournament import Tournament


def main():
    """
    Retrieve information on USTA tournaments.

    Returns
    -------
    None
    """
    # Example of creating a tournament
    # f = Facility(
    #     name="La Jolla Tennis Club",
    #     address="7632 Draper Ave, La Jolla, CA, 92037",
    #     district="SAN_DIEGO",
    #     section="SOUTHERN_CALIFORNIA",
    # )

    # d = Dates("2024-04-13", "2024-04-14")

    # e = [Event("DOUBLES", 4.5, "WOMEN", 30, 9), Event("DOUBLES", 4.5, "MIXED", 30, 6)]

    # t = Tournament(
    #     name="Level 5 Open: SoCal NTRP Tour 750, La Jolla (Doubles)",
    #     category="ADULT",
    #     level=5,
    #     facility=f,
    #     status="OPEN",
    #     dates=d,
    #     events=e,
    # )

    # tournaments = [t]
    # for ind, tourney in enumerate(tournaments):
    #     print(f"----- Tournament {ind+1} -----\n{tourney}")

    # Set up Chrome options to block location requests
    chrome_options = webdriver.ChromeOptions()
    prefs = {
        "profile.default_content_setting_values.geolocation": 2  # 1: allow, 2: block
    }
    chrome_options.add_experimental_option("prefs", prefs)

    # Set up the Selenium WebDriver with Chrome options
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    url = (
        "https://playtennis.usta.com/tournaments?panel=section"
        "&level-category=adult&organisation-group=6f20620d-90b5-4a74-bf20-18b0cdd90f98"
    )

    try:
        # Open the webpage
        driver.get(url)

        # Wait for the page to load completely
        time.sleep(5)

        # Click the search button
        try:
            search_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "button-text"))
            )
            search_button.click()
        except Exception as e:
            print("Search button not found or error:", e)

        # Wait for the results to load
        time.sleep(5)

        path = (
            "//div[@class='csa-show-more-wrap']//"
            "button[contains(text(), 'Show more results')]"
        )
        # Click the "Show more results" button until it is no longer present
        while True:
            try:
                show_more_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, path))
                )
                show_more_button.click()
                time.sleep(5)  # Wait for new results to load
            except Exception:
                break

        # Extract the page source
        page_source = driver.page_source

        # Parse the page source with BeautifulSoup
        soup = BeautifulSoup(page_source, "html.parser")

        # Find and extract the list of tournaments
        results = soup.find("div", class_="csa-results")
        tournaments = results.find_all("div", class_="csa-search-result-item")

        print(f"{len(tournaments)} found")

        # Loop through the tournaments and print their details
        for tournament in tournaments:
            descriptions = tournament.find_all("div", class_="csa-description")
            title = descriptions[0].find("h3", class_="csa-title").text.strip()
            print(f"Title: {title}")

            a_tag = tournament.find("a")
            title = a_tag.text.strip()
            url = a_tag["href"]
            print(f"URL: {url}")

            address = descriptions[0].find("p", class_="csa-location").text.strip()
            print(f"Address: {address}")

            dates = descriptions[0].find("li", class_="csa-date-v2").text.strip()
            print(f"Address: {dates}")

            registration = descriptions[1].find("div", class_="csa-registration")
            registration_status = registration.find(
                "p", class_="csa-status"
            ).text.strip()
            print(f"Registration Status: {registration_status}")

            print("-" * 20)
    finally:
        # Close the WebDriver
        driver.quit()


if __name__ == "__main__":
    main()
