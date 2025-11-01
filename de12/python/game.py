from rich.console import Console
from rich.panel import Panel
import time, sys, random

console = Console()

def horror_print(text, delay=0.07, color="bright_white"):
    for c in text:
        console.print(c, end="", style=color, highlight=False)
        sys.stdout.flush()
        time.sleep(random.uniform(delay/2, delay*1.3))
    print()

#題名
console.print(Panel.fit("[bold red]幼い頃に遊んでいたお人形を捨てよう!!![/bold red]", border_style="red"))
time.sleep(1.5)

horror_print("今年大学生になったあなたは一人暮らしのために荷造りをしている。", color="bright_white")
time.sleep(2)

horror_print("「マリアちゃん懐かしいな〜！もう遊ばないから捨てるか」", color="bright_white")
time.sleep(2)

horror_print("...", color="dim white")
time.sleep(2)

horror_print("1ヶ月後...",color="bold red")
time.sleep(1.5)

horror_print("「おかしいな…捨てたはずなのに…」", color="bright_white")
time.sleep(2)

horror_print("捨てたはずのマリアちゃんが新しい引越し先に居た。",color="bold red")
time.sleep(2)

#選択肢１
horror_print("\n選択肢:", color="dim white")
time.sleep(2)
horror_print("1.家の近くのゴミ捨て場に行く", color="dim white")
time.sleep(1.5)
horror_print("2.遠くの山で燃やす", color="dim white")
time.sleep(1.5)
horror_print("3.捨てずに一緒にいる", color="dim white")
time.sleep(1)

choice1 = input("番号を入力: ")

if choice1 == "1":
      if choice1 == "1":
            horror_print("「近くのゴミ捨て場に行こう」",color="bright_white")
            time.sleep(1)
            horror_print("ガサッ........",color="bright_white")
            time.sleep(1)
            horror_print("----------------------",color="dim white")
            time.sleep(2)
            horror_print("「なんで.. なんでいるの..また戻ってきた...」",color="bright_white")
            time.sleep(2)

             #選択肢2
            horror_print("\n選択肢:", color="dim white")
            time.sleep(2)
            horror_print("1.押し入れにしまっておく",color="dim white")
            time.sleep(2)
            horror_print("2.塩で清める",color="dim white")
            time.sleep(2)

            choice2 = input("番号を入力: ")

      if choice2 == "1":
            horror_print("「そうだ、押し入れにしまっておこう」",color="bright_white")
            time.sleep(1)
            horror_print("あなたはマリアちゃんを押し入れに置いておくことにした。",color="bright_white")
            time.sleep(1)
            horror_print("「...遊ンデ 一緒二遊ボウ」",color="dim red")
            time.sleep(3)
            horror_print("あなたはマリアちゃんと一緒に過ごすにつれて違和感を感じるようになった。何に対しても悲観的になっていったのだ。",color="bright_white")
            time.sleep(4)
            horror_print("次第に大学へも行かなくなった。",color="bright_white")
            time.sleep(1)
            horror_print("⚪︎月▲日アパートの一室から女子大学生の遺体が見つかった。",color="bold red")
            time.sleep(3)
            horror_print("---BAD END2---",color="dim red")
            time.sleep(1)

      elif choice2 == "2":
            horror_print("「清めよう!!!!!」",color="bright_white")
            time.sleep(1)
            horror_print("一晩中マリアちゃんの周りを塩で囲んだ",color="bright_white")
            time.sleep(1)

            #選択肢３
            horror_print("\n選択肢:", color="dim white")
            time.sleep(2)
            horror_print("1.神社で供養を頼む",color="dim white")
            time.sleep(2)
            horror_print("2.壊す", color="dim white")
            time.sleep(2)
            horror_print("3.一緒にお出かけする",color="dim white")
            time.sleep(2)
        
            choice3 = input("番号を入力: ")

            if choice3 == "1":
             horror_print("「よし神社に行こう」", color="bright_white")
             time.sleep(2)
             horror_print("神社で供養を頼んだ。",color="bright_white")
             time.sleep(2)
             horror_print("しかし...マリアちゃんは無傷なまま家にいた",color="bold red")
             time.sleep(4)
             horror_print("「もうなんで供養してもらったはずなのに...!!」",color="bright_white")
             time.sleep(2)
             horror_print("あなたは人形を思わず投げつけてしまった。", color="bright_white")
             time.sleep(2)
             horror_print("...その夜",color="bright_white")
             time.sleep(3)
             horror_print("神社とアパートの一室が全焼",color="bright_white")
             time.sleep(3)
             horror_print("2人の焼死体だけが発見された",color="bold red")
             time.sleep(3)
             horror_print("---BAD END1.5---",color="dim red")
             time.sleep(2)

            elif choice3 == "2":
             horror_print("「もう壊すしかない。」", color="bold red")
             time.sleep(3)
             horror_print("あなたは思いっきり壊した",color="bright_white")
             time.sleep(2)
             horror_print("マリアちゃんはバラバラになった。",color="bold red")
             time.sleep(3)
             horror_print("...「気味が悪い。」",color="bright_white")
             time.sleep(2)
             horror_print("それから4年が経った",color="bright_white")
             time.sleep(2)
             horror_print("その間あなたは充実した日々を過ごした", color="bright_white")
             time.sleep(2)
             horror_print("「忘レタカ 忘レタオマエガ悪イ」", color="bold red")
             time.sleep(3)
             horror_print("[22歳 死因:原因不明の心臓麻痺]",color="bright_white")
             time.sleep(4)
             horror_print("---BAD END3---",color="dim red")
             time.sleep(2)
      
            elif choice3 == "3":
             horror_print("「もうどうしたらいいかわからない。」",color="bright_white")
             time.sleep(3)
             horror_print("あなたは為す術がなく外に持ち出した。",color="bright_white")
             time.sleep(3)
             horror_print("...公園のベンチに座った。",color="bright_white")
             time.sleep(3)
             horror_print("???「かわいいお人形さん!!!」",color="bright_white")
             time.sleep(3)
             horror_print("「え?」",color="bright_white")
             time.sleep(3)
             horror_print("公園で遊んでいた少女が人形を欲しがっている。",color="bright_white")
             time.sleep(3)
             horror_print("放心状態だったあなたは人形を少女に渡してしまった。",color="bright_white")
             time.sleep(3)
             horror_print("少女「くれるの?」",color="bright_white")
             time.sleep(3)
             horror_print("「マリアちゃんっていうの。でも他のお人形にした方がいいよ。」",color="bright_white")
             time.sleep(3)
             horror_print("少女「この子がいいの!!!絶対大切にする!!!!」",color="bright_white")
             time.sleep(3)
             horror_print("あなたは一刻も早くこの人形を手放したかった。考えるよりも先に口が動いていた。",color="bright_white")
             time.sleep(4)
             horror_print("「大切にしてね。たくさん遊んであげて。」",color="bright_white")
             time.sleep(3)
             horror_print("「タイセツ二シテ ズット遊ンデ」",color="dim red")
             time.sleep(3)
             horror_print("---HAPPY END???---",color="dim white")
             time.sleep(2)

            else:
                  horror_print("ERROR----",color="bright_white")
                  time.sleep(1)
        
      else:
            horror_print("errorrrrrrrrrrrr",color="bright_white")
            time.sleep(1)

elif choice1 == "2":
            horror_print("\n「山に向かおう」",color="bright_white")
            time.sleep(1)
            horror_print(".........",color="bright_white")
            time.sleep(1)
            horror_print("あなたは山に向かいマリアちゃんを燃やした。",color="bold red")
            time.sleep(1)
            horror_print("「これで流石に来ないよね」",color="bright_white")
            time.sleep(1)
            horror_print("....「要ラナイノ? ワタシ要raナイ? ",color="dim red")
            time.sleep(2)
            horror_print("......ソレナラ、アナタ要ラナイ ",color="dim red")
            time.sleep(2)
            horror_print("翌日その山での大火事が報道された。",color="bright_white")
            time.sleep(1)
            horror_print("人間は発見されず... ",color="bright_white")
            time.sleep(1)
            horror_print("無傷の洋人形だけが発見された。",color="bright_white")
            time.sleep(3)
            horror_print("---BAD END1---",color="dim red")
            time.sleep(1)
elif choice1 == "3":
            horror_print("「やっぱ、一緒にいよう」",color="bright_white")
            time.sleep(1)
            horror_print("あなたはマリアちゃんを捨てずに置いておくことにした。",color="bright_white")
            time.sleep(1)
            horror_print("「...遊ンデ 一緒二遊ボウ」",color="dim red")
            time.sleep(3)
            horror_print("あなたはマリアちゃんと一緒に過ごすにつれて違和感を感じるようになった。何に対しても悲観的になっていったのだ。",color="bright_white")
            time.sleep(1)
            horror_print("次第に大学へも行かなくなった。",color="bright_white")
            time.sleep(1)
            horror_print("⚪︎月▲日アパートの一室から女子大学生の遺体が見つかった。",color="bold red")
            time.sleep(1)
            horror_print("---BAD END2---",color="dim red")
            time.sleep(1)
            
            
else:
            horror_print("エラー---~ー",color="bright_white")
            time.sleep(1)
