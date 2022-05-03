# REST API란
## 정의 & 특징
- REST(Representational State Transfer): 각 자원에 대하여 자원의 상태에 대한 정보를 주고받는 개발방식
- API: 프로그램이 상호작용하기 위한 인터페이스
- 서버와 클라이언트가 상호작용을 하려면 이를 연결하는 인터페이스가 필요한데 이러한 인터페이스를 API라 한다.
- REST API: REST 아키텍처를 따르는 API를 의미.
- 클라이언트 입장에서 REST API 호출이란: REST 방식을 따르고 있는 서버에 특정한 요청을 보내서 데이터를 가져오는 것을 의미

## REST 구성 요소
1. 자원(resource): URI를 이용하여 표현
2. 행위(Verb): HTTP 메서드를 이용하여 표현
3. 표현(representations)

# JSON
- JavaScript Object Notation
- 데이터를 주고받는 데 사용하는 경량의 데이터 형식
- REST API를 사용할 때, 데이터의 형식으로는 일반적으로 JSON을 사용
- key-value 쌍으로 이루어진 데이터 객체를 저장
- 파싱(parsing): 특정한 형식으로 저장된 데이터에 접근하여 원하는 정보만 찾아서 가공하는 작업

## json 형식을 따르는 데이터 예시
```json
{
  "id": "gildong",
  "password": "192837",
  "age": 30,
  "hobby": ["football", "programming"]
}
```

# 출처 & 깃허브
[이것이 취업을 위한 코딩 테스트다 with python](http://www.yes24.com/Product/Goods/91433923)

[github](https://github.com/KYUSEONGHAN/python-for-coding-test)