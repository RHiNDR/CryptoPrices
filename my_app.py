import streamlit as st
from streamlit_autorefresh import st_autorefresh

from BTCprices import BTC

def main():
    # Assuming data is your list of dictionaries
    data = BTC()
    inner_dict = data[0]

    keys = inner_dict.keys()
    values = inner_dict.values()
    values_list = list(values)

    with st.container(height=350):
        st.markdown("<h1 style='text-align: center; color: black;'>BTC AUD PRICES</h1>", unsafe_allow_html=True)
        for i, key in enumerate(keys):
            st.link_button(key + ": $" + str(values_list[i][0]), str(values_list[i][1]), use_container_width=True)
    
    st_autorefresh(interval=10000)

if __name__ == "__main__":
    main()