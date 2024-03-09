import streamlit as st
from streamlit_autorefresh import st_autorefresh

from BTCprices import BTC
from ETHprices import ETH
from USDTprices import USDT

def main():
    bitcoin()
    ethereum()
    usdt()
    st_autorefresh(interval=10000)


def bitcoin():
    # Assuming data is your list of dictionaries
    data = BTC()
    inner_dict = data[0]

    keys = inner_dict.keys()
    values = inner_dict.values()
    values_list = list(values)

    with st.container(height=400):
        st.markdown("<h1 style='text-align: center; color: black;'>BTC AUD PRICES</h1>", unsafe_allow_html=True)
        for i, key in enumerate(keys):
            st.link_button(key + ": $" + str((values_list[i][0])), str(values_list[i][1]), use_container_width=True)
        st.link_button("Spread: $" + str(round((values_list[3][0])-(values_list[0][0]), 2)), 'https://ozcryptoprices.streamlit.app/', use_container_width=True)

def ethereum():
    # Assuming data is your list of dictionaries
    data = ETH()
    inner_dict = data[0]

    keys = inner_dict.keys()
    values = inner_dict.values()
    values_list = list(values)

    with st.container(height=400):
        st.markdown("<h1 style='text-align: center; color: black;'>ETH AUD PRICES</h1>", unsafe_allow_html=True)
        for i, key in enumerate(keys):
            st.link_button(key + ": $" + str((values_list[i][0])), str(values_list[i][1]), use_container_width=True)
        st.link_button("Spread: $" + str(round((values_list[3][0])-(values_list[0][0]), 2)), 'https://ozcryptoprices.streamlit.app/', use_container_width=True)

def usdt():
    # Assuming data is your list of dictionaries
    data = USDT()
    inner_dict = data[0]

    keys = inner_dict.keys()
    values = inner_dict.values()
    values_list = list(values)

    with st.container(height=400):
        st.markdown("<h1 style='text-align: center; color: black;'>USDT AUD PRICES</h1>", unsafe_allow_html=True)
        for i, key in enumerate(keys):
            st.link_button(key + ": $" + str((values_list[i][0])), str(values_list[i][1]), use_container_width=True)
        st.link_button("Spread: $" + str(round((values_list[3][0])-(values_list[0][0]), 2)), 'https://ozcryptoprices.streamlit.app/', use_container_width=True)


if __name__ == "__main__":
    main()