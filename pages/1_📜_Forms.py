import streamlit as st

st.set_page_config(page_title="Unicorn's \u2022 Forms", page_icon="📜")
st.sidebar.success("Navigate to other pages here")

st.markdown("""
# Available Forms
- [Pets Form](https://forms.gle/pkCsruRwu4LAN8nP8)
""")


def set_page_title(title):
    st.sidebar.markdown(unsafe_allow_html=True, body=f"""
        <iframe height=0 srcdoc="<script>
            const title = window.parent.document.querySelector('title') \

            const oldObserver = window.parent.titleObserver
            if (oldObserver) {{
                oldObserver.disconnect()
            }} \

            const newObserver = new MutationObserver(function(mutations) {{
                const target = mutations[0].target
                if (target.text !== '{title}') {{
                    target.text = '{title}'
                }}
            }}) \

            newObserver.observe(title, {{ childList: true }})
            window.parent.titleObserver = newObserver \

            title.text = '{title}'
        </script>" />
    """)


set_page_title("Unicorn's \u2022 Forms")
