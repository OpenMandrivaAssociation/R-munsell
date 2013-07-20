%global packname munsell
%global rlibdir %{_libdir}/R/library

Name: R-%{packname}
Version: 0.4.2
Release: 1
Summary: Munsell color system
Group: Sciences/Mathematics
License: MIT
URL: http://cran.r-project.org/web/packages/%{packname}/index.html
Source0: http://cran.r-project.org/src/contrib/%{packname}_0.4.2.tar.gz
BuildArch: noarch
Requires: R-colorspace
BuildRequires: R-devel Rmath-devel texlive-collection-latex
BuildRequires: R-colorspace

%description
Functions for exploring and using the Munsell color system

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/LICENSE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/raw
