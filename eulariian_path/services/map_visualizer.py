import folium

def create_map(route):
    """
    Folium을 사용하여 경로를 지도 위에 표시하는 함수.
    """
    start_location = route["legs"][0]["start_location"]
    m = folium.Map(location=[start_location["lat"], start_location["lng"]], zoom_start=15)
    
    # 경로 표시
    for step in route["legs"][0]["steps"]:
        start = step["start_location"]
        end = step["end_location"]
        folium.PolyLine([(start["lat"], start["lng"]), (end["lat"], end["lng"])]).add_to(m)
    
    return m