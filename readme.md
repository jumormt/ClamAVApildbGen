apilist.xlsx文件为预置的敏感api和字符串列表

python apiGen.py
会读取apilist.xlsx的内容并生成apigen.ldb规则文件，该规则文件可用于clamscan静态扫描引擎

$ clamscan -z -d path/to/apigen.ldb -r target/ -l path/to/20171024.txt
