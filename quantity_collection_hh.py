from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
import sqlite3
import datetime  
from datetime import datetime


total_region = None
region_hh_part_url = None
i = 1
datenow = datetime.today()
datenow = datenow.strftime("%d-%m-%Y")

def quantity_all_db():
    global total_region
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()

# Подсчет общего числа компаний в базе
    cursor.execute('SELECT COUNT(*) FROM DB_region_task') 
    total_region = cursor.fetchone()[0]
    connection.close()

def info_i_region():
    global i
    connection = sqlite3.connect('my_database.db', detect_types=sqlite3.PARSE_DECLTYPES)
    cursor = connection.cursor()

    global region_hh_part_url
    cursor.execute('SELECT region_hh_part_url FROM DB_region_task WHERE id = ?', (i,))
    results = cursor.fetchall()[0][0]
    region_hh_part_url = results


def analise_region_hh():
    global region_hh_part_url

    options = Options()
    options.page_load_strategy = 'eager'
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    specialization = ('java', 'js', 'SA', 'SRE', 'python', 'scala', 'ml', 
                      'qa_auto', 'qa_auto_backend', 'qa_auto_frontend', 'qa_auto_mobile', 'qa_auto_load', 
                      '.net', 'go', 'c++', 'data', 'mobile_ios', 'mobile_android', 'TL', 
                      'inf_sec', 'sup_eng', '1c', 'staff+', '1C_Devops', 'InfraOps', 'Delivery manager', 
                      'IT_GM_1', 'IT_GM_2', 'IT_GM_3', 'IT_GM_4', 'Tech_PM_1', 'Tech_PM_2', 
                      'DCE_1', 'DCE_2', 'DCE_3', 'DB_1', 'DB_2', 'Product Manager', 'Project Manager', 'BA', 'PA')
    len_specialization = len(specialization)

    url_specialization = ('https://hh.ru/search/resume?logic=normal&pos=position%2Cworkplaces&exp_period=all_time&from=suggest_post&filter_exp_period=all_time&relocation=living&gender=unknown&order_by=relevance&items_on_page=50&no_magic=true&professional_role=96&text=Java&',
                          'https://hh.ru/search/resume?text=Javascript&from=suggest_post&professional_role=96&no_magic=true&ored_clusters=true&order_by=relevance&items_on_page=50&logic=normal&pos=position%2Cworkplaces&exp_period=all_time&relocation=living&hhtmFrom=resume_search_result&hhtmFromLabel=resume_search_line&',
                          'https://hh.ru/search/resume?text=Системный+аналитик+&logic=normal&pos=position%2Cworkplaces&exp_period=all_time&exp_company_size=any&text=DWH&logic=except&pos=position%2Cworkplaces&exp_period=all_time&exp_company_size=any&from=suggest_post&filter_exp_period=all_time&relocation=living&age_from=&age_to=&professional_role=10&professional_role=148&gender=unknown&salary_from=&salary_to=&currency_code=RUR&order_by=relevance&items_on_page=50&no_magic=true&',
                          'https://hh.ru/search/resume?text=SRE&logic=normal&pos=position%2Cworkplaces&exp_period=all_time&exp_company_size=any&filter_exp_period=all_time&relocation=living&age_from=&age_to=&gender=unknown&salary_from=&salary_to=&currency_code=RUR&order_by=relevance&items_on_page=50&no_magic=true&',
                          'https://hh.ru/search/resume?no_magic=true&ored_clusters=true&order_by=relevance&items_on_page=50&logic=normal&pos=position%2Cworkplaces&exp_period=all_time&hhtmFrom=resume_search_result&hhtmFromLabel=resume_search_line&filter_exp_period=all_time&professional_role=96&relocation=living&text=Python&gender=unknown&',
                          'https://hh.ru/search/resume?text=Scala&from=suggest_post&professional_role=96&no_magic=true&ored_clusters=true&order_by=relevance&items_on_page=50&logic=normal&pos=position%2Cworkplaces&exp_period=all_time&relocation=living&hhtmFrom=resume_search_result&hhtmFromLabel=resume_search_line&',
                          'https://hh.ru/search/resume?logic=normal&pos=position%2Cworkplaces&exp_period=all_time&from=suggest_post&filter_exp_period=all_time&relocation=living&gender=unknown&order_by=relevance&items_on_page=50&no_magic=true&text=Ml&',
                          'https://hh.ru/search/resume?text=Java+kotlin+python+c%23+C%2B%2B+scala+go+swift+javascript+typescript&logic=any&pos=position%2Cworkplaces&exp_period=all_time&exp_company_size=any&filter_exp_period=all_time&relocation=living&age_from=&age_to=&professional_role=124&gender=unknown&salary_from=&salary_to=&currency_code=RUR&order_by=relevance&items_on_page=50&no_magic=true&',
                          'https://hh.ru/search/resume?text=Java+kotlin+python+c%23+C%2B%2B+scala+go+swift+javascript+typescript&logic=any&pos=position%2Cworkplaces&exp_period=all_time&exp_company_size=any&text=Qa+тестировщик&logic=any&pos=position%2Cworkplaces&exp_period=all_time&exp_company_size=any&text=Backend&logic=any&pos=workplaces%2Cposition&exp_period=all_time&exp_company_size=any&from=suggest_post&filter_exp_period=all_time&relocation=living&age_from=&age_to=&professional_role=124&gender=unknown&salary_from=&salary_to=&currency_code=RUR&order_by=relevance&items_on_page=50&no_magic=true&',
                          'https://hh.ru/search/resume?text=Java+kotlin+python+c%23+C%2B%2B+scala+go+swift+javascript+typescript&logic=any&pos=position%2Cworkplaces&exp_period=all_time&exp_company_size=any&text=Qa+тестировщик&logic=any&pos=position%2Cworkplaces&exp_period=all_time&exp_company_size=any&text=Frontend&logic=any&pos=workplaces%2Cposition&exp_period=all_time&exp_company_size=any&from=suggest_post&filter_exp_period=all_time&relocation=living&age_from=&age_to=&professional_role=124&gender=unknown&salary_from=&salary_to=&currency_code=RUR&order_by=relevance&items_on_page=50&no_magic=true&',
                          'https://hh.ru/search/resume?text=Java+kotlin+python+c%23+C%2B%2B+scala+go+swift+javascript+typescript&logic=any&pos=position%2Cworkplaces&exp_period=all_time&exp_company_size=any&text=Qa+тестировщик&logic=any&pos=position%2Cworkplaces&exp_period=all_time&exp_company_size=any&text=Mobile&logic=any&pos=workplaces%2Cposition&exp_period=all_time&exp_company_size=any&from=suggest_post&filter_exp_period=all_time&relocation=living&age_from=&age_to=&professional_role=124&gender=unknown&salary_from=&salary_to=&currency_code=RUR&order_by=relevance&items_on_page=50&no_magic=true&',
                          'https://hh.ru/search/resume?text=Java+kotlin+python+c%23+C%2B%2B+scala+go+swift+javascript+typescript&logic=any&pos=position%2Cworkplaces&exp_period=all_time&exp_company_size=any&text=Qa+тестировщик&logic=any&pos=position%2Cworkplaces&exp_period=all_time&exp_company_size=any&text=Load+нагрузочное&logic=any&pos=workplaces%2Cposition&exp_period=all_time&exp_company_size=any&from=suggest_post&filter_exp_period=all_time&relocation=living&age_from=&age_to=&professional_role=124&gender=unknown&salary_from=&salary_to=&currency_code=RUR&order_by=relevance&items_on_page=50&no_magic=true&',
                          'https://hh.ru/search/resume?text=.net&logic=normal&pos=position%2Cworkplaces&exp_period=all_time&exp_company_size=any&from=suggest_post&filter_exp_period=all_time&relocation=living&age_from=&age_to=&professional_role=96&gender=unknown&salary_from=&salary_to=&currency_code=RUR&order_by=relevance&items_on_page=50&no_magic=true&',
                          'https://hh.ru/search/resume?text=Golang&from=suggest_post&professional_role=96&no_magic=true&ored_clusters=true&order_by=relevance&items_on_page=50&logic=normal&pos=position%2Cworkplaces&exp_period=all_time&relocation=living&exp_company_size=any&hhtmFrom=resume_search_result&hhtmFromLabel=resume_search_line&',
                          'https://hh.ru/search/resume?text=C%2B%2B&professional_role=96&no_magic=true&ored_clusters=true&order_by=relevance&items_on_page=50&logic=normal&pos=position%2Cworkplaces&exp_period=all_time&exp_company_size=any&relocation=living&hhtmFrom=resume_search_result&hhtmFromLabel=resume_search_line&',
                          'https://hh.ru/search/resume?from=suggest_post&no_magic=true&ored_clusters=true&order_by=relevance&items_on_page=50&logic=normal&pos=position%2Cworkplaces&exp_period=all_time&hhtmFrom=resume_search_result&hhtmFromLabel=resume_search_line&filter_exp_period=all_time&relocation=living&text=Dwh&gender=unknown&',
                          'https://hh.ru/search/resume?no_magic=true&ored_clusters=true&order_by=relevance&items_on_page=50&logic=normal&pos=position%2Cworkplaces&exp_period=all_time&hhtmFrom=resume_search_result&hhtmFromLabel=resume_search_line&filter_exp_period=all_time&professional_role=96&relocation=living&text=Mobile+ios&gender=unknown&',
                          'https://hh.ru/search/resume?no_magic=true&ored_clusters=true&order_by=relevance&items_on_page=50&logic=normal&pos=position%2Cworkplaces&exp_period=all_time&hhtmFrom=resume_search_result&hhtmFromLabel=resume_search_line&filter_exp_period=all_time&professional_role=96&relocation=living&text=Mobile+android&gender=unknown&',
                          'https://hh.ru/search/resume?logic=normal&pos=position%2Cworkplaces&exp_period=all_time&filter_exp_period=all_time&relocation=living&gender=unknown&order_by=relevance&items_on_page=50&no_magic=true&text=Teamlead&',
                          'https://hh.ru/search/resume?logic=phrase&logic=normal&pos=position%2Cworkplaces&pos=position%2Cworkplaces&exp_period=all_time&exp_period=all_time&filter_exp_period=all_time&relocation=living&gender=unknown&order_by=publication_time&items_on_page=50&no_magic=true&professional_role=116&text=security&text=Information+security&',
                          'https://hh.ru/search/resume?text=Product+manager&logic=phrase&pos=workplaces%2Cposition&exp_period=all_time&exp_company_size=any&filter_exp_period=all_time&relocation=living&age_from=&age_to=&professional_role=73&gender=unknown&salary_from=&salary_to=&currency_code=RUR&order_by=publication_time&items_on_page=50&no_magic=true&',
                          'https://hh.ru/search/resume?logic=phrase&pos=workplaces%2Cposition&exp_period=all_time&filter_exp_period=all_time&relocation=living&gender=unknown&order_by=publication_time&items_on_page=50&no_magic=true&text=Project+manager&',
                          'https://hh.ru/search/resume?logic=phrase&pos=position%2Cworkplaces&exp_period=all_time&filter_exp_period=all_time&relocation=living&gender=unknown&order_by=publication_time&items_on_page=50&no_magic=true&professional_role=150&text=Business+analyst&',
                          'https://hh.ru/search/resume?from=suggest_post&no_magic=true&ored_clusters=true&order_by=publication_time&items_on_page=50&logic=phrase&pos=position%2Cworkplaces&exp_period=all_time&relocation=living&hhtmFrom=resume_search_result&hhtmFromLabel=resume_search_line&filter_exp_period=all_time&gender=unknown&professional_role=164&text=Product+analyst&',
                          'https://hh.ru/search/resume?logic=normal&pos=full_text&exp_period=all_time&filter_exp_period=all_time&relocation=living&gender=unknown&order_by=relevance&items_on_page=50&no_magic=true&professional_role=69&professional_role=118&professional_role=117&professional_role=17&professional_role=171&professional_role=153&text=&',
                          'https://hh.ru/search/resume?no_magic=true&ored_clusters=true&order_by=relevance&items_on_page=50&relocation=living&hhtmFrom=resume_search_result&hhtmFromLabel=resume_search_line&logic=any&logic=normal&pos=workplaces%2Cposition&pos=position%2Cworkplaces&exp_period=all_time&exp_period=all_time&filter_exp_period=all_time&gender=unknown&professional_role=121&text=support+engineer&text=Helpdesk+Поддержка+SQL&',
                          'https://hh.ru/search/resume?text=1С&professional_role=96&no_magic=true&ored_clusters=true&order_by=relevance&items_on_page=50&relocation=living&logic=normal&pos=position%2Cworkplaces&exp_period=all_time&skill=1824216&hhtmFrom=resume_search_result&hhtmFromLabel=resume_search_line&',
                          'https://hh.ru/search/resume?no_magic=true&ored_clusters=true&order_by=relevance&relocation=living&context_predicted_vacancy_id=101628321&hhtmFrom=resume_search_result&hhtmFromLabel=resume_search_line&text=%22tech+lead%22+OR+%22solution+architect%22&logic=normal&pos=workplace_position&exp_period=all_time&exp_company_size=anyhttps://spb.hh.ru/search/resume?no_magic=true&ored_clusters=true&order_by=relevance&context_predicted_vacancy_id=101628321&hhtmFrom=resume_search_result&hhtmFromLabel=resume_search_line&text=%22tech+lead%22+OR+%22solution+architect%22&logic=normal&pos=workplace_position&exp_period=all_time&exp_company_size=any&',
                          'https://hh.ru/search/resume?no_magic=true&ored_clusters=true&order_by=relevance&logic=normal&pos=full_text&exp_period=all_time&context_predicted_vacancy_id=98263876&hhtmFrom=resume_search_result&hhtmFromLabel=resume_search_line&filter_exp_period=all_time&relocation=living&gender=unknown&professional_role=113&professional_role=160&skill=730&skill=1063&skill=1508&text=Linux+AND+PostgreSQL+AND+Cisco+AND+1%D0%A1+AND+1%D0%A1+Devops&',
                          'https://hh.ru/search/resume?no_magic=true&ored_clusters=true&order_by=relevance&items_on_page=50&context_predicted_vacancy_id=105093000&hhtmFrom=resume_search_result&hhtmFromLabel=resume_search_line&logic=any&logic=any&logic=any&logic=any&pos=full_text&pos=full_text&pos=full_text&pos=full_text&exp_period=all_time&exp_period=all_time&exp_period=all_time&exp_period=all_time&filter_exp_period=all_time&relocation=living&gender=unknown&text=Сетевой+инженер+Инженер+инфраструктуры+Network+Engineer&text=OSPF+BGP&text=Cisco+ASA+Juniper+SRX+Palo-Alto&text=Python+Ansible+автоматизация+скрипты&',
                          'https://hh.ru/search/resume?no_magic=true&ored_clusters=true&order_by=publication_time&exclude_suitable_hidden=true&context_predicted_vacancy_id=103054359&hhtmFrom=resume_search_result&hhtmFromLabel=resume_search_line&text=коуч+agile+scrum+скрам+RTE+coach+Delivery+"агент+изменений"+"change+agent"&logic=any&pos=workplace_position%2Cposition&exp_period=last_three_years&exp_company_size=any&text=KANBAN+SCRUM+SAFE+Less&logic=any&pos=workplace_description&exp_period=last_year&exp_company_size=any&',
                          'https://hh.ru/search/resume?exp_period=all_time&logic=any&no_magic=true&order_by=relevance&ored_clusters=true&pos=position%2Cworkplace_description&filter_exp_period=all_time&relocation=living&text=CTO&age_to=45&gender=unknown&',
                          'https://hh.ru/search/resume?age_to=45&exp_period=all_time&experience=moreThan6&logic=any&no_magic=true&order_by=relevance&ored_clusters=true&pos=position%2Cworkplace_description&professional_role=125&professional_role=104&professional_role=36&relocation=living&text=CTO&',
                          'https://hh.ru/search/resume?job_search_status=active_search&job_search_status=looking_for_offers&job_search_status=unknown&no_magic=true&order_by=relevance&ored_clusters=true&resume=ef97ff19000d788e5d0001332e34696b77627a&experience=moreThan6&filter_exp_period=all_time&professional_role=26&professional_role=87&professional_role=36&relocation=living&age_to=46&gender=unknown&',
                          'https://hh.ru/search/resume?isDefaultArea=true&ored_clusters=true&order_by=relevance&context_predicted_vacancy_id=106324893&logic=phrase&logic=any&pos=workplace_position%2Cworkplace_description&pos=workplace_organization&exp_period=last_three_years&exp_period=all_time&disableBrowserCache=true&hhtmFrom=resume_search_result&filter_exp_period=all_time&relocation=living&gender=unknown&experience=between3And6&experience=moreThan6&text=Руководитель+разработки&text=Авито+озон+яндекс+сбер+сбербанк+сбермаркет+вк+банк+sber+sberbank+avito+yandex+ozon+vk+mail+bank+sberdevices+x5+циан+mail+домлкик&exp_company_size=large&exp_company_size=any&',
                          'https://hh.ru/search/resume?exp_period=all_time&items_on_page=50&logic=phrase&no_magic=true&order_by=relevance&ored_clusters=true&pos=position%2Cworkplace_position&filter_exp_period=all_time&relocation=living&text=Technical+product+manager&gender=unknown&',
                          'https://hh.ru/search/resume?exp_period=last_three_years&exp_period=all_time&items_on_page=50&logic=normal&logic=normal&no_magic=true&order_by=relevance&ored_clusters=true&pos=position%2Cworkplace_position&pos=workplace_position&filter_exp_period=all_time&relocation=living&gender=unknown&experience=between3And6&experience=moreThan6&text=Product+manager&text=%22Разработчик%22+OR+%22системный+аналитик%22+OR+%22engineer%22+OR+%22developer%22&',                            
                          'https://hh.ru/search/resume?ored_clusters=true&order_by=relevance&search_period=30&logic=normal&pos=full_text&exp_period=all_time&hhtmFrom=resume_search_result&hhtmFromLabel=resume_search_line&filter_exp_period=all_time&relocation=living&gender=unknown&text=%D0%B8%D0%BD%D0%B6%D0%B5%D0%BD%D0%B5%D1%80+%D0%A6%D0%9E%D0%94&',
                          'https://hh.ru/search/resume?exp_period=all_time&logic=normal&no_magic=true&order_by=relevance&ored_clusters=true&pos=full_text&filter_exp_period=all_time&relocation=living&gender=unknown&text=%D0%B8%D0%BD%D0%B6%D0%B5%D0%BD%D0%B5%D1%80+%D0%B4%D0%B0%D1%82%D0%B0+%D1%86%D0%B5%D0%BD%D1%82%D1%80%D0%B0&',
                          'https://hh.ru/search/resume?exp_period=all_time&logic=normal&no_magic=true&order_by=relevance&ored_clusters=true&pos=full_text&relocation=living&text=%D1%81%D0%B5%D1%80%D0%B2%D0%B5%D1%80%D0%BD%D1%8B%D0%B9+%D0%B8%D0%BD%D0%B6%D0%B5%D0%BD%D0%B5%D1%80&',
                          'https://hh.ru/search/resume?exp_period=all_time&logic=normal&no_magic=true&order_by=relevance&ored_clusters=true&pos=full_text&relocation=living&text=PostgreSQL+%D0%90%D0%B4%D0%BC%D0%B8%D0%BD%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%82%D0%BE%D1%80+%D0%B1%D0%B0%D0%B7+%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85&',
                          'https://hh.ru/search/resume?exp_period=all_time&logic=normal&no_magic=true&order_by=relevance&ored_clusters=true&pos=full_text&filter_exp_period=all_time&relocation=living_or_relocation&gender=unknown&text=Oracle+SQL&',
                          'https://hh.ru/search/resume?logic=normal&pos=full_text&exp_period=all_time&show_conditions=false&filter_exp_period=all_time&relocation=living_or_relocation&gender=unknown&order_by=relevance&search_period=0&items_on_page=50&hhtmFrom=resume_search_form&professional_role=73&text=Product+Manager&',
                          'https://hh.ru/search/resume?text=Project+Manager&professional_role=107&ored_clusters=true&order_by=relevance&items_on_page=50&search_period=0&logic=normal&pos=full_text&exp_period=all_time&context_predicted_vacancy_id=101628980&hhtmFrom=resume_search_result&hhtmFromLabel=resume_search_line&',
                          'https://hh.ru/search/resume?text=%D0%91%D0%B8%D0%B7%D0%BD%D0%B5%D1%81-%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D1%82%D0%B8%D0%BA+OR+business+analyst&logic=normal&pos=position%2Cworkplace_position&exp_period=all_time&exp_company_size=any&show_conditions=true&filter_exp_period=all_time&relocation=living_or_relocation&age_from=&age_to=&gender=unknown&salary_from=&salary_to=&currency_code=RUR&order_by=relevance&search_period=0&items_on_page=50&hhtmFrom=resume_search_form&',
                          'https://hh.ru/search/resume?text=%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D0%BE%D0%B2%D1%8B%D0%B9+%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D1%82%D0%B8%D0%BA&logic=normal&pos=position%2Cworkplace_position&exp_period=all_time&exp_company_size=any&show_conditions=true&filter_exp_period=all_time&relocation=living_or_relocation&age_from=&age_to=&gender=unknown&salary_from=&salary_to=&currency_code=RUR&order_by=relevance&search_period=0&items_on_page=50&hhtmFrom=resume_search_form&')

    # Опыт
    experience_part_url = ('&experience=moreThan6&experience=between3And6')
        #варианты опыта &experience=noExperience', '&experience=moreThan6&experience=between3And6&experience=between1And3&'

    # Период обновления резюме
    search_period_part_url = ("&search_period=0")
    #search_period_part_url = ('&search_period=-1&date_from=01.08.2023&date_to=31.01.2024')

    x = 0
    while x <= (len_specialization - 1):
        specialization_i = specialization[x]
        url_specialization_i = url_specialization[x]

        driver.get(url_specialization_i + region_hh_part_url + experience_part_url[0] + search_period_part_url)

        time.sleep(5)
        
        try:    
            search_string = driver.find_element(By.CSS_SELECTOR,'#HH-React-Root > div > div.magritte-redesign > div.HH-MainContent.HH-Supernova-MainContent > div.main-content.main-content_broad-spacing > div.magritte-grid-layout___JiVGG_2-2-11 > div > div.magritte-grid-column___rhP24_2-2-11.magritte-grid-column_xs-4___eVCYh_2-2-11.magritte-grid-column_s-8___vihhu_2-2-11.magritte-grid-column_m-12___KQXbY_2-2-11.magritte-grid-column_l-12___vHTF5_2-2-11.magritte-grid-column_xl-12___SC-2y_2-2-11.magritte-grid-column_xxl-12___faE5U_2-2-11 > div > div.magritte-text-alignment-left___BreG5_6-0-0 > h1').text
            quantity_all_hh = ""
            for a in search_string:
                if a.isdigit():
                    quantity_all_hh = quantity_all_hh + a
        except:
            quantity_all_hh = '0'

        connection = sqlite3.connect('my_database.db', detect_types=sqlite3.PARSE_DECLTYPES)
        cursor = connection.cursor() 
        cursor.execute('INSERT INTO quantity_region_task (date, quantity, site, stack, region_id) VALUES(?, ?, ?, ?, ?)', (datenow, quantity_all_hh, 'hh', specialization_i + '_more3year', i))
        connection.commit()
        connection.close()
        x += 1
    
    driver.close()
    driver.quit()

def cycle_i():
    global i
    global total_region
    
    while i <= total_region:
        info_i_region()
        analise_region_hh()
        i += 1

quantity_all_db()
cycle_i()
