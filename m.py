import threading
import time
import sys


def time_format(seconds):
    return time.strftime('%M:%S', time.localtime(seconds))

LOG_WIDTH = 35
CLEAR_TO_END = '\033'
def progress_log(current, total):
    sys.stdout.write(f'\r{CLEAR_TO_END}')
    progress = 1 - current/total
    hashes = '#' * int(progress * LOG_WIDTH)
    spaces = ' ' * int(LOG_WIDTH - len(hashes))
    sys.stdout.write(f'\r{time_format(current)}/{time_format(total)}[{hashes + spaces}] {progress * 100:.2f}%')


class TimeThread(threading.Thread):
    def __init__(self, time):
        threading.Thread.__init__(self)
        self.remain_time = time
        self.total_time = time

    def run(self):
        print(f'倒计时开始，剩余时间 {time_format(self.remain_time)}')
        while self.remain_time > 0:
            self.remain_time -= 1
            time.sleep(1)
            progress_log(self.remain_time, self.total_time)
            time.sleep(1)
        print('\n倒计时结束，请选择下一项任务')        



def print_category():
    print('\n\n--- 命令行番茄钟 ---')
    print('1. 25分钟')
    print('2. 10分钟')
    print('3. 5分钟')
    print('4. 1分钟')
    print('5. 退出')
    print('> ', end='')

    input_s = input()

    while input_s not in ['1', '2', '3', '4', '5']:
        print('输入有误，请重新输入')
        print('> ', end='')
        input_s = input()

    return input_s


def main():
    while True:
        input_s = print_category()
        if input_s == '1':
            thread = TimeThread(1500)
            thread.start()
        elif input_s == '2':
            thread = TimeThread(600)
            thread.start()
        elif input_s == '3':
            thread = TimeThread(300)
            thread.start()
        elif input_s == '4':
            thread = TimeThread(60)
            thread.start()            
        else:
            return

        thread.join()


if __name__ == "__main__":
    main()
