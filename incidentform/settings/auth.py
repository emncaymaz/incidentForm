import ssoauth


PREDEFINED_GROUPS = {
    "WEB_incidentform_admin": [
        ssoauth.SUPERUSER_PERM_CODENAME
    ],
    "WEB_incidentform_editor": [
        "staff",

    ]
}
