-- ==========================================
-- Task 3: Alter and Extend the Schema
-- ==========================================

-- Step 10: Add phone_number column to students table
ALTER TABLE students
ADD phone_number VARCHAR(15);

-- Step 11: Add max_seats column to courses table
ALTER TABLE courses
ADD max_seats INT DEFAULT 60;

-- Step 12: Add CHECK constraint to enrollments table
ALTER TABLE enrollments
ADD CONSTRAINT chk_grade
CHECK (grade IN ('A','B','C','D','F') OR grade IS NULL);

-- Step 13: Rename department head column
-- (Assuming the departments table has a column named hod_name)

ALTER TABLE departments
CHANGE hod_name head_of_dept VARCHAR(100);

-- Step 14: Drop phone_number column from students table
ALTER TABLE students
DROP COLUMN phone_number;