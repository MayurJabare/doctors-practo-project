from django.shortcuts import render, HttpResponse
from .models import DoctorInfo
from .forms import DoctorFilterForm
import json, requests
from bs4 import BeautifulSoup



data=[
    {
        "doctor_name": "Dr. Reshma Phulwar",
        "specialty": "Dentist",
        "experience": "28years experience overall",
        "locality": "Chembur,",
        "city": "Mumbai",
        "clinic_name": "32 Pearls Dental Clinic",
        "consultation_fee": "₹500",
        "recommendation": "96%",
        "patient_stories": "383Patient Stories"
    },
    {
        "doctor_name": "Dr. Parag M. Khatri",
        "specialty": "Dentist",
        "experience": "31years experience overall",
        "locality": "Andheri East,",
        "city": "Mumbai",
        "clinic_name": "Dental Square",
        "consultation_fee": "₹500",
        "recommendation": "99%",
        "patient_stories": "344Patient Stories"
    },
    {
        "doctor_name": "Dr. Rajesh Shetty",
        "specialty": "Dentist",
        "experience": "28years experience overall",
        "locality": "Bandra West,",
        "city": "Mumbai",
        "clinic_name": "Dazzle Dental Clinic",
        "consultation_fee": "N/A",
        "recommendation": "98%",
        "patient_stories": "210Patient Stories"
    },
    {
        "doctor_name": "Dr. Manish Kachhara",
        "specialty": "Dentist",
        "experience": "22years experience overall",
        "locality": "Ghatkopar East,",
        "city": "Mumbai",
        "clinic_name": "Dental Solutions",
        "consultation_fee": "₹500",
        "recommendation": "99%",
        "patient_stories": "229Patient Stories"
    },
    {
        "doctor_name": "Dr. Manoj Bodhwani",
        "specialty": "Dentist",
        "experience": "18years experience overall",
        "locality": "Khar West,",
        "city": "Mumbai",
        "clinic_name": "Tooth Avenue",
        "consultation_fee": "₹500",
        "recommendation": "98%",
        "patient_stories": "167Patient Stories"
    },
    {
        "doctor_name": "Dr. Bhavin Shah",
        "specialty": "Dentist",
        "experience": "15years experience overall",
        "locality": "Goregaon East,",
        "city": "Mumbai",
        "clinic_name": "American Dental Practices",
        "consultation_fee": "₹500",
        "recommendation": "99%",
        "patient_stories": "158Patient Stories"
    },
    {
        "doctor_name": "Dr. Manish S. Sonawane",
        "specialty": "Dentist",
        "experience": "19years experience overall",
        "locality": "Lokhandwala,",
        "city": "Mumbai",
        "clinic_name": "Millennium Smile Dental Clinic",
        "consultation_fee": "₹500",
        "recommendation": "98%",
        "patient_stories": "66Patient Stories"
    },
    {
        "doctor_name": "Dr. Gautam Laud",
        "specialty": "Dentist",
        "experience": "26years experience overall",
        "locality": "Kemps Corner,",
        "city": "Mumbai",
        "clinic_name": "Dazzle Dental",
        "consultation_fee": "N/A",
        "recommendation": "98%",
        "patient_stories": "108Patient Stories"
    },
    {
        "doctor_name": "Dr. Varoon Jain",
        "specialty": "Dentist",
        "experience": "17years experience overall",
        "locality": "Goregaon West,",
        "city": "Mumbai",
        "clinic_name": "Smile Sutra  Multi Speciality Dental Clinic",
        "consultation_fee": "₹500",
        "recommendation": "98%",
        "patient_stories": "82Patient Stories"
    },
    {
        "doctor_name": "Dr. Amruta Save",
        "specialty": "Dentist",
        "experience": "15years experience overall",
        "locality": "Goregaon East,",
        "city": "Mumbai",
        "clinic_name": "American Dental Practices",
        "consultation_fee": "₹500",
        "recommendation": "N/A",
        "patient_stories": "N/A"
    },
    {
        "doctor_name": "Dr. Sanket Mehta",
        "specialty": "Dentist",
        "experience": "19years experience overall",
        "locality": "Matunga,",
        "city": "Mumbai",
        "clinic_name": "Smile Studio Dental Clinic",
        "consultation_fee": "N/A",
        "recommendation": "99%",
        "patient_stories": "466Patient Stories"
    },
    {
        "doctor_name": "Dr. Manisha Mehta",
        "specialty": "Dentist",
        "experience": "18years experience overall",
        "locality": "Worli,",
        "city": "Mumbai",
        "clinic_name": "Smile Studio Dental Clinic",
        "consultation_fee": "₹500",
        "recommendation": "98%",
        "patient_stories": "642Patient Stories"
    },
    {
        "doctor_name": "Dr. Jatin Ashar",
        "specialty": "Ophthalmologist",
        "experience": "21years experience overall",
        "locality": "Ghatkopar East,",
        "city": "Mumbai",
        "clinic_name": "Mumbai Eye Care Cornea and Lasik Centre",
        "consultation_fee": "N/A",
        "recommendation": "96%",
        "patient_stories": "758Patient Stories"
    },
    {
        "doctor_name": "Dr. Nita A Shah",
        "specialty": "Ophthalmologist",
        "experience": "39years experience overall",
        "locality": "Chembur East,",
        "city": "Mumbai",
        "clinic_name": "Aayush Eye Clinic - A Unit of Dr Agarwals Eye Hospital",
        "consultation_fee": "N/A",
        "recommendation": "89%",
        "patient_stories": "23Patient Stories"
    },
    {
        "doctor_name": "Dr. Aditi Agrawal",
        "specialty": "General Surgeon",
        "experience": "19years experience overall",
        "locality": "Borivali West,",
        "city": "Mumbai",
        "clinic_name": "Apex Superspeciality Hospitals",
        "consultation_fee": "N/A",
        "recommendation": "96%",
        "patient_stories": "118Patient Stories"
    },
    {
        "doctor_name": "Dr. Shradha Goel",
        "specialty": "Ophthalmologist",
        "experience": "22years experience overall",
        "locality": "Andheri West,",
        "city": "Mumbai",
        "clinic_name": "Arohi Eye Hospital",
        "consultation_fee": "N/A",
        "recommendation": "99%",
        "patient_stories": "170Patient Stories"
    },
    {
        "doctor_name": "Dr. Sambit Patnaik",
        "specialty": "General Surgeon",
        "experience": "20years experience overall",
        "locality": "Chembur,",
        "city": "Mumbai",
        "clinic_name": "Mumbai Piles Clinic",
        "consultation_fee": "N/A",
        "recommendation": "97%",
        "patient_stories": "549Patient Stories"
    },
    {
        "doctor_name": "Dr. Ankesh Sahetya",
        "specialty": "Gynecologist/Obstetrician",
        "experience": "16years experience overall",
        "locality": "Andheri West,",
        "city": "Mumbai",
        "clinic_name": "Pushpaa Hospital",
        "consultation_fee": "N/A",
        "recommendation": "100%",
        "patient_stories": "1363Patient Stories"
    },
    {
        "doctor_name": "Dr. Bhavik Shah",
        "specialty": "Ear-Nose-Throat (ENT) Specialist",
        "experience": "18years experience overall",
        "locality": "Chembur,",
        "city": "Mumbai",
        "clinic_name": "SRV-C Hospital",
        "consultation_fee": "N/A",
        "recommendation": "97%",
        "patient_stories": "60Patient Stories"
    },
    {
        "doctor_name": "Dr. Manjushri Kothekar",
        "specialty": "Gynecologist/Obstetrician",
        "experience": "20years experience overall",
        "locality": "Kurla West,",
        "city": "Mumbai",
        "clinic_name": "ART Fertility Clinics",
        "consultation_fee": "N/A",
        "recommendation": "100%",
        "patient_stories": "25Patient Stories"
    },
    {
        "doctor_name": "Dr. Akash Surana",
        "specialty": "Gynecologist/Obstetrician",
        "experience": "16years experience overall",
        "locality": "Kurla West,",
        "city": "Mumbai",
        "clinic_name": "ART Fertility Clinics",
        "consultation_fee": "N/A",
        "recommendation": "97%",
        "patient_stories": "9Patient Stories"
    },
    {
        "doctor_name": "Dr. R K Deshpande",
        "specialty": "General Surgeon",
        "experience": "42years experience overall",
        "locality": "Kemps Corner,",
        "city": "Mumbai",
        "clinic_name": "Asian Cancer Institute",
        "consultation_fee": "N/A",
        "recommendation": "98%",
        "patient_stories": "68Patient Stories"
    },
    {
        "doctor_name": "Dr. Raju Sahetya",
        "specialty": "Gynecologist/Obstetrician",
        "experience": "45years experience overall",
        "locality": "Andheri West,",
        "city": "Mumbai",
        "clinic_name": "Pushpaa Hospital",
        "consultation_fee": "N/A",
        "recommendation": "95%",
        "patient_stories": "32Patient Stories"
    },
    {
        "doctor_name": "Dr. Swapnil Tople",
        "specialty": "Urologist",
        "experience": "16years experience overall",
        "locality": "Wadala,",
        "city": "Mumbai",
        "clinic_name": "Galaxy Multispeciality Hospital",
        "consultation_fee": "N/A",
        "recommendation": "84%",
        "patient_stories": "10Patient Stories"
    },
    {
        "doctor_name": "Dr. S.Natarajan",
        "specialty": "Ophthalmologist",
        "experience": "40years experience overall",
        "locality": "Wadala,",
        "city": "Mumbai",
        "clinic_name": "Aditya Jyot Eye Hospital - A unit of Dr. Agarwals Eye Hospital",
        "consultation_fee": "N/A",
        "recommendation": "61%",
        "patient_stories": "9Patient Stories"
    },
    {
        "doctor_name": "Dr. Sanjeed C Pujary",
        "specialty": "Orthopedist",
        "experience": "17years experience overall",
        "locality": "Andheri West,",
        "city": "Mumbai",
        "clinic_name": "Thunga STH Hospital",
        "consultation_fee": "N/A",
        "recommendation": "100%",
        "patient_stories": "3Patient Stories"
    },
    {
        "doctor_name": "Dr. Richa Jagtap",
        "specialty": "Gynecologist/Obstetrician",
        "experience": "23years experience overall",
        "locality": "Kurla West,",
        "city": "Mumbai",
        "clinic_name": "ART Fertility Clinics",
        "consultation_fee": "N/A",
        "recommendation": "100%",
        "patient_stories": "N/A"
    },
    {
        "doctor_name": "Dr. Ayush Sharma",
        "specialty": "Spine Surgeon",
        "experience": "16years experience overall",
        "locality": "Wadala,",
        "city": "Mumbai",
        "clinic_name": "Galaxy Multispeciality Hospital",
        "consultation_fee": "N/A",
        "recommendation": "N/A",
        "patient_stories": "N/A"
    },
    {
        "doctor_name": "Dr. Bhushan Ghodke",
        "specialty": "Ophthalmologist",
        "experience": "16years experience overall",
        "locality": "Andheri West,",
        "city": "Mumbai",
        "clinic_name": "IKSHA Eye Care",
        "consultation_fee": "N/A",
        "recommendation": "99%",
        "patient_stories": "410Patient Stories"
    },
    {
        "doctor_name": "Dr. Nasreen Gite",
        "specialty": "Urologist",
        "experience": "17years experience overall",
        "locality": "Chembur,",
        "city": "Mumbai",
        "clinic_name": "SRV-C Hospital",
        "consultation_fee": "N/A",
        "recommendation": "100%",
        "patient_stories": "2Patient Stories"
    },
    {
        "doctor_name": "Dr. Kavita Rao",
        "specialty": "Ophthalmologist",
        "experience": "28years experience overall",
        "locality": "Wadala,",
        "city": "Mumbai",
        "clinic_name": "Aditya Jyot Eye Hospital - A unit of Dr. Agarwals Eye Hospital",
        "consultation_fee": "N/A",
        "recommendation": "100%",
        "patient_stories": "N/A"
    },
    {
        "doctor_name": "Dr. Chintan Hegde",
        "specialty": "Orthopedist",
        "experience": "16years experience overall",
        "locality": "Andheri West,",
        "city": "Mumbai",
        "clinic_name": "Thunga STH Hospital",
        "consultation_fee": "N/A",
        "recommendation": "50%",
        "patient_stories": "6Patient Stories"
    },
    {
        "doctor_name": "Dr. Sanjay Sharma",
        "specialty": "General Surgeon",
        "experience": "48years experience overall",
        "locality": "Kemps Corner,",
        "city": "Mumbai",
        "clinic_name": "Asian Cancer Institute",
        "consultation_fee": "N/A",
        "recommendation": "80%",
        "patient_stories": "3Patient Stories"
    },
    {
        "doctor_name": "Dr. Pankaj Gandhi",
        "specialty": "General Surgeon",
        "experience": "23years experience overall",
        "locality": "Goregaon West,",
        "city": "Mumbai",
        "clinic_name": "SRV Hospitals Goregaon",
        "consultation_fee": "N/A",
        "recommendation": "100%",
        "patient_stories": "3Patient Stories"
    },
    {
        "doctor_name": "Dr. Sachin Bhat",
        "specialty": "Orthopedist",
        "experience": "26years experience overall",
        "locality": "Goregaon West,",
        "city": "Mumbai",
        "clinic_name": "SRV Hospitals Goregaon",
        "consultation_fee": "N/A",
        "recommendation": "100%",
        "patient_stories": "N/A"
    },
    {
        "doctor_name": "Dr. Siddharth V. Nachane",
        "specialty": "General Surgeon",
        "experience": "16years experience overall",
        "locality": "Wadala,",
        "city": "Mumbai",
        "clinic_name": "Galaxy Multispeciality Hospital",
        "consultation_fee": "N/A",
        "recommendation": "100%",
        "patient_stories": "N/A"
    },
    {
        "doctor_name": "Dr. Vinaykumar Thati",
        "specialty": "Laparoscopic Surgeon",
        "experience": "23years experience overall",
        "locality": "Andheri West,",
        "city": "Mumbai",
        "clinic_name": "Thunga STH Hospital",
        "consultation_fee": "N/A",
        "recommendation": "N/A",
        "patient_stories": "N/A"
    },
    {
        "doctor_name": "Dr. Sahay Chandra Bansh",
        "specialty": "General Surgeon",
        "experience": "44years experience overall",
        "locality": "Borivali East,",
        "city": "Mumbai",
        "clinic_name": "Apex MultiSpeciality Hospital",
        "consultation_fee": "N/A",
        "recommendation": "N/A",
        "patient_stories": "N/A"
    },
    {
        "doctor_name": "Dr. Ashwini S Nabar",
        "specialty": "Gynecologist/Obstetrician",
        "experience": "28years experience overall",
        "locality": "Andheri West,",
        "city": "Mumbai",
        "clinic_name": "Thunga STH Hospital",
        "consultation_fee": "N/A",
        "recommendation": "100%",
        "patient_stories": "1Patient Story"
    },
    {
        "doctor_name": "Dr. Harsh Parekh",
        "specialty": "Endocrinologist",
        "experience": "15years experience overall",
        "locality": "Andheri West,",
        "city": "Mumbai",
        "clinic_name": "Thunga STH Hospital",
        "consultation_fee": "N/A",
        "recommendation": "100%",
        "patient_stories": "1Patient Story"
    },
    {
        "doctor_name": "Dr. Padagatti Shridhar",
        "specialty": "Cardiac Surgeon",
        "experience": "28years experience overall",
        "locality": "Mulund West,",
        "city": "Mumbai",
        "clinic_name": "Apex Hospitals",
        "consultation_fee": "N/A",
        "recommendation": "100%",
        "patient_stories": "2Patient Stories"
    },
    {
        "doctor_name": "Dr. Chaudhary Vaishali Ninad",
        "specialty": "Gynecologist/Obstetrician",
        "experience": "27years experience overall",
        "locality": "Andheri West,",
        "city": "Mumbai",
        "clinic_name": "Thunga STH Hospital",
        "consultation_fee": "N/A",
        "recommendation": "100%",
        "patient_stories": "N/A"
    },
    {
        "doctor_name": "Dr. Lalit Patil",
        "specialty": "Gynecologist/Obstetrician",
        "experience": "22years experience overall",
        "locality": "Wadala,",
        "city": "Mumbai",
        "clinic_name": "Galaxy Multispeciality Hospital",
        "consultation_fee": "N/A",
        "recommendation": "100%",
        "patient_stories": "N/A"
    },
    {
        "doctor_name": "Dr. Samir Parekh",
        "specialty": "Spine Surgeon",
        "experience": "21years experience overall",
        "locality": "Kandivali,",
        "city": "Mumbai",
        "clinic_name": "Apex Hospitals Kandivali",
        "consultation_fee": "N/A",
        "recommendation": "100%",
        "patient_stories": "2Patient Stories"
    },
    {
        "doctor_name": "Dr. Anupam Shukla",
        "specialty": "General Surgeon",
        "experience": "15years experience overall",
        "locality": "Kandivali,",
        "city": "Mumbai",
        "clinic_name": "Apex Hospitals Kandivali",
        "consultation_fee": "N/A",
        "recommendation": "N/A",
        "patient_stories": "N/A"
    },
    {
        "doctor_name": "Dr. Vivek Patel",
        "specialty": "Neurosurgeon",
        "experience": "19years experience overall",
        "locality": "Borivali West,",
        "city": "Mumbai",
        "clinic_name": "Apex Superspeciality Hospitals",
        "consultation_fee": "N/A",
        "recommendation": "N/A",
        "patient_stories": "N/A"
    },
    {
        "doctor_name": "Dr. Deokar Ami Atul",
        "specialty": "Pediatrician",
        "experience": "27years experience overall",
        "locality": "Andheri West,",
        "city": "Mumbai",
        "clinic_name": "Thunga STH Hospital",
        "consultation_fee": "N/A",
        "recommendation": "N/A",
        "patient_stories": "N/A"
    },
    {
        "doctor_name": "Dr. Jaydeep A Walinjkar",
        "specialty": "Ophthalmologist",
        "experience": "11years experience overall",
        "locality": "Wadala,",
        "city": "Mumbai",
        "clinic_name": "Aditya Jyot Eye Hospital - A unit of Dr. Agarwals Eye Hospital",
        "consultation_fee": "N/A",
        "recommendation": "N/A",
        "patient_stories": "N/A"
    },
    {
        "doctor_name": "Dr. Ravindra Ghule",
        "specialty": "Cardiologist",
        "experience": "17years experience overall",
        "locality": "Mulund West,",
        "city": "Mumbai",
        "clinic_name": "Apex Hospitals",
        "consultation_fee": "N/A",
        "recommendation": "N/A",
        "patient_stories": "N/A"
    },
    {
        "doctor_name": "Dr. Simit Vora",
        "specialty": "General Surgeon",
        "experience": "18years experience overall",
        "locality": "Borivali West,",
        "city": "Mumbai",
        "clinic_name": "Apex Superspeciality Hospitals",
        "consultation_fee": "N/A",
        "recommendation": "50%",
        "patient_stories": "2Patient Stories"
    },
    {
        "doctor_name": "Dr. Nagraj S. Shetty",
        "specialty": "Orthopedist",
        "experience": "22years experience overall",
        "locality": "Andheri West,",
        "city": "Mumbai",
        "clinic_name": "Thunga STH Hospital",
        "consultation_fee": "N/A",
        "recommendation": "97%",
        "patient_stories": "17Patient Stories"
    },
    {
        "doctor_name": "Dr. Dhanashree Mane Dhabalia",
        "specialty": "Ophthalmologist",
        "experience": "16years experience overall",
        "locality": "Andheri West,",
        "city": "Mumbai",
        "clinic_name": "IKSHA Eye Care",
        "consultation_fee": "N/A",
        "recommendation": "100%",
        "patient_stories": "6Patient Stories"
    },
    {
        "doctor_name": "Dr. Nita Shanbhag",
        "specialty": "Ophthalmologist",
        "experience": "35years experience overall",
        "locality": "Chembur East,",
        "city": "Mumbai",
        "clinic_name": "Aayush Eye Clinic - A Unit of Dr Agarwals Eye Hospital",
        "consultation_fee": "N/A",
        "recommendation": "100%",
        "patient_stories": "2Patient Stories"
    },
    {
        "doctor_name": "Dr. Sachin Pahade",
        "specialty": "Urologist",
        "experience": "23years experience overall",
        "locality": "Goregaon West,",
        "city": "Mumbai",
        "clinic_name": "SRV Hospitals Goregaon",
        "consultation_fee": "N/A",
        "recommendation": "100%",
        "patient_stories": "6Patient Stories"
    },
    {
        "doctor_name": "Dr. Haresh Asnani",
        "specialty": "Ophthalmologist",
        "experience": "38years experience overall",
        "locality": "Chembur East,",
        "city": "Mumbai",
        "clinic_name": "Aayush Eye Clinic - A Unit of Dr Agarwals Eye Hospital",
        "consultation_fee": "N/A",
        "recommendation": "100%",
        "patient_stories": "1Patient Story"
    },
    {
        "doctor_name": "Dr. Neeraj Kumar Tulara",
        "specialty": "General Physician",
        "experience": "23years experience overall",
        "locality": "Powai,",
        "city": "Mumbai",
        "clinic_name": "Dr L H Hiranandani Hospital",
        "consultation_fee": "N/A",
        "recommendation": "94%",
        "patient_stories": "73Patient Stories"
    },
    {
        "doctor_name": "Dr. Vimal J.Pahuja",
        "specialty": "General Physician",
        "experience": "19years experience overall",
        "locality": "Powai,",
        "city": "Mumbai",
        "clinic_name": "Dr L H Hiranandani Hospital",
        "consultation_fee": "N/A",
        "recommendation": "89%",
        "patient_stories": "10Patient Stories"
    },
    {
        "doctor_name": "Dr. Lakin Vira",
        "specialty": "General Surgeon",
        "experience": "15years experience overall",
        "locality": "Tardeo,",
        "city": "Mumbai",
        "clinic_name": "Apollo Spectra Hospitals",
        "consultation_fee": "N/A",
        "recommendation": "100%",
        "patient_stories": "23Patient Stories"
    },
    {
        "doctor_name": "Dr. Shalini Suralkar",
        "specialty": "General Physician",
        "experience": "18years experience overall",
        "locality": "Powai,",
        "city": "Mumbai",
        "clinic_name": "Dr L H Hiranandani Hospital",
        "consultation_fee": "N/A",
        "recommendation": "78%",
        "patient_stories": "6Patient Stories"
    },
    {
        "doctor_name": "Dr. Pankaj Mistry",
        "specialty": "General Physician",
        "experience": "42years experience overall",
        "locality": "Vileparle East,",
        "city": "Mumbai",
        "clinic_name": "Keep Fit Clinic",
        "consultation_fee": "N/A",
        "recommendation": "97%",
        "patient_stories": "49Patient Stories"
    },
    {
        "doctor_name": "Dr. Bhavik Saglani",
        "specialty": "General Physician",
        "experience": "15years experience overall",
        "locality": "Tardeo,",
        "city": "Mumbai",
        "clinic_name": "Apollo Spectra Hospitals",
        "consultation_fee": "N/A",
        "recommendation": "100%",
        "patient_stories": "30Patient Stories"
    },
    {
        "doctor_name": "Dr. Ravindra Hodarkar",
        "specialty": "Urologist",
        "experience": "47years experience overall",
        "locality": "Chembur,",
        "city": "Mumbai",
        "clinic_name": "Apollo Spectra Hospitals",
        "consultation_fee": "N/A",
        "recommendation": "44%",
        "patient_stories": "10Patient Stories"
    },
    {
        "doctor_name": "Dr. Rajesh Shinde",
        "specialty": "General Physician",
        "experience": "29years experience overall",
        "locality": "Borivali West,",
        "city": "Mumbai",
        "clinic_name": "Healthspring Clinic - Borivali",
        "consultation_fee": "N/A",
        "recommendation": "96%",
        "patient_stories": "25Patient Stories"
    },
    {
        "doctor_name": "Dr. Rajanshu Tiwari",
        "specialty": "General Physician",
        "experience": "14years experience overall",
        "locality": "Chembur East,",
        "city": "Mumbai",
        "clinic_name": "Dr. Tiwari's Clinic",
        "consultation_fee": "N/A",
        "recommendation": "93%",
        "patient_stories": "69Patient Stories"
    },
    {
        "doctor_name": "Dr. Shubhashree Patil",
        "specialty": "Diabetologist",
        "experience": "19years experience overall",
        "locality": "Andheri East,",
        "city": "Mumbai",
        "clinic_name": "Diabetes And Wellness Clinic",
        "consultation_fee": "N/A",
        "recommendation": "99%",
        "patient_stories": "266Patient Stories"
    },
    {
        "doctor_name": "Dr. Seema S. Masrani",
        "specialty": "General Physician",
        "experience": "31years experience overall",
        "locality": "Kandivali West,",
        "city": "Mumbai",
        "clinic_name": "Dr. Seema S. Masrani's Clinic",
        "consultation_fee": "N/A",
        "recommendation": "93%",
        "patient_stories": "6Patient Stories"
    },
    {
        "doctor_name": "Dr. Akshay Jain",
        "specialty": "General Physician",
        "experience": "10years experience overall",
        "locality": "Lower Parel,",
        "city": "Mumbai",
        "clinic_name": "Health and Beyond Clinic",
        "consultation_fee": "N/A",
        "recommendation": "98%",
        "patient_stories": "111Patient Stories"
    },
    {
        "doctor_name": "Dr. Kiran C Mhatre",
        "specialty": "General Physician",
        "experience": "26years experience overall",
        "locality": "Chembur East,",
        "city": "Mumbai",
        "clinic_name": "Sushrut Hospital and Research Center",
        "consultation_fee": "N/A",
        "recommendation": "89%",
        "patient_stories": "21Patient Stories"
    },
    {
        "doctor_name": "Dr. Bharti Desai",
        "specialty": "General Physician",
        "experience": "38years experience overall",
        "locality": "Matunga West,",
        "city": "Mumbai",
        "clinic_name": "Total Health Clinic",
        "consultation_fee": "N/A",
        "recommendation": "93%",
        "patient_stories": "13Patient Stories"
    },
    {
        "doctor_name": "Dr. Avinash Deo",
        "specialty": "General Physician",
        "experience": "37years experience overall",
        "locality": "Mahim,",
        "city": "Mumbai",
        "clinic_name": "S L Raheja Fortis Hospital",
        "consultation_fee": "N/A",
        "recommendation": "91%",
        "patient_stories": "17Patient Stories"
    },
    {
        "doctor_name": "Dr. Anil  Bhoraskar",
        "specialty": "General Physician",
        "experience": "46years experience overall",
        "locality": "Mahim,",
        "city": "Mumbai",
        "clinic_name": "S L Raheja Fortis Hospital",
        "consultation_fee": "N/A",
        "recommendation": "100%",
        "patient_stories": "3Patient Stories"
    },
    {
        "doctor_name": "Dr. Madhulika Goyle",
        "specialty": "General Physician",
        "experience": "17years experience overall",
        "locality": "Andheri West,",
        "city": "Mumbai",
        "clinic_name": "Health Care Clinic",
        "consultation_fee": "N/A",
        "recommendation": "81%",
        "patient_stories": "9Patient Stories"
    },
    {
        "doctor_name": "Dr. Trupti Gilada",
        "specialty": "General Physician",
        "experience": "17years experience overall",
        "locality": "Lamington Road,",
        "city": "Mumbai",
        "clinic_name": "Unison Medicare And Research Centre",
        "consultation_fee": "N/A",
        "recommendation": "75%",
        "patient_stories": "8Patient Stories"
    },
    {
        "doctor_name": "Dr. Samvaad Shetty",
        "specialty": "General Physician",
        "experience": "12years experience overall",
        "locality": "Andheri East,",
        "city": "Mumbai",
        "clinic_name": "Arihantha Family Clinic",
        "consultation_fee": "N/A",
        "recommendation": "100%",
        "patient_stories": "19Patient Stories"
    },
    {
        "doctor_name": "Dr. Anshudeep Dodake",
        "specialty": "General Physician",
        "experience": "13years experience overall",
        "locality": "Parel,",
        "city": "Mumbai",
        "clinic_name": "Health Omega Clinic",
        "consultation_fee": "N/A",
        "recommendation": "100%",
        "patient_stories": "23Patient Stories"
    },
    {
        "doctor_name": "Dr. Rupesh.N.Nayak",
        "specialty": "General Physician",
        "experience": "17years experience overall",
        "locality": "Chembur,",
        "city": "Mumbai",
        "clinic_name": "Surana Sethia Hospital and Research Center",
        "consultation_fee": "N/A",
        "recommendation": "97%",
        "patient_stories": "15Patient Stories"
    },
    {
        "doctor_name": "Dr. Kalpana B Tiwari",
        "specialty": "General Physician",
        "experience": "13years experience overall",
        "locality": "Chembur East,",
        "city": "Mumbai",
        "clinic_name": "Dr. Tiwari's Clinic",
        "consultation_fee": "N/A",
        "recommendation": "98%",
        "patient_stories": "38Patient Stories"
    },
    {
        "doctor_name": "Dr. Gail Chaudhari",
        "specialty": "General Physician",
        "experience": "31years experience overall",
        "locality": "Oshiwara,",
        "city": "Mumbai",
        "clinic_name": "Healthspring Clinic",
        "consultation_fee": "N/A",
        "recommendation": "94%",
        "patient_stories": "25Patient Stories"
    },
    {
        "doctor_name": "Dr. Santosh Jagtap",
        "specialty": "General Physician",
        "experience": "29years experience overall",
        "locality": "Chembur East,",
        "city": "Mumbai",
        "clinic_name": "Sushrut Hospital and Research Center",
        "consultation_fee": "N/A",
        "recommendation": "95%",
        "patient_stories": "13Patient Stories"
    },
    {
        "doctor_name": "Dr. Amey Jadhav",
        "specialty": "General Physician",
        "experience": "12years experience overall",
        "locality": "Parel,",
        "city": "Mumbai",
        "clinic_name": "Healthspring Clinic",
        "consultation_fee": "N/A",
        "recommendation": "100%",
        "patient_stories": "16Patient Stories"
    },
    {
        "doctor_name": "Dr. Irfan Mamawala",
        "specialty": "General Physician",
        "experience": "24years experience overall",
        "locality": "Cuffe Parade,",
        "city": "Mumbai",
        "clinic_name": "Healthspring Clinic",
        "consultation_fee": "N/A",
        "recommendation": "100%",
        "patient_stories": "7Patient Stories"
    },
    {
        "doctor_name": "Dr. Siddharth Vinod Lakhani",
        "specialty": "Nephrologist",
        "experience": "15years experience overall",
        "locality": "Mahim,",
        "city": "Mumbai",
        "clinic_name": "S L Raheja Fortis Hospital",
        "consultation_fee": "N/A",
        "recommendation": "96%",
        "patient_stories": "22Patient Stories"
    },
    {
        "doctor_name": "Dr. Nikhil Kulkarni",
        "specialty": "General Physician",
        "experience": "29years experience overall",
        "locality": "Mahim,",
        "city": "Mumbai",
        "clinic_name": "S L Raheja Fortis Hospital",
        "consultation_fee": "N/A",
        "recommendation": "50%",
        "patient_stories": "1Patient Story"
    },
    {
        "doctor_name": "Dr. Ashwini Bansode",
        "specialty": "General Physician",
        "experience": "20years experience overall",
        "locality": "Goregaon East,",
        "city": "Mumbai",
        "clinic_name": "Healthspring Clinic",
        "consultation_fee": "N/A",
        "recommendation": "80%",
        "patient_stories": "31Patient Stories"
    },
    {
        "doctor_name": "Dr. Rajshree Sonavane",
        "specialty": "General Physician",
        "experience": "23years experience overall",
        "locality": "Powai,",
        "city": "Mumbai",
        "clinic_name": "Healthspring Clinic",
        "consultation_fee": "N/A",
        "recommendation": "100%",
        "patient_stories": "N/A"
    },
    {
        "doctor_name": "Dr. R.B. Phatak",
        "specialty": "Internal Medicine",
        "experience": "40years experience overall",
        "locality": "Mahim,",
        "city": "Mumbai",
        "clinic_name": "S L Raheja Fortis Hospital",
        "consultation_fee": "N/A",
        "recommendation": "100%",
        "patient_stories": "N/A"
    },
    {
        "doctor_name": "Dr. Mital Mukesh Chandra",
        "specialty": "General Physician",
        "experience": "14years experience overall",
        "locality": "Ghatkopar West,",
        "city": "Mumbai",
        "clinic_name": "Zynova Shalby Hospital",
        "consultation_fee": "N/A",
        "recommendation": "N/A",
        "patient_stories": "N/A"
    },
    {
        "doctor_name": "Dr. Veda",
        "specialty": "General Physician",
        "experience": "23years experience overall",
        "locality": "Santacruz West,",
        "city": "Mumbai",
        "clinic_name": "Dr Veda Bhatt Clinic",
        "consultation_fee": "N/A",
        "recommendation": "100%",
        "patient_stories": "1Patient Story"
    },
    {
        "doctor_name": "Dr. Balbirsingh Kohli",
        "specialty": "General Physician",
        "experience": "29years experience overall",
        "locality": "Mulund West,",
        "city": "Mumbai",
        "clinic_name": "Apex Hospitals",
        "consultation_fee": "N/A",
        "recommendation": "N/A",
        "patient_stories": "N/A"
    },
    {
        "doctor_name": "Dr. Neha Pokharna Garg",
        "specialty": "Hematologist",
        "experience": "5years experience overall",
        "locality": "Malad West,",
        "city": "Mumbai",
        "clinic_name": "Garg Multispeciality Hospital",
        "consultation_fee": "N/A",
        "recommendation": "100%",
        "patient_stories": "N/A"
    },
    {
        "doctor_name": "Dr. Ashish Jain",
        "specialty": "General Physician",
        "experience": "7years experience overall",
        "locality": "Chandivali,",
        "city": "Mumbai",
        "clinic_name": "Nahar Medical Centre",
        "consultation_fee": "N/A",
        "recommendation": "100%",
        "patient_stories": "6Patient Stories"
    },
    {
        "doctor_name": "Dr. Aliya Siddiqui",
        "specialty": "General Physician",
        "experience": "8years experience overall",
        "locality": "Cuffe Parade,",
        "city": "Mumbai",
        "clinic_name": "Healthspring Clinic",
        "consultation_fee": "N/A",
        "recommendation": "N/A",
        "patient_stories": "N/A"
    },
    {
        "doctor_name": "Dr. Kruti Patel",
        "specialty": "General Physician",
        "experience": "10years experience overall",
        "locality": "Ghatkopar West,",
        "city": "Mumbai",
        "clinic_name": "Shanti Nursing Home",
        "consultation_fee": "N/A",
        "recommendation": "N/A",
        "patient_stories": "N/A"
    },
    {
        "doctor_name": "Dr. Tejas Dharia",
        "specialty": "Radiologist",
        "experience": "14years experience overall",
        "locality": "Santacruz West,",
        "city": "Mumbai",
        "clinic_name": "Mumbai Endovascular Centre",
        "consultation_fee": "N/A",
        "recommendation": "N/A",
        "patient_stories": "N/A"
    },
    {
        "doctor_name": "Dr. Manasi Dave",
        "specialty": "General Physician",
        "experience": "17years experience overall",
        "locality": "Kandivali,",
        "city": "Mumbai",
        "clinic_name": "Aashirwad Medical And Dental Clinic",
        "consultation_fee": "N/A",
        "recommendation": "N/A",
        "patient_stories": "N/A"
    },
    {
        "doctor_name": "Dr. Harshil Shah",
        "specialty": "Pulmonologist",
        "experience": "7years experience overall",
        "locality": "Kandivali,",
        "city": "Mumbai",
        "clinic_name": "Apex Hospitals Kandivali",
        "consultation_fee": "N/A",
        "recommendation": "82%",
        "patient_stories": "10Patient Stories"
    },
    {
        "doctor_name": "Dr. Tarun Jain",
        "specialty": "General Physician",
        "experience": "16years experience overall",
        "locality": "Kandivali,",
        "city": "Mumbai",
        "clinic_name": "Apex Hospitals Kandivali",
        "consultation_fee": "N/A",
        "recommendation": "N/A",
        "patient_stories": "N/A"
    },
    {
        "doctor_name": "Dr. Vijay Agarwal",
        "specialty": "General Physician",
        "experience": "42years experience overall",
        "locality": "Kandivali East,",
        "city": "Mumbai",
        "clinic_name": "London Dental Clinic",
        "consultation_fee": "N/A",
        "recommendation": "92%",
        "patient_stories": "38Patient Stories"
    },
    {
        "doctor_name": "Dr. Mili S. Joshi",
        "specialty": "Pediatrician",
        "experience": "27years experience overall",
        "locality": "Santacruz East,",
        "city": "Mumbai",
        "clinic_name": "Dr. Mili Joshi's Clinic",
        "consultation_fee": "N/A",
        "recommendation": "97%",
        "patient_stories": "61Patient Stories"
    },
    {
        "doctor_name": "Dr. Harish V. Dhuri",
        "specialty": "General Physician",
        "experience": "28years experience overall",
        "locality": "Goregaon West,",
        "city": "Mumbai",
        "clinic_name": "Indira Clinic",
        "consultation_fee": "N/A",
        "recommendation": "88%",
        "patient_stories": "41Patient Stories"
    }
]




def scrap_data(request=None):

    
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



def handle(request):
    for doctor_data in data:
        DoctorInfo.objects.create(
            doctor_name=doctor_data['doctor_name'],
            specialty=doctor_data['specialty'],
            experience=doctor_data['experience'],
            locality=doctor_data['locality'],
            city=doctor_data['city'],
            clinic_name=doctor_data['clinic_name'],
            consultation_fee=doctor_data['consultation_fee'],
            recommendation=doctor_data['recommendation'],
            patient_stories=doctor_data['patient_stories']
        )
    HttpResponse('Data loaded successfully')
    
    

def doctor_list(request):
    form = DoctorFilterForm(request.GET)
    doctors = DoctorInfo.objects.all()

    if form.is_valid():
        if form.cleaned_data['specialty']:
            doctors = doctors.filter(specialty=form.cleaned_data['specialty'])
        if form.cleaned_data['locality']:
            doctors = doctors.filter(locality=form.cleaned_data['locality'])

    return render(request, 'index.html', {'form': form, 'doctors': doctors})