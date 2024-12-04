-- Seed for account_types
INSERT INTO dic_account_types (name) VALUES 
('Admin'),
('Student'),
('Teacher'),
('Staff');

-- Seed for accounts
INSERT INTO dic_accounts (username, email, first_name, last_name, account_type_id, password) VALUES
('admin_adebayo', 'adebayo.admin@example.com', 'Adebayo', 'Ogunleye', 1, 'password'),
('admin_ifeoma', 'ifeoma.admin@example.com', 'Ifeoma', 'Okafor', 1, 'password'),
('staff_bello', 'bello.staff@example.com', 'Bello', 'Ahmed', 4, 'password'),
('staff_funmi', 'funmi.staff@example.com', 'Funmilayo', 'Akinyemi', 4, 'password'),
('student_bolaji', 'bolaji.student@example.com', 'Bolaji', 'Adebisi', 2, 'password'),
('student_kemi', 'kemi.student@example.com', 'Kemi', 'Oladele', 2, 'password'),
('student_chinedu', 'chinedu.student@example.com', 'Chinedu', 'Ibekwe', 2, 'password'),
('student_amaka', 'amaka.student@example.com', 'Amaka', 'Eze', 2, 'password'),
('student_ibrahim', 'ibrahim.student@example.com', 'Ibrahim', 'Aliyu', 2, 'password'),
('student_ifeanyi', 'ifeanyi.student@example.com', 'Ifeanyi', 'Okoro', 2, 'password'),
('student_ngozi', 'ngozi.student@example.com', 'Ngozi', 'Onwumere', 2, 'password'),
('student_sheriff', 'sheriff.student@example.com', 'Sheriff', 'Adamu', 2, 'password'),
('student_sola', 'sola.student@example.com', 'Sola', 'Ogunbiyi', 2, 'password'),
('student_musa', 'musa.student@example.com', 'Musa', 'Garba', 2, 'password');

-- Seed for departments
INSERT INTO dic_departments (name, description) VALUES
('Department of Geography and Environmental Sustainability M.Sc. and PhD', 
 'Offering advanced studies in geography and environmental sustainability.'),
('Department of Computer Science', 'Department focused on computer science education and research.'),
('Department of Engineering', 'Department offering various engineering disciplines.'),
('Arts', 'Department for creative arts and humanities.');

INSERT INTO dic_programs (name, department_id, description) VALUES
-- Existing programs
('Global Security and Terrorism', 1, 'Focuses on security studies, terrorism, and global challenges.'),
('International Trade and Economics', 1, 'Covers trade relations and economic development.'),
('Human Rights and Humanitarian Intervention', 1, 'Addresses human rights issues and interventions.'),
('Climate Change and Global Governance', 1, 'Examines climate policy and governance challenges.'),
('Diplomacy and Conflict Resolution', 1, 'Focuses on diplomacy and strategies for conflict resolution.'),
('Conflict Resolution', 1, 'Specializes in theories and practices of conflict resolution.'),
('Cartography', 2, 'Studies map-making techniques and their applications in geography.'),
('Remote Sensing', 2, 'Focuses on satellite imagery and aerial photography in environmental studies.'),
('Urban and Regional Planning', 2, 'Examines the planning and development of urban areas.'),
('Environmental Impact Assessment', 3, 'Covers techniques to assess environmental impacts of projects.'),
('Sustainable Development', 3, 'Focuses on sustainable practices in development and resource management.'),
('Natural Disaster Management', 3, 'Explores strategies to manage and mitigate natural disasters.'),
('Geographical Information Systems (GIS)', 3, 
 'Focuses on spatial data analysis and mapping technologies.'),
('Global Urbanization Studies', 3, 'Explores the challenges and opportunities of global urbanization.'),
('Environmental Policy and Planning', 3, 'Examines the development and implementation of environmental policies.');

-- Seed for courses
INSERT INTO dic_courses (name, program_id, description) VALUES
('Introduction to Global Security', 1, 'Learn the fundamentals of global security studies.'),
('Understanding Terrorism', 1, 'Examine terrorism as a global issue and its implications.'),
('Security Policy Development', 1, 'Develop security policies for various scenarios.'),
('Global Trade Dynamics', 2, 'Analyze trends in global trade and economics.'),
('International Economic Policies', 2, 'Explore policies affecting global trade.'),
('Trade and Economic Development', 2, 'Study trade as a tool for economic growth.'),
('Introduction to Human Rights', 3, 'Understand the foundations of human rights.'),
('Global Humanitarian Challenges', 3, 'Study humanitarian interventions worldwide.'),
('Conflict and Human Rights', 3, 'Examine the intersection of human rights and conflict.'),
('Climate Policy Frameworks', 4, 'Learn the structure of climate change policies.'),
('Global Governance Systems', 4, 'Explore governance in addressing climate challenges.'),
('Climate Change and Society', 4, 'Study the societal impacts of climate change.'),
('Introduction to Diplomacy', 5, 'Understand the basics of diplomatic relations.'),
('Conflict Management Strategies', 5, 'Learn effective strategies for managing conflicts.'),
('Global Conflict Resolution', 5, 'Analyze case studies of global conflict resolution.'),
('Conflict Resolution Theories', 6, 'Study theories underpinning conflict resolution.'),
('Mediation Practices', 6, 'Learn the art of mediation in resolving disputes.'),
('Peacebuilding Strategies', 6, 'Explore strategies to build and maintain peace.');

-- Seed for applications
INSERT INTO dic_applications (photo_url, first_name, last_name, email, phone_number, gender, date_of_birth, 
program_id, application_form_url, description) VALUES
('https://example.com/photos/bolaji.jpg', 'Bolaji', 'Adebisi', 'bolaji.student@example.com', 
'+2347012345678', 'Male', '2000-05-12', 1, 'https://example.com/forms/bolaji_form.pdf', 
'Application for the Software Engineering program.'),

('https://example.com/photos/ngozi.jpg', 'Ngozi', 'Onwumere', 'ngozi.student@example.com', 
'+2348012345678', 'Female', '1998-11-22', 3, 'https://example.com/forms/ngozi_form.pdf', 
'Application for the Graphic Design program.');

