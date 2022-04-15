SUMMARY = "Test"
DESCRIPTION = "Test Script"
HOMEPAGE = "https://github.com/milanpreetkaur502/TEST.git"
LICENSE = "CLOSED"


SRCREV = "${AUTOREV}"

SRC_URI = "git://github.com/milanpreetkaur502/TEST.git;protocol=https;user=milanpreetkaur502+deploy-token-1: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;branch=master" 

inherit allarch

S = "${WORKDIR}/git"

do_compile(){
}

do_install_append(){
	install -d ${D}${sbindir}/test
	cp -r ${S}/* ${D}${sbindir}/test

}


FILES_${PN} += "${sbindir}/*"

