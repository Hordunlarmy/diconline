CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE IF NOT EXISTS dic_account_types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS dic_batches (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    year INT NOT NULL,
    description TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS dic_departments (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    head_of_department VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS dic_accounts (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255) NOT NULL,
    phone_number VARCHAR(255),
    state VARCHAR(255),
    local_government VARCHAR(255),
    address TEXT,
    gender VARCHAR(255),
    account_type_id INT NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_account_type FOREIGN KEY (account_type_id) REFERENCES dic_account_types(id)
);

CREATE TABLE IF NOT EXISTS dic_students (
    id SERIAL PRIMARY KEY,
    account_id INT NOT NULL,
    batch_id INT NOT NULL,
    department_id INT NOT NULL,
    next_of_kin_name VARCHAR(255),
    status VARCHAR(255) DEFAULT 'Active' CHECK (status IN ('Active', 'Dropout', 'Graduated', 'Suspended')),
    enrollment_date DATE NOT NULL DEFAULT CURRENT_DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_account FOREIGN KEY (account_id) REFERENCES dic_accounts(id),
    CONSTRAINT fk_batch FOREIGN KEY (batch_id) REFERENCES dic_batches(id),
    CONSTRAINT fk_department FOREIGN KEY (department_id) REFERENCES dic_departments(id)
);

CREATE TABLE IF NOT EXISTS dic_staffs (
    id SERIAL PRIMARY KEY,
    account_id INT NOT NULL,
    department_id INT NOT NULL,
    status VARCHAR(255) DEFAULT 'Active' CHECK (status IN ('Active', 'Resigned', 'Suspended')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_account FOREIGN KEY (account_id) REFERENCES dic_accounts(id),
    CONSTRAINT fk_department FOREIGN KEY (department_id) REFERENCES dic_departments(id)
);

CREATE TABLE IF NOT EXISTS dic_programs (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    department_id INT NOT NULL,
    description TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_department FOREIGN KEY (department_id) REFERENCES dic_departments(id)
);

CREATE TABLE IF NOT EXISTS dic_courses (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    program_id INT NOT NULL,
    description TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_program FOREIGN KEY (program_id) REFERENCES dic_programs(id)
);

CREATE TABLE IF NOT EXISTS dic_courses_enrollments (
    id SERIAL PRIMARY KEY,
    course_id INT NOT NULL,
    student_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_course FOREIGN KEY (course_id) REFERENCES dic_courses(id),
    CONSTRAINT fk_student FOREIGN KEY (student_id) REFERENCES dic_accounts(id)
);

CREATE TABLE IF NOT EXISTS dic_course_videos (
    id SERIAL PRIMARY KEY,
    course_id INT NOT NULL,
    video_url VARCHAR(255) NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_course FOREIGN KEY (course_id) REFERENCES dic_courses(id)
);

CREATE TABLE IF NOT EXISTS dic_applications (
    id SERIAL PRIMARY KEY,
    photo_url VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone_number VARCHAR(255) NOT NULL,
    gender VARCHAR(255) NOT NULL,
    date_of_birth DATE NOT NULL,
    program_id INT NOT NULL,
    application_form_url VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(255) DEFAULT 'Pending' CHECK (status IN ('Pending', 'Approved', 'Rejected')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_program FOREIGN KEY (program_id) REFERENCES dic_programs(id),
    CONSTRAINT chk_gender CHECK (gender IN ('Male', 'Female', 'Other'))
);

CREATE TABLE IF NOT EXISTS dic_exams (
    id SERIAL PRIMARY KEY,
    course_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    question_paper_url VARCHAR(255) NOT NULL,
    duration INT NOT NULL,
    pass_mark INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_course FOREIGN KEY (course_id) REFERENCES dic_courses(id)
);

CREATE TABLE IF NOT EXISTS dic_assignments (
    id SERIAL PRIMARY KEY,
    course_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    due_date DATE NOT NULL,
    pass_mark INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_course FOREIGN KEY (course_id) REFERENCES dic_courses(id)
);

CREATE TABLE IF NOT EXISTS dic_assignment_submissions (
    id SERIAL PRIMARY KEY,
    assignment_id INT NOT NULL,
    student_id INT NOT NULL,
    submission_url VARCHAR(255) NOT NULL,
    score INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_assignment FOREIGN KEY (assignment_id) REFERENCES dic_assignments(id),
    CONSTRAINT fk_student FOREIGN KEY (student_id) REFERENCES dic_accounts(id)
);

CREATE TABLE IF NOT EXISTS dic_exam_results (
    id SERIAL PRIMARY KEY,
    exam_id INT NOT NULL,
    student_id INT NOT NULL,
    student_submission_url VARCHAR(255) NOT NULL,
    score INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_exam FOREIGN KEY (exam_id) REFERENCES dic_exams(id),
    CONSTRAINT fk_student FOREIGN KEY (student_id) REFERENCES dic_accounts(id)
);

