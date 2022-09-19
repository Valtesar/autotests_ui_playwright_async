from playwright.sync_api import Page, expect


class DocsPage:
    def __init__(self, page: Page):
        self.page = page

    def get_active_button(self):
        """Возвращает название текущей нажатой кнопки"""
        pass

    def get_files_sizes(self):
        """Метод собирает значения размера файлов на странице в список"""
        pass

    def pick_biggest_file(self):
        """Выбирает самый большой файл из списка"""
        pass

    def try_download_file(self):
        """Метод скачивает файл со страницы"""
        pass
