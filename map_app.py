import streamlit as st
from streamlit_folium import folium_static
import folium
from geopy.geocoders import Nominatim
# ページ設定
st.set_page_config(
    page_title="streamlit-foliumテスト",
)
with st.form("my_form", clear_on_submit=False):
    address = st.text_input('住所を入力してください')
    submitted = st.form_submit_button("地図を出力")

if submitted:
    geocoder = Nominatim(user_agent="hagakure_pgm")
    location = geocoder.geocode(address)
    lat,lng = (location.latitude,location.longitude)
    # 地図の中心の緯度/経度、タイル、初期のズームサイズを指定します。
    m = folium.Map(
        # 地図の中心位置の指定(今回は栃木県の県庁所在地を指定)
        location=[lat,lng],
        # タイル、アトリビュートの指定
        tiles="OpenStreetMap",
        # ズームを指定
        zoom_start=10
    )

    folium.Marker(
        # 緯度と経度を指定pip
        location=[lat,lng],
        # ツールチップの指定
        tooltip="my_home",
        # ポップアップの指定
        popup=folium.Popup("yeah!!", max_width=300),
        # アイコンの指定(アイコン、色)
        icon=folium.Icon(icon="home",icon_color="white", color="red")
    ).add_to(m)

    st_data = folium_static(m, width=800, height=800)