import requests
from bs4 import BeautifulSoup
import json


'''Below is the api which return the 10 entries per page'''
base_url = 'https://www.practo.com/mumbai/doctors?page={}'




doctor_data = []


'''
Iterate over each page and fetch doctors details
'''
for page_num in range(1, 11):
    url = base_url.format(page_num)
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        doctor_cards = soup.find_all('div', class_='listing-doctor-card')
        for card in doctor_cards:
            info_section = card.find('div', class_='info-section')
            if info_section:
                doctor_name = info_section.find('h2', class_='doctor-name').get_text(strip=True)
                specialty_section = info_section.find('div', class_='u-d-flex')
                specialty = specialty_section.find('span').get_text(strip=True) if specialty_section else "N/A"
                experience = info_section.find('div', {'data-qa-id': 'doctor_experience'}).get_text(strip=True) if info_section.find('div', {'data-qa-id': 'doctor_experience'}) else "N/A"
                locality = info_section.find('span', {'data-qa-id': 'practice_locality'}).get_text(strip=True) if info_section.find('span', {'data-qa-id': 'practice_locality'}) else "N/A"
                city = info_section.find('span', {'data-qa-id': 'practice_city'}).get_text(strip=True) if info_section.find('span', {'data-qa-id': 'practice_city'}) else "N/A"
                clinic_name = info_section.find('span', {'data-qa-id': 'doctor_clinic_name'}).get_text(strip=True) if info_section.find('span', {'data-qa-id': 'doctor_clinic_name'}) else "N/A"
                consultation_fee = info_section.find('span', {'data-qa-id': 'actual_consultation_fee'}).get_text(strip=True) if info_section.find('span', {'data-qa-id': 'actual_consultation_fee'}) else "N/A"
                recommendation = info_section.find('span', {'data-qa-id': 'doctor_recommendation'}).get_text(strip=True) if info_section.find('span', {'data-qa-id': 'doctor_recommendation'}) else "N/A"
                patient_stories = info_section.find('span', {'data-qa-id': 'total_feedback'}).get_text(strip=True) if info_section.find('span', {'data-qa-id': 'total_feedback'}) else "N/A"

        
                doctor_data.append({
                    'doctor_name': doctor_name,
                    'specialty': specialty,
                    'experience': experience,
                    'locality': locality,
                    'city': city,
                    'clinic_name': clinic_name,
                    'consultation_fee': consultation_fee,
                    'recommendation': recommendation,
                    'patient_stories': patient_stories
                })
    else:
        print(f"Failed to retrieve the webpage for page {page_num}. Status code: {response.status_code}")
with open('doctors_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(doctor_data, json_file, ensure_ascii=False, indent=4)

print("Data has been scraped and saved to 'doctors_data.json'")
