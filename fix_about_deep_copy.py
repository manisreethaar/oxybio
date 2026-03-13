import traceback

def update_about_page():
    try:
        with open(r'e:\OXYBIO\about.html', 'r', encoding='utf-8') as f:
            content = f.read()

        original = content

        # Re-aligning the "Clinical Data" Stat on About page
        content = content.replace(
            "Peer-reviewed nutritional diagnostics analyzed",
            "Peer-reviewed food science & fermentation journals analyzed"
        )
        content = content.replace(
            "Clinical Data",
            "Food Science Data"
        )

        # Re-aligning Chapter 1 Intro text
        content = content.replace(
            "CHAPTER 01",
            "CHAPTER 01: THE ORIGIN"
        )
        content = content.replace(
            "We spent six months trying to find a daily nutrition",
            "We spent six months trying to find an on-the-go functional"
        )

        if content != original:
            with open(r'e:\OXYBIO\about.html', 'w', encoding='utf-8') as f:
                f.write(content)
            print("Successfully updated about.html deep copy")
        else:
            print("No changes needed or strings not found in about.html")

    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()

update_about_page()
