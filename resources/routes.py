from resources.auth import UserSignUpResource, UserSignInResource
from resources.concerts import ConcertsResource, ConcertResource, ConcertDeleteResource
from resources.purchases import PurchaseResource, OwnPurchasesResource

routes = (
    (UserSignUpResource, "/sign-up"),
    (UserSignInResource, "/sign-in"),
    (ConcertsResource, "/concerts"),
    (ConcertResource, "/concert/<int:pk>/edit"),
    (ConcertDeleteResource, "/concert/<int:pk>/delete"),
    (PurchaseResource, "/purchases"),
    (OwnPurchasesResource, "/mypurchases"),
)