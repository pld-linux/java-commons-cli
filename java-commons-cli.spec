#
# Conditional build:
%bcond_without	javadoc		# don't build javadoc
%bcond_without	tests		# don't run tests

%if "%{pld_release}" == "ti"
%bcond_without	java_sun	# build with gcj
%else
%bcond_with	java_sun	# build with java-sun
%endif

%include	/usr/lib/rpm/macros.java
%define		srcname		commons-cli
Summary:	Commons CLI - API for working with command line
Summary(pl.UTF-8):	Commons CLI - API do pracy z linią poleceń
Name:		java-commons-cli
Version:	1.1
Release:	3
License:	Apache v2
Group:		Libraries/Java
Source0:	http://www.apache.org/dist/commons/cli/source/commons-cli-%{version}-src.tar.gz
# Source0-md5:	ccc1aa194132e2387557bbb7f65391f4
Patch0:		%{name}-target.patch
URL:		http://commons.apache.org/cli/
BuildRequires:	ant
BuildRequires:	java-commons-lang
BuildRequires:	java-commons-logging
%{!?with_java_sun:BuildRequires:	java-gcj-compat-devel}
%{?with_java_sun:BuildRequires:	java-sun}
BuildRequires:	jaxp_parser_impl
BuildRequires:	jdk >= 1.4
BuildRequires:	jpackage-utils
%{?with_tests:BuildRequires:	junit}
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jpackage-utils
Requires:	jre >= 1.4
Provides:	jakarta-commons-cli
Obsoletes:	jakarta-commons-cli
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Commons CLI provides a simple API for working with the command line
arguments and options.

%description -l pl.UTF-8
Commons CLI dostarcza prostego API do pracy z argumentami i opcjami
linii poleceń.

%package javadoc
Summary:	Commons CLI documentation
Summary(pl.UTF-8):	Dokumentacja do Commons CLI
Group:		Documentation
Requires:	jpackage-utils
Obsoletes:	jakarta-commons-cli-doc

%description javadoc
Commons CLI documantation.

%description javadoc -l pl.UTF-8
Dokumentacja do Commons CLI.

%prep
%setup -q -n commons-cli-%{version}-src
%patch0 -p1

%build
required_jars="commons-lang"
CLASSPATH=$(build-classpath $required_jars)

%ant dist \
	-Dnoget="true"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

install dist/commons-cli-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
ln -sf commons-cli-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/commons-cli.jar

%if %{with javadoc}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
cp -a dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
ln -s %{srcname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{srcname} # ghost symlink
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{srcname}-%{version} %{_javadocdir}/%{srcname}

%files
%defattr(644,root,root,755)
%doc LICENSE.txt
%{_javadir}/*.jar

%if %{with javadoc}
%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{srcname}-%{version}
%ghost %{_javadocdir}/%{srcname}
%endif
