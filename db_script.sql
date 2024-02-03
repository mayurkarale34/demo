create database demo_1;

CREATE TABLE `user_master` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `city_name` VARCHAR(45) NULL,
  `blood_group` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));
