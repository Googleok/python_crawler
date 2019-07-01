from bs4 import BeautifulSoup

html = '''<td class="title black">
<div class="tit3" id = "my-div" >
<a href="/movie/bi/mi/basic.nhn?code=161967" title="기생충">기생충</a>
</div>
</td>'''

html2 = '''
<tbody>
				<tr><td colspan="8" class="blank01"></td></tr>
				<!-- 예제
				<tr>
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g50.gif" alt="50" width="14" height="13"></td>
					<td class="title"><a href="#">트랜스포머</a></td>
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_down_1.gif" alt="down" width="7" height="10"></td>
					<td class="range ac">7</td>
				</tr>
				-->
				
				<tr>
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_r01.gif" alt="01" width="14" height="13"></td>
					
						
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=161967" title="기생충">기생충</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_na_1.gif" alt="na" width="7" height="10" class="arrow"></td>
					<td class="range ac">0</td>
					
					
				</tr>
					
					
				
				<tr>
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_r02.gif" alt="02" width="14" height="13"></td>
					
						
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=163788" title="알라딘">알라딘</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_na_1.gif" alt="na" width="7" height="10" class="arrow"></td>
					<td class="range ac">0</td>
					
					
				</tr>
					
					
				
				<tr>
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_r03.gif" alt="03" width="14" height="13"></td>
					
						
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=97631" title="맨 인 블랙: 인터내셔널">맨 인 블랙: 인터내셔널</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_na_1.gif" alt="na" width="7" height="10" class="arrow"></td>
					<td class="range ac">0</td>
					
					
				</tr>
					
					
				
				<tr>
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_r04.gif" alt="04" width="14" height="13"></td>
					
						
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=164125" title="엑스맨: 다크 피닉스">엑스맨: 다크 피닉스</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_na_1.gif" alt="na" width="7" height="10" class="arrow"></td>
					<td class="range ac">0</td>
					
					
				</tr>
					
					
				
				<tr>
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_r05.gif" alt="05" width="14" height="13"></td>
					
						
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=177371" title="0.0MHz">0.0MHz</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_na_1.gif" alt="na" width="7" height="10" class="arrow"></td>
					<td class="range ac">0</td>
					
					
				</tr>
					
					
				
				<tr>
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_r06.gif" alt="06" width="14" height="13"></td>
					
						
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=183836" title="천로역정: 천국을 찾아서">천로역정: 천국을 찾아서</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">3</td>
					
					
				</tr>
					
					
				
				<tr>
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_r07.gif" alt="07" width="14" height="13"></td>
					
						
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=181704" title="로켓맨">로켓맨</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_down_1.gif" alt="down" width="7" height="10" class="arrow"></td>
					<td class="range ac">1</td>
					
					
				</tr>
					
					
				
				<tr>
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_r08.gif" alt="08" width="14" height="13"></td>
					
						
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=136900" title="어벤져스: 엔드게임">어벤져스: 엔드게임</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_na_1.gif" alt="na" width="7" height="10" class="arrow"></td>
					<td class="range ac">0</td>
					
					
				</tr>
					
					
				
				<tr>
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_r09.gif" alt="09" width="14" height="13"></td>
					
						
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=18781" title="이웃집 토토로">이웃집 토토로</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_down_1.gif" alt="down" width="7" height="10" class="arrow"></td>
					<td class="range ac">2</td>
					
					
				</tr>
					
					
				
				<tr>
					
						
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_r10.gif" alt="010" width="14" height="13"></td>
						
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=179125" title="롱 리브 더 킹: 목포 영웅">롱 리브 더 킹: 목포 영웅</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">1</td>
					
					
				</tr>
					
					
						<tr><td colspan="8" class="line01"></td></tr>
					
				
				<tr>
					
						
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g11.gif" alt="11" width="14" height="13"></td>
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=180169" title="어린 의뢰인">어린 의뢰인</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">1</td>
					
					
				</tr>
					
					
				
				<tr>
					
						
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g12.gif" alt="12" width="14" height="13"></td>
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=167053" title="업사이드">업사이드</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">1</td>
					
					
				</tr>
					
					
				
				<tr>
					
						
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g13.gif" alt="13" width="14" height="13"></td>
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=177967" title="악인전">악인전</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_down_1.gif" alt="down" width="7" height="10" class="arrow"></td>
					<td class="range ac">3</td>
					
					
				</tr>
					
					
				
				<tr>
					
						
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g14.gif" alt="14" width="14" height="13"></td>
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=101966" title="토이 스토리 4">토이 스토리 4</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_na_1.gif" alt="na" width="7" height="10" class="arrow"></td>
					<td class="range ac">0</td>
					
					
				</tr>
					
					
				
				<tr>
					
						
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g15.gif" alt="15" width="14" height="13"></td>
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=137865" title="세상을 바꾼 변호인">세상을 바꾼 변호인</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_na_1.gif" alt="na" width="7" height="10" class="arrow"></td>
					<td class="range ac">0</td>
					
					
				</tr>
					
					
				
				<tr>
					
						
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g16.gif" alt="16" width="14" height="13"></td>
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=139673" title="여교사">여교사</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">2</td>
					
					
				</tr>
					
					
				
				<tr>
					
						
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g17.gif" alt="17" width="14" height="13"></td>
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=183132" title="교회오빠">교회오빠</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_down_1.gif" alt="down" width="7" height="10" class="arrow"></td>
					<td class="range ac">1</td>
					
					
				</tr>
					
					
				
				<tr>
					
						
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g18.gif" alt="18" width="14" height="13"></td>
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=97672" title="노리개: 그녀의 눈물">노리개: 그녀의 눈물</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">1</td>
					
					
				</tr>
					
					
				
				<tr>
					
						
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g19.gif" alt="19" width="14" height="13"></td>
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=181698" title="존 윅 3: 파라벨룸">존 윅 3: 파라벨룸</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">2</td>
					
					
				</tr>
					
					
				
				<tr>
					
						
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g20.gif" alt="20" width="14" height="13"></td>
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=174065" title="걸캅스">걸캅스</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_down_1.gif" alt="down" width="7" height="10" class="arrow"></td>
					<td class="range ac">3</td>
					
					
				</tr>
					
					
						<tr><td colspan="8" class="line01"></td></tr>
					
				
				<tr>
					
						
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g21.gif" alt="21" width="14" height="13"></td>
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=175322" title="마녀">마녀</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">7</td>
					
					
				</tr>
					
					
				
				<tr>
					
						
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g22.gif" alt="22" width="14" height="13"></td>
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=173123" title="스파이더맨: 파 프롬 홈">스파이더맨: 파 프롬 홈</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_na_1.gif" alt="na" width="7" height="10" class="arrow"></td>
					<td class="range ac">0</td>
					
					
				</tr>
					
					
				
				<tr>
					
						
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g23.gif" alt="23" width="14" height="13"></td>
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=183820" title="사탄의 인형">사탄의 인형</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">7</td>
					
					
				</tr>
					
					
				
				<tr>
					
						
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g24.gif" alt="24" width="14" height="13"></td>
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=183850" title="애나벨 집으로">애나벨 집으로</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">1</td>
					
					
				</tr>
					
					
				
				<tr>
					
						
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g25.gif" alt="25" width="14" height="13"></td>
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=159366" title="호랑이보다 무서운 겨울손님">호랑이보다 무서운 겨울손님</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_down_1.gif" alt="down" width="7" height="10" class="arrow"></td>
					<td class="range ac">1</td>
					
					
				</tr>
					
					
				
				<tr>
					
						
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g26.gif" alt="26" width="14" height="13"></td>
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=185935" title="좀비 워">좀비 워</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">1</td>
					
					
				</tr>
					
					
				
				<tr>
					
						
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g27.gif" alt="27" width="14" height="13"></td>
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=137327" title="고질라: 킹 오브 몬스터">고질라: 킹 오브 몬스터</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_down_1.gif" alt="down" width="7" height="10" class="arrow"></td>
					<td class="range ac">7</td>
					
					
				</tr>
					
					
				
				<tr>
					
						
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g28.gif" alt="28" width="14" height="13"></td>
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=152471" title="미친사랑">미친사랑</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">7</td>
					
					
				</tr>
					
					
				
				<tr>
					
						
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g29.gif" alt="29" width="14" height="13"></td>
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=180209" title="기방도령">기방도령</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_down_1.gif" alt="down" width="7" height="10" class="arrow"></td>
					<td class="range ac">3</td>
					
					
				</tr>
					
					
				
				<tr>
					
						
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g30.gif" alt="30" width="14" height="13"></td>
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=165022" title="호텔 뭄바이">호텔 뭄바이</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_down_1.gif" alt="down" width="7" height="10" class="arrow"></td>
					<td class="range ac">7</td>
					
					
				</tr>
					
					
						<tr><td colspan="8" class="line01"></td></tr>
					
				
				<tr>
					
						
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g31.gif" alt="31" width="14" height="13"></td>
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=177508" title="강변호텔">강변호텔</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">2</td>
					
					
				</tr>
					
					
				
				<tr>
					
						
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g32.gif" alt="32" width="14" height="13"></td>
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=179875" title="비스트">비스트</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">2</td>
					
					
				</tr>
					
					
				
				<tr>
					
						
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g33.gif" alt="33" width="14" height="13"></td>
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=167633" title="마담 싸이코">마담 싸이코</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">4</td>
					
					
				</tr>
					
					
				
				<tr>
					
						
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g34.gif" alt="34" width="14" height="13"></td>
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=183113" title="극장판 오소마츠 6쌍둥이">극장판 오소마츠 6쌍둥이</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">2</td>
					
					
				</tr>
					
					
				
				<tr>
					
						
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g35.gif" alt="35" width="14" height="13"></td>
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=177483" title="배심원들">배심원들</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_down_1.gif" alt="down" width="7" height="10" class="arrow"></td>
					<td class="range ac">4</td>
					
					
				</tr>
					
					
				
				<tr>
					
						
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g36.gif" alt="36" width="14" height="13"></td>
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=167657" title="명탐정 피카츄">명탐정 피카츄</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_down_1.gif" alt="down" width="7" height="10" class="arrow"></td>
					<td class="range ac">5</td>
					
					
				</tr>
					
					
				
				<tr>
					
						
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g37.gif" alt="37" width="14" height="13"></td>
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=184977" title="아나운서 살인사건">아나운서 살인사건</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">5</td>
					
					
				</tr>
					
					
				
				<tr>
					
						
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g38.gif" alt="38" width="14" height="13"></td>
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=173668" title="나랏말싸미">나랏말싸미</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_na_1.gif" alt="na" width="7" height="10" class="arrow"></td>
					<td class="range ac">0</td>
					
					
				</tr>
					
					
				
				<tr>
					
						
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g39.gif" alt="39" width="14" height="13"></td>
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=162203" title="폴라로이드">폴라로이드</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_down_1.gif" alt="down" width="7" height="10" class="arrow"></td>
					<td class="range ac">10</td>
					
					
				</tr>
					
					
				
				<tr>
					
						
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g40.gif" alt="40" width="14" height="13"></td>
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=69598" title="체 게바라: 1부 아르헨티나">체 게바라: 1부 아르헨티나</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_down_1.gif" alt="down" width="7" height="10" class="arrow"></td>
					<td class="range ac">1</td>
					
					
				</tr>
					
					
						<tr><td colspan="8" class="line01"></td></tr>
					
				
				<tr>
					
						
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g41.gif" alt="41" width="14" height="13"></td>
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=183782" title="독고다이">독고다이</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_down_1.gif" alt="down" width="7" height="10" class="arrow"></td>
					<td class="range ac">1</td>
					
					
				</tr>
					
					
				
				<tr>
					
						
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g42.gif" alt="42" width="14" height="13"></td>
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=151550" title="서스페리아">서스페리아</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">2</td>
					
					
				</tr>
					
					
				
				<tr>
					
						
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g43.gif" alt="43" width="14" height="13"></td>
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=162875" title="해피엔드">해피엔드</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">9</td>
					
					
				</tr>
					
					
				
				<tr>
					
						
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g44.gif" alt="44" width="14" height="13"></td>
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=178544" title="사자">사자</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">3</td>
					
					
				</tr>
					
					
				
				<tr>
					
						
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g45.gif" alt="45" width="14" height="13"></td>
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=185045" title="엘리펀트킹 덤보">엘리펀트킹 덤보</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">4</td>
					
					
				</tr>
					
					
				
				<tr>
					
						
					
						<td class="ac"></td>
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=182045" title="나의 마더">나의 마더</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">1</td>
					
					
				</tr>
					
					
				
				<tr>
					
						
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g47.gif" alt="47" width="14" height="13"></td>
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=164907" title="레드슈즈">레드슈즈</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_down_1.gif" alt="down" width="7" height="10" class="arrow"></td>
					<td class="range ac">2</td>
					
					
				</tr>
					
					
				
				<tr>
					
						
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g48.gif" alt="48" width="14" height="13"></td>
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=169637" title="라이온 킹">라이온 킹</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">3</td>
					
					
				</tr>
					
					
				
				<tr>
					
						
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g49.gif" alt="49" width="14" height="13"></td>
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=159743" title="평일 오후 3시의 연인">평일 오후 3시의 연인</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_down_1.gif" alt="down" width="7" height="10" class="arrow"></td>
					<td class="range ac">1</td>
					
					
				</tr>
					
					
				
				<tr>
					
						
					
						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g50.gif" alt="50" width="14" height="13"></td>
					
					
					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=181912" title="파이브 피트">파이브 피트</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->  
					
					<!----------------------------------------->  
					
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">5</td>
					
					
				</tr>
					
					
				
					<tr><td colspan="8" class="blank01"></td></tr>
			</tbody>
'''

# 1. tag 조회
def ex1():
    bs = BeautifulSoup(html, 'html.parser')
    # print(bs)
    # print(type(bs))

    tag = bs.td
    # print(tag)
    # print(type(tag))

    tag = bs.a
    print(tag)
    print(type(tag))

    tag = bs.td.div
    print(tag)
    print(type(tag))

# 2. attribute 값 가져오기
def ex2():
    bs = BeautifulSoup(html, 'html.parser')

    tag = bs.td
    print(tag['class']) # 클래스가 여러개 일수 있어서

    tag = bs.div
    # print(tag['id']) 없는거 가져오면 error

    print(tag.attrs)

# 3. attribute로 태그 조회하기
def ex3():
    bs = BeautifulSoup(html, 'html.parser')

    tag = bs.find('td', attrs={'class': 'black'})
    tag2 = bs.find('div', attrs={'id': 'my-div'})
    print(tag)
    print("===============================")
    print(tag2)
    print("===============================")
    tag = bs.find('div', attrs={'class': 'tit3'})
    print(tag)

def ex4():
    bs = BeautifulSoup(html2, 'html.parser')

    tag = bs.findAll('div', attrs={'class': 'tit3'})
    print(tag)
if __name__ == '__main__':
  # ex1()
  # ex2()
  # ex3()
  ex4()