import os

# List of filenames to create
filenames = [
    "1-braarvigHinduismUniversalSelf2014b.md",
    "2-duwellFrontmatter2014b.md",
    "3-lohmannHumanDignitySocialism2014b.md",
    "4-duwellOriginsConceptEuropean2014b.md",
    "5-duwellAcknowledgments2014b.md",
    "6-westermanNaturalRightsHuman2014b.md",
    "7-duwellListContributors2014b.md",
    "8-duwellContents2014b.md",
    "9-duwellHumanDignityConcepts2014b.md",
    "10-duwellScopeEuropeanTradition2014b.md",
    "11-pharoCouncilValladolid155015512014b.md",
    "12-marothForeword2014b.md",
    "13-luoHumanDignityTraditional2014b.md",
    "14-qiaoDignityTraditionalChinese2014b.md",
    "15-lindemannSocialCulturalPresuppositions2014b.md",
    "16-verbeekRousseauHumanDignity2014b.md",
    "17-brownswordHumanDignityLegal2014b.md",
    "18-duwellSystematicConceptualization2014b.md",
    "19-miethHumanDignityLatemedieval2014b.md",
    "20-duwellWhyHandbookHuman2014b.md",
    "21-duwellLegalImplementation2014.md",
    "22-beyleveldHumanDignityHuman2014.md",
    "23-mayerIslamicWorldAlternative2014.md",
    "24-davisSchelerHumanDignity2014.md",
    "25-menkeDignityRightHave2014.md",
    "26-valadierJacquesMaritainsPersonalist2014.md",
    "27-junker-kennyDignityFragilitySingularity2014.md",
    "28-duwellConflictsViolence2014.md",
    "29-degaayfortmanEqualDignityInternational2014.md",
    "30-campagnaHumanDignityProstitution2014.md",
    "31-claassenHumanDignityCapability2014.md",
    "32-bykHumanDignityUseless2014.md",
    "33-peterDignityOtherDignity2014.md",
    "34-faganHumanDignitySouth2014.md",
    "35-sneadHumanDignityUS2014.md",
    "36-hillKantianPerspectivesRational2014.md",
    "37-limamarquesHumanDignitySouth2014.md",
    "38-dreierHumanDignityGerman2014.md",
    "39-weissPosthumanDignity2014.md",
    "40-metzDignityUbuntuTradition2014.md",
    "41-poggeDignityGlobalJustice2014.md",
    "42-andersonHumanDignityConcept2014.md",
    "43-duwellBiologyBioethics2014.md",
    "44-klangRiseFallFreedom2014.md",
    "45-campbellHumanDignityCommodification2014.md",
    "46-steiglederHumanDignitySocial2014.md",
    "47-illiesThreefoldChallengeDarwinism2014.md",
    "48-duwellIndex2014.md",
    "49-thiemHumanDignityGender2014.md",
    "50-duwellHumanDignityFuture2014.md",
    "51-duwellFurtherReading2014.md",
    "52-duwellUniversalDeclarationHuman2014.md",
    "53-graumannHumanDignityPeople2014.md",
    "54-schaberDignityOnlyHumans2014.md",
    "55-duwellBorderLifeDeath2014.md",
    "56-heegerDignityOnlyHumans2014.md",
    "57-duwellContextsJustice2014.md",
    "58-collsteHumanDignityImmigration2014.md",
]

# Create each file if it doesn't exist
for filename in filenames:
    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('')
        print(f'Created: {filename}')
    else:
        print(f'Skipped (already exists): {filename}')