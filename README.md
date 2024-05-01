# baigiamasis
Repozitorija Python kursų baigiamąjam darbui talpinti.

Projekto idėja- interneto puslapis, kuris primena palaistyti augalus. Vartotojas prisiregistruoja, prideda savo augalus, gauna priminimus į el. paštą. Augalų duomenys paimami iš API. Suplanuota užduotis (scheduled task) nustatytu laiku tikrina kuriuos augalus atėjo laikas laistyti ir jų savininkams išsiunčia laišką su priminimu.

Paleidžiant puslapį, reikia terminale įsijungti celery worker su komanda "celery -A mysite worker -l info -P solo".
Taip pat terminale reikia paleisti celery beat su komanda 
"celery -A mysite beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler"
Reikalingas Redis.

Kadangi projekte naudojamas nemokamo plano API key - nesuteikiamas priėjimas prie visų įrašų ir ribojamas užklausų skaičius iki 300 per dieną. Tačiau to užtenka funkcionalumui pademonstruoti. 

requirements.txt faile surašyti instaliuoti paketai. Yra pora nenaudojamų, kuriuos reikėtų pašalinti, tačiau palikau, kad paskutinę akimirką ko nors nesugadinčiau.
