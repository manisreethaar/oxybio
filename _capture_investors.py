from playwright.sync_api import sync_playwright
import time
import os

def capture_screenshots():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={'width': 1440, 'height': 900})
        # Navigate to the local server
        page.goto('http://localhost:8765/investors.html')
        time.sleep(2)  # Wait for CSS animations to settle
        
        # 1. Hero Section
        page.screenshot(path='investors_hero_redesign.png')
        
        # 2. Opportunity / Chart Section
        page.evaluate('window.scrollTo(0, 800)')
        time.sleep(1)
        page.screenshot(path='investors_opportunity_redesign.png')
        
        # 3. Competitor Table
        page.evaluate('window.scrollTo(0, 1600)')
        time.sleep(1)
        page.screenshot(path='investors_competitors_redesign.png')
        
        # 4. Ask Section
        page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(1)
        page.screenshot(path='investors_ask_redesign.png')
        
        browser.close()
        print("Screenshots captured successfully.")

if __name__ == "__main__":
    capture_screenshots()
