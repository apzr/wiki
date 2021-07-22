/* ***********************原发布计划变动命令***********************
-- step 1
create table `custom__jda_replenishment_proposal_order`(`U_PROMO_ID` varchar(256) null, `isDeleted` tinyint not null default 0, `RESWK` varchar(256) null, `U_UOM_DESCR` varchar(256) null, `U_FCST_QTY` decimal(9, 2) null, `U_PLANARRIVAL_STORE_LINENO` varchar(256) null, `U_UOM` varchar(256) null, `U_OHINVENTORY` decimal(9, 2) null, `id` bigint not null, `U_VEHICLELOADLINE` decimal(9, 2) null, `U_PLANARRIVAL_TYPE` varchar(256) null, `SCHEDARRIVDATE` datetime null, `updatedAt` datetime not null, `U_CHANGE_FLAG` tinyint null, `U_BARCODE` varchar(256) null, `ISPROCESSED` tinyint null, `ITEM` varchar(256) null, `U_PLANARRIVAL_STORE_CD` varchar(256) null, `SOURCE` varchar(256) null, `U_PACKNUMBER` decimal(9, 2) null, `DEST` varchar(256) null, `U_SPEC` varchar(256) null, `U_TRANSLOC` varchar(256) null, `SCHEDSHIPDATE` datetime null, `U_DEST_DESCR` varchar(256) null, `U_ARRIVALDATE` datetime null, `U_MIDCATEGORY_DESCR` varchar(256) null, `createdAt` datetime not null, `U_SUBCATEGORY_DESCR` varchar(256) null, `LIFNR` varchar(256) null, `U_SUBCATEGORY_CD` varchar(256) null, `U_CATEGORY_CD` varchar(256) null, `U_PROMO_STARTDATE` datetime null, `U_TRANSLOCSCHEDARRIVALDATE` datetime null, `DESCR` varchar(256) null, `QTY` decimal(9, 2) null, `U_PROMO_ENDDATE` datetime null, `U_OUTSTANDINGDAYS` decimal(9, 2) null, `U_MINSHIPNUMBER` decimal(9, 2) null, `U_PROMO_FLAG` tinyint null, `U_MIDCATEGORY_CD` varchar(256) null, `U_OUTPUT` varchar(256) null, `DBTIME` datetime null, `U_SSCOVER` decimal(9, 2) null, `U_CATEGORY_DESCR` varchar(256) null, `deletedAt` bigint not null default 0, primary key (`id`)) comment ''ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- step 15
alter table `custom__jda_replenishment_proposal_order` add `UpdatedBy` varchar(32) null COMMENT '最后修改人 ';
-- step 16
create index `UpdatedBy` on `custom__jda_replenishment_proposal_order`(`UpdatedBy`);
-- step 19
alter table `custom__jda_replenishment_proposal_order` add `CreatedBy` varchar(32) null COMMENT '创建人 ';
-- step 20
create index `CreatedBy` on `custom__jda_replenishment_proposal_order`(`CreatedBy`);
-- step 21
create index `uk_U_PLANARRIVAL_STORE_LINENO` on `custom__jda_replenishment_proposal_order`(`U_PLANARRIVAL_STORE_LINENO`);
-- step 22
create index `uk_U_PLANARRIVAL_STORE_CD` on `custom__jda_replenishment_proposal_order`(`U_PLANARRIVAL_STORE_CD`);
*/

/* ***********************导出结构命令***********************
 Navicat Premium Data Transfer

 Source Server         : 预发10.98.152.11
 Source Server Type    : MySQL
 Source Server Version : 50723
 Source Host           : 10.98.152.11:3306
 Source Schema         : trantor

 Target Server Type    : MySQL
 Target Server Version : 50723
 File Encoding         : 65001

 Date: 22/07/2021 16:08:50
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for custom__jda_replenishment_proposal_order
-- ----------------------------
DROP TABLE IF EXISTS `custom__jda_replenishment_proposal_order`;
CREATE TABLE `custom__jda_replenishment_proposal_order`  (
  `U_PROMO_ID` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `isDeleted` tinyint(4) NOT NULL DEFAULT 0,
  `RESWK` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `U_UOM_DESCR` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `U_FCST_QTY` decimal(9, 2) NULL DEFAULT NULL,
  `U_PLANARRIVAL_STORE_LINENO` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `U_UOM` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `U_OHINVENTORY` decimal(9, 2) NULL DEFAULT NULL,
  `id` bigint(20) NOT NULL,
  `U_VEHICLELOADLINE` decimal(9, 2) NULL DEFAULT NULL,
  `U_PLANARRIVAL_TYPE` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `SCHEDARRIVDATE` datetime NULL DEFAULT NULL,
  `updatedAt` datetime NOT NULL,
  `U_CHANGE_FLAG` tinyint(4) NULL DEFAULT NULL,
  `U_BARCODE` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `ISPROCESSED` tinyint(4) NULL DEFAULT NULL,
  `ITEM` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `U_PLANARRIVAL_STORE_CD` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `SOURCE` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `U_PACKNUMBER` decimal(9, 2) NULL DEFAULT NULL,
  `DEST` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `U_SPEC` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `U_TRANSLOC` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `SCHEDSHIPDATE` datetime NULL DEFAULT NULL,
  `U_DEST_DESCR` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `U_ARRIVALDATE` datetime NULL DEFAULT NULL,
  `U_MIDCATEGORY_DESCR` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `createdAt` datetime NOT NULL,
  `U_SUBCATEGORY_DESCR` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `LIFNR` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `U_SUBCATEGORY_CD` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `U_CATEGORY_CD` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `U_PROMO_STARTDATE` datetime NULL DEFAULT NULL,
  `U_TRANSLOCSCHEDARRIVALDATE` datetime NULL DEFAULT NULL,
  `DESCR` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `QTY` decimal(9, 2) NULL DEFAULT NULL,
  `U_PROMO_ENDDATE` datetime NULL DEFAULT NULL,
  `U_OUTSTANDINGDAYS` decimal(9, 2) NULL DEFAULT NULL,
  `U_MINSHIPNUMBER` decimal(9, 2) NULL DEFAULT NULL,
  `U_PROMO_FLAG` tinyint(4) NULL DEFAULT NULL,
  `U_MIDCATEGORY_CD` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `U_OUTPUT` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `DBTIME` datetime NULL DEFAULT NULL,
  `U_SSCOVER` decimal(9, 2) NULL DEFAULT NULL,
  `U_CATEGORY_DESCR` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `deletedAt` bigint(20) NOT NULL DEFAULT 0,
  `UpdatedBy` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL COMMENT '最后修改人 ',
  `CreatedBy` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL COMMENT '创建人 ',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `UpdatedBy`(`UpdatedBy`) USING BTREE,
  INDEX `CreatedBy`(`CreatedBy`) USING BTREE,
  INDEX `uk_U_PLANARRIVAL_STORE_LINENO`(`U_PLANARRIVAL_STORE_LINENO`) USING BTREE,
  INDEX `uk_U_PLANARRIVAL_STORE_CD`(`U_PLANARRIVAL_STORE_CD`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
