## Machine Translation


It's a simple Machine Translation website using django  to translate from English to French along with a seq2seq model .


<details>
<summary> Take a look:</summary>
  
### OverView of the web page:

![image](https://github.com/lam843/MachineTranslation/assets/78732216/9da7b44f-b7ef-4eb4-99dc-7b4e14a33e03)

### Screen Record the testing :

[screen-capture.webm](https://github.com/lam843/MachineTranslation/assets/78732216/991b233e-9beb-4288-8f62-417e3f538b0a)
  
</details>

<details>
<summary> Presentation :</summary>
  
![image](https://github.com/lam843/MachineTranslation/assets/78732216/963787af-1e18-4c4d-b523-1b6a63029998)
  
[Machine Translation NLP.pdf](https://github.com/lam843/MachineTranslation/files/11606452/Machine.Translation.NLP.pdf)

  
</details>

===========================================================================


####  USAGE
Pour exécuter ce projet Django, vous pouvez suivre ces étapes :

1. Installer Django : Assurez-vous d'avoir Django installé sur votre machine. Vous pouvez utiliser la commande suivante pour installer Django à l'aide de pip, en supposant que vous ayez déjà installé Python et pip :
   ```
   pip install django
   ```

2. Installer Anaconda : Si vous n'avez pas déjà installé Anaconda, rendez-vous sur le site web d'Anaconda (https://www.anaconda.com/products/individual) et téléchargez la version appropriée pour votre système d'exploitation. Suivez les instructions d'installation fournies.

3. Créer un environnement virtuel (facultatif) : Il est conseillé de créer un environnement virtuel pour votre projet Django afin d'isoler ses dépendances. Vous pouvez créer un environnement virtuel à l'aide d'Anaconda. Ouvrez un terminal ou une invite de commandes et exécutez la commande suivante :
   ```
   conda create --name myenv
   ```
   Remplacez `myenv` par le nom souhaité pour votre environnement virtuel.

4. Activer l'environnement virtuel : Après avoir créé l'environnement virtuel, activez-le à l'aide de la commande suivante :
   - Sur Windows :
     ```
     conda activate myenv
     ```
   - Sur macOS et Linux :
     ```
     source activate myenv
     ```

5. Accéder au répertoire du projet : Utilisez la commande `cd` dans le terminal ou l'invite de commandes pour accéder au répertoire où se trouve votre projet Django. Par exemple :
   ```
   cd /chemin/vers/votre/projet
   ```

6. Exécuter les migrations : Django utilise des migrations pour gérer les changements de schéma de base de données. Appliquez toutes les migrations en attente pour créer ou mettre à jour le schéma de la base de données. Utilisez la commande suivante :
   ```
   python manage.py migrate
   ```

7. Démarrer le serveur de développement : Lancez le serveur de développement Django pour exécuter votre projet en local. Exécutez la commande suivante :
   ```
   python manage.py runserver
   ```

8. Accéder au projet : Ouvrez un navigateur web et rendez-vous à l'URL `http://127.0.0.1:8000/` . Vous devriez voir votre projet Django s'exécuter.

