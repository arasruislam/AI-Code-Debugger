# File: app.py
import streamlit as st

from config.settings import API_KEY
from components.ui import (
    setup_page,
    render_input_section,
    render_option_bar,
    render_response,
)
from services.gemini_service import analyze_code_error


def main() -> None:
    # 1. Setup page & header
    setup_page()

    # 2. Render input section (Screenshot upload & Code paste)
    uploaded_image, code_input = render_input_section()

    # 3. Render option bar ("Hints" / "Solution with code")
    response_type = render_option_bar()

    # 4. "Debug Code" button — nothing is displayed unless clicked
    if st.button("Debug Code", type="primary", use_container_width=True):
        has_input = (uploaded_image is not None) or bool(code_input.strip())
        has_type = response_type is not None

        # Validate inputs and show warning via st.error()
        if not has_input and not has_type:
            st.error(
                "⚠️ অনুগ্রহ করে কোডের স্ক্রিনশট আপলোড (অথবা কোড পেস্ট) করুন "
                "এবং একটি অপশন ('Hints' বা 'Solution with code') সিলেক্ট করুন!"
            )
        elif not has_input:
            st.error(
                "⚠️ অনুগ্রহ করে একটি স্ক্রিনশট ইমেজ (PNG, JPG, JPEG) আপলোড করুন "
                "অথবা আপনার কোড পেস্ট করুন!"
            )
        elif not has_type:
            st.error(
                "⚠️ অনুগ্রহ করে অপশন বার থেকে 'Hints' অথবা 'Solution with code' সিলেক্ট করুন!"
            )
        elif not API_KEY:
            st.error(
                "⚠️ `.env` ফাইলে `GEMINI_API_KEY` পাওয়া যায়নি। "
                "অনুগ্রহ করে `.env` ফাইলে আপনার API Key যুক্ত করুন।"
            )
        else:
            # Call Gemini API with st.spinner()
            with st.spinner(
                "🔍 Gemini আপনার কোড বিশ্লেষণ করছে... অনুগ্রহ করে অপেক্ষা করুন..."
            ):
                try:
                    result_markdown = analyze_code_error(
                        api_key=API_KEY,
                        response_type=response_type,
                        code_input=code_input,
                        image=uploaded_image,
                    )
                    render_response(response_type, result_markdown)
                except Exception as exc:
                    st.error(f"❌ API কলের সময় একটি সমস্যা হয়েছে: {exc}")


if __name__ == "__main__":
    main()
