#
# Conditional build:
%bcond_without	doc		# Sphinx documentation
%bcond_with	tests		# py.test tests [sensitive to coverage and pytest output, few tests fail for me]

Summary:	pytest plugin for measuring coverage
Summary(pl.UTF-8):	Wtyczka pytest do mierzenia pokrycia
Name:		python3-pytest-cov
Version:	6.0.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-cov/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-cov/pytest-cov-%{version}.tar.gz
# Source0-md5:	a7a0814b5fdec547764d3a57b99e8527
URL:		https://github.com/pytest-dev/pytest-cov
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-coverage >= 5.2.1
BuildRequires:	python3-fields
BuildRequires:	python3-process_tests >= 2.0.2
BuildRequires:	python3-pytest >= 4.6.10
BuildRequires:	python3-pytest-xdist >= 1.27.0
BuildRequires:	python3-six
BuildRequires:	python3-toml
BuildRequires:	python3-virtualenv
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-docutils >= 0.16
BuildRequires:	python3-jinja2
BuildRequires:	python3-sphinx_py3doc_enhanced_theme >= 2.4.0
BuildRequires:	sphinx-pdg-3 >= 3.0.3
%endif
Requires:	python3-modules >= 1:3.7
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
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd)/src:$(pwd)/tests \
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=pytest_cov.plugin,xdist.looponfail,xdist.plugin \
%{__python3} -m pytest tests
%endif

%if %{with doc}
sphinx-build-3 -b html docs docs/_build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS.rst CHANGELOG.rst LICENSE README.rst
%{py3_sitescriptdir}/pytest-cov.pth
%{py3_sitescriptdir}/pytest_cov
%{py3_sitescriptdir}/pytest_cov-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
