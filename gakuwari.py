import flet as ft
import math

def main(page: ft.Page):
    def calculation(e):
        
        if ofwari.value ==False and of.value == True:#往復適用:
            dc_results = int(money.value) *0.8
            dc_results = myround(dc_results)
            dc_results = dc_results * 2
        elif ofwari.value ==True and of.value == True:#往復割適用:
            dc_results = int(money.value) *0.8
            dc_results = myround(dc_results)
            dc_results = dc_results * 2
            dc_results = int(dc_results)* 0.9
            dc_results = myround(dc_results)
        elif ofwari.value ==False and of.value == False:#それ以外:
            dc_results = int(money.value) *0.8
            dc_results = myround(dc_results)

        msg = f"{dc_results}円です。"
        result.value = msg
        result.update()

    def myround(g):
        g=(math.floor(g/10))*10
        return g

    page.title = "学割・往復割引 計算"  # アプリタイトル

    of = ft.Checkbox(label="往復適用")
    ofwari = ft.Checkbox(label="往復割引適用あり")

    Note1 = ft.Text("注意: 往復割引は往復切符(片道600km以上)にのみ適用されます.")
    Note2 = ft.Text("この結果はあくまで参考程度です.詳しくはJRのサイトをご確認ください.")
    money = ft.TextField(label="元の乗車券代")
    result = ft.TextField(label="計算結果", disabled=True)
    judge = ft.ElevatedButton("計算！", icon="Done", on_click=calculation)

    page.controls.append
    page.add(money,of,ofwari,result,judge,Note1,Note2)


ft.app(port=8550,target=main)