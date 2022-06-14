PARTICIPATION_OF_THIRD = (
    ('yes', 'Ja'),
)
PROTECTION_AFFECTED = (
    ('confidentiality', 'Vertraulichkeit'),
    ('integrity', 'Integrität'),
    ('availability', 'Verfügbarkeit'),
)
INCIDENT_TYPE = (
    ('device_lorS', 'Gerät/Datenträger verloren oder gestohlen'),
    ('doc_lorS', 'Dokumente verloren, gestohlen oder unsicher aufbewahrt (Papier)'),
    ('post_orS', 'Post (auch E-Mail) verloren oder geöffnet bevor sie zum Absender zurück kam'),
    ('hacking', 'Hacking, Malware (z.B. Ransomware) und/oder Phishing'),
    ('mail', 'Unrichtige Entsorgung personenbezogener Daten auf Papier'),
    ('incorrect', 'Unrichtige Entsorgung personenbezogener Daten auf Papier'),
    ('release', 'Unbeabsichtigte Veröffentlichung'),
    ('data', 'Daten falscher Betroffener im Kundenportal angezeigt'),
    ('recipient', 'Falscher Empfänger'),
    ('disclosure', 'Mündliche Bekanntgabe personenbezogener Daten')
)

PERSONAL_DATA = [
    ('', (
        ('identity', 'Identität von Betroffenen (Vornamen, Nachnamen, Geburtsdaten)'),
        ('contact', 'Kontaktdaten'),  # contact details
        ('identification', 'Daten zur Identifikation'),  # identification data
        ('eco_fin_data', 'Ökonomische Daten sowie Finanzdaten'),  # Economic data and financial data
        ('doc_cert', 'Amtliche Dokumente und Urkunden'),  # Official documents and certificates
        ('loc_mov', 'Standort- sowie Bewegungsdaten'),  # Location and movement data
    )
     ),
    ('Besondere Kategorien', (
        ('gen_bio', 'Genetische oder biometrische Daten'),  # Genetic or biometric data
        ('criminal','Daten über strafrechtliche Verurteilungen, Straftaten sowie Sicherungsmaßnahmen (z.B. Sicherungsverwahrung)'),
        # Data on criminal convictions, criminal offenses and security measures (e.g. preventive detention)
        ('ethnic', 'Daten über die ‚rassische‘ oder ethnische Herkunft'),  # Data on 'racial' or ethnic origin
        ('opinion', 'Politische Meinung'),  # political opinion
        ('belief', 'Religiöse oder weltanschauliche Überzeugung'),  # Religious or philosophical belief
        ('affiliation', 'Gewerkschaftszugehörigkeit'),  # union affiliation
        ('sex_life', 'Daten zum Sexualleben'),  # sex life data
        ('health', 'Gesundheitsdaten'),  # health data
        ('not_known', 'Noch nicht bekannt'),  # Not yet known
    )
     ),

]
AFFECTED_PEOPLE = (
    ('employees', 'Beschäftigte'),
    ('user', 'Benutzer'),
    ('subscribers', 'Abonnenten'),
    ('student', 'Schülerinnen, Schüler sowie Studierende'),
    ('customer', 'Kunden (aktuelle und potenzielle)'),
    ('patients', 'Patienten'),
    ('minor', 'Minderjährige'),
    ('vulnerable', 'Schutzbedürftige Personen'),
    ('not_known', 'Noch nicht bekannt'),  # Not yet known
)
VIOLATION_CONSEQUENCE = (
    # Higher distribution than necessary or not covered by the consent of those affected
    ('distribution', 'Höhere Verbreitung als nötig bzw. nicht von der Einwilligung der Betroffenen gedeckt'),
    # Data could be combined with other information about data subjects
    ('combined', 'Daten könnten mit anderen Informationen über die Betroffenen verbunden werden'),
    # Data could be misused for other purposes or in an unfair way
    ('misused', 'Daten könnten für andere Zwecke oder auf unfaire Weise missbraucht werden'),
)
VIOLATION_COMPLETENESS = (
    # Data may have been modified and used even though it is no longer accurate
    ('modified', 'Daten könnten geändert und genutzt worden sein, obwohl sie nicht mehr zutreffend sind'),
    # Data could be changed to otherwise applicable data and subsequently used for other purposes
    ('chanced',  'Daten könnten in anderweitig zutreffende Daten geändert und in der Folge für andere Zwecke genutzt werden'),
)
VIOLATION_AVAILABILITY = (
    # Lost opportunity to provide critical service to victims
    ('lost', 'Verlorene Möglichkeit einen kritischen Dienst für Betroffene anzubieten'),
    # Changing the ability to provide a critical service to those affected
    ('changing', 'Änderung der Möglichkeit einen kritischen Dienst für die Betroffenen anzubieten')
)
SEVERITY_POTENTIAL_IMPACT = (
    ('slightly', 'Geringfügig'),  # message if the risk is low
    ('limited', 'Begrenzt'),
    ('significant', 'Bedeutend'),
    ('maximum', 'Maximal'),
)
AFFECTED_INFORMED = (
    ('yes', 'Ja'),  # message time of information
    ('taught', 'Nein, aber sie werden noch unterrichtet'),  # No, but they are still taught
    ('not_taught', 'Nein, sie werden nicht unterrichtet'),  # No, they are not taught
)
