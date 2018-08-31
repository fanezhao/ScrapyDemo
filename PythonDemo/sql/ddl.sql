# 备案信息
create table wdzj_company_business_information (
  id                         bigint(20) primary key auto_increment comment '主键',
  platform_id                bigint(20)       not null comment '平台ID',
  platform_name            varchar(50)       default null comment '平台名称',
  corporate_name             varchar(500)       default null comment '公司名称',
  unified_social_credit_code varchar(100)       default null comment '统一社会信用代码',
  legal_representative       varchar(100)       default null comment '法人代表',
  registered_capital         varchar(100)       default null comment '注册资本',
  type_of_company            varchar(500)       default null comment '公司类型',
  paid_capital               varchar(100)       default null comment '实缴资本',
  registered_address         varchar(500)       default null comment '注册地址',
  opening_date               varchar(100)       default null comment '开业日期',
  registration_status        varchar(10)        default null comment '登记状态',
  operating_period           varchar(100)       default null comment '营业期限',
  registration_authority     varchar(200)       default null comment '登记机关',
  approval_date              varchar(100)       default null comment '核准日期',
  domain_name                varchar(50)        default null comment '备案域名',
  filing_time                varchar(100)       default null comment '备案时间',
  name_of_record_unit        varchar(500)       default null comment '备案单位名称',
  nature_of_record_unit      varchar(20)        default null comment '备案单位性质',
  icp_record_number          varchar(100)       default null comment 'ICP备案号',
  icp_business_license       varchar(100)       default null comment 'ICP经营许可证',
  platform_used_name         varchar(500)       default null comment '平台曾用名',
  scope_of_operation         varchar(1000)      default null comment '经营范围',
  create_user_id             bigint(20)         default null comment '创建人ID',
  update_user_id             bigint(20)         default null comment '更新人ID',
  insert_time                datetime           default now() comment '插入时间',
  update_time                datetime           default now() comment '更新时间',
  isdeleted                  varchar(1)         default '0' comment '是否删除：0 未删除；1 已删除'
) comment '工商备案信息表';

# 概览
create table wdzj_company_overview {
  id    bigint(20) primary key auto_increment comment '主键',
  platform_id bigint(20) not null comment '平台id',
  platform_name varchar(50) not null comment '平台名称',
  register_money varchar(50) default null comment '注册资金',
  public_equity varchar(50) default null comment '股权上市',
  bank_depository varchar(50) default null comment '银行存管',
  financing varchar(500) default null comment '融资记录',
  association varchar(100) default null comment '监管协会',
  icp varchar(50) default null comment 'ICP号',
  create_user_id             bigint(20)         default null comment '创建人ID',
  update_user_id             bigint(20)         default null comment '更新人ID',
  insert_time                datetime           default now() comment '插入时间',
  update_time                datetime           default now() comment '更新时间',
  isdeleted                  varchar(1)         default '0' comment '是否删除：0 未删除；1 已删除'
} comment '概览信息'