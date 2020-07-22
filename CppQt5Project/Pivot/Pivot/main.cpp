#include "pivot.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    Pivot w;
    w.setWindowIcon(QIcon(":/ico/logo.ico")); //设置窗口图标
    w.show();
    
    return a.exec();
}
