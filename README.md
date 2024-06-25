# baigiamasis

TECHSTACK: Python, Django, Celery, Redis, HTML, CSS

Repozitorija Python kursų baigiamąjam darbui talpinti.

Projekto idėja- interneto puslapis, kuris primena palaistyti augalus. Vartotojas prisiregistruoja, prideda savo augalus, gauna priminimus į el. paštą. Augalų duomenys paimami iš API. Suplanuota užduotis (scheduled task) nustatytu laiku tikrina kuriuos augalus atėjo laikas laistyti ir jų savininkams išsiunčia laišką su priminimu.

Paleidžiant puslapį, reikia terminale įsijungti celery worker su komanda "celery -A mysite worker -l info -P solo" (Windows).
Taip pat terminale reikia paleisti celery beat su komanda 
"celery -A mysite beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler"
Reikalingas Redis.

Kadangi projekte naudojamas nemokamo plano API key - nesuteikiamas priėjimas prie visų įrašų ir ribojamas užklausų skaičius iki 300 per dieną. Tačiau to užtenka funkcionalumui pademonstruoti. 

![image](https://github.com/Daunoras/baigiamasis/assets/159426406/eb386a3c-c7b9-44c3-b181-f37ebd9dff45)
