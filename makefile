.PHONY: all clean

all: przyklad


%: %.py
	python3 $@.py > $@.tex
	pdflatex $@.tex
	rm -rf *.aux *.log

	
clean:
	rm -rf *.pdf *.tex *.aux *.log
