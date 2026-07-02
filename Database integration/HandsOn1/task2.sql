-- ==========================================
-- Task 2: Verify Normalization
-- ==========================================

-- 1NF (First Normal Form)
-- All tables contain atomic values.
-- Each column stores only one value.
-- Example violation: Storing multiple phone numbers in one column
-- such as '9876543210,9123456789' would violate 1NF.

-- 2NF (Second Normal Form)
-- All non-key attributes are fully dependent on the primary key.
-- In the enrollments table, the logical candidate key is
-- (student_id, course_id). Attributes like enrollment_date
-- and grade depend on the entire key, not just student_id
-- or course_id individually.

-- 3NF (Third Normal Form)
-- There are no transitive dependencies.
-- Department information is stored only in the departments table.
-- Students, courses, and professors reference departments using
-- department_id as a foreign key.
-- Storing department_name directly in the students table would
-- violate 3NF because:
-- student_id → department_id → department_name.

-- Enrollments Table Analysis
-- The enrollments table satisfies 3NF because all non-key
-- attributes depend only on the primary key and not on
-- any other non-key attribute.