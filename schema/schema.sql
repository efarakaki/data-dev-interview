CREATE DATABASE data_tech_interview;

CREATE TABLE data_tech_interview.`films_by_year` (
  `year` int(11) NOT NULL,
  `rating` varchar(100) NOT NULL,
  `count` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;