# DevKor-Hackathon
Hackathon on August 21.

## 프로그램명

* 음식 월드컵을 통한 **음식 추천 시스템**

## 프로그램 개요 
* 웹사이트에서 음식 월드컵을 진행하고 음식 월드컵 결과에 따라 사용자가 좋아할만한 음식을 추천해준다.

## 프로그램 구성

```
template_project
├── dataset
│   ├── FoodLists.csv
│   └── FoodData.csv
├── src
│   ├── Dataset.py
│   ├── Recommender.py
│   └── main.py
└── README.md
```

1. src

* 파이썬 프로그램이 저장될 소스 폴더

2. dataset

* 음식 리스트를 담은 csv 파일이 저장되어 있다.
* 파이썬 코드를 통해 Wikipedia에 있는 음식 데이터를 크롤링하여 만든 자체 Dataset을 csv파일로 저장한다.

## 역할 배정

* 웹사이트 구성 : 이건협
* 추천시스템 및 데이터셋 형성 : 안수진

