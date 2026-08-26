CREATE DATABASE IF NOT EXISTS hostel_management;

USE hostel_management;

-- Users table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(20) DEFAULT 'admin'
);

-- Students table
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id VARCHAR(20) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(15),
    gender VARCHAR(20),
    course VARCHAR(100),
    year INT,
    department VARCHAR(100),
    address VARCHAR(255),
    room_number VARCHAR(20)
);

-- Rooms table
CREATE TABLE rooms (
    id INT AUTO_INCREMENT PRIMARY KEY,
    room_number VARCHAR(20) UNIQUE NOT NULL,
    block VARCHAR(20),
    floor INT,
    capacity INT NOT NULL,
    occupied_beds INT DEFAULT 0,
    status VARCHAR(20) DEFAULT 'Available'
);

-- Complaints table
CREATE TABLE complaints (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id VARCHAR(20) NOT NULL,
    complaint_type VARCHAR(100),
    description TEXT,
    status VARCHAR(30) DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Fees table
CREATE TABLE fees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id VARCHAR(20) NOT NULL,
    amount DECIMAL(10,2),
    due_date DATE,
    payment_date DATE,
    status VARCHAR(30) DEFAULT 'Pending',
    payment_method VARCHAR(50)
);

-- Sample rooms
INSERT INTO rooms
(room_number, block, floor, capacity, occupied_beds, status)
VALUES
('A-101', 'A', 1, 3, 0, 'Available'),
('A-102', 'A', 1, 3, 0, 'Available'),
('A-103', 'A', 1, 2, 0, 'Available'),
('B-201', 'B', 2, 3, 0, 'Available'),
('B-202', 'B', 2, 2, 0, 'Available');