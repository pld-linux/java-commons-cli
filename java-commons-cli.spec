#
# Conditional build:
%bcond_without	tests		# don't run tests
#
%include	/usr/lib/rpm/macros.java
Summary:	Jakarta Commons CLI - API for working with command line
Summary(pl.UTF-8):	Jakarta Commons CLI - API do pracy z linią poleceń
Name:		jakarta-commons-cli
Version:	1.1
Release:	2
License:	Apache v1.1
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/commons/cli/source/commons-cli-%{version}-src.tar.gz
# Source0-md5:	ccc1aa194132e2387557bbb7f65391f4
URL:		http://jakarta.apache.org/commons/cli/
Patch0:		%{name}-target.patch
BuildRequires:	ant
BuildRequires:	jakarta-commons-lang
BuildRequires:	jakarta-commons-logging
BuildRequires:	jaxp_parser_impl
BuildRequires:	jdk >= 1.4
BuildRequires:	jpackage-utils
%{?with_tests:BuildRequires:	junit}
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jre >= 1.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jakarta Commons CLI provides a simple API for working with the command
line arguments and options.

%description -l pl.UTF-8
Jakarta Commons CLI dostarcza prostego API do pracy z argumentami i
opcjami linii poleceń.

%package javadoc
Summary:	Jakarta Commons CLI documentation
Summary(pl.UTF-8):	Dokumentacja do Jakarta Commons CLI
Group:		Documentation
Requires:	jpackage-utils
Obsoletes:	jakarta-commons-cli-doc

%description javadoc
Jakarta Commons CLI documantation.

%description javadoc -l pl.UTF-8
Dokumentacja do Jakarta Commons CLI.

%prep
%setup -q -n commons-cli-%{version}-src
%patch0 -p1

%build
required_jars="commons-lang"
export CLASSPATH=$(build-classpath $required_jars)
%ant dist \
	-Dnoget="true"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

install dist/commons-cli-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
ln -sf commons-cli-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/commons-cli.jar

install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -a dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(644,root,root,755)
%doc LICENSE.txt
%{_javadir}/*.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}
