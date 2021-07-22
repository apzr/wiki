-- step 1
alter table `requisition_center__purchase_line` add `schedArriveDate` datetime null;
-- step 2
alter table `requisition_center__purchase_line` add `supplierFactory` varchar(256) null;
-- step 3
alter table `requisition_center__purchase_line` add `saleCountNWeek` decimal(9, 2) null;
-- step 4
alter table `requisition_center__purchase_line` add `midCategory` varchar(256) null;
-- step 5
alter table `requisition_center__purchase_line` add `sumDate` datetime null;
-- step 6
alter table `requisition_center__purchase_line` add `promoId` varchar(256) null;
-- step 7
alter table `requisition_center__purchase_line` add `changeFlag` tinyint null;
-- step 8
alter table `requisition_center__purchase_line` add `promoFlag` tinyint null;


-- step 1 修改原因
alter table `requisition_center__purchase_line` add `changeReason` varchar(256) null;


-- 还有一个requisition-center项目里边更新了io.terminus.srm.requisition.model.dicts.SourceType;
-- 添加了 @Label("自动补货-JDA")public static final String REQUSITION_JDA = "REQUSITION_JDA";