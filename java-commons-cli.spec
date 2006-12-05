Summary:	Jakarta Commons CLI - API for working with command line
Summary(pl):	Jakarta Commons CLI - API do pracy z lini± poleceñ
Name:		jakarta-commons-cli
Version:	1.0
Release:	2
License:	Apache v1.1
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/jakarta/commons/cli/source/cli-%{version}-src.tar.gz
# Source0-md5:  ba34d585046b1f17dacbb13b377f4255
URL:		http://jakarta.apache.org/commons/cli/
BuildRequires:	ant
BuildRequires:	jakarta-commons-lang
BuildRequires:	jakarta-commons-logging
BuildRequires:	jaxp_parser_impl
BuildRequires:	jdk >= 1.4
BuildRequires:	jpackage-utils
BuildRequires:	rpmbuild(macros) >= 1.294
Requires:	jre >= 1.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jakarta Commons CLI provides a simple API for working with the command
line arguments and options.

%description -l pl
Jakarta Commons CLI dostarcza prostego API do pracy z argumentami i
opcjami linii poleceñ.

%package doc
Summary:	Jakarta Commons CLI documentation
Summary(pl):	Dokumentacja do Jakarta Commons CLI
Group:		Development/Languages/Java

%description doc
Jakarta Commons CLI documantation.

%description doc -l pl
Dokumentacja do Jakarta Commons CLI.

%prep
%setup -q -n commons-cli-%{version}

%build
install -d lib
# Doesn't build without it, thou it get's the rest deps OK
ln -s %{_javadir}/commons-lang.jar lib/commons-lang.jar
%ant dist \
	-Dnoget="true"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

install dist/*.jar $RPM_BUILD_ROOT%{_javadir}
ln -sf commons-cli-%{version}-beta-2-dev.jar $RPM_BUILD_ROOT%{_javadir}/commons-cli.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt
%{_javadir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc dist/docs
