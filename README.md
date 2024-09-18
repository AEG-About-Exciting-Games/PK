# Popcorn Killer (가제)
영화 관련 정보를 제공하는 웹 서비스

영화진흥공단 API를 활용하여, 박스오피스 랭킹 리스트 정보와 각 영화의 출연진, 출연진의 필모그래피를 제공합니다.

## 기술스택
```
- Python 3.10
- Django 4.2
- sqlite 3
```

## 과제
- 회원 인증과 권한 관리
    - [장고 세션 관리](https://docs.djangoproject.com/ko/4.2/topics/http/sessions/#settings)
- Map API 지역 추가
    - Naver Maps API 요금은 2023년부터 아래와 같이 변경되었습니다.
        - 동적 웹 지도(Web Dynamic Map): 무료 -> 월 1000만건 무료, 이후로는 건당 0.1원이 부과됩니다. 
        - 정적 지도(Static Map): 무료 -> 월 300만건 무료, 이후로는 건당 2원이 부과됩니다.
        - 위치 정보로부터 주소를 찾는 지오코딩(Geocoding)과 주소로부터 위치를 찾는 역지오코딩(Reverse Geocoding): 무료 -> 월 300만건 무료, 이후로는 건당 0.5원이 부과됩니다.
    - Kakao Map API 요금은 아래와 같이 변경되었습니다.
        - 무료 -> 1일 300,000회 사용 가능
    - Naver Maps API의 경우, 기본적으로 사용하기 위해서 결제 방식을 등록해야되는 번거로움이 있어, kakao Map API로 적용
    - .env 파일에서 API_KEY를 로드하여 깃허브에 키를 노출하는 것을 감안했지만, 호스팅 시 개발자 모드에서 script의 src단에서 키 확인이 가능하여 보완 필요
        - 리퍼러 제한으로 특정 도메인 요청만 사용가능하도록 설정했지만, 추가 보안 필요
            > 리퍼러 제한이란?
            ```
            리퍼러(Referrer) 제한은 API 제공자(예: Kakao, Google 등)에서 제공하는 보안 기능으로, 특정 도메인에서만 API 키를 사용할 수 있도록 제한하는 방법입니다. 
            리퍼러는 웹 브라우저가 서버에 요청을 보낼 때 요청이 어디에서 왔는지를 나타내는 정보입니다. 
            예를 들어, 사용자가 example.com 페이지에서 다른 서버로 요청을 보낸다면, 해당 요청에 포함된 리퍼러는 example.com이 됩니다.

            리퍼러 제한을 설정하면, 등록된 도메인(리퍼러)에서만 API 키를 사용할 수 있게 되며, 다른 도메인이나 URL에서 API 키를 사용하려고 하면 요청이 차단됩니다.
            ```
        - 그외 API Proxy Server를 고려했으나, 사용자 편의성을 위한 UI (지도)를 제공하지 못하고 JSON 형식으로 제공받아 미적용
