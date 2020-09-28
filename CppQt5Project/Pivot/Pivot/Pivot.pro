#-------------------------------------------------
#
# Project created by QtCreator 2019-11-27T07:06:04
#
#-------------------------------------------------
# Tips::注释快捷键 ctrl+"/"

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets printsupport

TARGET = Pivot  # 指定生成的应用程序名
TEMPLATE = app  # 模板变量告诉qmake为这个应用程序生成哪种makefile



# The following define makes your compiler emit warnings if you use
# any feature of Qt which has been marked as deprecated (the exact warnings
# depend on your compiler). Please consult the documentation of the
# deprecated API in order to know how to port your code away from it.
DEFINES += QT_DEPRECATED_WARNINGS

# You can also make your code fail to compile if you use deprecated APIs.
# In order to do so, uncomment the following line.
# You can also select to disable deprecated APIs only up to a certain version of Qt.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0




#工程中包含的源文件
SOURCES += \
        database.cpp \
        dataframe.cpp \
        dataseries.cpp \
        main.cpp \
        pivot.cpp \
        pivot_import.cpp \
        pivot_slot.cpp

#工程中包含的头文件
HEADERS += \
        base_define.h \
        base_number.h \
        database.h \
        dataframe.h \
        dataseries.h \
        pivot.h \
        version.h

#工程中包含的.ui设计文件
FORMS += \
        pivot.ui

##指定uic命令将.ui文件转化成ui_*.h文件的存放的目录
#UI_DIR += UI_HEAD

RC_FILE += \
    pivot.rc

RESOURCES += \
    pivot.qrc

#指定rcc命令将.qrc文件转换成qrc_*.h文件的存放目录
#RCC_DIR += ../tmp


#头文件包含路径,一般要编译链接第三方库时配置include目录
#INCLUDEPATH += .


#指定moc命令将含Q_OBJECT的头文件转换成标准.h文件的存放目录
#MOC_DIR += ../tmp

#指定目标文件(obj)的存放目录
#OBJECTS_DIR += ../tmp

#程序编译时依赖的相关路径,一般要编译链接第三方库时配置include目录
#DEPENDPATH += . forms include qrc sources


#CONFIG += console  # 告诉qmake关于应用程序的配置信息
#win32:CONFIG(debug, debug|release):CONFIG += console







## 设置windows平台资源文件
#RC_FILE +=  \
#    fennec.rc

##工程中包含的资源文件
#RESOURCES += \
#    icon.qrc





##qwt start
#include(../Qwt-6.1.3/features/qwt.prf )
#win32:CONFIG(release, debug|release): LIBS += -L$$PWD/../Qwt-6.1.3/lib/ -lqwt
#else:win32:CONFIG(debug, debug|release): LIBS += -L$$PWD/../Qwt-6.1.3/lib/ -lqwtd
#else:unix: LIBS += -L$$PWD/../Qwt-6.1.3/lib/ -lqwt
#INCLUDEPATH += $$PWD/../Qwt-6.1.3/include # 编译链接第三方库时配置include目录
#DEPENDPATH += $$PWD/../Qwt-6.1.3/include
##qwtAddLibrary(qwt)
##qwt end



