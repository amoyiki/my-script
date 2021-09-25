#!/usr/bin/python3
"""
批量生成 anki 卡片
"""
import genanki

my_model = genanki.Model(
    1632558973,
    'N1核心词汇800',
    fields=[
        {'name': 'Level'},
        {'name': 'FrontSound'},
        {'name': 'Front'},
        {'name': 'WordType'},
        {'name': 'Meaning'},
        {'name': 'Sentence'},
        {'name': 'SentenceSound'},
        {'name': 'Notes'},
    ],
    templates=[
        {
            'name': '日语能力考模板',
            'qfmt': '''<div class="body-upper" style="border-radius: 5px;">
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
                    <div class="level">{{Level}}</div>
                    <div id="audio">{{FrontSound}}</div>
                    <div class="soundFront" onclick="playAudio()"></div>
                    {{Front}}
                    </div>
                    
                    <div class="body-lower" style="border-radius: 0px 0px 5px 5px;">
                    
                    <div class="type">{{WordType}}</div><div class="meaning"> {{Meaning}}</div>
                    
                    <div id="senaudio">{{SentenceSound}}</div>
                    
                    <div class="sentence">
                    {{Sentence}} <i class="fas fa-comment-dots" onclick="playSenAudio()"></i>
                    </div>
                    
                    
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
                       function playSenAudio(){
                            var audioDiv = document.getElementById('senaudio');
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
                
                .sentence {
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
import csv
with open(r'file_path', 'r', encoding='UTF-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if row:
            w = row[1]
            desc = row[3]
            note = row[4]
            print(w)
            try:
                my_note = genanki.Note(
                    model=my_model,
                    fields=['N1', '[sound:{}.mp3]'.format(w), w, '词性', desc, '句子', '[sound:{}.mp3]'.format(w), note])
                my_deck.add_note(my_note)
            except Exception as e:
                print(e)


genanki.Package(my_deck).write_to_file('output.apkg')