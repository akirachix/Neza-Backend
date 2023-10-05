from django.db import models

# Create your models here.

from django.db import models

class Locations(models.Model):
    name = models.CharField(max_length=100)
    lat = models.FloatField()
    lng = models.FloatField()
    # percentage = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name

# In your Django shell or a script, create instances of the LeadPoisoningLocation model for each location:
locations_data = [
    {'lat': -1.2400, 'lng': 36.7688, 'name': 'Kitisuru'},
    {'lat': -1.2560, 'lng': 36.8175, 'name': 'Parklands/Highridge'},
    { 'lat': -1.250916, 'lng': 36.845914, 'name': 'Karura' },
    { 'lat': -1.252794, 'lng': 36.764977, 'name': 'Kangemi'},
    { 'lat': -1.2693100, 'lng': 36.7386300, 'name': 'Mountain View'},
    { 'lat': -1.283922, 'lng': 36.798107, 'name': 'Kilimani' },
    { 'lat': -1.2784631, 'lng': 36.752321, 'name': 'Kawangware'},
    { 'lat': -1.277659, 'lng': 36.752845, 'name': 'Gatina' },
    { 'lat': -1.278319, 'lng': 36.784644, 'name': 'Kileleshwa' },
    { 'lat': -1.28730775, 'lng': 36.7480163, 'name': 'Kabiro' },
    { 'lat': -1.3000000, 'lng': 36.7000000, 'name': 'Mutu-ini'},
    { 'lat': -1.3041200, 'lng': 36.7397800, 'name': 'Ngando'},
    { 'lat': -1.292471, 'lng': 36.736275, 'name': 'Riruta'},
    { 'lat': -1.271887, 'lng': 36.70381, 'name': 'Uthiru' },
    { 'lat': -1.2820, 'lng':  36.7140, 'name': 'Waithaka'},
    { 'lat': -1.320853, 'lng': 36.684936, 'name': 'Karen'},
    { 'lat': -1.3, 'lng': 36.81667, 'name': 'Nairobi West'},
    { 'lat': -1.317003, 'lng': 36.796653, 'name': 'Mugumu-ini'},
    { 'lat': -1.32423, 'lng': 36.827719, 'name': 'South C' },
    { 'lat': -1.315817, 'lng': 36.805836, 'name': 'Nyayo Highrise' },
    { 'lat': -1.31234835, 'lng': 36.796114350954, 'name': 'Laini Saba'},
    { 'lat': -1.312024 , 'lng': 36.790161, 'name': 'Lindi Makina'},
    { 'lat': -1.30490661132, 'lng': 36.7691307156, 'name': 'Woodley/Kenyatta Golf Course'},
    { 'lat': -1.184392, 'lng': 36.464872, 'name': 'Sarangombe'},
    { 'lat': -1.206415, 'lng': 36.913794, 'name': 'Githurai'},
    { 'lat': -1.187234, 'lng': 36.90304, 'name': 'Kahawa West'},
    { 'lat': -1.210542, 'lng': 36.897663, 'name': 'Zimmerman'},
    { 'lat': -1.218459, 'lng': 36.886906, 'name': 'Roysambu'},
    { 'lat': -1.1833, 'lng': 36.9167, 'name': 'Kahawa' },
    { 'lat': -1.272758, 'lng': 36.827899, 'name': 'Clay City'},
    { 'lat': -1.225602, 'lng': 36.924546, 'name': 'Mwiki'},
    { 'lat': -1.227841, 'lng': 36.905729, 'name': 'Kasarani' },
    { 'lat': -1.2505, 'lng': 36.9271, 'name': 'Njiru'},
    { 'lat': -1.253287, 'lng': 37.007823, 'name': 'Ruai' },
    { 'lat': -1.243926, 'lng': 36.881712, 'name': 'Baba Dogo'},
    { 'lat': -1.2527, 'lng': 36.8640, 'name': 'Utalii'},
    { 'lat': -1.1333300, 'lng': 34.5500000, 'name': 'Mathare North' },
    { 'lat': -1.238604 , 'lng': 36.899007, 'name': 'Lucky Summer' },
    { 'lat': -1.250364, 'lng': 36.89094, 'name': 'Korogocho' },
    { 'lat': -1.325051, 'lng': 36.878502, 'name': 'Imara Daima' },
    { 'lat': -1.3028, 'lng': 36.8843, 'name': 'Mukuru Kwa Njenga' },
    { 'lat': -1.31833, 'lng': 36.87250, 'name': 'Mukuru Kwa Ruben' },
    { 'lat': -1.31629833333, 'lng': 36.8811983333, 'name': 'Pipeline'},
    { 'lat': -1.31043197, 'lng': 36.8960322, 'name': 'Kware'},
    { 'lat': -1.25501220915, 'lng': 36.8822600693, 'name': 'Kariobangi North'},
    { 'lat': -1.29816, 'lng': 36.88927, 'name': 'Dandora Area I'},
    { 'lat': -1.28452, 'lng': 36.88536, 'name': 'Dandora Area II' },
    { 'lat': -1.2820, 'lng': 36.7140, 'name': 'Dandora Area III'},
    { 'lat': -1.28097, 'lng': 36.88233, 'name': 'Dandora Area IV' },
    { 'lat': 1.2660, 'lng': 36.9219, 'name': 'Kayole North' },
    { 'lat': -1.276162, 'lng': 36.913794, 'name': 'Kayole Central' },
    { 'lat': -1.26746, 'lng': 36.91582, 'name': 'Kayole South' },
    { 'lat': -1.250562 , 'lng': 36.937984, 'name': 'Komarock' },
    { 'lat': -1.2592, 'lng': 36.9236, 'name': 'Matopeni/Spring Valley' },
    { 'lat': -1.27796, 'lng': 36.83526, 'name': 'Upper Savannah'},
    { 'lat': -1.2820, 'lng': 36.83526, 'name': 'Lower Savannah'},
    { 'lat': -1.332686, 'lng': 36.900351, 'name': 'Embakasi'},
    { 'lat': -1.27496478, 'lng': 36.96090454, 'name': 'Utawala' },
    { 'lat':  -1.286558, 'lng': 36.962825, 'name': 'Mihango'},
    { 'lat': -1.2776, 'lng': 36.8883, 'name': 'Umoja I'},
    { 'lat': -1.28321065001, 'lng': 36.90048185, 'name': 'Umoja II'},
    { 'lat': -1.2645912, 'lng': 36.895515, 'name': 'Mowlem'},
    { 'lat':  -1.264884, 'lng': 36.892285, 'name': 'Kariobangi South' },
    { 'lat': -1.2946400, 'lng': 36.8651600, 'name': 'Maringo/Hamza' },
    { 'lat': -1.3061, 'lng': 36.8627, 'name': 'Industrial Area' },
    { 'lat': -1.2891666, 'lng': 36.8239696, 'name': 'Harambee'},
    { 'lat': -1.056954, 'lng': 37.107094, 'name': 'Makongeni' },
    { 'lat': -1.2816645, 'lng': 36.8458837, 'name': 'Pumwani' },
    { 'lat': -1.2731795, 'lng': 36.8600088, 'name': 'Eastleigh North' },
    { 'lat': -1.2859085, 'lng': 36.8532829, 'name': 'Eastleigh South' },
    { 'lat': -1.2700900, 'lng': 36.8603400, 'name': 'Airbase' },
    { 'lat': -1.2820, 'lng': 36.83526, 'name': 'California' },
    { 'lat': -1.274665, 'lng': 36.829065, 'name': 'Ngara' },
    { 'lat': -1.2815735 , 'lng': 36.82233580000002, 'name': 'Nairobi Central'},
    { 'lat': -1.272545 , 'lng': 36.839829, 'name': 'Pangani' },
    { 'lat': -1.27717, 'lng': 36.835121, 'name': 'Ziwani/Kariokor' },
    { 'lat': -1.2899, 'lng': 36.836, 'name': 'Landmawe'},
    { 'lat': -1.2820, 'lng': 36.83526, 'name': 'Nairobi South' },
    { 'lat': -1.27977509162, 'lng': 36.8326941433, 'name': 'Mabatini' },
    { 'lat': -1.25649, 'lng': 36.872114, 'name': 'Huruma' },
    { 'lat': -1.3277100, 'lng': 36.7836000, 'name': 'Ngei'},
    { 'lat': -1.2668038395293, 'lng': 36.848135618581, 'name': 'Mlango Kubwa' },
    { 'lat': -1.2525036534071, 'lng': 36.878572857815, 'name': 'Kiamaiko' },
    { 'lat': -1.312217, 'lng': 36.791376, 'name': 'Kibra' },
    { 'lat': -1.2619, 'lng': 36.8585, 'name': 'Mathare South'},
    { 'lat': -1.30332, 'lng': 36.8315224, 'name': 'Embakasi Central' },
    { 'lat': -1.2997, 'lng': 36.9167, 'name': 'Embakasi East' },
    { 'lat': -1.2800, 'lng': 36.9167, 'name': 'Embakasi North' },
    { 'lat': -1.3000, 'lng': 36.9167, 'name': 'Embakasi South'},
    { 'lat': -1.28478, 'lng': 36.833774, 'name': 'Kamukunji' },
    { 'lat': -1.2959673, 'lng': 36.8724832, 'name': 'Makadara' },
    { 'lat': -1.284457, 'lng': 36.824504, 'name': 'Starehe' },
    { 'lat': -1.268264, 'lng': 36.811121, 'name': 'Westlands' },
    { 'lat': -1.145703, 'lng': 36.964853, 'name': 'Ruiru' },
    { 'lat': -1.457725, 'lng': 36.978503, 'name': 'Athi River'},
    { 'lat': -1.359227, 'lng': 36.937984, 'name': 'Syokimau'},
    { 'lat': -1.475289, 'lng':  36.96201, 'name': 'Kitengela' },
    { 'lat': -1.038757, 'lng': 37.083375, 'name': 'Thika' },
    
    # Add the rest of your locations here
]

for location_data in locations_data:
    location = Locations(**location_data)
    location.save()

