-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost:8889
-- Généré le : jeu. 28 mars 2024 à 14:29
-- Version du serveur : 5.7.39
-- Version de PHP : 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `AiWriterReader-3`
--

-- --------------------------------------------------------

--
-- Structure de la table `AntiHero`
--

CREATE TABLE `AntiHero` (
  `antihero_id` int(11) NOT NULL,
  `id_story` int(11) DEFAULT NULL,
  `antihero_name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `chapter`
--

CREATE TABLE `chapter` (
  `id_chapter` int(11) NOT NULL,
  `id_story` int(11) NOT NULL,
  `numéro_de_chapitre` int(11) NOT NULL,
  `titre_du chapitre` varchar(50) NOT NULL,
  `Contenu_du_chapitre` varchar(50) NOT NULL,
  `date_de _création` date NOT NULL,
  `dernière_date_de_modification` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `Character`
--

CREATE TABLE `Character` (
  `character_id` int(11) NOT NULL,
  `id_story` int(11) DEFAULT NULL,
  `character_name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `comment`
--

CREATE TABLE `comment` (
  `id_comment` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `id_story` int(11) NOT NULL,
  `id_chapter` int(11) NOT NULL,
  `contenu_du_commentaire` varchar(50) NOT NULL,
  `date_du_commentaire` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `Hero`
--

CREATE TABLE `Hero` (
  `hero_id` int(11) NOT NULL,
  `id_story` int(11) DEFAULT NULL,
  `hero_name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `LeaderType`
--

CREATE TABLE `LeaderType` (
  `leader_type_id` int(11) NOT NULL,
  `id_story` int(11) DEFAULT NULL,
  `leader_type_name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `preferences`
--

CREATE TABLE `preferences` (
  `id_pref` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `genre_préféré` varchar(50) NOT NULL,
  `Style` varchar(50) NOT NULL,
  `durée` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `Setting`
--

CREATE TABLE `Setting` (
  `setting_id` int(11) NOT NULL,
  `id_story` int(11) DEFAULT NULL,
  `theme` varchar(255) DEFAULT NULL,
  `era` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `story`
--

CREATE TABLE `story` (
  `id_story` int(11) NOT NULL,
  `titre` int(11) NOT NULL,
  `description` int(11) NOT NULL,
  `date_de_création` datetime NOT NULL,
  `date_de_modification` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `user`
--

CREATE TABLE `user` (
  `id_user` int(11) NOT NULL,
  `nom_utilisateur` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `mdp` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `users_choice`
--

CREATE TABLE `users_choice` (
  `id_choice` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `id_chapter` int(11) NOT NULL,
  `choix_utilisateur` varchar(50) NOT NULL,
  `date_du_choix` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `user`
--

CREATE TABLE `favorites` (
  `id_favorite` INT(11) AUTO_INCREMENT PRIMARY KEY,
  `id_user` INT(11) NOT NULL,
  `id_story` INT(11) NOT NULL,
  `date_added` DATETIME NOT NULL,
  FOREIGN KEY (`id_user`) REFERENCES `users`(`id`),
  FOREIGN KEY (`id_story`) REFERENCES `stories`(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------
--
-- Index pour les tables déchargées
--

--
-- Index pour la table `AntiHero`
--
ALTER TABLE `AntiHero`
  ADD UNIQUE KEY `id_story` (`id_story`);

--
-- Index pour la table `chapter`
--
ALTER TABLE `chapter`
  ADD PRIMARY KEY (`id_chapter`),
  ADD UNIQUE KEY `id_story` (`id_story`);

--
-- Index pour la table `Character`
--
ALTER TABLE `Character`
  ADD UNIQUE KEY `id_story` (`id_story`);

--
-- Index pour la table `comment`
--
ALTER TABLE `comment`
  ADD PRIMARY KEY (`id_comment`),
  ADD UNIQUE KEY `id_user` (`id_user`),
  ADD UNIQUE KEY `id_story` (`id_story`),
  ADD UNIQUE KEY `id_chapter` (`id_chapter`);

--
-- Index pour la table `Hero`
--
ALTER TABLE `Hero`
  ADD UNIQUE KEY `id_story` (`id_story`);

--
-- Index pour la table `LeaderType`
--
ALTER TABLE `LeaderType`
  ADD UNIQUE KEY `id_story` (`id_story`);

--
-- Index pour la table `preferences`
--
ALTER TABLE `preferences`
  ADD PRIMARY KEY (`id_pref`),
  ADD UNIQUE KEY `id_user` (`id_user`);

--
-- Index pour la table `Setting`
--
ALTER TABLE `Setting`
  ADD UNIQUE KEY `id_story` (`id_story`);

--
-- Index pour la table `story`
--
ALTER TABLE `story`
  ADD PRIMARY KEY (`id_story`);

--
-- Index pour la table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id_user`);

--
-- Index pour la table `users_choice`
--
ALTER TABLE `users_choice`
  ADD PRIMARY KEY (`id_choice`),
  ADD UNIQUE KEY `id_user` (`id_user`),
  ADD UNIQUE KEY `id_chapter` (`id_chapter`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `chapter`
--
ALTER TABLE `chapter`
  MODIFY `id_chapter` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `comment`
--
ALTER TABLE `comment`
  MODIFY `id_comment` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `preferences`
--
ALTER TABLE `preferences`
  MODIFY `id_pref` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `story`
--
ALTER TABLE `story`
  MODIFY `id_story` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `user`
--
ALTER TABLE `user`
  MODIFY `id_user` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `users_choice`
--
ALTER TABLE `users_choice`
  MODIFY `id_choice` int(11) NOT NULL AUTO_INCREMENT;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `AntiHero`
--
ALTER TABLE `AntiHero`
  ADD CONSTRAINT `antihero_ibfk_1` FOREIGN KEY (`id_story`) REFERENCES `story` (`id_story`);

--
-- Contraintes pour la table `chapter`
--
ALTER TABLE `chapter`
  ADD CONSTRAINT `chapter_ibfk_1` FOREIGN KEY (`id_story`) REFERENCES `story` (`id_story`);

--
-- Contraintes pour la table `Character`
--
ALTER TABLE `Character`
  ADD CONSTRAINT `character_ibfk_1` FOREIGN KEY (`id_story`) REFERENCES `story` (`id_story`);

--
-- Contraintes pour la table `comment`
--
ALTER TABLE `comment`
  ADD CONSTRAINT `comment_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `user` (`id_user`),
  ADD CONSTRAINT `comment_ibfk_2` FOREIGN KEY (`id_story`) REFERENCES `story` (`id_story`),
  ADD CONSTRAINT `comment_ibfk_3` FOREIGN KEY (`id_chapter`) REFERENCES `chapter` (`id_chapter`);

--
-- Contraintes pour la table `Hero`
--
ALTER TABLE `Hero`
  ADD CONSTRAINT `hero_ibfk_1` FOREIGN KEY (`id_story`) REFERENCES `story` (`id_story`);

--
-- Contraintes pour la table `preferences`
--
ALTER TABLE `preferences`
  ADD CONSTRAINT `preferences_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `user` (`id_user`);

--
-- Contraintes pour la table `Setting`
--
ALTER TABLE `Setting`
  ADD CONSTRAINT `setting_ibfk_1` FOREIGN KEY (`id_story`) REFERENCES `story` (`id_story`);

--
-- Contraintes pour la table `users_choice`
--
ALTER TABLE `users_choice`
  ADD CONSTRAINT `users_choice_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `user` (`id_user`),
  ADD CONSTRAINT `users_choice_ibfk_2` FOREIGN KEY (`id_chapter`) REFERENCES `chapter` (`id_chapter`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
