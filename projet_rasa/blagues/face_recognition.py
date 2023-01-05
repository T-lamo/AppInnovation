from naoqi import ALProxy

IP = "192.168."  # Adresse IP de votre robot
PORT = 9559

# Création d'un proxy pour accéder aux services de reconnaissance de visage
face_detection = ALProxy("ALFaceDetection", IP, PORT)

face_detection.subscribe("Test_Face", 500, 0.0)  # "Test_Face" est le nom du sujet d'abonnement

# Capture d'une image en couleur
resolution = 2  # Qualité de l'image : 2 = 640x480
color_space = 11  # Espace de couleur : 11 = RGB
video_client = video_device.subscribe("python_client", resolution, color_space, 5)
image = video_device.getImageRemote(video_client)

# Analyse de l'image en utilisant le service de reconnaissance de visage
result = face_detection.process(image)

# Récupération des informations sur les visages détectés
if result is None:
    print("Aucun visage détecté")
else:
    # Pour chaque visage détecté
    for face in result[1]:
        # Récupération des informations générales (coordonnées, angle, etc.)
        face_info = face[0]
        print("Coordonnées du visage :", face_info[0], face_info[1], face_info[2], face_info[3])
        print("Angle du visage :", face_info[4])
        print("Score de confiance :", face_info[5])