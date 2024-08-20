from tkinter import *
import tkinter.messagebox
import threading
from chatbot import continue_conversation  # chatbot.py의 continue_conversation 함수 가져오기
import time

window_size = "400x400"

class ChatInterface(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        # 색상 및 폰트 설정
        self.tl_bg = "#EEEEEE"
        self.tl_bg2 = "#EEEEEE"
        self.tl_fg = "#000000"
        self.font = "Verdana 10"

        # 메뉴바 설정
        menu = Menu(self.master)
        self.master.config(menu=menu, bd=5)
        
        # 파일 메뉴
        file = Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=file)
        file.add_command(label="Clear Chat", command=self.clear_chat)  # 채팅 기록 지우기
        file.add_command(label="Exit", command=self.chatexit)  # 종료
        
        # 옵션 메뉴
        options = Menu(menu, tearoff=0)
        menu.add_cascade(label="Options", menu=options)

        # 폰트 설정
        font = Menu(options, tearoff=0)
        options.add_cascade(label="Font", menu=font)
        font.add_command(label="Default", command=self.font_change_default)
        font.add_command(label="Times", command=self.font_change_times)
        font.add_command(label="System", command=self.font_change_system)
        font.add_command(label="Helvetica", command=self.font_change_helvetica)
        font.add_command(label="Fixedsys", command=self.font_change_fixedsys)

        # 색상 테마 설정
        color_theme = Menu(options, tearoff=0)
        options.add_cascade(label="Color Theme", menu=color_theme)
        color_theme.add_command(label="Default", command=self.color_theme_default)
        color_theme.add_command(label="Grey", command=self.color_theme_grey)
        color_theme.add_command(label="Blue", command=self.color_theme_dark_blue)
        color_theme.add_command(label="Torque", command=self.color_theme_turquoise)
        color_theme.add_command(label="Hacker", command=self.color_theme_hacker)

        # 도움말 메뉴
        help_option = Menu(menu, tearoff=0)
        menu.add_cascade(label="Help", menu=help_option)
        help_option.add_command(label="Develpoers", command=self.about)  # 개발자 정보

        # 대화 내용 표시를 위한 프레임
        self.text_frame = Frame(self.master, bd=6)
        self.text_frame.pack(expand=True, fill=BOTH)

        # 스크롤바 설정
        self.text_box_scrollbar = Scrollbar(self.text_frame, bd=0)
        self.text_box_scrollbar.pack(fill=Y, side=RIGHT)

        # 대화 내용 표시를 위한 텍스트 박스
        self.text_box = Text(self.text_frame, yscrollcommand=self.text_box_scrollbar.set, state=DISABLED,
                             bd=1, padx=6, pady=6, spacing3=8, wrap=WORD, bg=None, font="Verdana 10", relief=GROOVE,
                             width=10, height=1)
        self.text_box.pack(expand=True, fill=BOTH)
        self.text_box_scrollbar.config(command=self.text_box.yview)

        # 사용자 입력을 위한 프레임
        self.entry_frame = Frame(self.master, bd=1)
        self.entry_frame.pack(side=LEFT, fill=BOTH, expand=True)

        # 사용자 입력 필드
        self.entry_field = Entry(self.entry_frame, bd=1, justify=LEFT)
        self.entry_field.pack(fill=X, padx=6, pady=6, ipady=3)

        # 전송 버튼과 이모지 버튼을 위한 프레임
        self.send_button_frame = Frame(self.master, bd=0)
        self.send_button_frame.pack(fill=BOTH)

        # 전송 버튼
        self.send_button = Button(self.send_button_frame, text="Send", width=5, relief=GROOVE, bg='white',
                                  bd=1, command=lambda: self.send_message_insert(None), activebackground="#FFFFFF",
                                  activeforeground="#000000")
        self.send_button.pack(side=LEFT, ipady=8)
        self.master.bind("<Return>", self.send_message_insert)  # Enter 키로 메시지 전송

        self.last_sent_label(date="No messages sent.")  # 마지막 메시지 라벨 초기화

    # 마지막 메시지 라벨 업데이트
    def last_sent_label(self, date):
        try:
            self.sent_label.destroy()
        except AttributeError:
            pass

        self.sent_label = Label(self.entry_frame, font="Verdana 7", text=date, bg=self.tl_bg2, fg=self.tl_fg)
        self.sent_label.pack(side=LEFT, fill=X, padx=3)

    # 채팅 기록 지우기
    def clear_chat(self):
        self.text_box.config(state=NORMAL)
        self.last_sent_label(date="No messages sent.")
        self.text_box.delete(1.0, END)
        self.text_box.config(state=DISABLED)

    # 애플리케이션 종료
    def chatexit(self):
        exit()

    # 개발자 정보 표시
    def about(self):
        tkinter.messagebox.showinfo("KKWBOT Developers","Prasad Bhasme")

    # 메시지 전송 및 응답 처리
    def send_message_insert(self, event=None):
        user_input = self.entry_field.get()
        pr1 = "Human : " + user_input + "\n"
        self.text_box.configure(state=NORMAL)
        self.text_box.insert(END, pr1)
        self.text_box.configure(state=DISABLED)
        self.text_box.see(END)

        # chatbot 응답 생성
        try:
            ob = continue_conversation(user_input)
        except Exception as e:
            ob = f"Error: {str(e)}"
        pr = "KKWBOT: " + ob + "\n"
        self.text_box.configure(state=NORMAL)
        self.text_box.insert(END, pr)
        self.text_box.configure(state=DISABLED)
        self.text_box.see(END)
        self.last_sent_label(str(time.strftime("Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
        self.entry_field.delete(0, END)  # 입력 필드 비우기

    # 폰트 변경 함수들
    def font_change_default(self):
        self.text_box.config(font="Verdana 10")
        self.entry_field.config(font="Verdana 10")
        self.font = "Verdana 10"

    def font_change_times(self):
        self.text_box.config(font="Times")
        self.entry_field.config(font="Times")
        self.font = "Times"

    def font_change_system(self):
        self.text_box.config(font="System")
        self.entry_field.config(font="System")
        self.font = "System"

    def font_change_helvetica(self):
        self.text_box.config(font="Helvetica")
        self.entry_field.config(font="Helvetica")
        self.font = "Helvetica"

    def font_change_fixedsys(self):
        self.text_box.config(font="Fixedsys")
        self.entry_field.config(font="Fixedsys")
        self.font = "Fixedsys"

    # 색상 테마 설정 함수들
    def color_theme_default(self):
        self.master.config(bg="#eeeeee")
        self.text_frame.config(bg="#eeeeee")
        self.text_box.config(bg="#ffffff", fg="#000000")
        self.entry_frame.config(bg="#eeeeee")
        self.entry_field.config(bg="#ffffff", fg="#000000", insertbackground="#000000")
        self.send_button_frame.config(bg="#eeeeee")
        self.send_button.config(bg="#ffffff", fg="#000000", activebackground="#f0f0f0", activeforeground="#000000")
        self.sent_label.config(bg="#eeeeee", fg="#000000")

        self.tl_bg = "#ffffff"
        self.tl_bg2 = "#eeeeee"
        self.tl_fg = "#000000"

    def color_theme_grey(self):
        self.master.config(bg="#444444")
        self.text_frame.config(bg="#444444")
        self.text_box.config(bg="#333333", fg="#ffffff")
        self.entry_frame.config(bg="#444444")
        self.entry_field.config(bg="#333333", fg="#ffffff", insertbackground="#ffffff")
        self.send_button_frame.config(bg="#444444")
        self.send_button.config(bg="#333333", fg="#ffffff", activebackground="#4f4f4f", activeforeground="#ffffff")
        self.sent_label.config(bg="#444444", fg="#ffffff")

        self.tl_bg = "#333333"
        self.tl_bg2 = "#444444"
        self.tl_fg = "#ffffff"

    def color_theme_turquoise(self):
        self.master.config(bg="#003333")
        self.text_frame.config(bg="#003333")
        self.text_box.config(bg="#669999", fg="#FFFFFF")
        self.entry_frame.config(bg="#003333")
        self.entry_field.config(bg="#669999", fg="#FFFFFF", insertbackground="#FFFFFF")
        self.send_button_frame.config(bg="#003333")
        self.send_button.config(bg="#669999", fg="#FFFFFF", activebackground="#669999", activeforeground="#FFFFFF")
        self.sent_label.config(bg="#003333", fg="#FFFFFF")

        self.tl_bg = "#669999"
        self.tl_bg2 = "#003333"
        self.tl_fg = "#FFFFFF"

    def color_theme_dark_blue(self):
        self.master.config(bg="#263b54")
        self.text_frame.config(bg="#263b54")
        self.text_box.config(bg="#1c2e44", fg="#FFFFFF")
        self.entry_frame.config(bg="#263b54")
        self.entry_field.config(bg="#1c2e44", fg="#FFFFFF", insertbackground="#FFFFFF")
        self.send_button_frame.config(bg="#263b54")
        self.send_button.config(bg="#1c2e44", fg="#FFFFFF", activebackground="#1c2e44", activeforeground="#FFFFFF")
        self.sent_label.config(bg="#263b54", fg="#FFFFFF")

        self.tl_bg = "#1c2e44"
        self.tl_bg2 = "#263b54"
        self.tl_fg = "#FFFFFF"

    def color_theme_hacker(self):
        self.master.config(bg="#0F0F0F")
        self.text_frame.config(bg="#0F0F0F")
        self.entry_frame.config(bg="#0F0F0F")
        self.text_box.config(bg="#0F0F0F", fg="#33FF33")
        self.entry_field.config(bg="#0F0F0F", fg="#33FF33", insertbackground="#33FF33")
        self.send_button_frame.config(bg="#0F0F0F")
        self.send_button.config(bg="#0F0F0F", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF")
        self.sent_label.config(bg="#0F0F0F", fg="#33FF33")

        self.tl_bg = "#0F0F0F"
        self.tl_bg2 = "#0F0F0F"
        self.tl_fg = "#33FF33"

    # 기본 폰트 및 색상 테마 설정
    def default_format(self):
        self.font_change_default()
        self.color_theme_default()

# 애플리케이션 창 설정
root = Tk()
a = ChatInterface(root)
root.geometry(window_size)  # 창 크기 설정
root.title("cafe")  # 창 제목 설정
root.mainloop()  # 메인 이벤트 루프 시작