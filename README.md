# MakePepperDance
Python script to learn Pepper dances

Team: Ibrahim ELouard - Marceau Fillon - Jean-Baptiste Rambaud



## Projet Pricipal 

Lancer le script python main.py ( default ip = adresse ip de pepper_3:192.168.1.34), si autre mettre l'adresse en argument:
$python main.py --ip 192.168.XX.XX

Toucher la tête pour lancer l'interaction.
la fonction playsound() lance une musique qui n'est présente que sur pepper_3 et qui est donc à modifier si utilisation d'un autre robot.


Mots reconnus par Pepper: Apprendre - Danser - Terminer


Quand Pepper dit : touche moi la tête quand tu finis s'il te plait, vous pouvez commencer à le bouger.


Il peut alors vous montrez la chorégraphie que vous lui avez apprise (keyword: Danser)


Après avoir fini, il vous suffit de dire "terminer" pour mettre pepper en mode veille.


Pour le relancer il suffit de lui toucher la tête.



## Partie non intégrée

chucknorris.py: 
  installer goslate, Json, requests
  chucknorris( mot ) : cette fonction retourne la premiere blague contenant le mot en argument. cette blague est traduite en français avant d'être retournée.
  
Transcrib.py:\r
  installer speech_recognition
  transcription(audiofile): cette fonction transcrit le fichier audio passé en paramêtre
  
Audio_test.py:
  Enregistre un fichier audio grâce au micros de Pepper et le transcrit
