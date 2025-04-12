import asyncio
from playwright.async_api import async_playwright, Playwright

url = "https://samewaterjet.com.au/"

async def scroll_to_bottom(page):
    await page.evaluate("""
        () => {
            return new Promise((resolve) => {
                let totalHeight = 0;
                const distance = 100;
                const timer = setInterval(() => {
                    const scrollHeight = document.body.scrollHeight;
                    window.scrollBy(0, distance);
                    totalHeight += distance;

                    if (totalHeight >= scrollHeight) {
                        clearInterval(timer);
                        resolve();
                    }
                }, 100);
            });
        }
    """)
    await page.wait_for_timeout(1000)  # wait for animations

async def run(playwright: Playwright):
    devices = ["iPhone 12 Pro", "iPad Pro 11", "Desktop Chrome"]
    browser = await playwright.webkit.launch()

    for device_name in devices:
        device = playwright.devices[device_name]
        context = await browser.new_context(**device)
        page = await context.new_page()
        await page.goto(url)
        await scroll_to_bottom(page)
        page.on("domcontentloaded", await page.screenshot(path=f"{device_name.replace(' ', '_')}.png", full_page=True, animations="disabled") )
        # await page.screenshot(path=f"{device_name.replace(' ', '_')}.png", full_page=True, animations="disabled")
        print(device_name)
        await context.close()

    # Desktop screenshot without device emulation
    # context = await browser.new_context()
    # page = await context.new_page()
    # await page.goto(url)
    # await scroll_to_bottom(page)
    # await page.screenshot(path="Desktop_Chrome.png", full_page=True, animations="disabled")
    # print("Desktop")
    # await context.close()

    await browser.close()

async def main():
    async with async_playwright() as playwright:
        
        await run(playwright)

asyncio.run(main())
