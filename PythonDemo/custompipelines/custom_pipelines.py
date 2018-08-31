import pymysql
import json
import datetime
from PythonDemo.pipelines import PythondemoPipeline
from PythonDemo.settings import mongo_host, mongo_port, mongo_db_name, mongo_db_collection
from PythonDemo.settings import mysql_host, mysql_port, mysql_username, mysql_password, mysql_db_name
from PythonDemo.items import PythondemoItem
from PythonDemo.items import TestItem
from PythonDemo.items import BusinessInformationItem
from PythonDemo.items import OverViewItem

# 工商信息管道，继承PythondemoPipeline
class BusinessInformationPipelines(PythondemoPipeline):
    def process_item(self, item, spider):
        if isinstance(item, BusinessInformationItem):
            data = dict(item)
            db = pymysql.Connect(mysql_host, mysql_username, mysql_password, mysql_db_name)
            cursor = db.cursor()
            platform_name = data['platform_name']
            # 获取平台ID
            id = self.get_id_by_platform_name(platform_name)
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            sql = """
                insert into wdzj_company_business_information
                    (platform_id, platform_name, corporate_name, unified_social_credit_code, legal_representative,
                    registered_capital, type_of_company, paid_capital, registered_address, opening_date,
                    registration_status, operating_period, registration_authority, approval_date, domain_name,
                    filing_time, name_of_record_unit, nature_of_record_unit, icp_record_number, icp_business_license,
                    platform_used_name, scope_of_operation, create_user_id, update_user_id, insert_time, update_time, isdeleted)
                    values
                    (%d, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s',
                    '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', %d, %d, '%s', '%s', %s)
                """ % (id, platform_name, data['corporate_name'], data['unified_social_credit_code'],
                        data['legal_representative'], data['registered_capital'], data['type_of_company'],
                        data['paid_capital'], data['registered_address'], data['opening_date'],
                        data['registration_status'], data['operating_period'], data['registration_authority'],
                        data['approval_date'], data['domain_name'], data['filing_time'], data['name_of_record_unit'],
                        data['nature_of_record_unit'], data['icp_record_number'], data['icp_business_license'],
                        data['platform_used_name'], data['scope_of_operation'], 0, 0, now, now, '0'
                        )
            try:
                cursor.execute(sql)
                db.commit()
            except ConnectionError:
                db.rollback()
            finally:
                db.close()
            return item