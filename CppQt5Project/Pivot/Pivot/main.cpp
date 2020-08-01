#include "pivot.h"
#include <QDebug>
#include <QApplication>
#include <QStyleFactory>

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    //qDebug()<<QStyleFactory::keys(); //("Windows", "WindowsXP", "WindowsVista", "Fusion") //QT内置样式
    app.setStyle(QStyleFactory::create("Fusion"));
    Pivot w;
    w.setWindowIcon(QIcon(":/ico/logo.ico")); //设置窗口图标
    w.show();
    
    return app.exec();
}
