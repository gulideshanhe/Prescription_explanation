import jieba
from selenium import webdriver
from selenium.webdriver.common.by import By


def remove(div) -> None:  # 删除带有div中含有广告的大标签
	# 大标签是“广告”的第10个父元素
	wd.execute_script(f'{div}.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement'
	                  f'.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.remove();')


def find_advertisements() -> None:  # 定位广告元素，传给remove函数进行删除
	advertisements = wd.find_elements(By.CSS_SELECTOR, "._2awtgst")
	for advertisement in advertisements:
		remove(advertisement)
	# 建议用sleep函数等待1秒左右，避免被百度要求进行验证
	wd.execute_script("alert('医疗信息具有强领域专业性，就诊用药需谨慎。');")


def view() -> None:  # 利用pyside6实现的可视化操作界面
	import ui_case as name
	app = name.QApplication([])
	MainWindow = name.QWidget()
	global ui
	ui = name.Ui_Form()
	ui.setupUi(MainWindow)
	ui.go_query.setEnabled(False)
	ui.sure.clicked.connect(get_words)
	ui.go_query.clicked.connect(search)
	MainWindow.show()
	app.exec()


def search() -> None:  # 利用selenium库实现的自动化查询
	global wd
	wd = webdriver.Edge()
	some_words = ui.comboBox.currentText()
	wd.get("https://www.baidu.com")
	wd.find_element(By.CSS_SELECTOR, "#kw").send_keys(some_words)
	wd.find_element(By.CSS_SELECTOR, "#su").click()
	find_advertisements()


def get_words() -> None:  # 获取输入的病例，并利用jieba进行分词
	words = ui.textEdit.toPlainText()
	seg_list = jieba.cut(words)
	ui.comboBox.addItems(seg_list)
	ui.go_query.setEnabled(True)


if __name__ == '__main__':
	view()
