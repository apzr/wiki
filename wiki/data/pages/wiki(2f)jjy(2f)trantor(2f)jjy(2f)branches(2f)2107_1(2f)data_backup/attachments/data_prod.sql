/*
 Navicat Premium Data Transfer

 Source Server         : 预发10.98.152.11
 Source Server Type    : MySQL
 Source Server Version : 50723
 Source Host           : 10.98.152.11:3306
 Source Schema         : trantor

 Target Server Type    : MySQL
 Target Server Version : 50723
 File Encoding         : 65001

 Date: 22/07/2021 17:09:02
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for custom__jda_replenishment_proposal_order
-- ----------------------------
DROP TABLE IF EXISTS `custom__jda_replenishment_proposal_order`;
CREATE TABLE `custom__jda_replenishment_proposal_order`  (
  `U_PROMO_ID` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `isDeleted` tinyint(4) NULL DEFAULT 0,
  `RESWK` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `U_UOM_DESCR` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `U_FCST_QTY` decimal(9, 2) NULL DEFAULT NULL,
  `U_PLANARRIVAL_STORE_LINENO` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `U_UOM` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `U_OHINVENTORY` decimal(9, 2) NULL DEFAULT NULL,
  `id` bigint(20) UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT,
  `U_VEHICLELOADLINE` decimal(9, 2) NULL DEFAULT NULL,
  `U_PLANARRIVAL_TYPE` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `SCHEDARRIVDATE` datetime NULL DEFAULT NULL,
  `updatedAt` datetime NULL DEFAULT NULL,
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
  `createdAt` datetime NULL DEFAULT NULL,
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
  `deletedAt` bigint(20) NULL DEFAULT 0,
  `UpdatedBy` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL COMMENT '最后修改人 ',
  `CreatedBy` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL COMMENT '创建人 ',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `UpdatedBy`(`UpdatedBy`) USING BTREE,
  INDEX `CreatedBy`(`CreatedBy`) USING BTREE,
  INDEX `uk_U_PLANARRIVAL_STORE_LINENO`(`U_PLANARRIVAL_STORE_LINENO`) USING BTREE,
  INDEX `uk_U_PLANARRIVAL_STORE_CD`(`U_PLANARRIVAL_STORE_CD`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of custom__jda_replenishment_proposal_order
-- ----------------------------
INSERT INTO `custom__jda_replenishment_proposal_order` VALUES ('99999999', 0, NULL, 'KG', 20.00, '1', 'KG', 20.00, 00000000000000000001, 20.00, '自动补货-JDA', '2021-07-24 00:00:00', NULL, 1, '2006', NULL, '10002006', '111212021072220061', 'W001', 20.00, '1112', '200ml', 'W002', '2021-07-23 00:00:00', '测试1', NULL, '测试1', NULL, '测试1', NULL, '20060101', '2006', '2021-09-15 00:00:00', '2021-07-23 00:00:00', '测试1', 20.00, '2021-10-01 00:00:00', 1.00, 20.00, 1, '200601', '1', '2021-07-22 16:11:04', 5.00, '测试1', 0, NULL, NULL);
INSERT INTO `custom__jda_replenishment_proposal_order` VALUES (NULL, 0, NULL, 'KG', 20.00, '1', 'KG', 20.00, 00000000000000000002, 20.00, '自动补货-JDA', '2021-07-24 00:00:00', NULL, 1, '2007', NULL, '10002007', '111212021072220071', 'W001', 20.00, '1113', '200ml', 'W002', '2021-07-23 00:00:00', '测试2', NULL, '测试2', NULL, '测试2', NULL, '20070101', '2007', NULL, '2021-07-23 00:00:00', '测试2', 20.00, NULL, 1.00, 20.00, 0, '200701', '1', '2021-07-22 16:11:46', 5.00, '测试2', 0, NULL, NULL);
INSERT INTO `custom__jda_replenishment_proposal_order` VALUES (NULL, 0, NULL, 'KG', 20.00, '1', 'KG', 20.00, 00000000000000000003, 20.00, '自动补货-JDA', '2021-07-24 00:00:00', NULL, 1, '2008', NULL, '10002008', '111212021072220081', 'W001', 20.00, '1114', '200ml', 'W002', '2021-07-23 00:00:00', '测试3', NULL, '测试3', NULL, '测试3', NULL, '20080101', '2008', NULL, '2021-07-23 00:00:00', '测试3', 20.00, NULL, 1.00, 20.00, 0, '200801', '1', '2021-07-22 16:12:51', 5.00, '测试3', 0, NULL, NULL);

SET FOREIGN_KEY_CHECKS = 1;
