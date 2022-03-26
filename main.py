from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from Screenshot import Screenshot_Clipping
from methods.options import set_options
from pyfiglet import Figlet
import time
import configparser
import os

#  Work with config.ini
config = configparser.ConfigParser()
dirpath = os.getcwd()
config.read(dirpath + r'\config.ini')


login = config.get('SETTINGS', 'LOGIN')
password = config.get('SETTINGS', 'PASSWORD')
#  End work with config.ini

#  Start a browser with preset options
driver = webdriver.Firefox(options=set_options())


def extra_page_continue():
    """
    Condition if an extra page comes out.
    """
    try:
        #  Find extra page
        driver.find_element(By.XPATH, '/html/body/div/div[2]/div[4]/a')
        return True
    except NoSuchElementException:
        return False


def school_mos_reg():
    """
    Make screenshots at schoolmosreg and save it.
    """
    print('Попали на главную страницу школьного портала')
    time.sleep(1.5)

    # Take a screenshot of main page and save it
    obs = Screenshot_Clipping.Screenshot()
    print('Делаем скриншот...')
    obs.full_Screenshot(driver, save_path=r'.', image_name='Main.png')  # noqa
    print('Сохранили скриншот в Main.png')

    # Go to academic performance
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/ul/li[1]/ul/li[3]/a').click()  # noqa
    print('Нажали на кнопку "Успеваемость" ')

    # Take a screenshot of a work week
    print('Делаем скриншот...')
    obs.full_Screenshot(driver, save_path=r'.', image_name='Academic_performance.png')  # noqa
    print('Скриншот сохранен в Academic_performance.png')

    # Go to marks
    driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[6]/ul/li[4]/a').click()  # noqa
    print('Нажали на кнопку "По семестрам"')

    # Take a screenshot of a marks
    print('Делаем скриншот...')
    obs.full_Screenshot(driver, save_path=r'.', image_name='All_Marks.png')  # noqa
    print('Скриншот сохранен в All_Marks.png')

    print('Закончили работу.')


def main():
    """
    Function for WebDriver.
    Parse schoolmosreg and get grades by subject.
    """
    try:
        # Get the google.com
        driver.get('https://www.google.com/')
        print('Попали в поисковик')
        time.sleep(1.5)

        # Enter a request
        driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys('школьный портал войти')  # noqa
        print('Ввели "школьный портал"')
        time.sleep(1.5)

        # CLick on the button "Find"
        driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]').click()   # noqa
        time.sleep(1.5)
        print('Кликнули на кнопку "Поиск"')

        try:
            # CLick on the search query
            driver.find_element(By.XPATH, '/html/body/div[7]/div/div[10]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/table/tbody/tr[1]/td[1]/div/h3/a').click()  # noqa
            time.sleep(1.8)
            print('Нашли страницу входа в школьный портал')
        except Exception as exc:
            print('Возникла непредвиденная ошибка!')
            print(f'Ошибка: {exc}')
            print('Пожалуйста, запустите заново программу!')

        # Enter a login at schoolmosreg
        loginning = driver.find_element(By.NAME, 'login')
        time.sleep(1.5)
        loginning.send_keys(login)
        print('Ввели логин')

        # Enter a password at schoolmosreg
        passwording = driver.find_element(By.NAME, 'password')
        time.sleep(1.5)
        passwording.send_keys(password)
        print('Ввели пароль')

        # Click on button 'Enter'
        enter = driver.find_element(By.XPATH, '/html/body/div/div/div/form/input[3]')  # noqa
        enter.click()
        time.sleep(2)
        print('Нажали на кнопку "Войти"')

        #  Check if extra page is exist
        if extra_page_continue() is True:
            print('Попали на лишнюю страницу, производим перенаправление')

            #  Redirect to main page
            time.sleep(1.5)
            continues = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[4]/a')  # noqa
            continues.click()

            school_mos_reg()

        elif extra_page_continue() is False:
            school_mos_reg()
        else:
            print('Something went wrong')

    except Exception as exc:
        print(exc)
    finally:
        #  Exit the browser
        driver.close()
        driver.quit()
        print('Закрыли браузер.')

        os.remove(dirpath + r'\geckodriver.log')


if __name__ == '__main__':
    f = Figlet(font="banner3-D")
    little = f.renderText('Little')
    f3ck = f.renderText('F3CK')
    MosReg = f.renderText('MosReg')
    print(little)
    print(f3ck)
    print(MosReg)

    main()
    a = input()
