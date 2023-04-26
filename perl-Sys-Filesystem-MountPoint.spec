#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Sys
%define		pnam	Filesystem-MountPoint
Summary:	Sys::Filesystem::MountPoint - shortcuts to resolve paths and devices to mount points
Name:		perl-Sys-Filesystem-MountPoint
Version:	1.02
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Sys/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	48ca0252c812dcfb607ef45e45677842
# generic URL, check or change before uncommenting
#URL:		https://metacpan.org/release/Sys-Filesystem-MountPoint
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl(Getopt::Std::Strict) >= 1.01
BuildRequires:	perl(Sys::Filesystem) >= 1.22
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
What if you have a path of a file on disk, and you want to know what
that file's mount point is? Or a device, and you want to resolve it?
These are shortcuts to get that kind of info.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mounpointq
%{perl_vendorlib}/Sys/Filesystem/MountPoint.pm
%{_mandir}/man3/Sys::Filesystem::MountPoint.3*
