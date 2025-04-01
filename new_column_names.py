new_column_names = {
    'Quel est votre âge ?': 'age',
    'Quel est votre statut administratif ?': 'statut_administratif',
    'Dans quel établissement exercez-vous actuellement ?': 'etablissement',
    'Dans combien de pays avez-vous déjà enseigné ?': 'nb_pays_enseignes',
    "Au total, combien d'années avez-vous exercé en tant qu’enseignant(e) (en incluant les éventuelles interruptions de carrière) ": 'annees_experience_totale',
    'Dans combien d’établissements scolaires avez-vous travaillé au cours de votre carrière ?': 'nb_etablissements_carriere',
    "Combien d'années avez-vous travaillé dans l'enseignement en France ?": 'annees_enseignement_france',
    "Combien d'années avez-vous travaillé dans l'enseignement français à l'étranger, dans des établissements de la Mlf ?": 'annees_enseignement_mlf',
    "Combien d'années avez-vous travaillé dans l'enseignement français à l'étranger, dans des établissements de l'AEFE ?": 'annees_enseignement_aefe',
    "Combien d'années avez-vous travaillé dans l'enseignement dans un autre système éducatif (hors France, Mlf, AEFE) ?": 'annees_enseignement_autres',
    'Quel type de formation initiale avez-vous ? ': 'formation_initiale',
    'Possédez-vous des certifications complémentaires en lien avec le secteur éducatif ?': 'certifications_educatives',
    'Avez-vous actuellement ou avez-vous eu par le passé des responsabilités complémentaires ?': 'responsabilites_complementaires',
    'Avez-vous déjà encadré des formations ?': 'encadrement_formations',
    'Sur quels niveaux intervenez-vous actuellement ?': 'niveaux_enseignement',
    'Quelles matières (second degré) ou niveaux (premier degré) enseignez-vous cette année ?': 'matieres_niveaux_actuels',
    'Combien de classes suivez-vous cette année ?': 'nb_classes',
    'Combien d’élèves (approximativement) suivez-vous cette année ?': 'nb_eleves',
    'Comment évaluez-vous votre charge de travail hors de la classe (préparation des cours, corrections, suivi des élèves, réunions…) ': 'charge_travail_hors_classe',
    'À quelle fréquence utilisez-vous les outils numériques dans vos cours ?': 'frequence_outils_numeriques',
    'Quels objectifs poursuivez-vous en utilisant les outils numériques dans vos cours ?': 'objectifs_outils_numeriques',
    'À quelle fréquence intégrez-vous des projets interdisciplinaires dans vos pratiques ?': 'frequence_projets_interdisciplinaires',
    'Si vous intégrez des pratiques innovantes dans vos cours, pourriez-vous les décrire brièvement ?': 'pratiques_innovantes',
    'À quelle fréquence collaborez-vous avec vos collègues sur des projets pédagogiques ou des concertations ?': 'frequence_collaboration_collegues',
    'Existe-t-il des espaces ou outils formels pour collaborer avec vos collègues dans votre établissement ?': 'outils_collaboration',
    'Avez-vous participé à une formation continue au cours des 12 derniers mois ?': 'formation_continue_12mois',
    'Quelles compétences professionnelles avez-vous développées grâce à ces formations ?': 'competences_dev_formations',
    'Dans quelle mesure ces formations ont-elles eu un impact sur votre façon d’enseigner ?': 'impact_formations',
    'Préférez-vous les formations en présentiel, distanciel ou hybride ?': 'preference_format_formation',
    'Quels freins rencontrez-vous pour participer à des formations continues ?': 'freins_formation_continue',
    'Quels types de contenus consommez-vous pour votre auto-formation ?': 'contenus_autoformation',
    'En moyenne, combien de fois évaluez-vous vos élèves durant une séquence ?': 'nb_evaluations_sequence',
    'À quelle fréquence adaptez-vous vos évaluations aux élèves à besoins éducatifs particuliers (EBEP) ?': 'adaptation_eval_ebep',
    'Si vous avez expérimenté des évaluations alternatives, lesquelles ?': 'evaluations_alternatives',
    'Décrivez une séance dans laquelle vous avez structuré votre cours en fonction de vos objectifs pédagogiques. Comment avez-vous adapté votre enseignement aux besoins de vos élèves ?': 'exemple_adaptation_enseignement',
    'Comment concevez-vous vos évaluations pour mesurer les progrès des élèves et quelles actions mettez-vous en place suite à une évaluation pour les aider à progresser ?': 'conception_evaluation_suivi',
    'Décrivez un moment où un outil numérique a amélioré votre enseignement. Quels ont été les bénéfices pour vos élèves ?': 'outil_numerique_benefices',
    'Quels outils ou supports utilisez-vous pour permettre à vos élèves de suivre leurs apprentissages et d’identifier leurs axes de progrès ? Donnez un exemple précis.': 'outils_suivi_apprentissage',
    'Comment créez-vous un climat de classe serein et favorable aux apprentissages ? Partagez une expérience concrète.': 'climat_classe',
    'Décrivez une situation où vous avez adapté vos pratiques pédagogiques pour répondre aux besoins spécifiques d’un ou plusieurs élèves.': 'adaptation_pratiques_specifiques',
    'Comment aidez-vous vos élèves à établir des liens entre leurs apprentissages et à se projeter dans leur parcours futur ? Donnez un exemple concret.': 'lien_apprentissages_parcours',
    'Avez-vous déjà réalisé un projet ou une activité en collaboration avec vos collègues ? Quel impact cela a-t-il eu sur les élèves ?': 'projets_collaboration_impact',
    'Comment impliquez-vous les parents dans le suivi des progrès de leurs enfants ? Donnez un exemple précis.': 'implication_parents_suivi',
    'Intégrez-vous les spécificités de votre établissement dans vos pratiques pédagogiques ? Si oui, donnez un exemple précis.': 'integration_contexte_etablissement',
    'Quels aspects de votre pratique aimeriez-vous améliorer ou explorer davantage ?': 'amelioration_pratiques',
    'Quelle(s) aide(s) vous serai(en)t utile pour concevoir ou adapter vos évaluations ?': 'besoins_aide_evaluation',
    'De quoi auriez-vous besoin pour mieux répondre à la diversité linguistique, culturelle et pédagogique des élèves dans votre classe ?': 'besoins_diversite_classe',
    'Y a-t-il un outil ou une compétence numérique que vous souhaiteriez mieux maîtriser ?': 'besoins_competence_numerique',
    'Qu’est-ce qui pourrait renforcer votre collaboration avec vos collègues ou les autres acteurs éducatifs ?': 'renforcement_collaboration',
    'Quel(s) type(s) d’accompagnement(s) préférez-vous aujourd’hui ?': 'preference_accompagnement',
    'Pour chacune des priorités de la Mlf suivantes, indiquez dans quelle mesure vous ressentez un besoin de formation continue. [Enseignement en milieu culturel plurilingue]': 'besoin_formation_plurilingue',
    'Pour chacune des priorités de la Mlf suivantes, indiquez dans quelle mesure vous ressentez un besoin de formation continue. [Enseignement des compétences transversales]': 'besoin_formation_transversales',
    'Pour chacune des priorités de la Mlf suivantes, indiquez dans quelle mesure vous ressentez un besoin de formation continue. [Besoins spécifiques à la maternelle]': 'besoin_formation_maternelle',
    'Pour chacune des priorités de la Mlf suivantes, indiquez dans quelle mesure vous ressentez un besoin de formation continue. [Besoins spécifiques à l’orientation]': 'besoin_formation_orientation',
    'Pour chacune des priorités de la Mlf suivantes, indiquez dans quelle mesure vous ressentez un besoin de formation continue. [Besoins spécifiques au STIAM]': 'besoin_formation_stiam',
    'Quel est votre principal besoin actuel en termes de développement professionnel ?': 'besoin_dev_professionnel'
}
