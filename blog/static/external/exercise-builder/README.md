# Instructions 

1) Dé-zipper le ExerciceBuilder
2) Mettre le dossier tel quel dans tes statics, dans un nouveau dossier **external**, **vendor**, **lib** appelle le comme tu veux
3) Dans le HTML de la page où tu souhaites intégrer le builder il te faut juste créer cette balise: 
    ```<exercise-builder></exercise-builder>```
4 ) Juste avant la balise de fermeture `</body>`, créer le code suivant : 
    ```html
    <!-- ton code habituel ici -->
    <script type="module" src="{% static 'lien-vers-ExerciceBuilder/exercise-builder.js' %}"></script>
    </body>
    ```
5 ) Tu peux ensuite supprimer le fichier `index.html` qui se trouve dans ExerciceBuilder. Je ne l'ai laissé que pour te donner un exemple de page HTML fonctionnel.