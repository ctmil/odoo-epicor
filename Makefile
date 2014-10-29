PROYECT=epicor
DESIGNDIR=design
WORKDIR=${DESIGNDIR}/tmp
ZARGO=${DESIGNDIR}/${PROYECT}.zargo
XMI=${WORKDIR}/${PROYECT}.xmi
DB=${WORKDIR}/${PROYECT}.db
XMICONV=xmi2oerp

all: addons

notify:
	while inotifywait -e close_write ${ZARGO}; do make addons; done

${XMI}: ${ZARGO}
	unzip -o -d ${WORKDIR} ${ZARGO}
	touch ${XMI}


addons: ${DB}
	${XMICONV} -r --dbfile $< --logfile $?.log --loglevel=2 --target $@

-addons: ${DB}
	-git branch argouml
	git checkout argouml
	${XMICONV} -r --dbfile $< --logfile $?.log --loglevel=2 --target $@
	git commit -am "[ARGOUML] $$(date)"

${DB}: ${XMI}
	${XMICONV} --infile $< --dbfile $@ ${XMI2OERP_OPT}

clean:
	rm -rf ${WORKDIR}

.PHONY: notify addons xxxx

.SUFFIXES:

