index.html: projects.json contributes.json index.html.tpl make.py
	python3 make.py  > index.html

clean:
	rm -rf index.html

