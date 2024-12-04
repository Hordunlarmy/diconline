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
('International Trade and Economics', 2, 'Covers trade relations and economic development.'),
('Human Rights and Humanitarian Intervention', 3, 'Addresses human rights issues and interventions.'),
('Climate Change and Global Governance', 4, 'Examines climate policy and governance challenges.'),
('Diplomacy and Conflict Resolution', 1, 'Focuses on diplomacy and strategies for conflict resolution.'),
('Conflict Resolution', 2, 'Specializes in theories and practices of conflict resolution.'),
('Cartography', 3, 'Studies map-making techniques and their applications in geography.'),
('Remote Sensing', 4, 'Focuses on satellite imagery and aerial photography in environmental studies.'),
('Urban and Regional Planning', 1, 'Examines the planning and development of urban areas.'),
('Environmental Impact Assessment', 2, 'Covers techniques to assess environmental impacts of projects.'),
('Sustainable Development', 3, 'Focuses on sustainable practices in development and resource management.'),
('Natural Disaster Management', 4, 'Explores strategies to manage and mitigate natural disasters.'),
('Geographical Information Systems (GIS)', 1, 
 'Focuses on spatial data analysis and mapping technologies.'),
('Global Urbanization Studies', 1, 'Explores the challenges and opportunities of global urbanization.'),
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
('Peacebuilding Strategies', 6, 'Explore strategies to build and maintain peace.'),
('Cartographic Techniques', 7, 'Learn techniques for map-making and analysis.'),
('GIS Applications in Geography', 7, 'Apply GIS tools to geographical studies.'),
('Remote Sensing Technologies', 8, 'Explore technologies for remote sensing and analysis.'),
('Urban Planning Principles', 9, 'Understand the principles of urban planning.'),
('Sustainable Urban Development', 9, 'Study sustainable practices in urban development.'),
('Environmental Impact Assessment', 10, 'Assess the environmental impacts of projects.'),
('Sustainable Development Practices', 11, 'Learn sustainable practices in development.'),
('Disaster Risk Management', 12, 'Manage and mitigate risks associated with disasters.'),
('GIS Data Analysis', 13, 'Analyze spatial data using GIS tools.'),
('Urbanization Challenges', 14, 'Examine challenges of urbanization worldwide.'),
('Environmental Policy Analysis', 15, 'Analyze and evaluate environmental policies.');

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

-- Seed for dic_courses_enrollments
INSERT INTO dic_courses_enrollments (course_id, student_id) VALUES
(1, 6), 
(1, 7), 
(2, 8), 
(2, 6), 
(3, 9), 
(3, 10), 
(4, 11), 
(4, 12), 
(5, 12), 
(5, 13), 
(6, 14), 
(6, 13); 


-- Seed for applications
INSERT INTO dic_applications (photo_url, first_name, last_name, email, phone_number, gender, date_of_birth, 
program_id, application_form_url, description) VALUES
('https://example.com/photos/bolaji.jpg', 'Bolaji', 'Adebisi', 'bolaji.student@example.com', 
'+2347012345678', 'Male', '2000-05-12', 1, 'https://example.com/forms/bolaji_form.pdf', 
'Application for the Software Engineering program.'),

('https://example.com/photos/ngozi.jpg', 'Ngozi', 'Onwumere', 'ngozi.student@example.com', 
'+2348012345678', 'Female', '1998-11-22', 3, 'https://example.com/forms/ngozi_form.pdf', 
'Application for the Graphic Design program.');

