# dba_to_dwd_tools
## 项目背景
在数仓重构迁移过程中涉及到大量的关系型数据库to数据中台dwd建表工作，基于目前的数据治理规划，迁移建表符合强规则逻辑，通过python构建自动化过程有很高的可操作性。基于个人工作习惯看，底层工作流程可以拆分为dba获取关系型数据库建表语句-->通过文本编辑器替换、人工替换最终格式化成标准dwd建表语句-->脚本存档-->中台建表。
## 项目价值
dwd迁移工作相对分散，数仓相关同事均有涉及，费时费力，同时存在由于重复劳动导致的脚本修改纰漏问题，增加返工成本。dba_to_dwd脚本转换工具可以直接解决该部分工作痛点，并且由于强规则逻辑，可以很大程度上统一dwd底层规范。从个人测试看，单表处理过程可由原先3分钟左右缩短至30秒左右，效率提升80%。
## 开发环境
MacOS 11.4
Python 3.7.5
## 软件运行
首先安装python依赖：
pip install -r requirements.txt
环境配置完成后通过如下命令运行程序：
python run.py
## 更新日志
### 20220106
该版本为首次提交
* 支持dba_mysql建表语句转义为dwd层标准建表语句
* 支持转义后编辑结果
* 支持转义结果以sql文件形式保存到本地