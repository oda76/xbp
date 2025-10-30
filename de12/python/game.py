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

horror_print("1ヶ月後...",color="dim red")
time.sleep(1.5)

horror_print("「おかしいな…捨てたはずなのに…」", color="bright_white")
time.sleep(2)

console.print(Panel.fit("[bold red]捨てたはずのマリアちゃんが新しい引越し先に居た。[/bold red]", border_style="bright_black"))
time.sleep(2)

#選択肢１
horror_print("\n選択肢:", color="dim white")
time.sleep(2)
horror_print("1.家の近くのゴミ捨て場に捨てに行く", color="dim white")
time.sleep(1.5)
horror_print("2.遠くの山で燃やす", color="dim white")
time.sleep(1.5)
horror_print("3.捨てずに一緒にいる", color="dim white")
time.sleep(1)

choice1 = input("番号を入力: ")

if choice1 == "1":
      if choice1 == "1":
            horror_print("「近くのゴミ箱に捨てよう」",color="bright_white")
            time.sleep(1)
            horror_print("........",color="bright_white")
            time.sleep(1)
elif choice1 == "2":
            horror_print("\n「車で山に向かおう」",color="bright_white")
            time.sleep(1)
            horror_print(".........",color="bright_white")
            time.sleep(1)
            horror_print("あなたは山に向かいマリアちゃんを燃やした。",color="bold red")
            time.sleep(1)
            horror_print("「これで流石に来ないよね」",color="bright_white")
            time.sleep(1)
            horror_print("「要ラナイノ? ワタシ要raナイ? ",color="dim red")
            time.sleep(1)
            horror_print("ソレナラ、アナタモ要ラナイ ",color="dim red")
            time.sleep(1)
            horror_print("翌日その山での大火事が報道された。",color="bright_white")
            time.sleep(2)
            horror_print("死者は発見されず... ",color="bright_white")
            time.sleep(1)
            horror_print("無傷の洋人形だけが発見された。",color="bright_white")
            time.sleep(3)
            horror_print("---BAD END1---",color="dim red")
            time.sleep(1)
elif choice1 == "3":
            horror_print("「やっぱ、一緒にいよう」",color="bright_white")
            time.sleep(1)
else:
            horror_print("\nエラー",color="bright_white")
            time.sleep(1)
    

console.print("\n[dim red]--- END ---[/dim red]")