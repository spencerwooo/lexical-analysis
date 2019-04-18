# Lexical Analysis

【编译原理】词法分析实验

## 目录结构

```bash
.
├── LICENSE
├── README.md
├── bin
...
├── config.xml
├── doc
│   ├── docs.pdf
│   ├── docs.tex
│   └── ...
├── input
│   └── ...
├── lib
│   └── BITMiniCC-obf.jar
├── run
│   ├── binary
│   │   └── scan.py
│   ├── config.xml
│   ├── run.sh
│   ├── test.token.xml
│   └── tests
│       ├── test.c
│       ├── test.pp.c
│       └── test.token.xml
└── src
    └── bit
    ...

23 directories, 86 files

```

## 使用方法

我实现的词法分析器位于 `run/binary/scan.py`，可传入参数。使用方法如：

```bash
# 进入 run 目录下
cd run
# 运行 binary 目录下的 scan.py，对 test 目录下的 test.c 进行词法分析
python3 binary/scan.py tests/test.c
```

## 嵌入框架

修改 `config.xml` 中 scanning 字段，添加 Python 可执行文件的路径，将 pp 和 scanning 阶段的 skip 修改为 false，其余修改为 true：

```xml
<config name="config.xml">
  <phases>
    <phase>
      <phase skip="false" type="java" path="" name="pp" />
      <phase skip="false" type="python" path="<path/to/python/executable>" name="scanning" />
      ...
      </phase>
  </phases>
</config>
```

之后，如下运行 Java `jar` 包：

```bash
# 进入 run 目录
cd run
# 执行 Java `jar` 包
java -jar ../lib/BITMiniCC-obf.jar tests/test.c
```