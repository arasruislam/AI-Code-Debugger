# File: components/ui.py
from typing import Optional, Tuple
import streamlit as st
from PIL import Image

from config.settings import (
    PAGE_TITLE,
    PAGE_ICON,
    ALLOWED_IMAGE_TYPES,
    RESPONSE_OPTIONS,
)


def setup_page() -> None:
    """Configures the Streamlit page and renders the header."""
    st.set_page_config(
        page_title=PAGE_TITLE,
        page_icon=PAGE_ICON,
        layout="centered",
    )
    st.title("🐞 AI Code Error Debugger")
    st.write(
        "আপনার কোডের এরর স্ক্রিনশট আপলোড করুন অথবা কোড পেস্ট করুন। "
        "Gemini API বাগ খুঁজে বের করে সমাধান বা হিন্টস দিয়ে সাহায্য করবে।"
    )


def render_input_section() -> Tuple[Optional[Image.Image], str]:
    """Renders the file uploader (PNG, JPG, JPEG) and code paste text area."""
    st.subheader("১. কোড অথবা এরর স্ক্রিনশট দিন")

    uploaded_file = st.file_uploader(
        "কোড এরর-এর স্ক্রিনশট আপলোড করুন (PNG, JPG, JPEG):",
        type=ALLOWED_IMAGE_TYPES,
    )

    loaded_image = None
    if uploaded_file is not None:
        loaded_image = Image.open(uploaded_file)
        st.image(loaded_image, caption="আপলোড করা স্ক্রিনশট", use_container_width=True)

    code_input = st.text_area(
        "অথবা এখানে আপনার কোড / এরর মেসেজ পেস্ট করুন:",
        height=180,
        placeholder="আপনার কোড বা এরর ট্রেসব্যাক এখানে পেস্ট করুন...",
    )

    return loaded_image, code_input


def render_option_bar() -> Optional[str]:
    """Renders the option bar for selecting 'Hints' or 'Solution with code'."""
    st.subheader("২. রেসপন্স টাইপ সিলেক্ট করুন")

    selected_option = st.radio(
        "আপনি কীভাবে সমাধান পেতে চান?",
        options=RESPONSE_OPTIONS,
        index=None,
        horizontal=True,
    )
    return selected_option


def render_response(response_type: str, markdown_text: str) -> None:
    """Displays the debugging result formatted with st.markdown()."""
    st.subheader(f"✅ ফলাফল ({response_type})")
    st.markdown(markdown_text)
