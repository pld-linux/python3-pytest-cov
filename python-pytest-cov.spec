#
# Conditional build:
%bcond_without	doc		# Sphinx documentation
%bcond_with	tests		# py.test tests [sensitive to coverage and pytest output, few tests fail for me]
%bcond_with	tests_py2	# Python 2 py.test tests [require some modules sources + the above]
%bcond_without	python2		# CPython 2.x module
%bcond_without	python3		# CPython 3.x module

Summary:	pytest plugin for measuring coverage
Summary(pl.UTF-8):	Wtyczka pytest do mierzenia pokrycia
Name:		python-pytest-cov
Version:	2.6.0
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-cov/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-cov/pytest-cov-%{version}.tar.gz
# Source0-md5:	7c8c1bf2a5c355a4c3ad9aafe4a1894d
URL:		https://github.com/pytest-dev/pytest-cov
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests_py2}
BuildRequires:	python-coverage >= 4.4
BuildRequires:	python-fields
BuildRequires:	python-process_tests >= 2.0.0
BuildRequires:	python-py
BuildRequires:	python-pytest >= 2.9
BuildRequires:	python-pytest-xdist >= 1.23.0
BuildRequires:	python-six
BuildRequires:	python-virtualenv
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-coverage >= 4.4
BuildRequires:	python3-fields
BuildRequires:	python3-process_tests >= 2.0.0
BuildRequires:	python3-py
BuildRequires:	python3-pytest >= 2.9
BuildRequires:	python3-pytest-xdist >= 1.23.0
BuildRequires:	python3-six
BuildRequires:	python3-virtualenv
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg
BuildRequires:	python3-sphinx_py3doc_enhanced_theme
%endif
Requires:	python-modules >= 1:2.7
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
Requires:	python3-modules >= 1:3.4

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

%if %{with tests_py2}
PYTHONPATH=$(pwd)/src:$(pwd)/tests \
XPYTEST_PLUGINS=pytest_cov.plugin \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd)/src:$(pwd)/tests \
XPYTEST_PLUGINS=pytest_cov.plugin \
%{__python3} -m pytest tests
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
