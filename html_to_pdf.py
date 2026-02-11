import asyncio
import os
from playwright.async_api import async_playwright

async def convert_html_to_pdf():
    # Get all HTML files in the current directory
    current_dir = os.getcwd()
    files = [f for f in os.listdir(current_dir) if f.endswith('.html')]
    
    if not files:
        print("No HTML files found in the current directory.")
        return

    print(f"Found {len(files)} HTML files to convert.")

    async with async_playwright() as p:
        try:
            # Launch the browser
            # headless=True means the browser will run in the background
            browser = await p.chromium.launch(headless=True)
        except Exception as e:
            print("\nError launching browser:")
            print(e)
            print("\nIt seems the browser binaries are missing or failed to launch.")
            print("Please try running: playwright install chromium")
            return

        page = await browser.new_page()

        for filename in files:
            html_path = os.path.join(current_dir, filename)
            pdf_filename = filename.replace('.html', '.pdf')
            pdf_path = os.path.join(current_dir, pdf_filename)
            
            print(f"Converting '{filename}' to '{pdf_filename}'...")
            
            try:
                # 'file://' prefix is needed for local files
                file_url = f"file:///{html_path.replace(os.sep, '/')}"
                
                await page.goto(file_url, wait_until="networkidle")
                
                # generate pdf
                # format='A4' is standard, you can change to 'Letter' or customize width/height
                # print_background=True ensures converting background colors/images
                await page.pdf(path=pdf_path, format="A4", print_background=True)
                
                print(f"Success: {pdf_filename}")
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")

        await browser.close()
        print("\nConversion completed!")

if __name__ == "__main__":
    # installing the browsers is required before running this script
    # command: playwright install chromium
    asyncio.run(convert_html_to_pdf())
