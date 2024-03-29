from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

from collection import crawler


def ex01():
    request = Request('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')

    response = urlopen(request)

    html = response.read().decode('cp949');
    bs = BeautifulSoup(html, 'html.parser')
    divs = bs.findAll('div', attrs={'class':'tit3'})
    for index, div in enumerate(divs):
        print(index + 1, div.a.text, div.a['href'], sep=':')

def proc_naver_movie_rank(data):
    bs = BeautifulSoup(data, 'html.parser')
    results = bs.findAll('div', attrs={'class': 'tit3'})
    return results

def store_naver_movie_rank(data):
    # output
    for index, div in enumerate(data):
        print(index + 1, div.a.text, div.a['href'], sep=':')
    return data

def error(e):
    pass

def ex02():
    # fetch
    crawler.crawling(
        url='https://movie.naver.com/movie/sdb/rank/rmovie.nhn',
        encoding='cp949',
        proc1=proc_naver_movie_rank,
        proc2=lambda data: list(map(lambda t: print(t[0] + 1, t[1].a.text, t[1].a['href'], sep=':'), enumerate(data))),
        err=error
    )

def ex03():
    html = crawler.crawling(
        url='https://movie.naver.com/movie/sdb/rank/rmovie.nhn',
        encoding='cp949',
        proc=proc_naver_movie_rank()
    )


__name__ == '__main__' and not ex01() and not ex02()


