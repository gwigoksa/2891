import streamlit as st
from services.google_maps import get_coordinates, get_directions
from services.map_visualizer import create_map
from streamlit_folium import st_folium

# 페이지 기본 설정
st.set_page_config(page_title="해운대구 장애인 도보 경로 추천", page_icon="🗺️", layout="wide")

# 로고 및 제목
st.image("assets/logo.png", width=200)
st.title("해운대구 장애인 도보 경로 추천 웹사이트")
st.markdown("### 출발지와 목적지를 입력하여 장애인 친화적인 도보 경로를 확인하세요!")

# 사용자 입력 섹션
col1, col2 = st.columns(2)

with col1:
    start_address = st.text_input("출발지 주소", "부산광역시 해운대구 장산역")
with col2:
    end_address = st.text_input("목적지 주소", "부산광역시 해운대구 중동역")

disability_type = st.selectbox("장애 유형", ["휠체어 사용자", "시각 장애인", "청각 장애인"])

if st.button("경로 추천"):
    try:
        # 좌표 확인
        start_lat, start_lng = get_coordinates(start_address)
        end_lat, end_lng = get_coordinates(end_address)
        st.write(f"출발지 좌표: {start_lat}, {start_lng}")
        st.write(f"목적지 좌표: {end_lat}, {end_lng}")
        
        # 경로 확인
        route = get_directions(start_lat, start_lng, end_lat, end_lng)
        st.write("추천 경로:", route)
        
        # 지도 표시
        m = create_map(route)
        st_folium(m, width=800, height=500)
    except Exception as e:
        st.error(f"오류 발생: {e}")