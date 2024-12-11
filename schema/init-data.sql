-- Seed for account_types
INSERT INTO dic_account_types (name) VALUES 
('Student'),
('Staff'),
('Admin');

-- Seed for departments
INSERT INTO dic_departments (name, description, head_of_department) VALUES
('Department of Geography and Environmental Sustainability', 
 'Offering advanced studies in geography and environmental sustainability.', 'Dr. John Doe'),
('Department of Computer Science', 'Department focused on computer science education and research.', 'Prof. Jane Smith'),
('Department of Engineering', 'Department offering various engineering disciplines.', 'Dr. Michael Johnson'),
('Department of Business Administration', 'Department offering programs in business and management.', 'Dr. Sarah Brown'),
('Department of Creative Arts', 'Department for creative arts and humanities.', 'Prof. David White'),
('Department of Social Sciences', 'Department offering social science programs.', 'Dr. Emily Green');

-- Seed for degrees
INSERT INTO dic_degrees (name, description) VALUES
('PGD', 'Postgraduate Diploma Program.'),
('MSc', 'Master of Science Program.'),
('PhD', 'Doctor of Philosophy Program.'),
('MSP', 'Master of Science in Programming Program.');

-- Seed for linking degrees and departments
INSERT INTO dic_programs (degree_id, department_id) VALUES
(1, 1),  -- PGD for Geography and Environmental Sustainability
(2, 1),  -- MSc for Geography and Environmental Sustainability
(3, 1),  -- PhD for Geography and Environmental Sustainability
(4, 1),  -- MSP for Geography and Environmental Sustainability

(1, 2),  -- PGD for Computer Science
(2, 2),  -- MSc for Computer Science
(3, 2),  -- PhD for Computer Science
(4, 2),  -- MSP for Computer Science

(1, 3),  -- PGD for Engineering
(2, 3),  -- MSc for Engineering
(3, 3),  -- PhD for Engineering
(4, 3),  -- MSP for Engineering

(1, 4),  -- PGD for Business Administration
(2, 4),  -- MSc for Business Administration
(3, 4),  -- PhD for Business Administration
(4, 4),  -- MSP for Business Administration

(1, 5),  -- PGD for Creative Arts
(2, 5),  -- MSc for Creative Arts
(3, 5),  -- PhD for Creative Arts
(4, 5),  -- MSP for Creative Arts

(1, 6),  -- PGD for Social Sciences
(2, 6),  -- MSc for Social Sciences
(3, 6),  -- PhD for Social Sciences
(4, 6);  -- MSP for Social Sciences


-- Seed for batches
INSERT INTO dic_batches (name, year, description) VALUES
('2019/2020', 2019, 'Batch for the academic year 2019/2020.'),
('2020/2021', 2020, 'Batch for the academic year 2020/2021.'),
('2021/2022', 2021, 'Batch for the academic year 2021/2022.'),
('2022/2023', 2022, 'Batch for the academic year 2022/2023.'),
('2023/2024', 2023, 'Batch for the academic year 2023/2024.'),
('2024/2025', 2024, 'Batch for the academic year 2024/2025.'),
('2025/2026', 2025, 'Batch for the academic year 2025/2026.');


-- Seed for accounts
INSERT INTO dic_accounts (first_name, last_name, email, gender, account_type_id, password, phone_number, state, local_government, address)
VALUES
('Nathaniel', 'Coder', 'student@gmail.com', 'Male', 1, crypt('password', gen_salt('bf')), '+2347012345678', 'Lagos', 'Ikeja', '123 Street Name, Ikeja, Lagos'),
('Bolaji', 'Adebisi', 'bolaji.student@example.com', 'Male', 1, crypt('password', gen_salt('bf')), '+2347012345678', 'Ogun', 'Abeokuta', '456 Lane, Abeokuta, Ogun'),
('Kemi', 'Oladele', 'kemi.student@example.com', 'Female', 1, crypt('password', gen_salt('bf')), '+2347012345678', 'Ekiti', 'Ado-Ekiti', '789 Ado Ekiti Road, Ekiti'),
('Chinedu', 'Ibekwe', 'chinedu.student@example.com', 'Male', 1, crypt('password', gen_salt('bf')), '+2347012345678', 'Enugu', 'Enugu', '234 Enugu Central, Enugu'),
('Amaka', 'Eze', 'amaka.student@example.com', 'Female', 1, crypt('password', gen_salt('bf')), '+2347012345678', 'Abuja', 'Central', '112 Central Avenue, Abuja'),
('Ibrahim', 'Aliyu', 'ibrahim.student@example.com', 'Male', 1, crypt('password', gen_salt('bf')), '+2347012345678', 'Kaduna', 'Kaduna', '32 Kaduna City Road, Kaduna'),
('Ifeanyi', 'Okoro', 'ifeanyi.student@example.com', 'Male', 1, crypt('password', gen_salt('bf')), '+2347012345678', 'Anambra', 'Awka', '56 Awka Road, Anambra'),
('Ngozi', 'Onwumere', 'ngozi.student@example.com', 'Female', 1, crypt('password', gen_salt('bf')), '+2347012345678', 'Imo', 'Owerri', '78 Owerri Lane, Imo'),
('Sheriff', 'Adamu', 'sheriff.student@example.com', 'Male', 1, crypt('password', gen_salt('bf')), '+2347012345678', 'Kano', 'Kano', '90 Kano Main Street, Kano'),
('Sola', 'Ogunbiyi', 'sola.student@example.com', 'Female', 1, crypt('password', gen_salt('bf')), '+2347012345678', 'Delta', 'Asaba', '123 Asaba Drive, Delta'),
('Musa', 'Garba', 'musa.student@example.com', 'Male', 1, crypt('password', gen_salt('bf')), '+2347012345678', 'Borno', 'Maiduguri', '234 Maiduguri Main Street, Borno'),
('Chinwe', 'Nwosu', 'chinwe.student@example.com', 'Male', 1, crypt('password', gen_salt('bf')), '+2347012345678', 'Rivers', 'Port Harcourt', '456 Port Harcourt Road, Rivers'),
('Aisha', 'Mohammed', 'aisha.student@example.com', 'Female', 1, crypt('password', gen_salt('bf')), '+2347012345678', 'Oyo', 'Ibadan', '789 Ibadan Road, Oyo'),
('Chidi', 'Okafor', 'chidi.student@example.com', 'Male', 1, crypt('password', gen_salt('bf')), '+2347012345678', 'Benue', 'Makurdi', '123 Makurdi Street, Benue'),
('Funmilayo', 'Akinyemi', 'funmi.staff@example.com', 'Female', 2, crypt('password', gen_salt('bf')), '+2347012345678', 'Lagos', 'Ikeja', '456 Street, Ikeja, Lagos'),
('Bello', 'Ahmed', 'bello.staff@example.com', 'Male', 2, crypt('password', gen_salt('bf')), '+2347012345678', 'Kaduna', 'Kaduna', '12 Kaduna Road, Kaduna'),
('Sam', 'Loco', 'admin@gmail.com', 'Male', 3, crypt('password', gen_salt('bf')), '+2347012345678', 'Abuja', 'Central', '101 Central Street, Abuja');

-- Seed for staffs
INSERT INTO dic_staffs (account_id, department_id) VALUES
(15, 1),
(16, 2);

-- Seed for courses
INSERT INTO dic_courses (name, description, created_at, lecturer_id) VALUES
('Introduction to Global Security', 'Learn the fundamentals of global security studies.', '2021-01-01 00:00:00', 15),
('Understanding Terrorism', 'Examine terrorism as a global issue and its implications.', '2021-02-15 00:00:00', 16),
('Security Policy Development', 'Develop security policies for various scenarios.', '2021-03-01 00:00:00', 15),
('Global Trade Dynamics', 'Analyze trends in global trade and economics.', '2020-05-10 00:00:00', 16),
('International Economic Policies', 'Explore policies affecting global trade.', '2020-06-20 00:00:00', 15),
('Trade and Economic Development', 'Study trade as a tool for economic growth.', '2020-07-15 00:00:00', 16),
('Introduction to Human Rights', 'Understand the foundations of human rights.', '2022-09-10 00:00:00', 15),
('Global Humanitarian Challenges', 'Study humanitarian interventions worldwide.', '2022-09-18 00:00:00', 16),
('Conflict and Human Rights', 'Examine the intersection of human rights and conflict.', '2022-10-05 00:00:00', 15),
('Climate Policy Frameworks', 'Learn the structure of climate change policies.', '2023-03-12 00:00:00', 16),
('Global Governance Systems', 'Explore governance in addressing climate challenges.', '2023-04-01 00:00:00', 15),
('Climate Change and Society', 'Study the societal impacts of climate change.', '2023-04-15 00:00:00', 16),
('Introduction to Diplomacy', 'Understand the basics of diplomatic relations.', '2024-01-10 00:00:00', 15),
('Conflict Management Strategies', 'Learn effective strategies for managing conflicts.', '2024-01-20 00:00:00', 16),
('Global Conflict Resolution', 'Analyze case studies of global conflict resolution.', '2024-02-05 00:00:00', 15),
('Mediation Practices', 'Learn the art of mediation in resolving disputes.', '2024-02-25 00:00:00', 16),
('Peacebuilding Strategies', 'Explore strategies to build and maintain peace.', '2024-03-05 00:00:00', 15),
('Cartographic Techniques', 'Learn techniques for map-making and analysis.', '2022-08-01 00:00:00', 16),
('GIS Applications in Geography', 'Apply GIS tools to geographical studies.', '2022-08-15 00:00:00', 15),
('Remote Sensing Technologies', 'Explore technologies for remote sensing and analysis.', '2023-07-01 00:00:00', 16),
('Urban Planning Principles', 'Understand the principles of urban planning.', '2021-06-10 00:00:00', 16),
('Sustainable Urban Development', 'Study sustainable practices in urban development.', '2021-07-01 00:00:00', 16),
('Environmental Impact Assessment', 'Assess the environmental impacts of projects.', '2020-11-01 00:00:00', 15),
('Sustainable Development Practices', 'Learn sustainable practices in development.', '2022-05-15 00:00:00', 16),
('Disaster Risk Management', 'Manage and mitigate risks associated with disasters.', '2023-02-20 00:00:00', 15),
('GIS Data Analysis', 'Analyze spatial data using GIS tools.', '2023-03-10 00:00:00', 16),
('Urbanization Challenges', 'Examine challenges of urbanization worldwide.', '2021-08-25 00:00:00', 15),
('Environmental Policy Analysis', 'Analyze and evaluate environmental policies.', '2024-04-01 00:00:00', 15),
('Software Development Fundamentals', 'Learn the basics of software development.', '2024-05-10 00:00:00', 15),
('Web Development Technologies', 'Explore web development tools and technologies.', '2024-05-15 00:00:00', 15),
('Graphic Design Principles', 'Understand the principles of graphic design.', '2022-12-01 00:00:00', 16),
('Visual Communication Techniques', 'Learn techniques for visual communication.', '2022-12-10 00:00:00', 15),
('Data Structures and Algorithms', 'Learn key data structures and algorithms.', '2023-01-01 00:00:00', 16),
('Machine Learning Fundamentals', 'Understand the basics of machine learning.', '2023-02-01 00:00:00', 16),
('Ethics in Technology', 'Explore ethical considerations in modern technology.', '2023-06-01 00:00:00', 15),
('Climate Change Adaptation Strategies', 'Learn strategies for adapting to climate change.', '2023-06-15 00:00:00', 15);
;

-- Seed for linking courses to programs
INSERT INTO dic_programs_courses (program_id, course_id) VALUES
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
(2, 7), (2, 8), (2, 9), (2, 10), (2, 11), (2, 12),
(3, 13), (3, 14), (3, 15), (3, 16), (3, 17), (3, 18),
(4, 19), (4, 20), (4, 21), (4, 22), (4, 23), (4, 24),
(5, 25), (5, 26), (5, 27), (5, 28), (5, 29), (5, 30),
(6, 31), (6, 32), (6, 33), (6, 34), (6, 35), (6, 36);

-- Seed for dic_course_videos
INSERT INTO dic_course_videos (course_id, video_url, title, description) VALUES
(1, 'https://example.com/videos/global-security.mp4', 'Introduction to Global Security', 
 'A comprehensive introduction to the field of global security studies.'),
(1, 'https://example.com/videos/terrorism.mp4', 'Understanding Terrorism', 
 'Detailed analysis of terrorism as a global issue and its implications.'),
(2, 'https://example.com/videos/trade-dynamics.mp4', 'Global Trade Dynamics', 
 'Explore the complexities and trends in global trade and economics.'),
(2, 'https://example.com/videos/economic-policies.mp4', 'International Economic Policies', 
 'Understand the policies shaping international trade and economic relations.'),
(3, 'https://example.com/videos/human-rights.mp4', 'Introduction to Human Rights', 
 'An introduction to human rights and their global significance.'),
(3, 'https://example.com/videos/humanitarian-challenges.mp4', 'Global Humanitarian Challenges', 
 'Examine humanitarian interventions across the world.'),
(4, 'https://example.com/videos/climate-policy.mp4', 'Climate Policy Frameworks', 
 'Learn about climate policies and their implementation.'),
(4, 'https://example.com/videos/global-governance.mp4', 'Global Governance Systems', 
 'An overview of global governance mechanisms for addressing climate change.'),
(5, 'https://example.com/videos/conflict-management.mp4', 'Conflict Management Strategies', 
 'Develop effective strategies for managing and resolving conflicts.'),
(5, 'https://example.com/videos/diplomacy.mp4', 'Introduction to Diplomacy', 
 'Understand the principles and practices of diplomatic relations.'),
(6, 'https://example.com/videos/peacebuilding.mp4', 'Peacebuilding Strategies', 
 'Explore practical strategies for building and maintaining peace.');

-- Seed for students
INSERT INTO dic_students (account_id, batch_id, program_id, status) VALUES
(1, 1, 1, 'Active'),
(2, 1, 2, 'Dropout'),
(3, 2, 3, 'Active'),
(4, 2, 4, 'Active'),
(5, 3, 5, 'Graduated'),
(6, 3, 6, 'Active'),
(7, 4, 7, 'Active'),
(8, 4, 8, 'Active'),
(9, 5, 9, 'Active'),
(10, 5, 10, 'Dropout'),
(11, 6, 11, 'Active'),
(12, 6, 12, 'Active'),
(13, 7, 13, 'Suspended');



-- Seed for dic_courses_enrollments
INSERT INTO dic_courses_enrollments (course_id, student_id) VALUES
(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1),
(1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2),
(1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3),
(1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4),
(1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5),
(1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6),
(1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7),
(1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8),
(1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9),
(1, 10), (2, 10), (3, 10), (4, 10), (5, 10), (6, 10),
(1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11),
(1, 12), (2, 12), (3, 12), (4, 12), (5, 12), (6, 12),
(1, 13), (2, 13), (3, 13), (4, 13), (5, 13), (6, 13);


-- Seed for applications
INSERT INTO dic_applications (photo_url, first_name, last_name, email, phone_number, gender, date_of_birth, 
program_id, application_form_url, description, status) VALUES
('https://example.com/photos/bolaji.jpg', 'Bolaji', 'Adebisi', 'bolaji.student@example.com', 
'+2347012345678', 'Male', '2000-05-12', 1, 'https://example.com/forms/bolaji_form.pdf', 
'Application for the Software Engineering program.', 'Pending'),
('https://example.com/photos/ngozi.jpg', 'Ngozi', 'Onwumere', 'ngozi.student@example.com', 
'+2348012345678', 'Female', '1998-11-22', 3, 'https://example.com/forms/ngozi_form.pdf', 
'Application for the Graphic Design program.', 'Approved'),
('https://example.com/photos/temi.jpg', 'Temi', 'Olajide', 'temi.student@example.com', 
'+2349012345678', 'Female', '1999-08-15', 2, 'https://example.com/forms/temi_form.pdf', 
'Application for the Business Administration program.', 'Rejected'),
('https://example.com/photos/chris.jpg', 'Chris', 'Ugochukwu', 'chris.student@example.com', 
'+2347012345679', 'Male', '2001-04-20', 1, 'https://example.com/forms/chris_form.pdf', 
'Application for the Software Engineering program.', 'Pending'),
('https://example.com/photos/adeola.jpg', 'Adeola', 'Fashola', 'adeola.student@example.com', 
'+2347023456789', 'Female', '1997-02-28', 4, 'https://example.com/forms/adeola_form.pdf', 
'Application for the Marketing program.', 'Approved'),
('https://example.com/photos/stanley.jpg', 'Stanley', 'Okafor', 'stanley.student@example.com', 
'+2347034567890', 'Male', '1995-10-14', 5, 'https://example.com/forms/stanley_form.pdf', 
'Application for the Civil Engineering program.', 'Pending'),
('https://example.com/photos/jane.jpg', 'Jane', 'Ademola', 'jane.student@example.com', 
'+2347045678901', 'Female', '1999-06-30', 3, 'https://example.com/forms/jane_form.pdf', 
'Application for the Graphic Design program.', 'Approved'),
('https://example.com/photos/bamidele.jpg', 'Bamidele', 'Ogunyemi', 'bamidele.student@example.com', 
'+2347056789012', 'Male', '2002-01-10', 2, 'https://example.com/forms/bamidele_form.pdf', 
'Application for the Business Administration program.', 'Pending'),
('https://example.com/photos/oluwaseun.jpg', 'Oluwaseun', 'Ibrahim', 'oluwaseun.student@example.com', 
'+2347067890123', 'Male', '2001-09-05', 1, 'https://example.com/forms/oluwaseun_form.pdf', 
'Application for the Software Engineering program.', 'Rejected'),
('https://example.com/photos/faith.jpg', 'Faith', 'Ogundele', 'faith.student@example.com', 
'+2347078901234', 'Female', '2000-12-17', 4, 'https://example.com/forms/faith_form.pdf', 
'Application for the Marketing program.', 'Pending'),
('https://example.com/photos/olumide.jpg', 'Olumide', 'Ajayi', 'olumide.student@example.com', 
'+2347089012345', 'Male', '1998-03-22', 2, 'https://example.com/forms/olumide_form.pdf', 
'Application for the Business Administration program.', 'Approved'),
('https://example.com/photos/precious.jpg', 'Precious', 'Akinmoladun', 'precious.student@example.com', 
'+2347090123456', 'Female', '2000-11-09', 5, 'https://example.com/forms/precious_form.pdf', 
'Application for the Civil Engineering program.', 'Pending');

-- Seed data for dic_exams
INSERT INTO dic_exams (course_id, title, description, question_paper_url, start_date, duration, pass_mark, created_at, updated_at) VALUES
(1, 'Final Exam: International Relations', 
    'This is the final exam for the International Relations and Diplomacy course. The exam covers all topics discussed during the course.', 
    'https://example.com/ir_exam.pdf', 
    '2024-01-03 12:30:00', 
    120, 70, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(2, 'Final Exam: Criminology', 
    'This exam covers criminology theories, types of crime, and the justice system.', 
    'https://example.com/criminology_exam.pdf', 
    '2024-01-05 09:00:00', 
    90, 50, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(3, 'Final Exam: Geography and Environmental Sustainability', 
    'This exam tests knowledge on climate change, geography, and sustainability practices.', 
    'https://example.com/geo_exam.pdf', 
    '2024-01-10 15:00:00', 
    180, 65, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(4, 'Final Exam: Global Trade Dynamics',
    'This exam covers global trade trends, economic policies, and trade relations.', 
    'https://example.com/trade_exam.pdf', 
    '2024-01-15 10:30:00', 
    120, 60, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(5, 'Final Exam: Human Rights and Humanitarian Intervention',
    'This exam tests knowledge on human rights issues and humanitarian interventions.', 
    'https://example.com/human_rights_exam.pdf', 
    '2024-01-20 14:00:00', 
    150, 70, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(6, 'Final Exam: Climate Policy and Governance',
    'This exam covers climate policy frameworks and global governance systems.', 
    'https://example.com/climate_policy_exam.pdf', 
    '2024-01-25 11:00:00', 
    90, 55, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(7, 'Final Exam: Conflict Resolution',
    'This exam tests knowledge on conflict resolution theories and practices.', 
    'https://example.com/conflict_resolution_exam.pdf', 
    '2024-02-01 09:30:00', 
    120, 60, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(8, 'Final Exam: Cartography',
    'This exam covers cartographic techniques and map-making principles.', 
    'https://example.com/cartography_exam.pdf', 
    '2024-02-05 13:00:00', 
    90, 50, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(9, 'Final Exam: Remote Sensing Technologies',
    'This exam tests knowledge on remote sensing technologies and applications.', 
    'https://example.com/remote_sensing_exam.pdf', 
    '2024-02-10 10:00:00', 
    120, 65, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(10, 'Final Exam: Urban Planning Principles',
    'This exam covers urban planning principles and sustainable development practices.', 
    'https://example.com/urban_planning_exam.pdf', 
    '2024-02-15 14:30:00', 
    150, 70, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

-- Seed data for dic_assignments
INSERT INTO dic_assignments (course_id, title, description, due_date, pass_mark, created_at, updated_at, assignment_url) VALUES
(1, 'Essay on Global Politics', 'Write a 2000-word essay on the role of global politics in international relations.', '2024-12-10', 60, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'http://example.com/assignments/essay-global-politics'),
(2, 'Research Paper on Crime Prevention', 'Submit a research paper discussing modern crime prevention methods and their effectiveness.', '2024-12-15', 50, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'http://example.com/assignments/research-paper-crime-prevention'),
(3, 'Project on Sustainability Practices', 'Submit a project on sustainable farming practices for urban environments.', '2024-12-20', 55, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'http://example.com/assignments/project-sustainability-practices'),
(4, 'Trade Policy Analysis', 'Analyze a recent trade policy and its impact on global trade dynamics.', '2024-12-25', 45, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'http://example.com/assignments/trade-policy-analysis'),
(5, 'Human Rights Case Study', 'Present a case study on a human rights violation and the corresponding humanitarian intervention.', '2025-01-01', 65, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'http://example.com/assignments/human-rights-case-study'),
(6, 'Climate Change Policy Review', 'Review a climate change policy framework and propose improvements for better governance.', '2025-01-05', 70, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'http://example.com/assignments/climate-change-policy-review'),
(7, 'Conflict Resolution Strategies', 'Develop a set of conflict resolution strategies for a hypothetical conflict scenario.', '2025-01-10', 60, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'http://example.com/assignments/conflict-resolution-strategies'),
(8, 'Cartographic Map Project', 'Create a detailed map using cartographic techniques and present its analysis.', '2025-01-15', 50, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'http://example.com/assignments/cartographic-map-project'),
(9, 'Remote Sensing Data Analysis', 'Analyze remote sensing data to identify environmental changes and trends.', '2025-01-20', 65, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'http://example.com/assignments/remote-sensing-data-analysis'),
(10, 'Urban Planning Proposal', 'Develop a proposal for sustainable urban planning practices in a growing city.', '2025-01-25', 70, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'http://example.com/assignments/urban-planning-proposal');

-- Seed data for dic_assignment_submissions
INSERT INTO dic_assignment_submissions (assignment_id, student_id, submission_url, score, created_at, updated_at) VALUES
(1, 1, 'https://example.com/submissions/ir_essay.pdf', 70, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(2, 2, 'https://example.com/submissions/criminology_paper.pdf', 45, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(3, 3, 'https://example.com/submissions/geo_project.pdf', 60, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(4, 4, 'https://example.com/submissions/trade_analysis.pdf', 40, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(5, 5, 'https://example.com/submissions/human_rights_case.pdf', 65, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(6, 6, 'https://example.com/submissions/climate_policy_review.pdf', 70, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(7, 7, 'https://example.com/submissions/conflict_strategies.pdf', 55, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(8, 8, 'https://example.com/submissions/cartographic_map.pdf', 50, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(9, 9, 'https://example.com/submissions/remote_sensing_analysis.pdf', 60, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(10, 10, 'https://example.com/submissions/urban_planning_proposal.pdf', 70, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(1, 2, 'https://example.com/submissions/ir_essay.pdf', 65, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(2, 3, 'https://example.com/submissions/criminology_paper.pdf', 40, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(3, 4, 'https://example.com/submissions/geo_project.pdf', 55, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(4, 5, 'https://example.com/submissions/trade_analysis.pdf', 35, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(5, 6, 'https://example.com/submissions/human_rights_case.pdf', 60, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(6, 7, 'https://example.com/submissions/climate_policy_review.pdf', 65, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(7, 8, 'https://example.com/submissions/conflict_strategies.pdf', 50, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(8, 9, 'https://example.com/submissions/cartographic_map.pdf', 45, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(9, 10, 'https://example.com/submissions/remote_sensing_analysis.pdf', 55, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(10, 11, 'https://example.com/submissions/urban_planning_proposal.pdf', 60, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(1, 3, 'https://example.com/submissions/ir_essay.pdf', 60, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(2, 4, 'https://example.com/submissions/criminology_paper.pdf', 50, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(3, 5, 'https://example.com/submissions/geo_project.pdf', 65, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(4, 6, 'https://example.com/submissions/trade_analysis.pdf', 40, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(5, 7, 'https://example.com/submissions/human_rights_case.pdf', 70, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(6, 8, 'https://example.com/submissions/climate_policy_review.pdf', 75, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(7, 9, 'https://example.com/submissions/conflict_strategies.pdf', 55, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(8, 10, 'https://example.com/submissions/cartographic_map.pdf', 50, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(9, 11, 'https://example.com/submissions/remote_sensing_analysis.pdf', 60, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(10, 12, 'https://example.com/submissions/urban_planning_proposal.pdf', 70, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

-- Seed data for dic_exam_results
INSERT INTO dic_exam_results (exam_id, student_id, student_submission_url, score, created_at, updated_at) VALUES
(1, 1, 'https://example.com/submissions/ir_exam.pdf', 75, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(1, 2, 'https://example.com/submissions/ir_exam.pdf', 70, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(1, 3, 'https://example.com/submissions/ir_exam.pdf', 65, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(1, 4, 'https://example.com/submissions/ir_exam.pdf', 80, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(1, 5, 'https://example.com/submissions/ir_exam.pdf', 85, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(1, 6, 'https://example.com/submissions/ir_exam.pdf', 90, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(1, 7, 'https://example.com/submissions/ir_exam.pdf', 55, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(1, 8, 'https://example.com/submissions/ir_exam.pdf', 60, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(1, 9, 'https://example.com/submissions/ir_exam.pdf', 70, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(1, 10, 'https://example.com/submissions/ir_exam.pdf', 75, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(1, 11, 'https://example.com/submissions/ir_exam.pdf', 80, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(1, 12, 'https://example.com/submissions/ir_exam.pdf', 85, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(2, 1, 'https://example.com/submissions/criminology_exam.pdf', 60, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(2, 2, 'https://example.com/submissions/criminology_exam.pdf', 55, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(2, 3, 'https://example.com/submissions/criminology_exam.pdf', 50, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(2, 4, 'https://example.com/submissions/criminology_exam.pdf', 65, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(2, 5, 'https://example.com/submissions/criminology_exam.pdf', 70, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(2, 6, 'https://example.com/submissions/criminology_exam.pdf', 75, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(2, 7, 'https://example.com/submissions/criminology_exam.pdf', 45, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(2, 8, 'https://example.com/submissions/criminology_exam.pdf', 50, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(2, 9, 'https://example.com/submissions/criminology_exam.pdf', 60, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(2, 10, 'https://example.com/submissions/criminology_exam.pdf', 65, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(2, 11, 'https://example.com/submissions/criminology_exam.pdf', 70, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(2, 12, 'https://example.com/submissions/criminology_exam.pdf', 75, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(3, 1, 'https://example.com/submissions/geo_exam.pdf', 65, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(3, 2, 'https://example.com/submissions/geo_exam.pdf', 60, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(3, 3, 'https://example.com/submissions/geo_exam.pdf', 55, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(3, 4, 'https://example.com/submissions/geo_exam.pdf', 70, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(3, 5, 'https://example.com/submissions/geo_exam.pdf', 75, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(3, 6, 'https://example.com/submissions/geo_exam.pdf', 80, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(3, 7, 'https://example.com/submissions/geo_exam.pdf', 45, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(3, 8, 'https://example.com/submissions/geo_exam.pdf', 50, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(3, 9, 'https://example.com/submissions/geo_exam.pdf', 60, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(3, 10, 'https://example.com/submissions/geo_exam.pdf', 65, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(3, 11, 'https://example.com/submissions/geo_exam.pdf', 70, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(3, 12, 'https://example.com/submissions/geo_exam.pdf', 75, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
