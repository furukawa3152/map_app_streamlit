import streamlit as st
import streamlit_folium
import folium
# ページ設定
st.set_page_config(
    page_title="streamlit-foliumテスト",
)

# 地図の中心の緯度/経度、タイル、初期のズームサイズを指定します。
m = folium.Map(
    # 地図の中心位置の指定(今回は栃木県の県庁所在地を指定)
    location=[33.2928452, 130.297359],
    # タイル、アトリビュートの指定
    tiles="OpenStreetMap",
    # ズームを指定
    zoom_start=10
)

folium.Marker(
    # 緯度と経度を指定pip
    location=[33.2928452, 130.297359],
    # ツールチップの指定
    tooltip="my_home",
    # ポップアップの指定
    popup=folium.Popup("yeah!!", max_width=300),
    # アイコンの指定(アイコン、色)
    icon=folium.Icon(icon="home",icon_color="white", color="red")
).add_to(m)

st_data = streamlit_folium.st_folium(m, width=1200, height=800)