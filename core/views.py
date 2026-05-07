from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.

from django.shortcuts import render
from datetime import datetime

def home(request):
    home_gallery_images = [f"happy clients ({i}).jpg" for i in range(11, 19)]  # first 8 images
    return render(request, 'home.html', {
        'home_gallery_images': home_gallery_images
    })


def about(request):
    return render(request, 'about.html', {'now': datetime.now()})

def certifications(request):
    return render(request, 'certifications.html', {'now': datetime.now()})

def accreditation(request):
    return render(request, 'accreditation.html', {'now': datetime.now()})



from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            send_mail(
                subject=f"Contact Form Submission from {name}",
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=["tiscertificationscontact@gmail.com"],
            )
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')  # Redirect to clear form
        except Exception as e:
            messages.error(request, f"Failed to send message. Error: {str(e)}")

    return render(request, "contact.html")


def iso_41001(request): return render(request, 'certifications/ISO41001.html')
def iso_22301(request): return render(request, 'certifications/ISO22301.html')
def iso_21001(request): return render(request, 'certifications/ISO21001.html')
def iso_45001(request): return render(request, 'certifications/ISO45001.html')
def iso_9001(request): return render(request, 'certifications/ISO9001.html')
def iso_20000_1(request): return render(request, 'certifications/ISO20000-1.html')
def iso_42001(request): return render(request, 'certifications/ISO42001.html')
def iso_37001(request): return render(request, 'certifications/ISO37001.html')
def iso_27001(request): return render(request, 'certifications/ISO27001.html')
def iso_14001(request): return render(request, 'certifications/ISO14001.html')
def iso_22000(request): return render(request, 'certifications/ISO22000.html')
def iso_13485(request): return render(request, 'certifications/ISO13485.html')
def iso_27701(request): return render(request, 'certifications/ISO27701.html')
def iso_50001(request): return render(request, 'certifications/ISO50001.html')
def iso_iec_27001(request): return render(request, 'certifications/iso_iec_27001.html')
def iso_iec_27701(request): return render(request, 'certifications/ISO27701.html')
def HACCP(request): return render(request, 'certifications/haccp.html' )
def FoodSafetycertification(request): return render(request, 'certifications/foodsafetycertification.html' )
def ISOTraining(request): return render(request, 'certifications/ISOtraining.html' )
def ISOawarenesstraining(request): return render(request, 'certifications/ISOawarenesstraining.html' )
def LeadAuditorTraining(request): return render(request, 'certifications/leadauditortraining.html' )
def InternalAuditorTraining(request): return render(request, 'certifications/ISOinternalauditortraining.html' )
def CE(request): return render(request, 'certifications/CE.html' )
def ISO8124(request): return render(request, 'certifications/ISO8124.html' )
def energyaudit(request): return render(request, 'certifications/energyaudit.html' )
def safetyaudit(request): return render(request, 'certifications/safetyaudit.html' )
from django.shortcuts import render

def DefenceIndustry(request):
    return render(request, 'industries/DefenceIndustry.html')

def FoodandFoodProducts(request):
    return render(request, 'industries/FoodandFoodProducts.html')

def HospitalityIndustry(request):
    return render(request, 'industries/HospitalityIndustry.html')

def TransportandLogistics(request):
    return render(request, 'industries/TransportandLogistics.html')

def MedicalDevices(request):
    return render(request, 'industries/MedicalDevices.html')

def PublicSector(request):
    return render(request, 'industries/PublicSector.html')

def PharmaceuticalIndustry(request):
    return render(request, 'industries/PharmaceuticalIndustry.html')

def QualityManagementSystem(request):
    return render(request, 'industries/QualityManagementSystem.html')

def SolarIndustry(request):
    return render(request, 'industries/SolarIndustry.html')

def TelecommunicationIndustry(request):
    return render(request, 'industries/TelecommunicationIndustry.html')

def AntiBriberyManagementSystem(request):
    return render(request, 'industries/AntiBriberyManagementSystem.html')

def ConstructionIndustry(request):
    return render(request, 'industries/ConstructionIndustry.html')

def ChemicalIndustry(request):
    return render(request, 'industries/ChemicalIndustry.html')

def ElectricalsAndElectronicsIndustry(request):
    return render(request, 'industries/ElectricalsAndElectronicsIndustry.html')

def EducationIndustry(request):
    return render(request, 'industries/EducationIndustry.html')

def EnergyIndustry(request):
    return render(request, 'industries/EnergyIndustry.html')

def InformationTechnologyIndustry(request):
    return render(request, 'industries/InformationTechnologyIndustry.html')

def TextileIndustry(request):
    return render(request, 'industries/TextileIndustry.html')

def AutomotiveIndustry(request):
    return render(request, 'industries/AutomotiveIndustry.html')

def BankingAndFinance(request):
    return render(request, 'industries/BankingandFinance.html')

def EnvironmentalManagementSystem(request):
    return render(request, 'industries/EnvironmentalManagementSystem.html')

def HotelRestaurantAndLeisureService(request):
    return render(request, 'industries/HotelRestaurantAndLeisureService.html')

def Railways(request):
    return render(request, 'industries/Railways.html')

def ImportAndExportIndustry(request):
    return render(request, 'industries/ImportAndExportIndustry.html')

def ManufacturingIndustries(request):
    return render(request, 'industries/ManufacturingIndustries.html')

def OilAndGasIndustry(request):
    return render(request, 'industries/OilAndGasIndustry.html')

def TobaccoIndustry(request):
    return render(request, 'industries/TobaccoIndustry.html')

def TourismIndustries(request):
    return render(request, 'industries/TourismIndustries.html')

def OccupationalHealthAndSafetyManagementSystem(request):
    return render(request, 'industries/OccupationalHealthandSafetyManagementSystem.html')



def gallery(request):
    images = [f"happy clients ({i}).jpg" for i in range(11, 69)]
    context = {"images": images}
    return render(request, "gallery.html", context)



from django.shortcuts import render
from django.utils import timezone
from core.models import Certificate

def verify_certificate(request):
    result = None
    status = None

    if request.method == "POST":
        cert_no = request.POST.get("certificateSerial", "").strip()

        try:
            certificate = Certificate.objects.get(
                certificate_number__iexact=cert_no
            )

            today = timezone.now().date()

            if certificate.expiry_date and certificate.expiry_date >= today:
                status = "valid"
            else:
                status = "expired"

            result = certificate

        except Certificate.DoesNotExist:
            status = "not_found"

    return render(
        request,
        "verify_certificate_result.html",
        {
            "certificate": result,
            "status": status
        }
    )
