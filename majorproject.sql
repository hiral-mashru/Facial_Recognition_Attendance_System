-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 04, 2020 at 08:22 PM
-- Server version: 10.3.16-MariaDB
-- PHP Version: 7.3.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `majorproject`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add class', 1, 'add_class'),
(2, 'Can change class', 1, 'change_class'),
(3, 'Can delete class', 1, 'delete_class'),
(4, 'Can view class', 1, 'view_class'),
(5, 'Can add faculties', 2, 'add_faculties'),
(6, 'Can change faculties', 2, 'change_faculties'),
(7, 'Can delete faculties', 2, 'delete_faculties'),
(8, 'Can view faculties', 2, 'view_faculties'),
(9, 'Can add week', 3, 'add_week'),
(10, 'Can change week', 3, 'change_week'),
(11, 'Can delete week', 3, 'delete_week'),
(12, 'Can view week', 3, 'view_week'),
(13, 'Can add subject', 4, 'add_subject'),
(14, 'Can change subject', 4, 'change_subject'),
(15, 'Can delete subject', 4, 'delete_subject'),
(16, 'Can view subject', 4, 'view_subject'),
(17, 'Can add students', 5, 'add_students'),
(18, 'Can change students', 5, 'change_students'),
(19, 'Can delete students', 5, 'delete_students'),
(20, 'Can view students', 5, 'view_students'),
(21, 'Can add schedule', 6, 'add_schedule'),
(22, 'Can change schedule', 6, 'change_schedule'),
(23, 'Can delete schedule', 6, 'delete_schedule'),
(24, 'Can view schedule', 6, 'view_schedule'),
(25, 'Can add attendance', 7, 'add_attendance'),
(26, 'Can change attendance', 7, 'change_attendance'),
(27, 'Can delete attendance', 7, 'delete_attendance'),
(28, 'Can view attendance', 7, 'view_attendance'),
(29, 'Can add log entry', 8, 'add_logentry'),
(30, 'Can change log entry', 8, 'change_logentry'),
(31, 'Can delete log entry', 8, 'delete_logentry'),
(32, 'Can view log entry', 8, 'view_logentry'),
(33, 'Can add permission', 9, 'add_permission'),
(34, 'Can change permission', 9, 'change_permission'),
(35, 'Can delete permission', 9, 'delete_permission'),
(36, 'Can view permission', 9, 'view_permission'),
(37, 'Can add group', 10, 'add_group'),
(38, 'Can change group', 10, 'change_group'),
(39, 'Can delete group', 10, 'delete_group'),
(40, 'Can view group', 10, 'view_group'),
(41, 'Can add user', 11, 'add_user'),
(42, 'Can change user', 11, 'change_user'),
(43, 'Can delete user', 11, 'delete_user'),
(44, 'Can view user', 11, 'view_user'),
(45, 'Can add content type', 12, 'add_contenttype'),
(46, 'Can change content type', 12, 'change_contenttype'),
(47, 'Can delete content type', 12, 'delete_contenttype'),
(48, 'Can view content type', 12, 'view_contenttype'),
(49, 'Can add session', 13, 'add_session'),
(50, 'Can change session', 13, 'change_session'),
(51, 'Can delete session', 13, 'delete_session'),
(52, 'Can view session', 13, 'view_session'),
(53, 'Can add attend images', 14, 'add_attendimages'),
(54, 'Can change attend images', 14, 'change_attendimages'),
(55, 'Can delete attend images', 14, 'delete_attendimages'),
(56, 'Can view attend images', 14, 'view_attendimages');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$216000$4uJ5k9h0Ux9c$Qd1sUkxqzO+N7HYrr5pU7zBY7XhAnGxPMLe2biEmRIQ=', '2020-11-01 12:58:02.668661', 0, 'c', '', '', 'c@gmail.com', 0, 1, '2020-10-31 20:46:46.311372'),
(2, 'pbkdf2_sha256$216000$gU94NlhxTq4s$dtffFZrhxeGCM2qczdj4R4V3EF0E/gnJe7O5DRclRr8=', NULL, 0, 'd', '', '', 'd@gmail.com', 0, 1, '2020-10-31 20:52:01.201472'),
(3, 'pbkdf2_sha256$216000$zRkK41vdKUiP$FYRUzyfGiDTdBSFr0rTZJdBB6GzZlJIZOYDon60M/Jk=', NULL, 0, 'e', '', '', 'e@gmail.com', 0, 1, '2020-10-31 20:57:24.787347'),
(4, 'pbkdf2_sha256$216000$SZs6fkFQD81C$FTB2lkbdVmmnAtIgD2TmVn435NCaFU1qOnboXLw9JK4=', '2020-11-01 12:44:48.885474', 0, 'vicky', '', '', 'vicky@gmail.com', 0, 1, '2020-11-01 12:44:48.251892'),
(5, 'pbkdf2_sha256$216000$idwTX85UqqUV$ndhWbYAWCWPidtIsjqupwr9MKJcfnhcqwXOk/Kieq2E=', '2020-11-05 07:22:41.706060', 0, 'harsh@gmail.com', '', '', 'harsh@gmail.com', 0, 1, '2020-11-01 13:00:12.419144'),
(6, 'pbkdf2_sha256$216000$rllQrhTk3YAu$9wmW6cDZvXH6OS2CDFxvH7ADomgDX6pBzbsBvx3qYyA=', '2020-11-05 07:53:19.187968', 0, 'admin@gmail.com', '', '', 'admin@gmail.com', 0, 1, '2020-11-05 07:25:07.016179'),
(9, 'pbkdf2_sha256$216000$HCa5O6eCsU7k$9mwxEHn8jCFUZnwADC3s+vfZfmTbylyrwVwfWkNtqkM=', '2020-12-02 11:55:01.257920', 0, 'hm@gmail.com', '', '', 'hm@gmail.com', 0, 1, '2020-12-02 11:55:00.436630'),
(11, 'pbkdf2_sha256$216000$WQUQyPynHh31$rfHh/Uwne+xkED7J2V97gjooJwlyQqyxicZEoUEAYaM=', '2020-12-04 11:26:06.830123', 0, 'sheru@gmail.com', '', '', 'sheru@gmail.com', 0, 1, '2020-12-02 17:20:06.939241'),
(12, 'pbkdf2_sha256$216000$knMCAOukUttD$DqDabu/cyjHAb4sw09AttRSZTSCVV9rnctF5hpZjzOc=', '2020-12-04 18:06:17.102685', 0, 'mummy@gmail.com', '', '', 'mummy@gmail.com', 0, 1, '2020-12-02 17:22:32.095870');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL
) ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(8, 'admin', 'logentry'),
(10, 'auth', 'group'),
(9, 'auth', 'permission'),
(11, 'auth', 'user'),
(12, 'contenttypes', 'contenttype'),
(7, 'login', 'attendance'),
(14, 'login', 'attendimages'),
(1, 'login', 'class'),
(2, 'login', 'faculties'),
(6, 'login', 'schedule'),
(5, 'login', 'students'),
(4, 'login', 'subject'),
(3, 'login', 'week'),
(13, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2020-10-31 20:40:21.537484'),
(2, 'auth', '0001_initial', '2020-10-31 20:40:23.074907'),
(3, 'admin', '0001_initial', '2020-10-31 20:40:32.261431'),
(4, 'admin', '0002_logentry_remove_auto_add', '2020-10-31 20:40:33.852243'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2020-10-31 20:40:33.928978'),
(6, 'contenttypes', '0002_remove_content_type_name', '2020-10-31 20:40:35.402214'),
(7, 'auth', '0002_alter_permission_name_max_length', '2020-10-31 20:40:35.593745'),
(8, 'auth', '0003_alter_user_email_max_length', '2020-10-31 20:40:35.984785'),
(9, 'auth', '0004_alter_user_username_opts', '2020-10-31 20:40:36.038058'),
(10, 'auth', '0005_alter_user_last_login_null', '2020-10-31 20:40:36.844003'),
(11, 'auth', '0006_require_contenttypes_0002', '2020-10-31 20:40:36.882923'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2020-10-31 20:40:36.938947'),
(13, 'auth', '0008_alter_user_username_max_length', '2020-10-31 20:40:37.038876'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2020-10-31 20:40:37.129350'),
(15, 'auth', '0010_alter_group_name_max_length', '2020-10-31 20:40:37.261996'),
(16, 'auth', '0011_update_proxy_permissions', '2020-10-31 20:40:37.316875'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2020-10-31 20:40:37.404128'),
(18, 'login', '0001_initial', '2020-10-31 20:40:37.638841'),
(19, 'login', '0002_auto_20201021_0302', '2020-10-31 20:40:40.894446'),
(20, 'login', '0003_auto_20201022_0037', '2020-10-31 20:40:52.450426'),
(21, 'login', '0004_delete_tc1_7', '2020-10-31 20:40:53.480831'),
(22, 'sessions', '0001_initial', '2020-10-31 20:40:53.921415'),
(23, 'login', '0005_remove_students_img', '2020-11-01 19:45:07.054420'),
(24, 'login', '0006_auto_20201102_0118', '2020-11-01 19:48:24.179328'),
(25, 'login', '0007_schedule_sclass', '2020-11-01 20:07:18.514204'),
(26, 'login', '0002_auto_20201111_0209', '2020-11-10 20:39:37.211649'),
(27, 'login', '0003_auto_20201111_0210', '2020-11-10 20:41:14.423763'),
(28, 'login', '0004_students_img', '2020-11-28 18:10:23.327756'),
(29, 'login', '0006_attendance_img', '2020-11-28 18:13:48.825413'),
(30, 'login', '0007_auto_20201128_2347', '2020-11-28 18:17:56.495847'),
(31, 'login', '0008_auto_20201129_0003', '2020-11-28 18:33:12.063406'),
(32, 'login', '0009_attendimages', '2020-11-30 13:22:07.917401'),
(33, 'login', '0010_remove_attendance_img', '2020-11-30 13:22:11.714938'),
(34, 'login', '0011_attendimages_date', '2020-11-30 13:28:43.469120');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('28c7roit8n4inux4vo3aney7s4oxugjo', '.eJxVjDsOwjAQBe_iGlnGn-yakj5nsHb9wQHkSHFSIe4OkVJA-2bmvUSgba1h63kJUxIXcdbi9DsyxUduO0l3ardZxrmty8RyV-RBuxznlJ_Xw_07qNTrt1ZcgJxzQ1KABCYqncAzYDEWNduEziiDCo0uxN6CMwDEoLMdvLco3h_m_TbR:1klFTF:NWuxYCugwHOzeQY9l-fSanKGWckqdoFJkOOWxG1TAKI', '2020-12-18 18:06:17.247957'),
('95996iy9s4sf7bu4tqkfq06ueg1gu0b9', '.eJxVjMEOwiAQRP-FsyFAKwsevfsNZFkWqRqalPZk_Hdp0oMeZ96beYuA21rC1ngJUxIXobU4_ZYR6cl1J-mB9T5Lmuu6TFHuijxok7c58et6uH8HBVvpa9IGFIFxdlRgCS0BonZp9Dwo9kAxZ0wMYAfIYHJP8YxeGdeJwSw-XwuZOP0:1kkt7q:901obcNW7TvU_NjOmcVoaFJ-e6PIaGMiSnJikmu9vxY', '2020-12-17 18:14:42.005447'),
('q0q6xtxkoss7hnmzukmmchzl5r6r51fy', 'e30:1kZCf4:Wbnt9dlH7ZGTIq9q7mal68XtqyzD6zwkvxJHBfIFe7s', '2020-11-15 12:40:42.290369');

-- --------------------------------------------------------

--
-- Table structure for table `login_attendance`
--

CREATE TABLE `login_attendance` (
  `id` int(11) NOT NULL,
  `Date` datetime(6) NOT NULL DEFAULT current_timestamp(6),
  `Attend` tinyint(1) NOT NULL,
  `AClassName_id` int(11) DEFAULT NULL,
  `AFID_id` int(11) DEFAULT NULL,
  `ASID_id` int(11) DEFAULT NULL,
  `AStartTime_id` int(11) DEFAULT NULL,
  `ASubject_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login_attendance`
--

INSERT INTO `login_attendance` (`id`, `Date`, `Attend`, `AClassName_id`, `AFID_id`, `ASID_id`, `AStartTime_id`, `ASubject_id`) VALUES
(113, '2020-12-04 15:44:15.749962', 1, 1, 13, 29, 12, 2),
(114, '2020-12-04 15:44:15.885446', 0, 1, 13, 30, 12, 2),
(115, '2020-12-04 16:06:55.809971', 0, 1, 13, 29, 12, 2),
(116, '2020-12-04 16:06:55.883854', 1, 1, 13, 30, 12, 2),
(117, '2020-12-04 17:59:21.576672', 1, 1, 13, 29, 12, 2),
(118, '2020-12-04 17:59:21.758779', 0, 1, 13, 30, 12, 2);

-- --------------------------------------------------------

--
-- Table structure for table `login_attendimages`
--

CREATE TABLE `login_attendimages` (
  `id` int(11) NOT NULL,
  `Image` varchar(100) DEFAULT NULL,
  `Schedule_id` int(11) DEFAULT NULL,
  `Date` datetime(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login_attendimages`
--

INSERT INTO `login_attendimages` (`id`, `Image`, `Schedule_id`, `Date`) VALUES
(5, '2015-09-01_22-13-33.jpg', 12, '2020-11-30 13:48:07.643816'),
(6, '20170528_190443.jpg', 12, '2020-11-30 13:49:21.084983'),
(7, '4-56A3ED1B-409461-480_-_Copy.jpg', 12, '2020-11-30 13:51:54.067614'),
(8, '_MG_0623.JPG.jpg', 12, '2020-11-30 13:52:09.029006'),
(9, '_20151220_221741.JPG', 12, '2020-11-30 13:53:43.745490'),
(10, '_MG_0623.JPG_qKUycd0.jpg', 12, '2020-11-30 13:55:33.912405'),
(11, '_MG_0623.JPG_qUTViQJ.jpg', 12, '2020-11-30 13:57:08.438894'),
(12, '2015-06-10_16-18-30.jpg', 12, '2020-11-30 14:00:05.394549'),
(13, '20170528_190646.jpg', 12, '2020-11-30 14:00:46.662627'),
(17, '20170528_190106.jpg', 12, '2020-12-04 13:19:57.124886'),
(18, '2015-09-01_22-13-33.jpg', 12, '2020-12-04 13:21:25.805775');

-- --------------------------------------------------------

--
-- Table structure for table `login_class`
--

CREATE TABLE `login_class` (
  `id` int(11) NOT NULL,
  `ClassName` varchar(200) NOT NULL,
  `ClassFaculty_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login_class`
--

INSERT INTO `login_class` (`id`, `ClassName`, `ClassFaculty_id`) VALUES
(1, '7TC1', 7),
(5, '7TC4', 13),
(7, '7ED2', 8);

-- --------------------------------------------------------

--
-- Table structure for table `login_faculties`
--

CREATE TABLE `login_faculties` (
  `id` int(11) NOT NULL,
  `FName` varchar(200) NOT NULL,
  `FEmailID` varchar(200) NOT NULL,
  `FPassword` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login_faculties`
--

INSERT INTO `login_faculties` (`id`, `FName`, `FEmailID`, `FPassword`) VALUES
(1, 'b', 'b@gmail.com', 'b123'),
(3, 'd', 'd@gmail.com', 'd123'),
(4, 'e', 'e@gmail.com', 'e123'),
(6, 'vicky', 'vicky@gmail.com', 'vicky123'),
(7, 'harsh', 'harsh@gmail.com', 'harsh123'),
(8, 'hiral', 'admin@gmail.com', 'hiral123'),
(9, 'Hiral Mashru', 'hiral@gmail.com', 'mashru'),
(10, 'gvhkjjkll', 'hkjlk@gmail.com', 'cfhhbjk'),
(11, 'ghjkm', 'dgfhghj@gmail.com', 'chgvhbjnk'),
(12, 'hiral', 'dwarikadhish@gmail.com', 'om'),
(13, 'Sherin Joy', 'sheru@gmail.com', 'sherin'),
(15, 'Hiral Mashru', 'hm@gmail.com', 'mashru'),
(17, 'Mummy', 'mummy@gmail.com', 'god');

-- --------------------------------------------------------

--
-- Table structure for table `login_schedule`
--

CREATE TABLE `login_schedule` (
  `id` int(11) NOT NULL,
  `StartTime` time(6) NOT NULL,
  `EndTime` time(6) NOT NULL,
  `SSubject_id` int(11) DEFAULT NULL,
  `SWeek_id` int(11) DEFAULT NULL,
  `SClass_id` int(11) DEFAULT NULL,
  `SFaculty_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login_schedule`
--

INSERT INTO `login_schedule` (`id`, `StartTime`, `EndTime`, `SSubject_id`, `SWeek_id`, `SClass_id`, `SFaculty_id`) VALUES
(6, '09:00:00.000000', '10:00:00.000000', 1, 3, 1, 9),
(10, '03:08:00.000000', '14:08:00.000000', 2, 3, 5, 9),
(12, '10:00:00.000000', '11:00:00.000000', 2, 3, 1, 13),
(14, '12:00:00.000000', '13:00:00.000000', 2, 3, 1, 12),
(15, '09:00:00.000000', '10:00:00.000000', 2, 1, 1, 11),
(16, '10:00:00.000000', '11:00:00.000000', 2, 1, 1, 9),
(17, '09:00:00.000000', '10:00:00.000000', 2, 2, 1, 8),
(18, '09:00:00.000000', '10:00:00.000000', 1, 4, 1, 7),
(19, '09:00:00.000000', '10:00:00.000000', 1, 5, 1, 3);

-- --------------------------------------------------------

--
-- Table structure for table `login_students`
--

CREATE TABLE `login_students` (
  `id` int(11) NOT NULL,
  `SID` bigint(20) NOT NULL,
  `SName` varchar(200) NOT NULL,
  `SClass_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login_students`
--

INSERT INTO `login_students` (`id`, `SID`, `SName`, `SClass_id`) VALUES
(29, 103309, 'Hiral', 1),
(30, 103477, 'Harsh Mashru', 1);

-- --------------------------------------------------------

--
-- Table structure for table `login_subject`
--

CREATE TABLE `login_subject` (
  `id` int(11) NOT NULL,
  `SubName` varchar(200) NOT NULL,
  `SubFaculty_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login_subject`
--

INSERT INTO `login_subject` (`id`, `SubName`, `SubFaculty_id`) VALUES
(1, 'Python', 8),
(2, 'Java', 7);

-- --------------------------------------------------------

--
-- Table structure for table `login_week`
--

CREATE TABLE `login_week` (
  `id` int(11) NOT NULL,
  `WName` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login_week`
--

INSERT INTO `login_week` (`id`, `WName`) VALUES
(1, 'Monday'),
(2, 'Tuesday'),
(3, 'Wednesday'),
(4, 'Thursday'),
(5, 'Friday'),
(6, 'Saturday'),
(7, 'Sunday');

-- --------------------------------------------------------

--
-- Table structure for table `userdata`
--

CREATE TABLE `userdata` (
  `ID` int(11) NOT NULL,
  `email` varchar(200) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `login_attendance`
--
ALTER TABLE `login_attendance`
  ADD PRIMARY KEY (`id`),
  ADD KEY `login_attendance_AClassName_id_8c7bc1fa_fk_login_class_id` (`AClassName_id`),
  ADD KEY `login_attendance_AFID_id_35955dc3_fk_login_faculties_id` (`AFID_id`),
  ADD KEY `login_attendance_ASID_id_d57beac1_fk_login_students_id` (`ASID_id`),
  ADD KEY `login_attendance_AStartTime_id_68514048_fk_login_schedule_id` (`AStartTime_id`),
  ADD KEY `login_attendance_ASubject_id_cbe8f03a_fk_login_subject_id` (`ASubject_id`);

--
-- Indexes for table `login_attendimages`
--
ALTER TABLE `login_attendimages`
  ADD PRIMARY KEY (`id`),
  ADD KEY `login_attendimages_Schedule_id_f45e88b2_fk_login_schedule_id` (`Schedule_id`);

--
-- Indexes for table `login_class`
--
ALTER TABLE `login_class`
  ADD PRIMARY KEY (`id`),
  ADD KEY `login_class_ClassFaculty_id_979f63c2_fk_login_faculties_id` (`ClassFaculty_id`);

--
-- Indexes for table `login_faculties`
--
ALTER TABLE `login_faculties`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `login_schedule`
--
ALTER TABLE `login_schedule`
  ADD PRIMARY KEY (`id`),
  ADD KEY `login_schedule_SClass_id_09706c8b_fk_login_class_id` (`SClass_id`),
  ADD KEY `login_schedule_SSubject_id_7fa7a267_fk_login_subject_id` (`SSubject_id`),
  ADD KEY `login_schedule_SWeek_id_09db9f65_fk_login_week_id` (`SWeek_id`),
  ADD KEY `SFaculty_id` (`SFaculty_id`) USING BTREE;

--
-- Indexes for table `login_students`
--
ALTER TABLE `login_students`
  ADD PRIMARY KEY (`id`),
  ADD KEY `login_students_SClass_id_946709c9_fk_login_class_id` (`SClass_id`);

--
-- Indexes for table `login_subject`
--
ALTER TABLE `login_subject`
  ADD PRIMARY KEY (`id`),
  ADD KEY `login_subject_SubFaculty_id_115449d2_fk_login_faculties_id` (`SubFaculty_id`);

--
-- Indexes for table `login_week`
--
ALTER TABLE `login_week`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userdata`
--
ALTER TABLE `userdata`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `FEmailID` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT for table `login_attendance`
--
ALTER TABLE `login_attendance`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=119;

--
-- AUTO_INCREMENT for table `login_attendimages`
--
ALTER TABLE `login_attendimages`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `login_class`
--
ALTER TABLE `login_class`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `login_faculties`
--
ALTER TABLE `login_faculties`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `login_schedule`
--
ALTER TABLE `login_schedule`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `login_students`
--
ALTER TABLE `login_students`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `login_subject`
--
ALTER TABLE `login_subject`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `login_week`
--
ALTER TABLE `login_week`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `userdata`
--
ALTER TABLE `userdata`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `login_attendance`
--
ALTER TABLE `login_attendance`
  ADD CONSTRAINT `login_attendance_AClassName_id_8c7bc1fa_fk_login_class_id` FOREIGN KEY (`AClassName_id`) REFERENCES `login_class` (`id`),
  ADD CONSTRAINT `login_attendance_AFID_id_35955dc3_fk_login_faculties_id` FOREIGN KEY (`AFID_id`) REFERENCES `login_faculties` (`id`),
  ADD CONSTRAINT `login_attendance_ASID_id_d57beac1_fk_login_students_id` FOREIGN KEY (`ASID_id`) REFERENCES `login_students` (`id`),
  ADD CONSTRAINT `login_attendance_AStartTime_id_68514048_fk_login_schedule_id` FOREIGN KEY (`AStartTime_id`) REFERENCES `login_schedule` (`id`),
  ADD CONSTRAINT `login_attendance_ASubject_id_cbe8f03a_fk_login_subject_id` FOREIGN KEY (`ASubject_id`) REFERENCES `login_subject` (`id`);

--
-- Constraints for table `login_attendimages`
--
ALTER TABLE `login_attendimages`
  ADD CONSTRAINT `login_attendimages_Schedule_id_f45e88b2_fk_login_schedule_id` FOREIGN KEY (`Schedule_id`) REFERENCES `login_schedule` (`id`);

--
-- Constraints for table `login_class`
--
ALTER TABLE `login_class`
  ADD CONSTRAINT `login_class_ClassFaculty_id_979f63c2_fk_login_faculties_id` FOREIGN KEY (`ClassFaculty_id`) REFERENCES `login_faculties` (`id`);

--
-- Constraints for table `login_schedule`
--
ALTER TABLE `login_schedule`
  ADD CONSTRAINT `login_schedule_SClass_id_09706c8b_fk_login_class_id` FOREIGN KEY (`SClass_id`) REFERENCES `login_class` (`id`),
  ADD CONSTRAINT `login_schedule_SSubject_id_7fa7a267_fk_login_subject_id` FOREIGN KEY (`SSubject_id`) REFERENCES `login_subject` (`id`),
  ADD CONSTRAINT `login_schedule_SWeek_id_09db9f65_fk_login_week_id` FOREIGN KEY (`SWeek_id`) REFERENCES `login_week` (`id`),
  ADD CONSTRAINT `login_schedule_ibfk_1` FOREIGN KEY (`SFaculty_id`) REFERENCES `login_faculties` (`id`);

--
-- Constraints for table `login_students`
--
ALTER TABLE `login_students`
  ADD CONSTRAINT `login_students_SClass_id_946709c9_fk_login_class_id` FOREIGN KEY (`SClass_id`) REFERENCES `login_class` (`id`);

--
-- Constraints for table `login_subject`
--
ALTER TABLE `login_subject`
  ADD CONSTRAINT `login_subject_SubFaculty_id_115449d2_fk_login_faculties_id` FOREIGN KEY (`SubFaculty_id`) REFERENCES `login_faculties` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
