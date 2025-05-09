import asyncio
from playwright.async_api import async_playwright, Playwright
import datetime

url = input("Website URL: ")


currentTime = datetime.datetime.now()
formattedTime = currentTime.strftime("%d-%m-%Y__%I-%M-%S%p")

async def run(playwright: Playwright):
    devices = ["iPhone 12 Pro", "iPad Mini", "Desktop Chrome"]
    browser = await playwright.chromium.launch() # Chrome

    print("Capturing..")
    
    for deviceName in devices:
        
        device = playwright.devices[deviceName]
        context = await browser.new_context(**device)
        await context.add_init_script(path="helpers.js")
        page = await context.new_page()


        # Wait for the load event (includes images, scripts, etc.)
        await page.wait_for_load_state("load")

        # Wait a bit more to ensure videos/extra JS-loaded content are done
        await page.wait_for_timeout(2000) 

        if deviceName == "Desktop Chrome":
            await page.set_viewport_size({"width": 1920, "height": 1080})
            await page.evaluate("window.setPageZoom(90)")
        
        try:
            await page.goto(url, wait_until='networkidle')
        except Exception as err:
            print(err)
        
        await page.evaluate("window.scrollToBottom()")
    
        page.on("load", await page.screenshot(
            path=f"screenshots/{formattedTime}/{deviceName.replace(' ', '_')}.png", 
            full_page=True, 
            animations="disabled"
        ))
    
        print("✅ " + deviceName + " Captured!")
        await context.close()


    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())
