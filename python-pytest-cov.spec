#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# py.test tests [require some modules sources, sensitive to coverage and pytest output]
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	pytest plugin for measuring coverage
Summary(pl.UTF-8):	Wtyczka pytest do mierzenia pokrycia
Name:		python-pytest-cov
Version:	2.4.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/simple/pytest-cov
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-cov/pytest-cov-%{version}.tar.gz
# Source0-md5:	2fda09677d232acc99ec1b3c5831e33f
URL:		https://github.com/pytest-dev/pytest-cov
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-coverage >= 3.7.1
BuildRequires:	python-helper
BuildRequires:	python-process_tests >= 1.2.0
BuildRequires:	python-pytest >= 2.6.0
BuildRequires:	python-pytest-capturelog
BuildRequires:	python-pytest-xdist >= 1.15.0
BuildRequires:	python-virtualenv
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-coverage >= 3.7.1
BuildRequires:	python3-helper
BuildRequires:	python3-process_tests >= 1.2.0
BuildRequires:	python3-pytest >= 2.6.0
BuildRequires:	python3-pytest-capturelog
BuildRequires:	python3-pytest-xdist >= 1.15.0
BuildRequires:	python3-virtualenv
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg
BuildRequires:	python3-sphinx_py3doc_enhanced_theme
%endif
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin produces coverage reports. It supports centralised testing
and distributed testing in both load and each modes. It also supports
coverage of subprocesses.

%description -l pl.UTF-8
Ta wtyczka tworzy raporty pokrycia. Obsługuje testowanie
zcentraliwowane i rozproszone, zarówno w trybie "load", jak i "each".
Obsługuje także pokrycie podprocesów.

%package -n python3-pytest-cov
Summary:	pytest plugin for measuring coverage
Summary(pl.UTF-8):	Wtyczka pytest do mierzenia pokrycia
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-pytest-cov
This plugin produces coverage reports. It supports centralised testing
and distributed testing in both load and each modes. It also supports
coverage of subprocesses.

%description -n python3-pytest-cov -l pl.UTF-8
Ta wtyczka tworzy raporty pokrycia. Obsługuje testowanie
zcentraliwowane i rozproszone, zarówno w trybie "load", jak i "each".
Obsługuje także pokrycie podprocesów.

%package apidocs
Summary:	Documentation for pytest-cov module
Summary(pl.UTF-8):	Dokumentacja do modułu pytest-cov
Group:		Documentation

%description apidocs
Documentation for pytest-cov module.

%description apidocs -l pl.UTF-8
Dokumentacja do modułu pytest-cov.

%prep
%setup -q -n pytest-cov-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTHONPATH=$(pwd)/build-2/lib PYTEST_PLUGINS=pytest_cov.plugin %{__python} -m pytest
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd)/build-3/lib PYTEST_PLUGINS=pytest_cov.plugin %{__python3} -m pytest
%endif
%endif

%if %{with doc}
cd docs
sphinx-build -b html . _build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS.rst CHANGELOG.rst LICENSE README.rst
%{py_sitescriptdir}/pytest-cov.pth
%{py_sitescriptdir}/pytest_cov
%{py_sitescriptdir}/pytest_cov-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pytest-cov
%defattr(644,root,root,755)
%doc AUTHORS.rst CHANGELOG.rst LICENSE README.rst
%{py3_sitescriptdir}/pytest-cov.pth
%{py3_sitescriptdir}/pytest_cov
%{py3_sitescriptdir}/pytest_cov-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
