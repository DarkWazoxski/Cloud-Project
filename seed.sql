
-- =========================================
-- UNIVERSITY DEPARTMENTS SAMPLE DATA
-- =========================================

INSERT INTO public.departments
(department_id, department_name, department_description, department_link)
OVERRIDING SYSTEM VALUE
VALUES
(9, 'Biologie',
 'Étude des êtres vivants, de leur structure, de leur fonctionnement et de leur environnement.',
 'https://elearning.univ-boumerdes.dz/course/index.php?categoryid=6276'),

(10, 'Mathématiques',
 'Formation axée sur le raisonnement logique, l’analyse et la résolution de problèmes complexes.',
 'https://elearning.univ-boumerdes.dz/course/index.php?categoryid=6277'),

(11, 'Informatique',
 'Formation dans les domaines de la programmation, des bases de données, des réseaux et des technologies numériques.',
 'https://elearning.univ-boumerdes.dz/course/index.php?categoryid=6278'),

(12, 'STAPS',
 'Étude des activités physiques et sportives, de l’entraînement et de l’éducation physique.',
 'https://elearning.univ-boumerdes.dz/course/index.php?categoryid=6279'),

(13, 'Chimie',
 'Étude de la matière, de sa composition, de ses propriétés et de ses transformations.',
 'https://elearning.univ-boumerdes.dz/course/index.php?categoryid=6280'),

(14, 'Agronomie',
 'Étude des sciences agricoles, des productions végétales et animales et de la gestion des ressources naturelles.',
 'https://elearning.univ-boumerdes.dz/course/index.php?categoryid=6281'),

(15, 'Physique',
 'Étude des phénomènes naturels et des lois fondamentales qui régissent l’univers.',
 'https://elearning.univ-boumerdes.dz/course/index.php?categoryid=6282');

-- Synchronize the department ID sequence
SELECT setval(
    'public.departments_department_id_seq',
    (SELECT MAX(department_id) FROM public.departments),
    true
);




-- =========================================
-- ADMINISTRATOR SAMPLE DATA
-- =========================================

INSERT INTO public.admins (id, username, password)
OVERRIDING SYSTEM VALUE
VALUES
(1, 'nabil', '2004');

-- Synchronize administrator ID sequence
SELECT setval(
    'public.admins_id_seq',
    (SELECT MAX(id) FROM public.admins),
    true
);
