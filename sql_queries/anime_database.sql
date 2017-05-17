CREATE TABLE `aa_anime_details_list` (
 `animeId` int(11) DEFAULT NULL,
 `name` longtext character set utf8mb4 DEFAULT NULL,
 `genre` varchar(255) DEFAULT NULL,
 `type` varchar(255) DEFAULT NULL,
 `numberOfEpisodes` int(11) DEFAULT NULL,
 `rating` double DEFAULT NULL,
 `members` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOAD DATA LOCAL INFILE 'V:/Anime Analytics/Kaggle/anime-recommendations-database/anime1.csv' INTO TABLE aa_anime_details_list FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';

drop table `aa_anime_details_list`;


CREATE TABLE `aa_user_ratings` (
 `userId` int(11) DEFAULT NULL,
 `animeId` int(11) DEFAULT NULL,
 `rating` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOAD DATA LOCAL INFILE 'V:/Anime Analytics/Kaggle/anime-recommendations-database/rating2.csv' INTO TABLE aa_user_ratings FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';

drop table `aa_user_ratings`;

select * from `aa_anime_details_list`;
select * from `aa_user_ratings`;