create database tooktook;
use tooktook;


CREATE TABLE `consultants` (
    `consultant_id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255),
    `department` VARCHAR(255),
    `major` VARCHAR(255),
    `join_date` DATE,
    `team` VARCHAR(255)
) ENGINE=InnoDB;

CREATE TABLE `customers` (
    `customer_id` INT AUTO_INCREMENT PRIMARY KEY,
    `age` INT,
    `gender` VARCHAR(10),
    `name` VARCHAR(255),
    `region` VARCHAR(255),
    `phone_number` VARCHAR(255),
    `business_type` VARCHAR(255)
) ENGINE=InnoDB;

CREATE TABLE `fund_types` (
    `fund_type_id` INT AUTO_INCREMENT PRIMARY KEY,
    `fund_type_name` VARCHAR(255) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE `documents` (
    `document_id` INT AUTO_INCREMENT PRIMARY KEY,
    `document_name` VARCHAR(255),
    `is_required` BOOLEAN,
    `is_submitted` BOOLEAN,
    `submission_date` DATE
) ENGINE=InnoDB;

CREATE TABLE `consultations` (
    `consultation_id` INT AUTO_INCREMENT PRIMARY KEY,
    `consultant_id` INT NOT NULL,
    `customer_id` INT NOT NULL,
    `start_time` TIMESTAMP NOT NULL,
    `end_time` TIMESTAMP,
    `consultation_date` DATE,
    `resolution_type` VARCHAR(50),
    `satisfaction_score` INT,
    FOREIGN KEY (`consultant_id`) REFERENCES `consultants`(`consultant_id`),
    FOREIGN KEY (`customer_id`) REFERENCES `customers`(`customer_id`)
) ENGINE=InnoDB;

CREATE TABLE `conversation_logs` (
    `log_id` INT AUTO_INCREMENT PRIMARY KEY,
    `consultation_id` INT NOT NULL,
    `timestamp` TIMESTAMP NOT NULL,
    `log_type` VARCHAR(50),
    `status` VARCHAR(50),
    `created_at` TIMESTAMP NOT NULL,
    FOREIGN KEY (`consultation_id`) REFERENCES `consultations`(`consultation_id`)
) ENGINE=InnoDB;


CREATE TABLE `consultation_fund_types` (
    `consultation_id` INT NOT NULL,
    `fund_type_id` INT NOT NULL,
    PRIMARY KEY (`consultation_id`, `fund_type_id`),
    FOREIGN KEY (`consultation_id`) REFERENCES `consultations`(`consultation_id`),
    FOREIGN KEY (`fund_type_id`) REFERENCES `fund_types`(`fund_type_id`)
) ENGINE=InnoDB;

CREATE TABLE `consultation_documents` (
    `consultation_id` INT NOT NULL,
    `document_id` INT NOT NULL,
    PRIMARY KEY (`consultation_id`, `document_id`),
    FOREIGN KEY (`consultation_id`) REFERENCES `consultations`(`consultation_id`),
    FOREIGN KEY (`document_id`) REFERENCES `documents`(`document_id`)
) ENGINE=InnoDB;


CREATE TABLE `statistics` (
    `statistic_id` INT AUTO_INCREMENT PRIMARY KEY,
    `date` DATE NOT NULL,
    `total_consultations` INT,
    `avg_consultation_time` INT,
    `completed_consultations` INT,
    `avg_satisfaction_score` DECIMAL(5, 2),
    `category` VARCHAR(255)
) ENGINE=InnoDB;

CREATE TABLE `predictions` (
    `prediction_id` INT AUTO_INCREMENT PRIMARY KEY,
    `ts_slot` TIMESTAMP NOT NULL,
    `weekday` INT,
    `slot_hour` INT,
    `label_lag7` VARCHAR(255),
    `pred_label` VARCHAR(255),
    `top1` VARCHAR(255),
    `p1` DECIMAL(10, 8),
    `top2` VARCHAR(255),
    `p2` DECIMAL(10, 8),
    `top3` VARCHAR(255),
    `p3` DECIMAL(10, 8),
    `weekday_ko` VARCHAR(10)
) ENGINE=InnoDB;

CREATE TABLE `tomorrow_predictions` (
    `prediction_id` INT AUTO_INCREMENT PRIMARY KEY,
    `ts_slot` TIMESTAMP NOT NULL,
    `weekday` INT,
    `slot_hour` INT,
    `y_pred` DECIMAL(15, 10)
) ENGINE=InnoDB;