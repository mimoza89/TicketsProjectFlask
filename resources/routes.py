from resources.auth import UserSignUpResource, UserSignInResource
from resources.concerts import ConcertsResource, ConcertResource, ConcertDeleteResource

routes = (
    (UserSignUpResource, "/sign-up"),
    (UserSignInResource, "/sign-in"),
    (ConcertsResource, "/concerts"),
    (ConcertResource, "/concert/<int:pk>/edit"),
    (ConcertDeleteResource, "/concert/<int:pk>/delete")

)