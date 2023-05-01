from django.urls import path

from .views import CreationUtilisateur,ChangerMotPasseiew ,BlacklistTokenUpdateView, UserConnecter

urlpatterns = [
     path('CreationUtilisateur/', CreationUtilisateur.as_view(), name="CreationUtilisateur"),
     path('changer_mot_passe/', ChangerMotPasseiew.as_view(), name='change-password'),
     path('CreationUtilisateur/<int:id>', CreationUtilisateur.as_view()),
     path('utilisateurConnecte/', UserConnecter.as_view(), name='userConncter'),
     path('deconnexion/blacklist/', BlacklistTokenUpdateView.as_view(),name='blacklist')
]

