# 필요한 라이브러리 임포트
import requests
from bs4 import BeautifulSoup
import csv

file = open('movie.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow(['영화 제목', '평점', '이미지 주소', '감독', '출연자', '개봉일자'])

# URL 가져와서 파싱
MOVIE_URL = f'https://movie.naver.com/movie/running/current.nhn'
movie_html = requests.get(MOVIE_URL)
movie_soup = BeautifulSoup(movie_html.text, 'html.parser')

# 영화 목록에 접근
movie_list_box = movie_soup.find('ul', {'class': 'lst_detail_t1'})
movie_list = movie_list_box.find_all('li')

# 영화 목록에서 원하는 정보를 추출
final_result = []
for movie in movie_list:
    title = movie.find('dt', {'class': 'tit'}).find('a').text
    score = movie.find('dd', {'class': 'star'}).find('div', {'class': 'star_t1'}).find('span', {'class': 'num'}).text
    img_address = movie.find('div', {'class': 'thumb'}).find('img')['src']
    director = movie.find('dl', {'class': 'info_txt1'}).find_all('span', {'class': 'link_txt'})[1].find('a').text
    # 출연자가 있는 영화와 없는 영화의 차이 반영
    if len(movie.find('dl', {'class': 'info_txt1'}).find_all('span', {'class': 'link_txt'})) < 3:
        actors = None
    else:
        movie_actors = movie.find('dl', {'class': 'info_txt1'}).find_all('span', {'class': 'link_txt'})[2].find_all('a')
        actor_list = []
        for actor in range(len(movie_actors)):
            actor_list.append(movie_actors[actor].text)
        actors = ', '.join(actor_list)

    released_date = movie.find('dl', {'class': 'info_txt1'}).find('dd').text.strip()[-13:-3]

    movie_info = {
        '영화 제목': title,
        '평점': score,
        '이미지 주소': img_address,
        '감독': director,
        '출연자': actors,
        '개봉일자': released_date
    }
    final_result.append(movie_info)

for result in final_result:
    row = []
    row.append(result['영화 제목'])
    row.append(result['평점'])
    row.append(result['이미지 주소'])
    row.append(result['감독'])
    row.append(result['출연자'])
    row.append(result['개봉일자'])
    writer.writerow(row)