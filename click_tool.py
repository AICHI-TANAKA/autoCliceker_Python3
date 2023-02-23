import pyautogui
import time
import tkinter
from tkinter import messagebox
import keyboard


# 画面クローズ時にwhile文を殺すためのフラグ
while_stopper = False


# 画面クローズ時処理
def click_close():
    if messagebox.askokcancel("確認", "本当に閉じていいですか？"):
        global while_stopper
        while_stopper = True
        root.destroy()


# ポインタ座標リアルタイム取得クラス
class point_get(tkinter.Frame):
    point_x_now = float()
    point_y_now = float()

    def __init__(self, master=None):
        super().__init__(master)

    def point_getter(self):
        now_position = pyautogui.position()
        self.point_x_now = now_position[0]
        self.point_y_now = now_position[1]

    def main(self):
        self.point_getter()
        self.x_data_txt = tkinter.Label(self.master, text='現在のx座標:')
        self.x_data_txt.place(x=30, y=10)
        self.y_data_txt = tkinter.Label(self.master, text='現在のy座標:')
        self.y_data_txt.place(x=150, y=10)
        while True:
            self.x_data_txt['text'] = '現在のx座標:' + str(self.point_x_now)
            self.y_data_txt['text'] = '現在のy座標:' + str(self.point_y_now)
            self.point_getter()
            # 表示を即時反映
            self.update()
            global while_stopper
            if (while_stopper == True):
                break


# クリック処理実行管理クラス
class clicker(tkinter.Frame):
    # 入力項目、開始ボタンのオブジェクト格納リスト
    content_list1 = []
    # 回数カウント、中止（終了）ボタンのオブジェクト格納リスト
    content_list2 = []
    # 中止フラグ
    stopper = False

    def __init__(self, master=None):
        super().__init__(master)
        # self.stopper = Value('i', False)
        # self.radio_value = tkinter.Text(value = 0)
        self.main()

    def main(self):
        self.button_make1()

    # ボタン作成初期処理
    def button_make1(self):
        if (self.stopper == True):
            self.contents_hide(self.stop_button)

        self.x_data = tkinter.Entry(self.master, width=20)
        self.x_data.place(x=120, y=50)
        self.x_data_txt = tkinter.Label(self.master, text='x座標(1回目)')
        self.x_data_txt.place(x=30, y=50)

        self.y_data = tkinter.Entry(self.master, width=20)
        self.y_data.place(x=120, y=70)
        self.y_data_txt = tkinter.Label(self.master, text='y座標(1回目)')
        self.y_data_txt.place(x=30, y=70)

        self.x2_data = tkinter.Entry(self.master, width=20)
        self.x2_data.place(x=120, y=110)
        self.x2_data_txt = tkinter.Label(self.master, text='x座標(2回目)')
        self.x2_data_txt.place(x=30, y=110)

        self.y2_data = tkinter.Entry(self.master, width=20)
        self.y2_data.place(x=120, y=130)
        self.y2_data_txt = tkinter.Label(self.master, text='y座標(2回目)')
        self.y2_data_txt.place(x=30, y=130)

        self.x3_data = tkinter.Entry(self.master, width=20)
        self.x3_data.place(x=120, y=170)
        self.x3_data_txt = tkinter.Label(self.master, text='x座標(3回目)')
        self.x3_data_txt.place(x=30, y=170)

        self.y3_data = tkinter.Entry(self.master, width=20)
        self.y3_data.place(x=120, y=190)
        self.y3_data_txt = tkinter.Label(self.master, text='y座標(3回目)')
        self.y3_data_txt.place(x=30, y=190)

        self.click_num = tkinter.Entry(self.master, width=20)
        self.click_num.place(x=120, y=240)
        self.click_num_txt = tkinter.Label(self.master, text='処理回数')
        self.click_num_txt.place(x=30, y=240)

        self.click_interval = tkinter.Entry(self.master, width=20)
        self.click_interval.place(x=120, y=260)
        self.click_interval_txt = tkinter.Label(self.master, text='周期間隔(秒)')
        self.click_interval_txt.place(x=30, y=260)

        self.start_button = tkinter.Button(self.master,
                                           text='開始',
                                           command=self.start_click)
        self.start_button.place(x=120, y=290)

        self.error_msg = tkinter.Label(self.master, text='')
        self.error_msg.place(x=40, y=320)

    # 中止ボタン作成
    def button_make2(self):
        self.stop_button = tkinter.Button(self.master,
                                          text='中止',
                                          command=self.stop_click)
        self.stop_button.place(x=120, y=290)

        self.click_counter = tkinter.Label(self.master,
                                           text='現在 : ' + '  ' + '回目')
        self.click_counter.place(x=100, y=320)

    # 開始ボタン押下時処理
    def start_click(self):
        self.stopper = False
        self.input_editer(self.x_data,
                          self.y_data,
                          self.x2_data,
                          self.y2_data,
                          self.x3_data,
                          self.y3_data,
                          self.click_num,
                          self.click_interval)
        if (self.input_checker() == False):
            self.error_msg['text'] = '全ての項目を半角数字で入力してください'
        elif (self.input_checker() == True):
            # インプットエリア非表示
            self.contents_hide(self.x_data,
                               self.y_data,
                               self.x2_data,
                               self.y2_data,
                               self.x3_data,
                               self.y3_data,
                               self.click_num,
                               self.click_interval,
                               self.start_button,
                               self.error_msg)
            # 一応ラベルも非表示
            self.contents_hide(self.x_data_txt,
                               self.y_data_txt,
                               self.x2_data_txt,
                               self.y2_data_txt,
                               self.x3_data_txt,
                               self.y3_data_txt,
                               self.click_num_txt,
                               self.click_interval_txt)
            self.button_make2()

            # 表示を即時反映
            self.update()
            self.update_idletasks()

            # クリック処理
            self.point_clicker()
            # self.stop_key_get()

    # 中止ボタン押下時処理
    def stop_click(self):
        self.stopper = True
        self.contents_hide(self.click_counter)
        self.button_make1()

    # 要素を非表示にする
    def contents_hide(self, *contents):
        self.x3_data.place_forget()
        for content in contents:
            content.place_forget()

    # 入力値を編集
    def input_editer(self, *contents):
        for content in contents:
            # 空白を削除
            text = content.get().replace(' ', '')
            content.delete(0, tkinter.END)
            content.insert(tkinter.END, text)

    # 入力値のチェックを行う
    def input_checker(self):
        if self.x_data.get() == '' or \
                self.y_data.get() == '' or \
                self.click_num.get() == '' or \
                self.click_interval.get() == '':
            return False
        elif (self.x2_data.get() != '' and self.y2_data.get() == '') or \
                (self.x2_data.get() == '' and self.y2_data.get() != ''):
            return False
        elif (self.x3_data.get() != '' and self.y3_data.get() == '') or \
                (self.x3_data.get() == '' and self.y3_data.get() != ''):
            return False
        else:
            return True

    # 連続クリック処理
    def point_clicker(self):
        # 入力値を変数に格納
        point_x = float(self.x_data.get())
        point_y = float(self.y_data.get())
        if (self.x2_data.get()):
            point_x2 = float(self.x2_data.get())
            point_y2 = float(self.y2_data.get())
        if (self.x3_data.get()):
            point_x3 = float(self.x3_data.get())
            point_y3 = float(self.y3_data.get())
        total_click = int(self.click_num.get())
        interval_sec = float(self.click_interval.get())
        # マウス移動
        pyautogui.moveTo(point_x, point_y, 0.5)
        # 連続クリックスタート
        for i in range(total_click):
            if self.stop_key_get() == False:
                # クリック回数表示
                self.counter_disp(i)
                # 指定秒待機
                time.sleep(interval_sec)
                # マウス移動
                pyautogui.moveTo(point_x, point_y, 0.25)
                # クリック
                pyautogui.click()
                if (self.x2_data.get()):
                    # マウス移動
                    pyautogui.moveTo(point_x2, point_y2, 0.5)
                    # クリック
                    pyautogui.click()
                if (self.x3_data.get()):
                    # マウス移動
                    pyautogui.moveTo(point_x3, point_y3, 0.5)
                    # クリック
                    pyautogui.click()
                # 表示を即時反映
                self.update()
                self.update_idletasks()
            else:
                break

    # クリック回数表示機能
    def counter_disp(self, count: int):
        count += 1
        self.click_counter['text'] = '現在 : ' + str(count) + '周目'
        if count == int(self.click_num.get()):
            self.click_counter['text'] = '現在 : ' + str(count) + '周目\n終了しました。'
            self.stop_button['text'] = '終了'

    # キーボードでの割り込み中断処理
    def stop_key_get(self):
        if keyboard.is_pressed("ctrl+z"):
            print("keyPress!!")
            self.stopper = True
            return True
        else:
            return False


if __name__ == "__main__":
    # ウィンドウ作成
    root = tkinter.Tk()
    # タイトルを変更
    root.title('クリッカー')
    # ウィンドウを最前面に表示
    root.attributes('-topmost', True)
    # サイズ指定
    root.minsize(width=300, height=370)
    # 終了時にメッセージを表示
    root.protocol("WM_DELETE_WINDOW", click_close)
    # フレーム作成
    frame = tkinter.Frame(root, width=300, height=370)
    # フレームのサイズを固定する（配下ウィジェットに押し出されないように）
    frame.propagate(False)
    # ウィジェットの配置方法を指定
    frame.pack()
    # クラスのインスタンス生成
    click_man = clicker(master=frame)
    point_XY = point_get(master=frame)
    # 入力フォーム作成
    click_man.main()
    # ポインタ座標リアルタイム取得実行
    point_XY.main()
    # 前実行処理でwhileがあるので必要ありませんが明示的に。
    root.mainloop()