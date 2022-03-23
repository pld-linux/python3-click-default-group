%define		module	click-default-group
Summary:	Extends click.Group to invoke a command without explicit subcommand name
Summary(pl.UTF-8):	Rozszerzenie click.Group o wywoływanie poleceń bez jawnej nazwy podpolecenia
Name:		python3-%{module}
Version:	1.2.2
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/c/click-default-group/%{module}-%{version}.tar.gz
# Source0-md5:	4f0f38b1105d032a19f24c2661b0a82a
URL:		https://pypi.org/project/click-default-group/
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Extends click.Group to invoke a command without explicit subcommand
name.

%description -l pl.UTF-8
Rozszerzenie click.Group o wywoływanie poleceń bez jawnej nazwy
podpolecenia.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/*.py
%{py3_sitescriptdir}/__pycache__/*.pyc
%{py3_sitescriptdir}/click_default_group-%{version}-py*.egg-info
