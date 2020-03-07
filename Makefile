content:
	@echo "[" > public/data.json
	@for a in $$(ls src/Contents); do \
		cat src/Contents/$$a >> public/data.json ; \
		echo "," >> public/data.json;\
     done
	@echo "]" >> public/data.json
