index.html: projects.json contributes.json
	python3 make.py  > index.html

clean:
	rm -rf index.html

