import re
import os

def mysql_trans_to_dwd(text, sys_name):
    """[summary]

    Args:
        text (string): 待解析的dba建表语句
        sys_name (string): dba源系统名称

    Returns:
        string: 解析后的dwd建表语句&dwd表名称
    """
    content_list=text.split('\n')
    trans_list=[]
    list_len=len(content_list)
    # 查找替换关键词
    for line in content_list:
        # 通用替换
        tmp_line=line
        tmp_line=tmp_line.replace('`', '')
        tmp_line=tmp_line.replace('CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT \'\' ', '')
        tmp_line=tmp_line.replace('NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP ', '')
        tmp_line=tmp_line.replace('NULL DEFAULT CURRENT_TIMESTAMP ', '')
        tmp_line=tmp_line.replace(' NOT ON UPDATE CURRENT_TIMESTAMP', '')
        tmp_line=tmp_line.replace(' DEFAULT CURRENT_TIMESTAMP ', '')
        tmp_line=tmp_line.replace('NOT NULL AUTO_INCREMENT ', '')
        tmp_line=tmp_line.replace('NOT NULL ', '')
        tmp_line=tmp_line.replace('NOT NULL', '')
        tmp_line=tmp_line.replace('DEFAULT NULL ', '')
        tmp_line=tmp_line.replace(' DEFAULT NULL', '')
        tmp_line=tmp_line.replace(' AUTO_INCREMENT', '')
        tmp_line=tmp_line.replace(' NULL', '')
        
        # 精准替换数据类型
        replace_dict={}
        words=tmp_line.split(' ')
        # 查找替换关键词
        for word in words:
                res=re.match("int\(\d+\)",word)
                if res!=None:
                    replace_dict[res.group()]='int'
                res=re.match("tinyint\(\d+\)",word)
                if res!=None:
                    replace_dict[res.group()]='int'
                res=re.match("bigint\(\d+\)",word)
                if res!=None:
                    replace_dict[res.group()]='bigint'
                res=re.match("varchar\(\d+\)",word)
                if res!=None:
                    replace_dict[res.group()]='string'
                res=re.match("char\(\d+\)",word)
                if res!=None:
                    replace_dict[res.group()]='string'
                res=re.match("datetime",word)
                if res!=None:
                    replace_dict[res.group()]='string'
                res=re.match("timestamp",word)
                if res!=None:
                    replace_dict[res.group()]='string'
                res=re.match("tinytext",word)
                if res!=None:
                    replace_dict[res.group()]='string'
                res=re.match("text",word)
                if res!=None:
                    replace_dict[res.group()]='string'
                res=re.match("json",word)
                if res!=None:
                    replace_dict[res.group()]='string'
                res=re.match("decimal\(\d+,\d+\)",word)
                if res!=None:
                    replace_dict[res.group()]='double'
        # 遍历替换词典准备替换
        if len(replace_dict.keys())>0:
            for key in replace_dict.keys():
                tmp_line=tmp_line.replace(key, replace_dict[key])
        else:
            pass
        
        # 首行替换表名
        if content_list.index(line)==0:
            dwd_tb_name='dwd_'+sys_name+'_'+words[-2]+'_df'
            tmp_line=tmp_line.replace(words[-2], dwd_tb_name)
        # 判定是否有主键定义
        if content_list.index(line)>0 and content_list.index(line)<list_len-1:
            # 发现主键定义，跳过当前行
            if tmp_line.find('PRIMARY')>=0 or tmp_line.find('KEY')>=0:
                continue
        # 末行提纯表注释
        if content_list.index(line)==list_len-1:
            if tmp_line.find('COMMENT')>=0:
                tmp_line=') '+words[-1]
                tmp_line=tmp_line.replace('=', ' ')
            else:
                tmp_line=')'
        # 解析后的行文本添加进新的list
        trans_list.append(tmp_line)
    
    # 添加etl_time并且修正最后一个字段结尾带逗号的问题
    # trans_list.insert(1,'  etl_time string comment \'etl_time\',')
    # trans_list[len(trans_list)-2]=trans_list[len(trans_list)-2].replace(',','')
    trans_list.insert(len(trans_list)-1,'  etl_time string COMMENT \'etl_time\'')
    # 添加分区部分
    trans_list.append('PARTITIONED BY(')
    trans_list.append(' dt string')
    trans_list.append(')')
    # 组装解析后文本
    trans_text='\n'.join(trans_list)
    return trans_text, dwd_tb_name

def check_save_path(save_path):
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    
def save_file(save_content,dwd_tb_name,save_path):
    real_path=save_path+'/'+dwd_tb_name+'建表.sql'
    fh = open(real_path, 'w', encoding='utf-8')
    fh.write(save_content)
    fh.close