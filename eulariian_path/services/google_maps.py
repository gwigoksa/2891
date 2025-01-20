import requests

# API 키를 직접 코드에 입력
API_KEY = "AIzaSyC1CJ45nTcFRVGsPtd10aE98RlNOtB53gY"

def get_coordinates(address):
    """
    주소를 위도와 경도로 변환하는 함수
    """
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={API_KEY}"
    response = requests.get(url).json()
    if response["status"] == "OK":
        location = response["results"][0]["geometry"]["location"]
        return location["lat"], location["lng"]
    else:
        raise Exception(f"주소 변환 실패: {response.get('error_message', '원인 불명')}")

def get_directions(start_lat, start_lng, end_lat, end_lng):
    url = (
        f"https://maps.googleapis.com/maps/api/directions/json?"
        f"origin={start_lat},{start_lng}&destination={end_lat},{end_lng}&mode=walking&key={API_KEY}"
    )
    print("요청 URL:", url)
    response = requests.get(url).json()
    print("Directions API 응답 데이터:", response)  # 응답 데이터를 출력하여 상태 확인
    if response["status"] == "OK":
        return response["routes"][0]
    elif response["status"] == "ZERO_RESULTS":
        raise Exception("경로를 찾을 수 없습니다. 도보 경로가 없을 수 있습니다.")
    else:
        raise Exception(f"경로 계산 실패: {response.get('error_message', response.get('status'))}")