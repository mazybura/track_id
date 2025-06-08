from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import os
import logging
from datetime import datetime
from selenium import webdriver
from pathlib import Path


class Config:
    download_base_dir = str(Path.home() / "Downloads")


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[logging.FileHandler("download_log.log"), logging.StreamHandler()],
    )


def configure_driver(download_dir):
    options = webdriver.ChromeOptions()
    options.add_experimental_option(
        "prefs",
        {
            "download.default_directory": download_dir,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,
        },
    )

    options.add_argument("--headless=new")
    options.add_argument("start-maximized")

    return webdriver.Chrome(options=options)


def create_unique_download_folder(base_dir):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    folder_name = f"downloads_{timestamp}"
    download_path = os.path.join(base_dir, folder_name)

    os.makedirs(download_path, exist_ok=True)
    logging.info(f"Created download folder: {download_path}")
    return download_path


def download_song(driver, song_name):
    try:
        driver.get("https://2024.myfreemp3juices.cc/")
        logging.info(f"Searching for: {song_name}")

        search_input_xpath = "/html/body/div[3]/div[1]/div/div[3]/input"
        search_input = wait_for_element(driver, (By.XPATH, search_input_xpath))
        search_input.send_keys(song_name)

        search_button_xpath = "/html/body/div[3]/div[1]/div/span/button"
        search_button = driver.find_element(By.XPATH, search_button_xpath)
        search_button.click()

        download_button_xpath = "/html/body/div[3]/div[3]/div[2]/li[1]/div/a[3]"
        download_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, download_button_xpath))
        )
        download_button.click()
        logging.info(f"Download button clicked for {song_name}")

        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

        new_window = driver.window_handles[-1]
        driver.switch_to.window(new_window)
        logging.info(f"Switched to new window for {song_name}")

        download_mp3_button_xpath = "/html/body/div[2]/div/div[2]/button"
        download_mp3_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, download_mp3_button_xpath))
        )
        download_mp3_button.click()
        logging.info(f"Final download button clicked for {song_name}")

        time.sleep(20)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    except NoSuchElementException as e:
        logging.error(f"Element not found for {song_name}: {e}")
    except TimeoutException as e:
        logging.error(f"Timeout for {song_name}: {e}")
    except Exception as e:
        logging.error(f"Unexpected error for {song_name}: {e}")


def wait_for_element(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )
