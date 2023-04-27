from resources.auth import UserSignUpResource, UserSignInResource
from resources.concerts import ConcertsResource, ConcertResource, ConcertDeleteResource, ConcertDetailsResource, OwnConcertsResource
from resources.purchases import PurchaseResource, OwnPurchasesResource, PurchasesResource

routes = (
    (UserSignUpResource, "/sign-up"),
    (UserSignInResource, "/sign-in"),
    (OwnConcertsResource, "/hosts/<int:host_id>/ownconcerts"),
    (ConcertsResource, "/concerts"),
    (ConcertResource, "/concert/<int:pk>/edit"),
    (ConcertDeleteResource, "/concert/<int:pk>/delete"),
    (ConcertDetailsResource, "/concert/<int:pk>/details"),
    (PurchaseResource, "/purchases"),
    (OwnPurchasesResource, "/mypurchases"),
    (PurchasesResource, "/allpurchases")
)