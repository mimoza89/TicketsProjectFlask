from resources.auth import UserSignUpResource, UserSignInResource
routes = (
    (UserSignUpResource, "/sign-up"),
    (UserSignInResource, "/sign-in"),
)