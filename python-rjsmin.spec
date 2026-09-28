Name:		python-rjsmin
Version:	1.2.0
Release:	1
Summary:	Javascript Minifier
License:	Apache-2.0
Group:		Development/Python
URL:		https://pypi.org/project/rjsmin/
Source0:	rjsmin-1.2.0.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	gcc
BuildRequires:	lib64python-devel
%description
Javascript Minifier.

%files
%{python_sitearch}/*
