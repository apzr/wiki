-- step 1 是否参与自动补货
alter table `custom__material_store_relation` add `automaticReplenishment` tinyint null;

-- 还有一个requisition-center项目里边更新了io.terminus.srm.requisition.model.dicts.SourceType;
-- 添加了 @Label("自动补货-JDA")public static final String REQUSITION_JDA = "REQUSITION_JDA";