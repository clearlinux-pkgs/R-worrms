#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-worrms
Version  : 0.4.2
Release  : 26
URL      : https://cran.r-project.org/src/contrib/worrms_0.4.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/worrms_0.4.2.tar.gz
Summary  : World Register of Marine Species (WoRMS) Client
Group    : Development/Tools
License  : MIT
Requires: R-crul
Requires: R-data.table
Requires: R-jsonlite
Requires: R-tibble
Requires: R-vcr
BuildRequires : R-crul
BuildRequires : R-data.table
BuildRequires : R-jsonlite
BuildRequires : R-tibble
BuildRequires : R-vcr
BuildRequires : buildreq-R

%description
worrms
======
[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)
[![cran checks](https://cranchecks.info/badges/worst/worrms)](https://cranchecks.info/pkgs/worrms)
[![Build Status](https://travis-ci.org/ropensci/worrms.svg?branch=master)](https://travis-ci.org/ropensci/worrms)
[![Build status](https://ci.appveyor.com/api/projects/status/e5q7fi97pl49h7v6?svg=true)](https://ci.appveyor.com/project/sckott/worrms)
[![codecov](https://codecov.io/gh/ropensci/worrms/branch/master/graph/badge.svg)](https://codecov.io/gh/ropensci/worrms)
[![rstudio mirror downloads](https://cranlogs.r-pkg.org/badges/worrms)](https://github.com/metacran/cranlogs.app)
[![cran version](https://www.r-pkg.org/badges/version/worrms)](https://cran.r-project.org/package=worrms)

%prep
%setup -q -c -n worrms
cd %{_builddir}/worrms

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1594222863

%install
export SOURCE_DATE_EPOCH=1594222863
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library worrms
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library worrms
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library worrms
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc worrms || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/worrms/DESCRIPTION
/usr/lib64/R/library/worrms/INDEX
/usr/lib64/R/library/worrms/LICENSE
/usr/lib64/R/library/worrms/Meta/Rd.rds
/usr/lib64/R/library/worrms/Meta/features.rds
/usr/lib64/R/library/worrms/Meta/hsearch.rds
/usr/lib64/R/library/worrms/Meta/links.rds
/usr/lib64/R/library/worrms/Meta/nsInfo.rds
/usr/lib64/R/library/worrms/Meta/package.rds
/usr/lib64/R/library/worrms/Meta/vignette.rds
/usr/lib64/R/library/worrms/NAMESPACE
/usr/lib64/R/library/worrms/NEWS.md
/usr/lib64/R/library/worrms/R/worrms
/usr/lib64/R/library/worrms/R/worrms.rdb
/usr/lib64/R/library/worrms/R/worrms.rdx
/usr/lib64/R/library/worrms/doc/index.html
/usr/lib64/R/library/worrms/doc/worrms.Rmd
/usr/lib64/R/library/worrms/doc/worrms.html
/usr/lib64/R/library/worrms/help/AnIndex
/usr/lib64/R/library/worrms/help/aliases.rds
/usr/lib64/R/library/worrms/help/paths.rds
/usr/lib64/R/library/worrms/help/worrms.rdb
/usr/lib64/R/library/worrms/help/worrms.rdx
/usr/lib64/R/library/worrms/html/00Index.html
/usr/lib64/R/library/worrms/html/R.css
/usr/lib64/R/library/worrms/tests/fixtures/wm_children.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_children_-error.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_children_.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_children_error.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_children_many.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_children_marine_only_false.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_children_marine_only_true.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_children_name.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_children_offset.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_classification.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_classification_.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_classification_many.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_common_id.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_common_id_.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_common_id_many.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_distribution.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_distribution_.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_distribution_many.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_external.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_external_.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_external_fishbase.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_external_many.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_id2name.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_id2name_.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_id2name_many.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_name2id.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_name2id_.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_name2id_many.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_ranks_id.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_ranks_id_error.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_ranks_name.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_ranks_name_error.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_record.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_record_by_external__many.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_record_by_external__tsn.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_record_by_external_fishbase.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_record_by_external_ncbi.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_record_by_external_tsn.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_record_error.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_record_plural_plural.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_records__many.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_records_common.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_records_common_fuzzy_false.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_records_common_fuzzy_true.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_records_common_offset.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_records_name.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_records_name_fuzzy.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_records_names.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_records_names_fuzzy.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_records_rank.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_records_rank_error.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_records_taxamatch.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_sources.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_sources__many.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_synonyms.yml
/usr/lib64/R/library/worrms/tests/fixtures/wm_synonyms__many.yml
/usr/lib64/R/library/worrms/tests/test-all.R
/usr/lib64/R/library/worrms/tests/testthat/helper-worrms.R
/usr/lib64/R/library/worrms/tests/testthat/test-wm_children.R
/usr/lib64/R/library/worrms/tests/testthat/test-wm_classification.R
/usr/lib64/R/library/worrms/tests/testthat/test-wm_common_id.R
/usr/lib64/R/library/worrms/tests/testthat/test-wm_distribution.R
/usr/lib64/R/library/worrms/tests/testthat/test-wm_external.R
/usr/lib64/R/library/worrms/tests/testthat/test-wm_id2name.R
/usr/lib64/R/library/worrms/tests/testthat/test-wm_name2id.R
/usr/lib64/R/library/worrms/tests/testthat/test-wm_ranks.R
/usr/lib64/R/library/worrms/tests/testthat/test-wm_record.R
/usr/lib64/R/library/worrms/tests/testthat/test-wm_record_by_external.R
/usr/lib64/R/library/worrms/tests/testthat/test-wm_records_common.R
/usr/lib64/R/library/worrms/tests/testthat/test-wm_records_date.R
/usr/lib64/R/library/worrms/tests/testthat/test-wm_records_name.R
/usr/lib64/R/library/worrms/tests/testthat/test-wm_records_names.R
/usr/lib64/R/library/worrms/tests/testthat/test-wm_records_rank.R
/usr/lib64/R/library/worrms/tests/testthat/test-wm_records_taxamatch.R
/usr/lib64/R/library/worrms/tests/testthat/test-wm_sources.R
/usr/lib64/R/library/worrms/tests/testthat/test-wm_synonyms.R
