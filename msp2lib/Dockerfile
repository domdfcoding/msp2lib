FROM tobix/wine-staging
LABEL MAINTAINER="Dominic Davis-Foster dominic@davis-foster.co.uk"

ARG BUILD_DATE
ARG VCS_REF

LABEL \
  org.label-schema.build-date=$BUILD_DATE \
  org.label-schema.license="MIT" \
  org.label-schema.name="The NIST Library Conversion program running in Wine and Docker" \
  org.label-schema.vcs-url="https://github.com/domdfcoding/msp2lib"

COPY make_nistlib.sh /make_nistlib.sh
RUN chmod +x /make_nistlib.sh

# Download and unzip Lib2Nist
RUN apt-get update && \
	apt-get install wget -y --no-install-recommends &&\
	wget https://chemdata.nist.gov/mass-spc/ms-search/downloads/LIB2NIST.zip &&\
	apt-get remove wget -y &&\
	apt-get clean &&\
	rm -rf /var/lib/apt/lists/*

RUN unzip LIB2NIST.zip -d /LIB2NIST

# Make input and output dirs
RUN mkdir /input && mkdir /output

ENV PYTHONUNBUFFERED=1
