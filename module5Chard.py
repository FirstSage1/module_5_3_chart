# Модуль 5 . Доп. задание.
# ========================
import time
class User:
    """
    Класс пользователя,содержащий атрибуты: логин, пароль,возраст.
    """
    def __init__(self, nickname:str, password:int, age:int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
        print(self)

    def __str__(self):
        return self.nickname

    def __repr__(self):
        return repr(self.nickname)

class Video:
    def __init__(self, title:str, duration:int, time_now=0,adult_mode=bool(False)):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title == other.title

    def __str__(self):
        return f'{self.title}'

    def dur(self):
        return self.duration

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname: str, password: int):
        for i in self.users:
            if i.nickname == nickname and i.password == hash(password):
                self.current_user = i
                return self.current_user
    def register(self, nickname: str, password: int, age: int):
        user = User(nickname, password, age)
        if user not in self.users:
            self.users.append(user)
            self.log_out()
            self.log_in(nickname, password)
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            if i not in self.videos:
                self.videos.append(i)
            else:
                print(f'Видео с названием {i.title} уже существует')

    def get_videos(self, text):
        list_videos = []
        for i in self.videos:
            if text.lower() in i.title.lower():
                list_videos.append(str(i))
        return list_videos

    def watch_video(self, video):
        if self.current_user and self.current_user.age < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
        elif self.current_user:
            for i in self.videos:
                if video in i.title:
                    dur = Video.dur(i)
                    for j in range(1, dur + 1):
                        print(j, end=' ')
                        time.sleep(1)
                    print('Конец видео')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')

if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')




