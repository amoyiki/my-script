#!/usr/bin/python3
"""
批量生成 anki 卡片
"""
import os

import genanki

my_model = genanki.Model(
    1632558973,
    'N1核心词汇800',
    fields=[
        {'name': 'id'},
        {'name': 'Level'},
        {'name': 'FrontSound'},
        {'name': 'Front'},
        {'name': 'Hirakana'},
        {'name': 'Kanji'},
        {'name': 'WordType'},
        {'name': 'Meaning'},
        {'name': 'Notes'},
    ],
    templates=[
        {
            'name': '日语能力考模板',
            'qfmt': '''<div class="body-upper" style="border-radius: 5px;">
                    <span style="display: none">{{id}}</span>
                    <div class="level">{{Level}}</div>
                    <div id="audio">{{FrontSound}}</div>
                    <div class="soundFront" onclick="playAudio()"></div>
                    {{Front}}
                    </div>
                    <script>
                        function playAudio(){
                            var audioDiv = document.getElementById('audio');
                            var audio = audioDiv.getElementsByTagName("*");
                            audio[0].click();
                        }
                    </script>''',
            'afmt': '''<div class="body-upper" style="border-radius: 5px 5px 0px 0px;">
                    <span style="display: none">{{id}}</span>
                    <div class="level">{{Level}}</div>
                    <div id="audio">{{FrontSound}}</div>
                    <div>{{Hirakana}}</div>
                    <div class="soundFront" onclick="playAudio()"></div>
                    {{Kanji}}
                    </div>
                    <div class="body-lower" style="border-radius: 0px 0px 5px 5px;">
                    <div class="type">{{WordType}}</div><div class="meaning"> {{Meaning}}</div>
                    {{#Notes}}<div class="notes">
                    {{Notes}}
                    </div>{{/Notes}}
                    </div>               
                    <script src="(replace with your own fontawesome link)" crossorigin="anonymous"></script>          
                    <script>
                        function playAudio(){
                            var audioDiv = document.getElementById('audio');
                            var audio = audioDiv.getElementsByTagName("*");
                            audio[0].click();
                        }
                    </script>''',
        },
    ],
    css='''u {
                 text-decoration-style: wavy;
                text-underline-position: under;
                 color: white;
                 padding: 1px;
                }
                
                .card {
                 font-family: UD Digi Kyokasho N-R;
                 font-size: 20px;
                 text-align: center;
                 background-color: #FDF8E9;
                 padding: 10px;
                }
                
                .body-upper {
                 font-family: Noto Sans JP Black;
                 font-size: 40px;
                 color: #EEE;
                 background-color: #555555;
                 padding: 40px 10px 10px;
                }
                
                .body-lower {
                 text-align: left;
                 color: #555555;
                 background-color: #9FDBDB;
                 padding: 20px;
                }
                
                .level {
                 position: absolute;
                 background-color: #9FDBDB;
                 color: #555555;
                 font-size: 20px;
                 padding: 5px;
                 margin-top: -30px;
                }
                
                .meaning {
                 width: fit-content;
                 font-family: Bree Serif;
                 font-size: 15px;
                 border: 1px solid #555555;
                 padding: 5px;
                 margin-bottom: 15px;
                 max-width: 100%;
                 display: inline-table;
                }
                
                .type {
                 width: fit-content;
                 display: inline-table;
                 border: 1px solid #555555;
                 background-color: #555555;
                 font-family: Bree Serif;
                 font-size: 15px;
                 color: #9FDBDB;
                 padding: 5px;
                 padding-left: 7px;
                }
                
                .soundFront {
                 position: absolute;
                 top: 40px;
                 right: 40px;
                 font-size: 18px;
                 content: url("play.png");
                 width: 6%;
                }
                
                
                .notes {
                 font-family: Noto Sans JP Regular;
                 font-size: 12px;
                 border: 1px dashed #555555;
                 padding: 10px;
                 margin-top: 20px;
                }''', )

my_deck = genanki.Deck(
    1632559573,
    'N1核心词汇800')

import bs4

with open(r'C:\Users\Administrator\Desktop\1.html', 'r', encoding='UTF-8') as f:
    r = f.read()
    soup = bs4.BeautifulSoup(r, 'lxml')
    tr_html = soup.find_all('tr')
    for tr in tr_html:
        if tr:
            data = tr.find_all('td')
            if data:
                i = data[0].text
                w = data[1].text
                h = tr.select_one('yomi') and tr.select_one('yomi').text or ''
                if not h:
                    h = tr.select_one('.xsjrh-word1') and tr.select_one('.xsjrh-word1').text or ''
                cx = tr.select_one('.xsjrh-cat') and tr.select_one('.xsjrh-cat').text or ''
                hanzi = tr.select_one('kanji') and tr.select_one('kanji').text or ''
                if not hanzi:
                    hanzi = tr.select_one('.xsjrh-word2') and tr.select_one('.xsjrh-word2').text or ''

                desc = tr.find_all('div', class_='xsjrh-sense')
                if desc:
                    desc_list = []
                    for d in desc:
                        _desc = ''
                        sid = d.find('span', class_='xsjrh-sid')
                        if sid:
                            _desc = '{}'.format(sid.text)

                        for x in d.find_all('span', class_='xsjrh-sense-li'):
                            ja = x.find('span', class_='xsjrh-j')
                            cn = x.find('span', class_='xsjrh-c')
                            if ja:
                                _desc = '{} {}<br/>'.format(
                                    _desc, ja.text)
                            if cn:
                                _desc = '{} {}'.format(
                                    _desc, cn.text)
                            desc_list.append(_desc)
                    desc = '<br>'.join(desc_list)
                    desc = '{}<br>'.format(desc)

                if not desc:
                    desc = tr.select_one('.description') and tr.select_one('.description').text or ''
                if not desc:
                    desc = tr.select_one('.explain_wrap_styleless') and tr.select_one(
                        '.explain_wrap_styleless').text or ''
                note = ''

                try:
                    my_note = genanki.Note(
                        model=my_model,
                        fields=['{}'.format(i), 'N1', '[sound:{}.mp3]'.format(w), w, h, hanzi, cx, desc, note])
                    my_deck.add_note(my_note)
                except Exception as e:
                    print(e)
my_package = genanki.Package(my_deck)
# 添加媒体文件
f_list = []
for parent, dirnames, filenames in os.walk(r"C:\Users\Administrator\AppData\Roaming\Anki2\账户1\collection.media"):
    for f in filenames:
        f_list.append(os.path.join(parent, f))
my_package.media_files = f_list
my_package.write_to_file('output.apkg')
