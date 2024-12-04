-- Seed for account_types
INSERT INTO dic_account_types (name) VALUES 
('Admin'),
('Student'),
('Teacher'),
('Staff');

-- Seed for departments
INSERT INTO dic_departments (name, description) VALUES
('Department of Geography and Environmental Sustainability M.Sc. and PhD', 
 'Offering advanced studies in geography and environmental sustainability.'),
('Department of Computer Science', 'Department focused on computer science education and research.'),
('Department of Engineering', 'Department offering various engineering disciplines.'),
('Arts', 'Department for creative arts and humanities.'),
('Department of Social Sciences', 'Department offering social science programs.');

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
('Environmental Policy and Planning', 3, 'Examines the development and implementation of environmental policies.'),
('Software Engineering', 5, 'Focuses on software development and engineering principles.'),
('Graphic Design', 5, 'Covers design principles and visual communication techniques.');

-- Seed for courses
INSERT INTO dic_courses (name, program_id, description, created_at) VALUES
('Introduction to Global Security', 1, 'Learn the fundamentals of global security studies.', '2021-01-01 00:00:00'),
('Understanding Terrorism', 1, 'Examine terrorism as a global issue and its implications.', '2021-02-15 00:00:00'),
('Security Policy Development', 1, 'Develop security policies for various scenarios.', '2021-03-01 00:00:00'),
('Global Trade Dynamics', 2, 'Analyze trends in global trade and economics.', '2020-05-10 00:00:00'),
('International Economic Policies', 2, 'Explore policies affecting global trade.', '2020-06-20 00:00:00'),
('Trade and Economic Development', 2, 'Study trade as a tool for economic growth.', '2020-07-15 00:00:00'),
('Introduction to Human Rights', 3, 'Understand the foundations of human rights.', '2022-09-10 00:00:00'),
('Global Humanitarian Challenges', 3, 'Study humanitarian interventions worldwide.', '2022-09-18 00:00:00'),
('Conflict and Human Rights', 3, 'Examine the intersection of human rights and conflict.', '2022-10-05 00:00:00'),
('Climate Policy Frameworks', 4, 'Learn the structure of climate change policies.', '2023-03-12 00:00:00'),
('Global Governance Systems', 4, 'Explore governance in addressing climate challenges.', '2023-04-01 00:00:00'),
('Climate Change and Society', 4, 'Study the societal impacts of climate change.', '2023-04-15 00:00:00'),
('Introduction to Diplomacy', 5, 'Understand the basics of diplomatic relations.', '2024-01-10 00:00:00'),
('Conflict Management Strategies', 5, 'Learn effective strategies for managing conflicts.', '2024-01-20 00:00:00'),
('Global Conflict Resolution', 5, 'Analyze case studies of global conflict resolution.', '2024-02-05 00:00:00'),
('Conflict Resolution Theories', 6, 'Study theories underpinning conflict resolution.', '2024-02-15 00:00:00'),
('Mediation Practices', 6, 'Learn the art of mediation in resolving disputes.', '2024-02-25 00:00:00'),
('Peacebuilding Strategies', 6, 'Explore strategies to build and maintain peace.', '2024-03-05 00:00:00'),
('Cartographic Techniques', 7, 'Learn techniques for map-making and analysis.', '2022-08-01 00:00:00'),
('GIS Applications in Geography', 7, 'Apply GIS tools to geographical studies.', '2022-08-15 00:00:00'),
('Remote Sensing Technologies', 8, 'Explore technologies for remote sensing and analysis.', '2023-07-01 00:00:00'),
('Urban Planning Principles', 9, 'Understand the principles of urban planning.', '2021-06-10 00:00:00'),
('Sustainable Urban Development', 9, 'Study sustainable practices in urban development.', '2021-07-01 00:00:00'),
('Environmental Impact Assessment', 10, 'Assess the environmental impacts of projects.', '2020-11-01 00:00:00'),
('Sustainable Development Practices', 11, 'Learn sustainable practices in development.', '2022-05-15 00:00:00'),
('Disaster Risk Management', 12, 'Manage and mitigate risks associated with disasters.', '2023-02-20 00:00:00'),
('GIS Data Analysis', 13, 'Analyze spatial data using GIS tools.', '2023-03-10 00:00:00'),
('Urbanization Challenges', 14, 'Examine challenges of urbanization worldwide.', '2021-08-25 00:00:00'),
('Environmental Policy Analysis', 15, 'Analyze and evaluate environmental policies.', '2024-04-01 00:00:00'),
('Software Development Fundamentals', 16, 'Learn the basics of software development.', '2024-05-10 00:00:00'),
('Web Development Technologies', 16, 'Explore web development tools and technologies.', '2024-05-15 00:00:00'),
('Graphic Design Principles', 17, 'Understand the principles of graphic design.', '2022-12-01 00:00:00'),
('Visual Communication Techniques', 17, 'Learn techniques for visual communication.', '2022-12-10 00:00:00');

-- Seed for batches
INSERT INTO dic_batches (name, year, description) VALUES
('2019/2020', 2019, 'Batch for the academic year 2019/2020.'),
('2020/2021', 2020, 'Batch for the academic year 2020/2021.'),
('2021/2022', 2021, 'Batch for the academic year 2021/2022.'),
('2022/2023', 2022, 'Batch for the academic year 2022/2023.'),
('2023/2024', 2023, 'Batch for the academic year 2023/2024.'),
('2024/2025', 2024, 'Batch for the academic year 2024/2025.'),
('2025/2026', 2025, 'Batch for the academic year 2025/2026.');

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

-- Seed for accounts
INSERT INTO dic_accounts (first_name, last_name, email, gender, account_type_id, password, phone_number) VALUES
('Bolaji', 'Adebisi', 'bolaji.student@example.com', 'Male', 1, 'password', '+2347012345678'),
('Kemi', 'Oladele', 'kemi.student@example.com', 'Female', 1, 'password', '+2347012345678'),
('Chinedu', 'Ibekwe', 'chinedu.student@example.com', 'Male', 1, 'password', '+2347012345678'),
('Amaka', 'Eze', 'amaka.student@example.com', 'Female', 1, 'password', '+2347012345678'),
('Ibrahim', 'Aliyu', 'ibrahim.student@example.com', 'Male', 1, 'password', '+2347012345678'),
('Ifeanyi', 'Okoro', 'ifeanyi.student@example.com', 'Male', 1, 'password', '+2347012345678'),
('Ngozi', 'Onwumere', 'ngozi.student@example.com', 'Female', 1, 'password', '+2347012345678'),
('Sheriff', 'Adamu', 'sheriff.student@example.com', 'Male', 1, 'password', '+2347012345678'),
('Sola', 'Ogunbiyi', 'sola.student@example.com', 'Female', 1, 'password', '+2347012345678'),
('Musa', 'Garba', 'musa.student@example.com', 'Male', 1, 'password', '+2347012345678'),
('Chinwe', 'Nwosu', 'chinwe.student@example.com', 'Male', 1, 'password', '+2347012345678'),
('Aisha', 'Mohammed', 'aisha.student@example.com', 'Female', 1, 'password', '+2347012345678'),
('Chidi', 'Okafor', 'chidi.student@example.com', 'Male', 1, 'password', '+2347012345678'),
('Funmilayo', 'Akinyemi', 'funmi.staff@example.com', 'Female', 1, 'password', '+2347012345678'),
('Bello', 'Ahmed', 'bello.staff@example.com', 'Male', 1, 'password', '+2347012345678');


-- Seed for students
INSERT INTO dic_students (account_id, batch_id, department_id, status) VALUES
(1, 1, 1, 'Active'),
(2, 1, 1, 'Dropout'),
(3, 2, 2, 'Active'),
(4, 2, 2, 'Active'),
(5, 3, 3, 'Graduated'),
(6, 3, 3, 'Active'),
(7, 4, 4, 'Active'),
(8, 4, 4, 'Active'),
(9, 5, 5, 'Active'),
(10, 5, 5, 'Dropout'),
(11, 6, 5, 'Active'),
(12, 6, 3, 'Active'),
(13, 7, 1, 'Suspended');

-- Seed for staffs
INSERT INTO dic_staffs (account_id, department_id) VALUES
(14, 1),
(15, 2);


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

